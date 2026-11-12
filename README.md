# Football Academy Analytics — Concept Deck

[![CI](https://github.com/Willian-Yudy-F/football-academy-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/Willian-Yudy-F/football-academy-analytics/actions/workflows/ci.yml)

An interactive HTML concept deck exploring how a youth football academy could organise
enrolment, attendance and coach-assessment data into useful operational reporting.

## Repository scope

The implemented artifact is the self-contained presentation:

- [`football_academy_analytics_demo.html`](football_academy_analytics_demo.html)
- [live GitHub Pages demo](https://willian-yudy-f.github.io/football-academy-analytics/football_academy_analytics_demo.html)

The dashboard, Google Sheets integration, PDF generator, email workflow and scoring model
shown in the deck are proposed components. They are not included in this repository and
have not been tested with an academy. All names, scores and KPI values in the deck are
synthetic interface examples.

## Problem explored

Small academies may collect enrolment, attendance and coach notes in disconnected files.
The concept asks how a simple data workflow could help staff:

- see participation and attendance patterns;
- prepare progress summaries for guardians;
- notice incomplete records before reporting;
- compare development over time without treating a score as an automatic selection
  decision;
- evaluate whether the workflow is usable before investing in a larger platform.

## Proposed architecture

```text
consented data collection
        │
        ▼
controlled operational dataset
        │
        ├──► aggregate academy dashboard
        └──► reviewed individual progress summary
```

Google Forms, Google Sheets, Python and Looker Studio appear in the deck as candidate
tools, not as a deployed production stack. Product limits, privacy controls and operating
costs would need to be checked before implementation.

## Privacy and safeguarding requirements

A real implementation would process information about children, so technical convenience
cannot be the only design criterion. Before collecting any real records, the academy would
need to define:

- guardian consent and a clear purpose for every field;
- role-based access for coaches and administrators;
- minimum necessary data and a retention/deletion schedule;
- secure credential storage and audit logging;
- a correction process for inaccurate assessments;
- human review of reports, alerts and any development score;
- aggregate reporting wherever individual identification is unnecessary.

This repository contains no real player or guardian data.

## Responsible use of scoring

The deck includes an illustrative weighted score to prompt discussion. It is not a
validated talent model. Coach ratings can be subjective, attendance can reflect access or
health circumstances, and a single ranking can amplify bias. A future prototype should
show component values, support corrections and never make selection or safeguarding
decisions automatically.

## Run locally

No installation or build step is required:

```bash
python -m http.server 8000
```

Open:

```text
http://localhost:8000/football_academy_analytics_demo.html
```

Run the repository checks with:

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
football_academy_analytics_demo.html   interactive concept deck
tests/test_deck.py                     static-content and link checks
README.md                              scope, safeguards and local setup
```

## Next honest milestone

Build a small synthetic dataset and one offline notebook that calculates aggregate
attendance trends. Only after the data contract and safeguards are reviewed should the
project add individual reports or external services.

---

Willian Yudy Futema · [Portfolio](https://willian-yudy-f.github.io/) ·
[LinkedIn](https://www.linkedin.com/in/willian-yudy-futema/)
