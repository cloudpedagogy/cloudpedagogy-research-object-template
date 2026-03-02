# USER INSTRUCTIONS

CloudPedagogy Research Object Template\
v0.1

------------------------------------------------------------------------

## 1. Getting Started

### Install Requirements

-   Install Quarto: https://quarto.org
-   (Optional) Install R or Python if you plan to execute code blocks

Check installation:

``` bash
quarto check
```

------------------------------------------------------------------------

## 2. Explore the Example First

Before editing the template, render the example project:

``` bash
cd example
quarto render
```

Open the generated HTML site in `_site/`.

This shows a fully populated synthetic healthcare research object,
including governance artefacts and optional AI reflection.

------------------------------------------------------------------------

## 3. Creating Your Own Research Object

### Step 1 -- Fork or Clone

Fork this repository or clone it locally.

### Step 2 -- Work from the Root Template

The root directory contains the blank template.\
Edit files under:

-   `/content/`
-   `/analysis/`
-   `/data/`
-   `/governance/`

Replace synthetic example text with your own research content.

### Step 3 -- Define Your Research Clearly

Ensure you: - State your research question explicitly - Define outcome
and predictors - Describe study design and assumptions - Document
limitations transparently

------------------------------------------------------------------------

## 4. Documenting Data Properly

Complete:

-   `codebook.csv`
-   `data_dictionary.qmd`
-   `dataset_card.qmd`

You should clearly describe: - Data source - Variable definitions -
Pre-processing steps - Known limitations

If using synthetic data, explicitly state this.

------------------------------------------------------------------------

## 5. Completing Governance Artefacts

The following files are intentionally included:

-   `model_card.qmd`
-   `risk_register.md`
-   `decision_log.md`
-   `reproducibility_checklist.md`

These should be completed before sharing or submitting your work.

Governance artefacts are not optional add-ons; they are part of
responsible research documentation.

------------------------------------------------------------------------

## 6. Using the AI Capability Checkpoints (Optional)

The AI Capability Checkpoints are located under `/ai-support/`.

You should complete them only if AI tools were used in:

-   Drafting
-   Code generation
-   Data synthesis
-   Analysis support
-   Editing or critique

Guidelines:

-   Be proportionate.
-   Do not overstate AI involvement.
-   Emphasise human oversight.
-   Maintain accountability with the research team.

If no AI tools were used, these sections can remain blank.

------------------------------------------------------------------------

## 7. Rendering Your Project

From the project root:

``` bash
quarto render
```

To render a specific folder:

``` bash
quarto render content/04-methods.qmd
```

Output will be generated in the `_site/` directory.

------------------------------------------------------------------------

## 8. Exporting for Sharing

Quarto supports:

-   HTML output
-   PDF output (requires LaTeX/TinyTeX)
-   Word export (optional configuration)

You may: - Share the HTML site - Export a PDF submission pack - Provide
a repository link for transparency

------------------------------------------------------------------------

## 9. Common Pitfalls

-   Leaving governance artefacts incomplete\
-   Forgetting to clarify synthetic vs real data\
-   Over-attributing intellectual contribution to AI tools\
-   Mixing template and example content\
-   Failing to render before sharing

Always render and review your site before distribution.

------------------------------------------------------------------------

## 10. Design Philosophy

This template is:

-   Lightweight
-   Static
-   Governance-oriented
-   AI-aware (optional)
-   Infrastructure-focused

It is not a data platform or compliance system.

Its purpose is to structure research transparently and responsibly using
a reproducible framework.

------------------------------------------------------------------------

## Version

v0.1 -- Synthetic Demonstration Release
