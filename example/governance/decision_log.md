# Decision Log

Track significant methodological, data, and analytical decisions that impact the research outcomes.

## Format

* **Date**: YYYY-MM-DD
* **Decision**: [What was decided]
* **Rationale**: [Why it was decided, including alternatives considered]
* **Impact**: [Expected impact on the project]

---

* **Date**: 2023-09-25
* **Decision**: Generate exactly N=10,000 synthetic records.
* **Rationale**: This size is large enough to demonstrate stable logistic regression coefficients without causing long loading or rendering times for the Quarto website.
* **Impact**: Ensures the demonstration repository remains lightweight and responsive.

* **Date**: 2023-09-26
* **Decision**: Utilise logistic regression instead of a more complex machine learning classifier (e.g., Random Forest).
* **Rationale**: Logistic regression provides easily interpretable Odds Ratios, which are standard in epidemiological literature and easier to interpret in a demonstration context.
* **Impact**: Prioritizes explainability over raw predictive power for this educational synthetic example.
