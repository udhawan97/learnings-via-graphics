# Grid-balance observation card

[Visual brief](brief.md) · [Full guide](index.html) · [Evidence](sources.md)

Use this paper exercise to explain a grid snapshot without pretending to operate a real system. Estimated time: 20 minutes.

## Scenario

An invented balancing area has:

- demand: **12,000 MW**
- generation: **11,400 MW**
- net imports: **400 MW**
- storage discharge: **0 MW**

For this exercise, supply is generation + net imports + storage discharge.

## Predict before calculating

- [ ] Supply exceeds demand; frequency tends high.
- [ ] Supply matches demand; frequency tends toward scheduled value.
- [ ] Demand exceeds supply; frequency tends low.

## Calculate

1. Total supply: `________ MW`
2. Supply minus demand: `________ MW`
3. Predicted frequency direction: `low / scheduled / high`

## Choose response families

Circle two that could move the balance in the needed direction:

`raise generation` · `lower generation` · `discharge storage` · `charge storage` · `increase imports` · `reduce demand`

Then write one constraint you would need to check: transmission, location, ramp rate, available reserves, energy in storage, or another documented limit.

## Answer guidance

Supply is 11,800 MW, so demand exceeds supply by 200 MW and frequency tends low. Raising generation, discharging storage, increasing imports or reducing demand all point in the corrective direction. This arithmetic does not choose a safe resource: real operators also need system location, limits, timing and reliability procedures.

**Observable success:** You calculate the sign correctly, select two directionally valid response families, and name a constraint without presenting the exercise as real-time operating advice.
