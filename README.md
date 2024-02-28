# Social-Research: Data-Driven Approaches to Social Change and Impact

## Preschool Assessment Project
**Supervisor:** Dr. Zhiling Shea  
**Team Members:** Qilin Zhou, Zhang Rui

### Overview
This project focuses on analyzing preschool assessments across various states in the USA. Using a data-driven approach, we aim to understand trends, variations, and impacts of different assessment strategies in early education.

### Data Sources
Our analysis is based on data from two primary sources:

1. **NIEER (National Institute For Early Education Research) State Preschool Yearbooks**
   - Comprehensive data on state-funded preschool programs.
   - Covers enrollment, funding, teacher qualifications, and quality standards.
   - [NIEER State Preschool Yearbooks](https://nieer.org/state-preschool-yearbooks)

2. **United States Census Bureau 2020 Shapefile of U.S. States**
   - Detailed geographic data for all U.S. states, crucial for geospatial analysis.
   - [Census Bureau TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)

### Methodology
Integrating preschool assessment data from the NIEER yearbooks with geospatial data from the Census Bureau to perform comprehensive analysis, including DID model and probit regression.

### Assessment example
Annual Spatial Data: ![Geospatial Data 2020](https://github.com/QilinZhou56/Social-Research/blob/main/prek_viz/primary_result/annual_spatial_analysis/Geospatial_Data_2020-01-01%2000%3A00%3A00.png)
State-level Data: ![Alabama_analysis](prek_viz/primary_result/annual_state_analysis/Assessment%20Type%20Change%20Over%20Years%20for%20ALABAMA.png)

### Objectives
- Evaluate and compare preschool assessment strategies across states.
- Understand the impact of these strategies on early childhood education outcomes.
- Provide data-driven insights for policymakers and educational stakeholders.

### Results and Reflection
- From 2007 to 2018, changes in assessment policies did not lead to improvements in student enrollment or resource allocation in the case analysis of South Carolina and Texas.

- While the assessment policy may not have a direct relationship with the overall performance of state preschool programs, it does reflect the quality of preK education a state aspires to provide and the level of attention it devotes to preK education. Despite the increasing emphasis on new assessment designs, resource allocation and enrollment rates did not increase or remain stable as expected. This calls for a re-evaluation of preschool resource allocation and an examination of the factors influencing household enrollment decisions.

### Tools and Technologies
- **Data Processing and Analysis:** Python, Pandas, NumPy
- **Geospatial Analysis:** GeoPandas, ArcGIS
- **Data Visualization:** Matplotlib, Seaborn
- **Data Management:** Power Query, MySQL

### Interactive Apps:
- Time-series PreK Education Data Visualization: [ArcGIS Visualization](https://arcg.is/nbK4v0)
- Interative Legend Version: [ArcGIS Visualization](https://arcg.is/0f0rHH0)

