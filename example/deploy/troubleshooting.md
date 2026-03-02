---
title: "Troubleshooting"
---

This section mirrors the troubleshooting advice from the main template.

## Common Issues

### Quarto Render Fails
- Check for YAML syntax errors in `_quarto.yml` or front matter block of `.qmd` files.
- Ensure all file paths referenced in `_quarto.yml` correctly match the directory structure.

### Missing Navigation Links
- Ensure the `href` in the `_quarto.yml` navbar matches the exact file name and path.
- Remember that Quarto websites require an `index.qmd` or `index.html` at the project root.

### Broken Markdown Links
- Remember that links between files should be relative.
