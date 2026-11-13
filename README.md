# E Ink Reader

A practical monochrome Obsidian theme for actual e-ink devices.

**Status: planning only. No theme code has been written.**

Plan date: 13 November 2026. This repository currently contains this planning README only. The name is a descriptive working name; Community name availability must be checked before any future submission.

Search keywords: Obsidian theme, e-ink, BOOX, monochrome, no animation, reader.

## Who this is for

BOOX and other e-ink device owners who read and edit Markdown notes.

## User need and evidence

A popular e-ink setup combined Minimal with custom CSS to remove animations, replace the blinking cursor and improve monochrome readability.

- [Obsidian setup on a BOOX Go 10.3](https://www.reddit.com/r/ObsidianMD/comments/1w1koh2/obsidian_eink_setup/)

The Reddit links come from the preceding idea research and represent qualitative demand, not a market-size estimate or proof that existing themes do not solve the problem. For Pure OLED Rainbow, the additional requirement comes directly from the owner. Other themes and snippets may already address parts of these needs.

## Planned appearance and features

- Use a white page with black text, strong borders and clearly visible active states.
- Avoid decorative textures, shadows, gradients and colour-dependent status distinctions.
- Disable theme transitions and animations; investigate a static, visible caret using supported styling.
- Keep icons, checkboxes, lists and selection states readable in monochrome.
- Use a lightweight layout with comfortable touch targets and no unnecessary visual refresh effects.
- Avoid assumptions about hardware refresh controls: a theme cannot control the display driver.

## Mode scope

Light monochrome mode is primary. An inverted mode is optional only after device testing.

## Future implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references for later implementation:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

These are future work items. No release, installation instructions, compatibility certification or Community listing is being claimed by this planning repository.

## Acceptance checklist for later implementation

- [ ] Test on a real e-ink device before claiming reduced ghosting or device compatibility.
- [ ] Verify cursor visibility, text selection, scrolling and menus on the tested device.
- [ ] Confirm core controls remain understandable without colour.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Current boundary

Only repository creation and this Markdown plan are authorised in this task. Do not add theme CSS, manifests, screenshots, release tags or submissions as part of this planning work. Future work stays on this repository's verified primary branch.
