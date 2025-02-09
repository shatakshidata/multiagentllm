import plotly.graph_objects as go
import pandas as pd
from utils import time_it, log_info

@time_it
def simulate_scenario(df):
    """ Simulates trends and generates visualizations. """
    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(include="object").columns

    if categorical_cols.any():
        cat_col, num_col = categorical_cols[0], numeric_cols[0]
        fig = go.Figure([go.Bar(x=df[cat_col], y=df[num_col])])
        fig.update_layout(title="Scenario Analysis", template="plotly_white")
        fig.show()
    
    log_info("Scenario simulation completed.")
