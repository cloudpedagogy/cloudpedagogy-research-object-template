# Risk Register

Identify, track, and mitigate project risks (e.g., data privacy leaks, biased outcomes, delays).

## Format

* **Date Identified**: YYYY-MM-DD
* **Risk Description**: [What could go wrong]
* **Likelihood**: [Low/Medium/High]
* **Impact**: [Low/Medium/High]
* **Mitigation Strategy**: [How this will be prevented or addressed]

---

* **Date Identified**: 2023-09-20
* **Risk Description**: Readers may mistake the synthetic example results for real clinical findings and attempt to implement corresponding operational changes.
* **Likelihood**: Low
* **Impact**: High
* **Mitigation Strategy**: Include bold, highly visible warnings across the `index.qmd`, `README.md`, `results.qmd`, and the Model Card explicitly stating the data is synthetic. 

* **Date Identified**: 2023-09-22
* **Risk Description**: The synthetic data generation script may accidentally replicate an identifiable statistical fingerprint of the researcher's home institution if based too closely on memory rather than abstract distributions.
* **Likelihood**: Low
* **Impact**: Medium
* **Mitigation Strategy**: Abstract all variables to generic integers/factors and use standard, uncalibrated uniform/poisson distributions without attempting to match local population baselines exactly.
