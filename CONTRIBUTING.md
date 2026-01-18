# Contributing / working as a group

## Basic workflow (simple + safe)

- Everyone works on their own branch.
- Merge to `main` when the notebook/script runs and the story still makes sense.

### Create a branch

```bash
git checkout -b yourname/topic
```

Examples:
- `bella/data-load-owid`
- `alex/sir-model`
- `group/poster-figures`

### Commit small, meaningful changes

```bash
git add -A
git commit -m "Add first pass at SIR model notebook"
```

### Pull latest `main` before you merge

```bash
git checkout main
git pull
git checkout yourname/topic
git merge main
```

## Notebook conventions (reduces merge conflicts)

- Keep notebooks small and ordered (`00_`, `01_`, `02_`…).
- Put reusable code in `src/epidemiology_project/`.
- Save final figures to `reports/figures/`.
- Record dataset details in `docs/DATA_SOURCES.md` and choices in `docs/DECISIONS.md`.

## Suggested division of work

- **Data person**: downloads + cleaning + documents sources
- **Model person**: implements model + parameter fitting
- **Visuals person**: clean plots + poster-ready figures
- **Writer/editor**: stitches narrative and checks consistency

