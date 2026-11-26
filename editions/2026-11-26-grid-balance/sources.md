# Sources and claim ledger — electric-grid balance

- Primary category / established track: `Frontier technology / The Horizon`
- Topic: `Electric-grid infrastructure`
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: `Why must the power grid keep supply and demand in balance?`
- Reporting as of (America/Chicago): `2026-11-26`
- Last fact checked: `2026-11-26`

| Claim or section | Status (confirmed/prototype/inference/foundation) | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| Balancing authorities maintain real-time supply, demand and interchange; frequency below 60 Hz indicates more demand than available supply, while frequency above 60 Hz indicates more supply than demand. | Confirmed public explanation | https://www.eia.gov/electricity/930-content/about.html | Live reference page; undated | 2026-11-26 | EIA describes the contiguous U.S. interconnections. The lesson does not generalize 60 Hz to regions using a different nominal frequency. |
| Frequency response combines physical behavior, equipment controls and operator-directed balancing over overlapping time scales. | Confirmed public explanation | https://www.energy.gov/cmei/articles/keeping-lights-essential-reliability-services | 2018-09-13 | 2026-11-26 | DOE describes hundredths of seconds through minutes and longer balancing. The brief compresses these into “automatic first, slower actions after” without specifying dispatch timing. |
| Generation, demand, interchange and storage can contribute to balancing; operating reserves help respond to unexpected loss or demand changes. | Confirmed public backgrounder | https://www.energy.gov/sites/default/files/2023-08/Balancing%20Authority%20Backgrounder_2022-Formatted_041723_508.pdf | 2023-08 posting; document formatted 2023-04-17 | 2026-11-26 | DOE lists contingency resources and demand-side measures. Availability depends on local rules and physical constraints. |
| Small mismatches occur continuously; interconnected frequency responds to the combined system and does not identify a disturbance’s cause by itself. | Confirmed concept and bounded inference | https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/rs/reference_document_nerc_balancing_and_frequency_control.pdf | 2021-05-11 | 2026-11-26 | NERC’s reference document is educational, not a compliance standard. The cause-diagnosis limit follows from its explanation of shared interconnection frequency and separate interchange/frequency errors. |
| The 1,000/950 MW brief example and 12,000/11,800 MW practice scenario. | Invented examples | n/a | 2026-11-26 | 2026-11-26 | Teach only imbalance direction. They do not model inertia, frequency magnitude, transmission, voltage, protection or operator procedures. |

## Artifacts and validation

- Visuals: `assets/grid-balance.svg`; original conceptual direction model, not measured data or an operating display.
- Practice: `grid-balance-card.md`; paper-only, no account or equipment. Success is calculating the imbalance sign, predicting frequency direction, naming two response families and one constraint.
- Review: pre-draft and exact-final sequential review across facts, domain, teaching, accessibility/design, and safety/minimalism.
- Checks actually run: recorded in the pull request after exact-file link, SVG/XML, markup, word-budget, coverage and rendering checks. Any check not completed remains explicitly unverified.
