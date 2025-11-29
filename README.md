# Dante-Evacuation-Crowd-Simulation
Agent-based evacuation simulation of the Dante building (Tilburg University) using NetLogo 3D. Analyzes evacuation time, crowd crush risk, and hazardous bottlenecks via pressure based modeling, statistical analysis, and spatial heatmaps.

## Modeling Evacuation Crowd Crush in the Dante Building

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

## Code overview

### NetLogo model

- **`NetLogo Simulation.nlogox3d`**  
  Core agent-based model of the Dante building in NetLogo 3D.  
  - Builds a multi-floor grid of the building (lecture halls, corridors, stairwells, exits).  
  - Spawns agents according to realistic occupancy (majority on the ground floor).  
  - Uses a flood-fill “exit score” field so agents always try to move to patches closer to an exit.  
  - Updates a **pressure** variable when agents are stuck because all neighboring patches are blocked; sustained high pressure is used as a proxy for crowd-crush risk.  
  - BehaviorSpace is used to run many simulations for different population sizes and record outputs such as `ticks`, `injury-count`, and agent counts.

### Statistical analysis scripts

- **`Stats 1.py`** and **`Stats 2.py`**  
  Python scripts for cleaning BehaviorSpace output and producing the evacuation-time figure. {index=1}  
  - Load the raw CSV exported from NetLogo (one row per tick per run).  
  - Drop redundant configuration columns (open exits, panic settings, etc.).  
  - Ensure `number-people`, `[run number]`, and `ticks` are numeric and sorted.  
  - Compute the maximum `ticks` per run and then the mean duration per population size.  
  - Plot **“Average Time to Complete Run by Population Size”** and save it as an image.

- **`Stats for MAS - Part 2.ipynb`**  
  Jupyter notebook with the main statistical analysis used in the report:  
  - Computes evacuation speed (population size / ticks) and injury ratios.  
  - Produces the scatterplots for evacuation speed vs. population and injured-people ratio vs. population. 
  - Runs inferential statistics (e.g., ANOVA) over the different population levels.

### Heatmap generation

- **`Pressure Heatmap.ipynb`**  
  Notebook that aggregates per-patch pressure over all runs to identify hazardous locations:  
  - Reads the cleaned simulation output with per-patch pressure values.  
  - Aggregates pressure across runs and clips extreme values to make the map readable.  
  - Produces the **pressure heatmap** used in the report to highlight stairwells, corridor junctions, and exit-adjacent hotspots.





