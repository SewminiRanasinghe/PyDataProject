# ICC Men's Cricket World Cup Analysis

This project analyzes the history of ICC Men's Cricket World Cup matches from 1975 to 2023, focusing on data preparation, visualization, and sentiment analysis.

## Project Overview

The project is divided into four tasks:
1. **GitHub Repository Management**: Maintain a well-structured GitHub repository with meaningful commits and branches.
2. **Data Preparation**: Process and clean World Cup data from CSV files.
3. **Sentiment Analysis**: Use a Hugging Face model to classify the sentiment of 2023 World Cup final match commentaries.
4. **Interactive Dashboard**: Create an insightful dashboard using Plotly Dash to showcase key findings.

## Dataset

- The data consists of detailed statistics from all ICC Men's Cricket World Cup matches (1975–2023).
- Key attributes include match dates, venues, scores, notable players, and commentary excerpts.

## Key Features

### Task 1: GitHub Repository Management
- Proper version control practices with meaningful commits and pull requests.

### Task 2: Data Preparation
- Combine 13 datasets into a unified DataFrame.
- Remove duplicates and handle missing values.
- Add derived columns like `match_status` and `winning_team`.
- Split nested lists into separate columns for detailed analysis.

### Task 3: Sentiment Analysis
- Analyze sentiment in the 2023 World Cup commentary using a Hugging Face model.
- Add a `sentiment` column to the dataset.
- Visualize sentiment distribution.

### Task 4: Dashboard Creation
- Develop an interactive Plotly Dash dashboard with multiple chart types.
- Highlight trends and insights from the data.

### Usage
Run Jupyter notebooks for data preparation and sentiment analysis.
Start the Plotly Dash dashboard:
python dashboard.py
