import json
import unittest
from pathlib import Path
from xml.etree.ElementTree import fromstring

import cssselect2
import tinycss2


ROOT = Path(__file__).resolve().parents[1]
MARKUP = """
<body id="app" class="theme-{mode}">
  <main class="workspace-leaf-content">
    <section class="markdown-source-view mod-cm6">
      <div class="cm-editor cm-focused">
        <div class="cm-scroller">
          <div class="cm-contentContainer">
            <div id="editor" class="cm-content" data-keyboard-focus="" />
          </div>
          <div id="cursor-layer" class="cm-layer cm-cursorLayer"><div id="cursor" class="cm-cursor" /></div>
        </div>
      </div>
      <span id="editor-bullet" class="list-bullet" />
    </section>
    <article class="markdown-rendered">
      <a id="link" href="#" />
      <span id="reader-bullet" class="list-bullet" />
      <aside id="callout" class="callout" />
    </article>
  </main>
  <div id="active-file" class="nav-file-title is-active" />
  <div id="inactive-file" class="nav-file-title" />
  <div id="menu" class="menu"><button id="menu-button" data-keyboard-focus="" /></div>
  <div id="modal" class="modal"><button id="modal-button" /></div>
</body>
"""


class ThemeTests(unittest.TestCase):
    def setUp(self):
        self.matcher = cssselect2.Matcher()
        css = (ROOT / "theme.css").read_text(encoding="utf-8")
        for rule in tinycss2.parse_stylesheet(css, skip_comments=True, skip_whitespace=True):
            self.assertEqual(rule.type, "qualified-rule", str(rule))
            declarations = tinycss2.parse_declaration_list(
                rule.content, skip_comments=True, skip_whitespace=True
            )
            for declaration in declarations:
                self.assertEqual(declaration.type, "declaration", str(declaration))
            # The static selector matcher cannot simulate keyboard focus.
            selector = tinycss2.serialize(rule.prelude).replace(":focus-visible", "[data-keyboard-focus]")
            for compiled in cssselect2.compile_selector_list(selector):
                self.matcher.add_selector(compiled, declarations)

    def styles(self, mode, element_id, pseudo=None):
        root = cssselect2.ElementWrapper.from_html_root(fromstring(MARKUP.format(mode=mode)))
        element = root.query(f"#{element_id}")
        styles = {}
        for _, _, pseudo_element, declarations in self.matcher.match(element):
            if pseudo_element == pseudo:
                for declaration in declarations:
                    previous = styles.get(declaration.name)
                    if declaration.important or previous is None or not previous.important:
                        styles[declaration.name] = declaration
        return {
            name: (tinycss2.serialize(declaration.value).strip(), declaration.important)
            for name, declaration in styles.items()
        }

    def test_only_light_mode_applies_theme_styles(self):
        for element, pseudo in (
            ("app", None), ("editor", None), ("cursor-layer", None), ("link", None),
            ("menu-button", None), ("reader-bullet", "after"), ("editor-bullet", "after"),
        ):
            with self.subTest(element=element):
                self.assertEqual(self.styles("dark", element, pseudo), {})

    def test_disables_motion_on_app_frame_controls_and_generated_content(self):
        for element, pseudo in (
            ("app", None), ("app", "before"), ("app", "after"),
            ("cursor-layer", None), ("menu-button", None),
            ("reader-bullet", "before"), ("reader-bullet", "after"),
        ):
            with self.subTest(element=element, pseudo=pseudo):
                styles = self.styles("light", element, pseudo)
                self.assertEqual(styles.get("animation"), ("none", True))
                self.assertEqual(styles.get("transition"), ("none", True))
                self.assertEqual(styles.get("scroll-behavior"), ("auto", True))
                self.assertEqual(styles.get("box-shadow"), ("none", True))

    def test_keeps_codemirror_in_charge_of_cursor_visibility(self):
        styles = self.styles("light", "cursor")
        self.assertNotIn("visibility", styles)
        self.assertNotIn("display", styles)

    def test_preserves_reading_and_keyboard_affordances(self):
        palette = self.styles("light", "app")
        self.assertEqual(palette["--background-primary"][0], "#ffffff")
        self.assertEqual(palette["--text-normal"][0], "#101010")
        self.assertNotEqual(palette["--text-selection"], palette["--text-highlight-bg"])
        self.assertEqual(self.styles("light", "link")["text-decoration"][0], "underline")
        for element in ("active-file", "menu", "modal", "callout"):
            with self.subTest(element=element):
                self.assertEqual(self.styles("light", element)["outline"][0], "1px solid #333")
        self.assertNotIn("outline", self.styles("light", "inactive-file"))
        self.assertNotIn("outline", self.styles("light", "modal-button"))
        for element in ("editor", "menu-button"):
            self.assertEqual(self.styles("light", element)["outline"][0], "2px solid var(--text-accent)")
        self.assertEqual(self.styles("light", "editor")["padding-inline"][0], "8px")
        for element in ("reader-bullet", "editor-bullet"):
            self.assertEqual(
                self.styles("light", element, "after")["background-color"][0], "var(--text-muted)"
            )

    def test_release_files_and_manifest(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "E Ink Reader")
        self.assertTrue(manifest["author"])
        for field in ("version", "minAppVersion"):
            self.assertRegex(manifest[field], r"^\d+\.\d+\.\d+$")
        for filename in ("theme.css", "screenshot.png", "LICENSE"):
            self.assertTrue((ROOT / filename).is_file(), filename)
