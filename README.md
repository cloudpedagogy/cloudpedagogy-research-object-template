# CloudPedagogy Research Object Template

**Governance-Ready, AI-Aware Healthcare Research Infrastructure
(Quarto-Based)**

------------------------------------------------------------------------

## Overview

This repository implements a structured, governance-ready research
object for healthcare research projects using Quarto.

It provides a reproducible, navigable framework that integrates:

-   A clear research lifecycle (question → protocol → data → methods →
    results → interpretation → reuse)
-   Governance artefacts (dataset card, model card, risk register,
    decision log, reproducibility checklist)
-   Optional AI capability reflection scaffolds
-   Static, portable publication via Quarto

This is not simply a writing template.\
It encodes research transparency and governance directly into project
structure.

------------------------------------------------------------------------

## What Problem This Solves

Healthcare research projects are often fragmented:

-   Manuscript in one place\
-   Code in another\
-   Governance documentation elsewhere\
-   AI usage inconsistently disclosed

This template addresses:

-   Structural fragmentation\
-   Reactive governance\
-   Opaque AI use\
-   Reproducibility gaps\
-   Inconsistent documentation practices

It transforms a research project into a coherent, version-controlled
research object.

------------------------------------------------------------------------

## What This Is Not

-   Not a data platform\
-   Not a journal replacement\
-   Not an AI automation system\
-   Not regulatory compliance software\
-   Not a learning management system

It is a lightweight infrastructure pattern for structuring and
documenting research projects responsibly.

------------------------------------------------------------------------

## Repository Structure

### Root (Template)

The root project contains the blank, reusable template:

-   Structured content pages\
-   Governance artefacts\
-   AI Capability Checkpoints (optional)\
-   Data documentation scaffolds\
-   Deployment guidance

This is the version intended for forking and reuse.

------------------------------------------------------------------------

### `/example/` (Fully Populated Demonstration)

Explore the synthetic demonstration project here:

-   Browse source: [`/example/`](./example/)

The `/example/` folder contains a synthetic, fully populated healthcare
research project:

> "Understanding Factors Associated with Missed Outpatient Appointments:
> A Synthetic Service Utilisation Study"

This example:

-   Uses entirely synthetic data\
-   Does not represent any real institution\
-   Demonstrates governance completion\
-   Demonstrates proportionate AI reflection\
-   Shows how the template can be implemented end-to-end

It serves as a working demonstration of good practice.

------------------------------------------------------------------------

### Live rendered demo:

http://cloudpedagogy-research-object-demo.s3-website.eu-west-2.amazonaws.com/

This site shows the fully rendered research object generated from the `/example/` project in this repository.

The demo allows users to explore the complete structure of a governance-ready research object, including:

• research lifecycle documentation  
• governance artefacts (dataset card, model card, risk register, decision log)  
• optional AI capability reflection checkpoints  
• reproducible research structure built with Quarto  

The demonstration uses entirely synthetic data and represents a fictional healthcare service utilisation study.

[![Research Object Demo](docs/research-object-demo.png)](http://cloudpedagogy-research-object-demo.s3-website.eu-west-2.amazonaws.com/)

------------------------------------------------------------------------

## AI Capability Layer (Optional)

This template includes optional AI Capability Checkpoints aligned to a
six-domain reflection model:

-   Awareness & Orientation\
-   Human--AI Co-Agency\
-   Applied Practice & Innovation\
-   Ethics, Equity & Impact\
-   Decision-Making & Governance\
-   Reflection, Learning & Renewal

AI use is **not required**.

These sections are designed to support transparent, proportionate
documentation where AI tools are used.\
Human responsibility remains central.

------------------------------------------------------------------------

## How to Use

1.  Fork or clone this repository.
2.  Edit content pages under `/content/`.
3.  Complete governance artefacts under `/governance/`.
4.  Fill AI Capability Checkpoints if applicable.
5.  Render using:

``` bash
quarto render
```

To render the example:

``` bash
cd example
quarto render
```

------------------------------------------------------------------------

## Detailed User Guide

For a step-by-step working guide, see:

[USER-INSTRUCTIONS.md](./USER-INSTRUCTIONS.md)

This document covers:

-   Getting started\
-   Completing governance artefacts\
-   Using AI Capability Checkpoints (optional)\
-   Rendering and exporting

------------------------------------------------------------------------

## Intended Audience

-   Healthcare researchers\
-   Service evaluation teams\
-   Applied analytics groups\
-   AI-in-health projects\
-   Governance-conscious research teams\
-   Institutions seeking lightweight transparency structures

------------------------------------------------------------------------

## Positioning Within CloudPedagogy

This project extends the CloudPedagogy ecosystem from curriculum
infrastructure into research infrastructure.

It demonstrates how governance and AI capability principles can be
operationalised in research practice.

------------------------------------------------------------------------

## Licence

-   Code structure: MIT\
-   Documentation content: see licence file

------------------------------------------------------------------------

## Version

v0.1 --- Synthetic demonstration release\
This is an evolving infrastructure pattern.
