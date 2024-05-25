import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(layout="wide")

# Function to read and display the CSV file
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to create and display various plots
def display_plots(data):
    # Score distribution plot
    # st.write("## Score Distribution")
    st.markdown("<h2 style='color: black;'>Score Distribution</h2>", unsafe_allow_html=True)
    unique_column = 'model'
    unique_values = data[unique_column].unique()

    # Create a subplot figure with 1 row and 3 columns
    fig = make_subplots(rows=1, cols=3, subplot_titles=[f'{unique_value} Distribution' for unique_value in unique_values])

    # Add a histogram for each unique value
    for i, unique_value in enumerate(unique_values):
        subset = data[data[unique_column] == unique_value]
        fig.add_trace(
            go.Histogram(x=subset['score'], nbinsx=10, name=f'{unique_value}'),
            row=1, col=i+1
        )

    # Update the layout to fix the x-axis range from 1 to 10 for all subplots
    fig.update_xaxes(range=[1, 10], row=1, col=1)
    fig.update_xaxes(range=[1, 10], row=1, col=2)
    fig.update_xaxes(range=[1, 10], row=1, col=3)

    # Update layout for overall title and spacing
    fig.update_layout(title_text="Score Distribution by Model", showlegend=False)

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    # Time distribution plot
    st.markdown("<h2 style='color: black;'>Time Distribution</h2>", unsafe_allow_html=True)
    # st.write("## Time Distribution")
    unique_column = 'model'
    unique_values = data[unique_column].unique()

    # Create a subplot figure with 1 row and 3 columns
    fig = make_subplots(rows=1, cols=3, subplot_titles=[f'{unique_value} Distribution' for unique_value in unique_values])

    # Add a histogram for each unique value
    for i, unique_value in enumerate(unique_values):
        subset = data[data[unique_column] == unique_value]
        fig.add_trace(
            go.Histogram(x=subset['time'], nbinsx=10, name=f'{unique_value}'),
            row=1, col=i+1
        )

    # Update the layout to fix the x-axis range appropriately
    max_time = data['time'].max()
    fig.update_xaxes(range=[1, max_time], row=1, col=1)
    fig.update_xaxes(range=[1, max_time], row=1, col=2)
    fig.update_xaxes(range=[1, max_time], row=1, col=3)

    # Update layout for overall title and spacing
    fig.update_layout(title_text="Time Distribution by Model", showlegend=False)

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    # Score vs Time scatter plot
    # st.write("## Score vs Time")
    st.markdown("<h2 style='color: black;'>Score vs Time</h2>", unsafe_allow_html=True)
    fig3 = px.scatter(
        data, 
        x='score', 
        y='time', 
        title='Score vs Time',
        color='model',  # Color by model to differentiate between them
        size='score',  # Size by score to emphasize higher scores
        hover_data=['model']
    )

    # Optionally reverse the y-axis to show that lower time is better
    fig3.update_yaxes(autorange="reversed")

    st.plotly_chart(fig3)

    # Radar chart for model comparison
    st.markdown("<h2 style='color: black;'>Model Comparison Radar Charts</h2>", unsafe_allow_html=True)
    # st.write("### Model Comparison Radar Charts")
    # Create two columns for side-by-side radar charts
    col1, col2 = st.columns(2)

    # Radar chart for score
    with col1:
        categories = data['model'].tolist()
        values_score = data['score'].tolist()

        fig_score = go.Figure()
        fig_score.add_trace(go.Scatterpolar(
            r=values_score + [values_score[0]],  # close the loop
            theta=categories + [categories[0]],  # close the loop
            fill='toself',
            name='Score'
        ))

        fig_score.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(values_score) * 1.1]  # Add some space to the max value
                )),
            showlegend=False,
            title="Radar Chart for Model Comparison (Score)"
        )

        st.plotly_chart(fig_score)

    # Radar chart for time
    with col2:
        values_time = data['time'].tolist()

        fig_time = go.Figure()
        fig_time.add_trace(go.Scatterpolar(
            r=values_time + [values_time[0]],  # close the loop
            theta=categories + [categories[0]],  # close the loop
            fill='toself',
            name='Time'
        ))

        fig_time.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(values_time) * 1.1]  # Add some space to the max value
                )),
            showlegend=False,
            title="Radar Chart for Model Comparison (Time)"
        )

        st.plotly_chart(fig_time)
        
    # Box plot for scores by model
    st.markdown("<h2 style='color: black;'>Scores by Model</h2>", unsafe_allow_html=True)
    # st.write("### Scores by Model")
    fig5 = px.box(data, x='model', y='score', title='Scores by Model', color='model')
    st.plotly_chart(fig5)

def main():

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    # left_co, cent_co,last_co = st.columns(3)
    # with cent_co:
    st.image('../Images/fitbot2.png', width = 300)

    # Load data from the local Stats.csv file
    try:
        data = load_data('Stats.csv')

        display_plots(data)
    except FileNotFoundError:
        st.error("The file 'Stats.csv' was not found. Please ensure it is in the same directory as this script.")

if __name__ == "__main__":
    main()