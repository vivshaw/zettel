# zettel

this is my [digital garden](https://maggieappleton.com/garden-history), built with [Logseq](https://logseq.com/). It's hosted at zettel.vivsha.ws.

## how is this built and deployed?

i use the [logseq/publish-spa](https://github.com/logseq/publish-spa) GitHub Action to build the app in CI. i publish to GitHub Pages, per that Action's defaults. simple as that.

## scripts

[./.scripts](the `.scripts/` directory) contains useful scripts for batch-processing Logseq notes. (for example, converting Logseq's tag format to standard YAML frontmatter.)
