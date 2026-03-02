---
title: "GitHub Pages"
---

This section is identical to the root template deployment guide. 

To deploy this Quarto website to GitHub Pages:

1. Create a GitHub repository and push this project to it.
2. In your terminal, ensure you have committed all changes.
3. Run the following command:
   ```bash
   quarto publish gh-pages
   ```
4. Quarto will build the site, create a `gh-pages` branch, and push the static assets.
5. In your GitHub repository settings, ensure Pages is set to deploy from the `gh-pages` branch.
