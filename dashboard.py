import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash
# Load the cricket dataset
try:
    df = pd.read_csv("processed_cricket_data.csv")
  
except FileNotFoundError:
    print("Error: 'processed_cricket_data.csv' not found. Please ensure the file path is correct.")
    exit()

# Check if the necessary columns exist
required_columns = ['team_1', 'team_1_runs', 'team_2', 'team_2_runs', 'match_category', 'world_cup_year']
if not all(col in df.columns for col in required_columns):
    print("Error: The dataset does not contain the required columns. Please check your data preparation.")
    exit()

# Initialize the Dash app
app = Dash(__name__)

#Layout
app.layout = html.Div([
    html.H1("Cricket World Cup Dashboard", style={'textAlign': 'center'}),
    dcc.Tabs([
        #Add Team Performance Tab
        dcc.Tab(label='Team Performance', children=[
            dcc.Graph(
                id='team-performance',
                figure=px.histogram(df, x='team_1', y='team_1_runs', color='team_1',
                              title="Runs Scored by Teams",
                              labels={'team_1': "Team", 'team_1_runs': "Total Runs"})
            )
        ]),
        # Tab 2: Match Outcomes
        dcc.Tab(label='Match Outcomes', children=[
            dcc.Graph(
                id='match-outcomes',
                figure=px.pie(df, names='match_category', title="Match Outcomes Distribution")
            )
        ]),
        # Tab 3: Yearly Trends
        dcc.Tab(label='Yearly Trends', children=[
            dcc.Graph(
                id='yearly-trends',
                figure=px.line(df, x='world_cup_year', y='team_1_runs', color='team_1',
                               title="Runs Scored Over the Years",
                               labels={'world_cup_year': "Year", 'team_1_runs': "Runs Scored"})
            )
        ]),
        

        # Tab 4 : Performance Scatter
        dcc.Tab(label='Performance Scatter', children=[
            dcc.Graph(
                id='scatter-performance',
                figure=px.scatter(df, x='team_1_runs', y='team_1_wickets', color='team_1',
                                  title="Runs vs Wickets by Teams",
                                  labels={'team_1_runs': "Runs Scored", 'team_1_wickets': "Wickets Lost"})
            )
        ]),

        # Tab 5: Win Margin Analysis
        dcc.Tab(label='Win Margins', children=[
        dcc.Graph(
                id='win-margins',
                figure=px.histogram(df, x='result',
                                    title="Win Margin Distribution",
                                    labels={'result': "Win Margin"})
            )
        ]),
        # Tab 6: Host Countries
        dcc.Tab(label='Host Countries', children=[
            dcc.Graph(
                id='host-map',
                figure=px.scatter_geo(df, locations="host_country", locationmode="country names",
                                      title="World Cup Hosting Locations",
                                      hover_name="host_country")
            )
        ]),
  ])
  
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)