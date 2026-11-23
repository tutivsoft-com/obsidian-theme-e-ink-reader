# E Ink Reader original design plan

A practical monochrome Obsidian theme for actual e-ink devices.

This plan dates to 13 November 2026, before the theme was implemented. See the [README](README.md) for current support and installation instructions.

Search keywords: Obsidian theme, e-ink, BOOX, monochrome, no animation, reader.

## Who this is for

BOOX and other e-ink device owners who read and edit Markdown notes.

## User need and evidence

A popular e-ink setup combined Minimal with custom CSS to remove animations, replace the blinking cursor and improve monochrome readability.

- [Obsidian setup on a BOOX Go 10.3](https://www.reddit.com/r/ObsidianMD/comments/1w1koh2/obsidian_eink_setup/)

The Reddit post came from the idea research and illustrates one reader's setup.

## Planned appearance and features

- Use a white page with black text, strong borders and clearly visible active states.
- Avoid decorative textures, shadows, gradients and colour-dependent status distinctions.
- Disable theme transitions and animations; investigate a static, visible caret using supported styling.
- Keep icons, checkboxes, lists and selection states readable in monochrome.
- Use a lightweight layout with comfortable touch targets and no unnecessary visual refresh effects.
- Avoid assumptions about hardware refresh controls: a theme cannot control the display driver.

## Mode scope

Light monochrome mode is primary. An inverted mode is optional only after device testing.

## Original implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references used for the plan:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

## Original acceptance checklist

- [ ] Test on a real e-ink device before claiming reduced ghosting or device compatibility.
- [ ] Verify cursor visibility, text selection, scrolling and menus on the tested device.
- [ ] Confirm core controls remain understandable without colour.
- [ ] Confirm each feature claim against the implementation and test results.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.
