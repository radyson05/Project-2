# Project 2 — Investment Management Application

> **AI disclosure:** I used ChatGPT/Codex for brainstorming the interface, drafting code, and editing documentation. I reviewed the logic and own the analysis and decision. **Education only; not investment advice.**

Prepared by **Ross Dyson**, this constraint-first ETF-allocation dashboard for an investment committee is called Sentinel Allocation. It turns a point-in-time regime signal into a transparent proposed allocation, shows it alongside two baselines, and makes mandate failures visible.

## Committee decision

**Pilot, not adopt.** Allocate **5–10%** of the model sleeve for one quarter. Expand only if data checks pass and live observations remain within the risk limits. See [docs/decision-memo.md](docs/decision-memo.md).

## Run it

Requires Python 3.10+.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`. A stranger can operate the stress controls without credentials or downloads.

## What is in the app

- Mandate: balanced real-capital preservation within a five-ETF universe.
- Benchmark: a transparent 60/40-style allocation; equal weight is the first baseline.
- Signal: lagged 12-month equity momentum plus a yield-curve proxy, with a point-in-time rule.
- Constraints: 10% BIL floor, 45% per-position cap, 60% equity cap, 6% one-month 95% VaR limit.
- Stress: change regime, VaR limit, or cost; a tighter risk-off combination invokes the explicit stop condition.

## Repository map

`app.py` contains the allocation, risk, and verdict logic. `templates/` and `static/` contain the UI. `docs/` contains the committee memo, data card, validation/AI record, manifest, and video transcript scripts.

## Data and limitations

The included numbers are deterministic teaching inputs, included so the app is reproducible offline; they are **not** current prices, a backtest, or a production data feed. The documented source plan is ETF adjusted closes cross-checked against CRSP/Yahoo Finance and Treasury data from FRED. Replace the teaching values with licensed, timestamped data before any real implementation. See [docs/data-card.md](docs/data-card.md).

The included [executed-output record](docs/executed-output.md) shows the material inputs and tested result without requiring the grader to run the application.

## Submission checklist

Before submitting: replace bracketed personal fields; commit the Locked Changed-Input prediction before executing its run; record actual video URLs and timestamps in [docs/manifest.md](docs/manifest.md); and record the actual executed result in [docs/validation-and-ai-use.md](docs/validation-and-ai-use.md).
