# Sources and claim ledger — Salt timing on winter surfaces

- Primary category / established track: `Everyday life / Dad's Field Notes`
- Topic: `Winter surfaces`
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: `Why do road crews salt before snow—and why does more salt stop helping?`
- Reporting as of (America/Chicago): `2026-11-24`
- Last fact checked: `2026-11-24`

| Claim or section | Status (confirmed/prototype/inference/foundation) | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| Anti-icing lowers water's freezing point before a strong pavement bond forms; deicing acts after a bond forms. Timing affects later removal. | Confirmed public guidance | [Federal Highway Administration: How do anti-icing methods work?](https://ops.fhwa.dot.gov/weather/resources/publications/tech_briefs/antiicin.htm) | Undated technical brief | 2026-11-24 | Highway operations use forecasts, calibrated equipment and trained staff. The lesson explains the mechanism; it does not transfer roadway application rates to homes. |
| Sodium chloride has a practical pavement-temperature range around 15–20°F and becomes much less effective below 15°F; pavement and air temperatures can differ. | Confirmed public guidance | [Minnesota Department of Transportation: Maintenance FAQ](https://www.dot.state.mn.us/maintenance/faq.html) | Living guidance; page footer 2026 | 2026-11-24 | The exact result depends on pavement temperature, moisture, concentration, precipitation, wind, surface and time. The 15°F figure is a practical boundary, not sodium chloride's laboratory eutectic temperature. |
| Remove snow before deicing; deicers melt but do not add traction, while sand adds traction but does not melt. | Confirmed public guidance | [Minnesota Stormwater Manual: Winter parking lot and sidewalk maintenance](https://stormwater.pca.state.mn.us/winter_parking_lot_and_sidewalk_maintenance_factsheet) | Undated living factsheet | 2026-11-24 | The factsheet targets winter-maintenance decisions. Household users must still follow product labels and local guidance. |
| Excess salt contributes to freshwater salinization, can harm aquatic life and drinking-water sources, and can damage infrastructure. | Confirmed federal overview | [U.S. Environmental Protection Agency: Salt](https://www.epa.gov/risk/salt) | Undated living overview | 2026-11-24 | Many sources contribute to salinization; the lesson does not attribute every local chloride problem to road salt alone. |
| Clearing first, scattering rather than piling salt, and switching away from ordinary salt below 15°F can reduce unnecessary chloride use. | Confirmed public guidance | [Wisconsin Department of Natural Resources: Help protect our waters by reducing winter salt use](https://dnr.wisconsin.gov/newsroom/release/117216) | 2026-01-16 | 2026-11-24 | The release gives resident-facing guidance. Product instructions and local restrictions remain controlling. |
| The 28°F road-crew scenario and 12°F shaded-walkway scenario | Invented examples | [Salt-timing diagram](assets/salt-timing.svg) | 2026-11-24 | Deliberately fictional. They demonstrate the decision sequence, not a prescription or guarantee. |

## Artifacts and validation

- Visuals: `assets/salt-timing.svg`; original conceptual diagram. Title, description, alt text and adjacent prose distinguish anti-icing, removal, deicing and traction without depending on color.
- Practice: `winter-surface-card.md`; a 15-minute observation and decision worksheet. Success means bulk material is removed where safe, the remaining job is named, the choice follows a label or local guidance, and the surface is scheduled for recheck.
- Review: sequential pre-draft and exact-final review from facts, domain, teaching, accessibility/design and safety/minimalism perspectives.
- Checks actually run: `python3 scripts/check_coverage.py --base origin/main` passed and selected a fresh `Winter surfaces` question in least-covered Everyday life. The repository's RAG, safe-save and coverage test suites passed. Python parsing confirmed resolving local links, unique HTML IDs, valid SVG XML with a title and description, and no template placeholders. The 54-word takeaway and approximately 404-word brief fit their editorial budgets. `git diff --cached --check` passed. The SVG was rendered through Inkscape and visually inspected after a cold-boundary label-fit correction. Local Chromium could not create its singleton socket (`Operation not permitted`), so HTML browser appearance, keyboard, zoom and screen-reader acceptance remain unverified.

**Boundary:** This household learning model is not a road-maintenance plan, a chemical-mixing guide or a promise of safe footing. It cannot account for every surface, product, disability, weather change, drainage path or local rule. Follow product labels and current local guidance; block access or ask for help when clearing is unsafe.
