# Zettel

This is my [digital garden](https://maggieappleton.com/garden-history), built with [Logseq](https://logseq.com/). It's hosted at zettel.vivsha.ws.

## How is this built and deployed?

I use the [logseq/publish-spa](https://github.com/logseq/publish-spa) GitHub Action to build the app in CI. I publish to GitHub Pages, per that Action's defaults. Simple as that.

## Scripts

[./.scripts](The `.scripts/` directory) contains useful scripts for batch-processing Logseq notes. (For example, converting Logseq's tag format to standard YAML frontmatter.)
