# E Ink Reader desktop verification

Tested on 24 November 2026 in Obsidian 1.15.1 on Windows. The source baseline was <code>56ec82c</code> and the tested patch is theme version 3.2.2. The isolated vault contained synthetic Markdown notes, a Canvas board and a Base table. The ten PNGs are direct captures of the Obsidian renderer.

## Issues reproduced and retested

| Surface | Baseline | Verified with 3.2.2 |
| --- | --- | --- |
| Reading view code and semantic colors | JavaScript property names rendered cyan at about 2.3:1 against white. Operators and the Sync status glyph rendered red. | The eight semantic colors and their RGB variants use the same grayscale values. All inspected tokens rendered grayscale. The lowest contrast across 41 tokens in the test note was 9.0:1. |
| Canvas and graph connectors | Canvas connectors used <code>#c0c0c0</code> at about 1.8:1 against white. The graph line variable was <code>#dadada</code>. | Canvas connector strokes rendered <code>#666666</code> at 5.74:1 against white. The built-in graph rendered its linked fixture notes with the darker graph line setting. |

## Cases and captures

| Case | Verified result | Evidence |
| --- | --- | --- |
| Reading and file navigation | Heading levels, properties, callout, active file outline, checkmarked and unchecked tasks, and nested list markers rendered. Toggling a task changed its status and a second click restored it. The main text measured 19.03:1 against white. | [Reading](01-reading-properties-and-tasks.png) |
| Live Preview keyboard editing | Shift+Right extended a selection. The selection used <code>#d2d2d2</code>, the caret rendered black, and the focused editor showed a 2 px outline. Inserting and deleting a character restored the original content. The CodeMirror cursor layer reported no CSS animation. | [Live Preview](02-live-preview-keyboard-selection.png) |
| Source mode and editor options | Raw Markdown and YAML appeared in Source mode. The line-number and readable-line-length commands changed the editor layout. The source maintained its 8 px inline padding. | [Source mode](03-source-line-numbers.png) |
| Context menu and command palette | The file menu opened with a solid outline and no CSS animation. Typing <code>outline</code> filtered the command palette, Arrow Down changed the selected result and Escape dismissed the overlays. | [File context menu](04-file-context-menu.png) |
| Search, links and Outline | A vault search for <code>tide</code> returned the field guide and showed a 2 px input focus outline. The link inside the callout opened the checklist. Outline listed the Markdown heading and all three sections. The reading table rendered three rows and all sampled internal, unresolved and external links were underlined. | [Vault search](05-vault-search.png) |
| Canvas | Three synthetic nodes and two connecting edges rendered. Zoom in and zoom to fit changed the board view. Canvas settings exposed snap to grid, snap to objects and read-only controls. | [Canvas](06-canvas-nodes-and-edges.png) |
| Bases | The built-in table rendered four note rows and three columns. Display, Sort, Filter and Properties opened their menus. | [Bases](07-bases-table.png) |
| Graph | The built-in graph rendered nodes and links at full workspace width. Its settings displayed filters, groups, display and forces. | [Graph](08-graph-links.png) |
| Narrow window and larger font | With both sidebars collapsed, the 560 × 780 viewport kept the page and Reading pane within their respective widths at 22 px text. A long paragraph wrapped to its available 440 px width. The screenshot shows tasks, a table, inline formatting, links and a block quote at that size. | [Narrow Reading view](09-narrow-reading-reflow.png) |
| Appearance and mode compatibility | Light loaded E Ink Reader, Dark used Obsidian's dark palette and Adapt to system selected the host's Light scheme. Switching between Default and E Ink Reader restored the correct palette. The Accent color control accepted and reset a test color while the theme's interactive accent stayed grayscale. The text size slider changed from 16 px to 22 px. | [Appearance](10-appearance-light-settings.png) |

All six stylesheet tests passed with <code>python -B -m unittest discover -s tests -v</code>. Physical e-ink refresh, ghosting and caret visibility remain unverified. This record covers the desktop source checkout.
