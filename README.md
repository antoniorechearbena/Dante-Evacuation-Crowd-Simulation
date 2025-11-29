# Dante-Evacuation-Crowd-Simulation
Agent-based evacuation simulation of the Dante building (Tilburg University) using NetLogo 3D. Analyzes evacuation time, crowd crush risk, and hazardous bottlenecks via pressure based modeling, statistical analysis, and spatial heatmaps.

# Modeling Evacuation Crowd Crush in the Dante Building

This project studies evacuation dynamics and crowd crush risk in the Dante building at Tilburg University using an agent-based simulation implemented in NetLogo 3D.

High-density evacuations can lead to dangerous crowd crush conditions, particularly at architectural bottlenecks such as stairwells and exits. Since real-world experimentation in such scenarios is not feasible, this project uses computational modeling to analyze evacuation performance and identify high-risk locations under full-occupancy conditions.

---

## Research Questions

1. How does population size affect evacuation time and efficiency?
2. What are the hazardous locations in the Dante building during high-density evacuation?

---

## Methodology

- 3D agent-based model of the Dante building implemented in **NetLogo 3D**
- Agents navigate using an exit-distance flood-fill algorithm
- Crowd crush modeled through **pressure accumulation** caused by sustained immobilization
- One simulation tick represents one real-world second
- Multiple population sizes tested with repeated simulation runs
- Statistical analysis performed using **ANOVA** and power analysis
- Spatial analysis conducted using **aggregated pressure heatmaps**

---

## Key Findings

- Evacuation time increases approximately linearly with population size
- Evacuation efficiency saturates at higher occupancies due to staircase and exit constraints
- The proportion of injured agents increases with crowd size and stabilizes at extreme densities
- Hazardous locations consistently emerge at:
  - Stairwell entrances and landings  
  - Narrow corridor junctions near large lecture halls  
  - Areas immediately upstream of exits  

These findings show that crowd crush risk is primarily driven by **structural bottlenecks and sustained immobility**, rather than panic or individual behavior.

---

## Data and Validation

Simulation output data were analyzed statistically using aggregated results from multiple runs.  
In addition, real evacuation and emergency response data from past **Dante building BHV exercises** are available, allowing for future validation and calibration of the model’s evacuation times, pressure thresholds, and congestion locations.

---

## Repository Structure


