# Sources and claim ledger — robot grasp pipeline

- Primary category / established track: `Frontier technology / The Horizon`
- Topic: `Robotics`
- Reading layers: [Visual brief](brief.md) · [Full guide](index.html)
- Edition title: `Why can a robot see a cup but still miss the pick?`
- Reporting as of (America/Chicago): `2026-11-22`
- Last fact checked: `2026-11-22`

| Claim or section | Status | Primary source URL | Source publication/update date | Access date | Notes, competing evidence and uncertainty |
| --- | --- | --- | --- | --- | --- |
| Robotic grasping can be evaluated through distinct kinematic and kinetic capabilities rather than one “works” label. | Foundation | [NIST grasping performance metrics](https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/grasping) | Updated 2026-05-29 | 2026-11-22 | NIST separates motion/pose measures from force/effort measures. The brief's four gates are an editorial synthesis, not a NIST standard pipeline. |
| Object pose estimation compares the hand-estimated Cartesian pose with a reference-measured pose; visual occlusion can occur during grasping. | Confirmed | [NIST grasping performance metrics](https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/grasping) | Updated 2026-05-29 | 2026-11-22 | Supports the distinction between recognition and grasp-ready pose. It does not specify a universal acceptable error. |
| Touch sensitivity, force tracking, grasp strength and slip resistance are separately measurable properties. | Confirmed | [NIST grasping performance metrics](https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/grasping) | Updated 2026-05-29 | 2026-11-22 | These properties interact in a system; separate metrics do not imply independent behavior during every task. |
| Benchmark protocols measure grasp strength, cycle time, finger strength and repeatability to characterize end effectors and match capabilities to applications. | Confirmed | [Falco et al., NIST publication page](https://www.nist.gov/publications/benchmarking-protocols-evaluating-grasp-strength-grasp-cycle-time-finger-strength-and) | Published 2020-04-01 | 2026-11-22 | Peer-reviewed IEEE Robotics and Automation Letters paper. The edition does not reproduce its apparatus or quantitative results. |
| Novel objects and uncertainty from clutter, random configurations and human behavior remain meaningful manipulation challenges; object properties include transparency, deformability and weight. | Confirmed competition context | [2024 Robotic Grasping and Manipulation Competition](https://www.nist.gov/publications/robotic-grasping-and-manipulation-competition-2024-ieeeras-international-conference) | Published 2024-09-24; updated 2024-10-25 | 2026-11-22 | Competition tasks test systems under specified scenarios. Results do not establish universal robot capability. |
| Ongoing NIST work develops test methods, artifacts, datasets and standards for grasping and manipulation. | Current program context | [NIST grasping, manipulation and contact safety project](https://www.nist.gov/programs-projects/grasping-manipulation-and-contact-safety-performance-robotic-systems) | Updated 2026-10-01 | 2026-11-22 | Ongoing program information is current context, not independent evidence that any particular commercial robot meets a capability threshold. |

## Artifacts and validation

- Visual: `assets/grasp-pipeline.svg`; original conceptual diagram with accessible title/description and adjacent text. No measurements or benchmark values are depicted.
- Practice: `review-card.md`; observation worksheet requiring explicit unknowns and a bounded conclusion. It does not qualify a robot or replace controlled testing.
- Review: pre-draft and exact-final Facts, Domain, Teaching, Accessibility/design, and Safety/minimalism reviews performed sequentially.
- Checks actually run: recorded in the pull request. Browser rendering, keyboard, zoom and screen-reader checks must be reported separately from static parsing.
