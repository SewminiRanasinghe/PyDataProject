import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash
# Load the cricket dataset
try:
    df = pd.read_csv("processed_cricket_data.csv")  
except FileNotFoundError:
    print("Error: 'cleaned_cricket_data.csv' not found. Please ensure the file path is correct.")
    exit()

# Check if the necessary columns exist
required_columns = ['team_1', 'team_1_runs', 'team_2', 'team_2_runs', 'match_category', 'world_cup_year']
if not all(col in df.columns for col in required_columns):
    print("Error: The dataset does not contain the required columns. Please check your data preparation.")
    exit()

