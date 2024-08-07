import pandas as pd
import plotly.express as px
import streamlit as st

def load_data(filepath):
    """Load the dataset from a CSV file."""
    return pd.read_csv(filepath)

def create_histogram(df):
    """Create and display a histogram for the 'fuel' column."""
    st.write('Creating a histogram for the car sales dataset')
    st.write('This chart allows us to see which fuel type is most commonly used by our customers')
    
    fig = px.histogram(df, x="fuel")
    st.plotly_chart(fig, use_container_width=True)

def create_scatter_plot(df):
    """Create and display a scatter plot for 'model_year' vs 'price'."""
    st.write('Creating a scatter plot for the car sales dataset')
    st.write('This chart shows the price of cars in relation to the model year')
    
    filtered_df = df[df['model_year'] != 0]
    fig = px.scatter(filtered_df, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)

def main():
    """Main function to run the Streamlit app."""
    df = load_data('new_csv.csv')

    st.title("VEHICLES ANALYSIS")

    st.write(
        """
        Welcome to the Vehicle Analysis application! This app allows you to visualize various aspects of a car sales dataset. 
        You can generate histograms to see the distribution of fuel types and scatter plots to analyze the relationship 
        between car prices and model years.
        """
    )

    st.dataframe(df)  # Displays the df in the app

    hist_button = st.button('Create Histogram')
    if hist_button:
        create_histogram(df)

    scatter_button = st.checkbox('Create Scatter Plot')
    if scatter_button:
        create_scatter_plot(df)

if __name__ == '__main__':
    main()
