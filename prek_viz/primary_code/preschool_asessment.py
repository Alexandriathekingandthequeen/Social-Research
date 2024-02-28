import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

""" 
Structure:
1. Function to Load GeoSpatial Data: Reads shapefile data into a GeoDataFrame.
2. Function to Load and Clean Preschool Data: Reads CSV data, cleans, and prepares it.
3. Function to Merge Data: Merges GeoDataFrame with DataFrame.
4. Function for Yearly Data and State Plotting: Iterates through years to plot data for each year.
"""

def load_geospatial_data(filepath):
    geo_usa = gpd.read_file(filepath)
    return geo_usa


def load_and_clean_preschool_data(filepath):
    preschool = pd.read_csv(filepath, keep_default_na=False)
    preschool.rename(columns={"state_abbrev": "STUSPS"}, inplace=True)
    preschool.drop("_merge", axis=1, inplace=True)
    return preschool


def merge_dataframes(preschool, geo_usa):
    geo_merge = preschool.merge(geo_usa, on="STUSPS", how='inner')
    geo_merge['Year'] = pd.to_datetime(geo_merge['Year'], format='%Y')
    return geo_merge


def plot_geospatial_data_by_year(geo_merge, result_path):
    geo_gdf = gpd.GeoDataFrame(geo_merge, geometry='geometry')
    unique_years = geo_gdf['Year'].unique()

    for year in unique_years:
        fig, ax = plt.subplots(1, 1, figsize=(35, 20))
        geo_gdf[geo_gdf['Year'] == year].plot(column='RequiredAssessmentforpreK', ax=ax, legend=True, cmap='tab20b', legend_kwds={'loc': 'center left', 'bbox_to_anchor':(1.1, 0.5),'fontsize': 20})
        plt.ylim(25,50)
        plt.xlim(-125, -65)
        plt.title(f'Preschool Assessment Requirements by State (USA) - {year}')

        plt.savefig(result_path / f'Geospatial_Data_{year}.png')
        plt.close() 

def plot_state_assessment_change(geo_gdf, result_path):
    assessment_types = geo_gdf['RequiredAssessmentforpreK'].unique()
    type_to_num = {t: i for i, t in enumerate(assessment_types)}
    
    geo_gdf['type_num'] = geo_gdf['RequiredAssessmentforpreK'].map(type_to_num)
    
    states = geo_gdf['State'].unique()
    for state in states:
        state_data = geo_gdf[geo_gdf['State'] == state].sort_values('Year')
        
        plt.figure(figsize=(12, 6))
        plt.plot(state_data['Year'], state_data['type_num'], marker='o')
        
        for x, y, label in zip(state_data['Year'], state_data['type_num'], state_data['RequiredAssessmentforpreK']):
            plt.text(x, y, label[:5], fontsize=8, ha='right', va='bottom')
        
        plt.title(f'Assessment Type Change Over Years for {state}')
        plt.xlabel('Year')
        plt.ylabel('Assessment Type')
        plt.yticks(range(len(assessment_types)), assessment_types)
        
        plt.savefig(result_state_path / f'Assessment Type Change Over Years for {state}.png') 
        plt.close()


if __name__ == '__main__':
    base_path = Path(__file__).parent
    data_path = base_path / "primary_data"
    result_path = base_path / "primary_result"
    result_path.mkdir(parents=True, exist_ok=True)
    result_year_path = result_path / "annual_spatial_analysis"
    result_year_path.mkdir(parents=True, exist_ok=True)
    result_state_path = result_path / "annual_state_analysis"
    result_state_path.mkdir(parents=True, exist_ok=True)
    
    geo_data_path = data_path
    preschool_data_path = data_path / 'preschool_assessment.csv'
    
    geo_usa = load_geospatial_data(geo_data_path)
    preschool = load_and_clean_preschool_data(preschool_data_path)
    geo_merge = merge_dataframes(preschool, geo_usa)
    print(geo_merge)
    plot_geospatial_data_by_year(geo_merge, result_year_path)
    plot_state_assessment_change(geo_merge, result_state_path)
