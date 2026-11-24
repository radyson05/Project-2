# Decision Memo — Sentinel Allocation

> **AI disclosure:** I used ChatGPT/Codex for brainstorming the interface, drafting code, and editing documentation. I reviewed the logic and own the analysis and decision. **Education only; not investment advice.**

**To:** Investment Committee  
**From:** Ross Dyson, Portfolio Analyst  
**Date / data as of:** 2026-11-22  
**Decision requested:** Approve a constrained **pilot** allocation, not an organization-wide adoption.

## Recommendation

Allocate **5–10%** of the model sleeve to Sentinel for one quarter. Rebalance monthly only upon a regime change or a five-percentage-point drift. Do not increase the allocation unless the pilot completes with valid point-in-time data, observed costs below 35 bps, and no more than one VaR exception.

The supplied snapshot is **risk-off**. Sentinel therefore holds SPY 15%, VXUS 10%, IEF 35%, GLD 20%, and BIL 20%. It passes all stated limits in the app. This is a process recommendation based on reproducible teaching inputs—not a forecast or a recommendation to trade these securities.

## Mandate and evidence

| Item | Definition |
| --- | --- |
| Objective | Preserve real capital while seeking balanced growth |
| Universe | SPY, VXUS, IEF, GLD, BIL |
| Benchmark | 60/40-style transparent baseline: 30/20/25/10/15 |
| Risk measure | One-month 95% parametric VaR using annualized supplied volatilities |
| Limits | VaR ≤6%; BIL ≥10%; any asset ≤45%; equities ≤60% |

The app visibly tests Sentinel against equal weight and the transparent 60/40-style baseline. Each receives a pass/fail verdict with the failed mandate rule. The signal is intentionally simple: only call risk-off when lagged 12-month SPY momentum is negative and a Treasury-curve proxy is inverted. This conjunction reduces whipsawing relative to either component alone, but it may also react late.

## Sensitivity and failure condition

I stressed signal state, transaction cost (0–100 bps), and the VaR limit in the UI. Under the supplied risk-off signal and a limit tighter than 4.5%, the process stops: the app directs the analyst to hold BIL and escalate rather than force an optimizer into a misleading answer. The process also pauses after a 7% one-month loss, timestamp/data-integrity failure, or two consecutive out-of-sample VaR breaches.

## Principal risks and monitoring

The principal risks are estimation error, changing correlations, ETF implementation frictions, lagged regime recognition, and a data feed that accidentally includes unavailable information. Monitor signal inputs and timestamps, realized turnover costs, drift, one-month loss, and VaR exceptions monthly. A production candidate requires licensed source data, a walk-forward backtest, and independent risk review.

## Committee ask

Approve the 5–10% one-quarter pilot only, with the monitoring triggers above. Reject full adoption at this time because the included research inputs are intentionally instructional and no live out-of-sample evidence has yet been collected. The complete AI-use and validation record is in [validation-and-ai-use.md](validation-and-ai-use.md).
