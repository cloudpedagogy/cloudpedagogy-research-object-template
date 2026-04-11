# Research Object Template — User Instructions

---
### 2. What This Tool Does
This publishing tool formats raw CloudPedagogy data dumps into governance-ready, institutional documents. It generates clean HTML, PDF, or LaTeX reports suitable for formal committee review, public transparency registers, or cross-institutional sharing.

---
### 3. Role in the Ecosystem
- **Phase:** Phase 5 — Infrastructure
- **Role:** Publication layer for governance-aware HTML and PDF reports.
- **Reference:** [../SYSTEM_OVERVIEW.md](../SYSTEM_OVERVIEW.md)

---
### 4. When to Use This Tool
- When submitting an AI capability assessment to an institutional ethics board.
- When publishing a newly designed curriculum for external regulatory review.
- To convert raw JSON dashboard payloads into a readable format for non-technical stakeholders.

---
### 5. Inputs
- Finalized JSON outputs from CloudPedagogy analysis tools (e.g., Risk Scanner results, Capability Stress Tests).

---
### 6. How to Use (Step-by-Step)
1. Locate the Quarto/Markdown source folder associated with the template.
2. Inject the target JSON payload into the document's data directory.
3. Update the YAML frontmatter with specific institutional metadata (date, author, version).
4. Run the publication command (e.g., `quarto render`).
5. Retrieve the highly styled, professional report in your specified format.

---
### 7. Key Outputs
- Formal, compliant PDF or HTML documents reflecting the underlying data.
- Built-in visual warnings if required governance metadata is missing.

---
### 8. How It Connects to Other Tools
- **Upstream:** Generally applied at the very end of a workflow, consuming outputs from **Phase 2 Governance** or **Phase 3 Capability** tools.
- **Downstream:** Outputs leave the system for human review.

---
### 9. Limitations
- This is a styling and publishing engine; it will faithfully render flawed data if flawed data is imported.
- Requires some technical familiarity with document generation pipelines to execute.

---
### 10. Tips
- Do not manually edit the generated PDF to fix typos; always fix the source JSON data or the Markdown template.
