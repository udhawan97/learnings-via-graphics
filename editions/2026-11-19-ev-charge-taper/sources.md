# Sources and claim ledger — EV fast-charge taper

- Primary category / established track: `Frontier technology / The Horizon`
- Topic: `Energy storage`
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: `Why does EV fast charging slow near full?`
- Reporting as of (America/Chicago): `2026-11-19`
- Last fact checked: `2026-11-19`

| Claim or section | Status (confirmed/prototype/inference/foundation) | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| Charging power varies with SOC, vehicle type and model year; NREL’s modeled DC fast-charge curves generally decrease around 80–85% SOC. | Confirmed for the cited model and general pattern | https://docs.nrel.gov/docs/fy23osti/87100.pdf | 2023-09 | 2026-11-19 | Figure 5 and pp. 9–10. Curves were developed with industry input for several modeled vehicle classes; they are not measurements of every vehicle. |
| A DC fast charger can offer up to 500 kW, while actual charging power varies by vehicle and battery SOC. | Confirmed public guidance | https://afdc.energy.gov/fuels/electricity-stations | Undated; live page | 2026-11-19 | AFDC also lists battery depletion, capacity, type, vehicle limits and equipment as charging-time factors. Published connector and market details can change; this edition relies only on the rate caveat. |
| Many batteries reduce charging power in the 80–100% range; conditions and trip needs can justify charging beyond 80%. | Confirmed public guidance | https://www.energy.gov/articles/winterizing-your-electric-vehicle | 2024-01-30 | 2026-11-19 | DOE presents this as common guidance, not a universal vehicle rule. The article is winter-focused, so the brief does not generalize its cold-weather advice. |
| The 60 kWh, 120 kW and 40 kW worked example. | Invented example | n/a | 2026-11-19 | 2026-11-19 | Uses idealized `time = energy / average power` before losses. It teaches the relationship and must not be used as a trip-time estimate. |

## Artifacts and validation

- Visuals: `assets/charge-taper.svg`; original conceptual diagram. Its 80% marker represents a common pattern supported by NREL and DOE, not measured data or a vehicle specification.
- Practice: the four-line session card in `brief.md` and `index.html#try`; no account, vehicle, or download required. Success is identifying the observed acceptance rate and explaining why route need matters more than a universal stop percentage.
- Review: pre-draft and exact-final sequential review across facts, domain, teaching, accessibility/design, and safety/minimalism.
- Checks actually run: recorded in the pull request after exact-file link, SVG/XML, markup, word-budget, coverage, and browser checks. Any check not completed remains explicitly unverified.
