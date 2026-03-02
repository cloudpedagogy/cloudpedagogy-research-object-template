# AI Capability Checkpoints

This document provides reflection scaffolds aligned to a six-domain AI Capability model. These checkpoints are designed to support responsible, transparent, and professional research practice in this synthetic example.

------------------------------------------------------------------------

## 1. Awareness & Orientation

If AI tools were used at this stage of the project:

-   **Tools Used**: A Large Language Model (LLM) was used as a drafting assistant to help shape the narrative structure of the synthetic protocol and generate the Python code for the synthetic dataset.
-   **Limitations**: Known limitations included a tendency for the LLM to hallucinate overly complex or clinically specific variables that were not appropriate for a generic synthetic dataset.
-   **Checks Performed**: Human researchers carefully reviewed all generated covariates and code against standard epidemiological principles before finalising the dataset. 

------------------------------------------------------------------------

## 2. Human--AI Co-Agency

If applicable:

-   **Tasks Supported**: Drafting boilerplate protocol text, commenting code, and structuring governance documents (like the risk register).
-   **Human Judgement**: The choice of logistic regression as the primary analytical method, and the specific distribution shapes of the synthetic data, remained entirely under human control.
-   **Human Oversight**: All AI-drafted sections were iteratively edited by human authors to ensure a neutral, governance-oriented tone.
-   **Evaluating Suggestions**: Suggestions to include complex machine learning algorithms (e.g., neural networks) in the methodology were rejected to maintain the educational simplicity of the example.

------------------------------------------------------------------------

## 3. Applied Practice & Innovation

If AI tools were used:

-   **Specific Ways AI Supported**: AI significantly accelerated the creation of the `data/codebook.csv` format and helped generate the repetitive markdown structure of the Quarto `.qmd` files.
-   **Independent Elements**: The core concept (investigating missed appointments) and the specific relationships injected into the synthetic data (e.g., `previous_missed` being strongly predictive) were developed independently by human researchers.
-   **Modifications**: AI outputs were substantially modified to remove any enthusiastic or promotional language regarding AI use itself, in line with governance requirements.

------------------------------------------------------------------------

## 4. Ethics, Equity & Impact

If AI tools were involved:

-   **Data Shared**: No sensitive or identifiable data was shared with AI systems; the entire project relies on simulated data.
-   **Bias/Fairness Risks**: When prompting the AI to draft the 'Interpretation' section, there was a risk of the model attributing missed appointments solely to patient non-compliance.
-   **Equity Implications Review**: The research team actively guided the AI drafting process to ensure structural factors (like lead time and deprivation quintile) were highlighted, mitigating the risk of framing bias.

------------------------------------------------------------------------

## 5. Decision-Making & Governance

If AI tools were used:

-   **Documentation**: AI use was documented transparently in the 'AI Capability Checkpoint' callouts embedded at the bottom of each relevant content page.
-   **Disclosure Requirements**: We considered standard journal AI disclosure requirements and ensured this standalone document serves as a comprehensive record of AI assistance.
-   **Justifications**: The decision to use AI to generate the synthetic dataset rather than hand-crafting it was justified by the need for reproducibility and scale (N=10,000) within a demonstration context.

------------------------------------------------------------------------

## 6. Reflection, Learning & Renewal

Optional reflective prompts:

-   **What Worked Well**: Using AI to overcome the "blank page" problem for governance documentation (e.g., generating the initial structure of the Model Card) was highly efficient.
-   **Future Changes**: In future iterations, we would rely less on open-ended conversational prompts and more on highly structured templates when asking the AI to synthesize data.
-   **Influence**: AI positively influenced the structural consistency of the markdown files but required careful editing to ensure the framing remained strictly neutral.

------------------------------------------------------------------------

## Important Notes

-   AI use is **not required** for this template.
-   These checkpoints are designed to support transparency and governance.
-   Responsibility for all research outputs remains with the human authors.
