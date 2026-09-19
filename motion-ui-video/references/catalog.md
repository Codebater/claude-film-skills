# animate-ui registry catalog

Registry base: `https://animate-ui.com/r/<item>.json` (shadcn-compatible, 580 items).
Install: `npx shadcn@latest add @animate-ui/<item> --yes --overwrite` (namespace mapped in the template's `components.json`).
Files land in `src/components/animate-ui/...`; npm deps and `@animate-ui/*` registry deps resolve automatically.

Every item below also has an installable usage example named `demo-<item>` — fetch its JSON and read `files[0].content` to learn props without installing.

## Picking for video: what carries a shot

- **Hero text moments** → `primitives-texts-*` (splitting, typing, morphing, rolling for headlines; counting-number, sliding-number, scrolling-number for stats/prices).
- **Satisfying click/press** → `components-buttons-liquid`, `-ripple`, `-flip`, `components-buttons-theme-toggler` (whole-screen theme wipe = great beat).
- **Ambient depth layer** → `components-backgrounds-*` at low opacity behind the hero.
- **"Product feels alive" story beats** → community pieces: notification-list, management-bar, playful-todolist, motion-carousel, radial-menu/intro/nav, user-presence-avatar.
- **Micro-polish on anything** → `primitives-effects-*` wrappers (shine, tilt, magnetic, blur, particles, image-zoom) and animated `icons-*`.

## Primitives — texts (the video workhorses)

`primitives-texts-` + : `counting-number`, `gradient`, `highlight`, `morphing`, `rolling`, `rotating`, `scrolling-number`, `shimmering`, `sliding-number`, `splitting`, `typing`

## Primitives — effects (wrappers that animate children)

`primitives-effects-` + : `auto-height`, `blur`, `click`, `effect` (generic in-view/hover effect), `fade`, `highlight`, `image-zoom`, `magnetic`, `particles`, `shine`, `slide`, `theme-toggler`, `tilt`, `zoom`

## Primitives — animate (bespoke)

`primitives-animate-` + : `avatar-group`, `code-block`, `cursor`, `github-stars`, `motion-grid`, `pinned-list`, `scroll-progress`, `slot`, `spring`, `tabs`, `tooltip`

## Components — backgrounds

`components-backgrounds-` + : `bubble`, `fireworks`, `gradient`, `gravity-stars`, `hexagon`, `hole`, `stars`

## Components — buttons

`components-buttons-` + : `button`, `copy`, `flip`, `github-stars`, `icon`, `liquid`, `ripple`, `theme-toggler`

## Components — animate (styled, ready-made)

`components-animate-` + : `avatar-group`, `code`, `code-tabs`, `cursor`, `github-stars-wheel`, `tabs`, `tooltip`

## Components — community (rich story widgets)

`components-community-` + : `flip-card`, `management-bar`, `motion-carousel`, `notification-list`, `pin-list`, `playful-todolist`, `radial-intro`, `radial-menu`, `radial-nav`, `share-button`, `user-presence-avatar`

## Components — headless UI / Base UI / Radix ports

Full animated shadcn-style sets in three flavors — use when the scene is "a real app UI in motion" (dialogs, sheets, sidebars, accordions):

- `components-radix-` + : `accordion`, `alert-dialog`, `checkbox`, `dialog`, `dropdown-menu`, `files`, `hover-card`, `popover`, `preview-link-card`, `progress`, `radio-group`, `sheet`, `sidebar`, `switch`, `tabs`, `toggle`, `toggle-group`, `tooltip`
- `components-base-` + : same idea (Base UI), adds `menu`, `preview-card`, `radio`
- `components-headless-` + : `accordion`, `checkbox`, `dialog`, `popover`, `switch`, `tabs`
- Matching unstyled primitives exist as `primitives-radix-*`, `primitives-base-*`, `primitives-headless-*`, plus `primitives-buttons-*`.

Prefer **one flavor per scene** (radix is the most complete) — mixing flavors duplicates deps.

## Icons (~200 animated Lucide icons)

`icons-<lucide-name>`, e.g. `icons-bell`, `icons-heart`, `icons-loader-pinwheel`, `icons-party-popper`, `icons-send`, `icons-sparkles`, `icons-thumbs-up`, `icons-check-check`, `icons-chart-spline`, `icons-terminal`, `icons-settings`, `icons-sun-moon`, `icons-wifi`, `icons-signal`, `icons-lock`, `icons-fingerprint`, `icons-bot`, `icons-message-circle-*`, `icons-panel-*`, `icons-clock-1`…`-12`, weather set (`icons-cloud-*`), battery/volume/arrow/chevron sets. If a Lucide icon exists, try `icons-<its-name>` — most common ones are covered. They animate on hover/trigger via a shared controller (`icons-icon` base installs automatically).

## Hooks & lib

`hooks-use-auto-height`, `hooks-use-controlled-state`, `hooks-use-data-state`, `hooks-use-is-in-view`, `hooks-use-motion-value-state`, `lib-get-strict-context` — installed automatically as dependencies; rarely needed directly.
