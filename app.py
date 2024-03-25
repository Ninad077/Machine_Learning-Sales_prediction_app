import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

model = joblib.load("mymodel.joblib")

st.set_page_config(
    page_title="Sales Prediction app"
)


# Custom CSS to style the sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("##")
st.title(':red[Sales Predictor app]')
st.markdown("""</span>Developed by- <span style='color:blue;'>Ninad S. Mandavkar""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([6, 5,1])

with col1:
    st.title("")
    st.title("")
    st.subheader(":red[Investment revenue]")
    tv = st.slider("**:red[TV Investment]**", min_value=0, max_value=300, value=150)
    radio = st.slider("**:red[Radio Investment]**", min_value=0, max_value=300, value=150)
    newspaper = st.slider("**:red[Newspaper Investment]**", min_value=0, max_value=300, value=150)
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)
    st.subheader(f""":red[Predicted sales:] {prediction[0]:.2f}""")

    # Calculate percentage distribution of investments
    total_investment = tv + radio + newspaper
    tv_percentage = (tv / total_investment) * 100
    radio_percentage = (radio / total_investment) * 100
    newspaper_percentage = (newspaper / total_investment) * 100

    # Create a DataFrame to store percentage distribution
    df = pd.DataFrame({
        'Investment': ['TV', 'Radio', 'Newspaper'],
        'Percentage': [tv_percentage, radio_percentage, newspaper_percentage]
    })

    st.set_option('deprecation.showPyplotGlobalUse', False)

    selected_page = st.selectbox("Visualizations", ["Heatmap", "Boxplot", "Boxplot of preprocessed data (without Outliers)"])

    if selected_page == "Heatmap":
        st.markdown("**:red[Heatmap]**")
        data = pd.read_csv("advertising.csv")
        sns.heatmap(data.corr(), annot=True)
        st.pyplot()
    elif selected_page == "Boxplot":
        st.markdown("**:red[Boxplot]**")
        data = pd.read_csv("advertising.csv")
        plt.boxplot(data)
        st.pyplot()
    elif selected_page == "Boxplot of preprocessed data (without Outliers)":
        st.markdown("**:red[Boxplot of preprocessed data (without Outliers)]**")
        data = pd.read_csv("advertising.csv")
        data_new = data[data["Newspaper"] < 90]
        plt.boxplot(data_new)
        st.pyplot()

with col2:
    
    # Create a donut chart with input_data values
    fig = go.Figure(data=[go.Pie(labels=['TV Investment', 'Radio Investment', 'Newspaper Investment'], values=input_data[0], hole=0.5)])

    # Add prediction value in the center of the donut chart
    fig.add_annotation(text=f"Predicted Sales: {prediction[0]:.2f}", x=0.5, y=0.5, showarrow=False, font=dict(size=14))


    # Display the donut chart with prediction value
    st.subheader("##")
    st.plotly_chart(fig)
    fig.update_layout(
        legend=dict(orientation="h", x=0.5, y=-0.1)
    )

    # Checkbox to preview data
    st.subheader("##")
    if st.checkbox("Preview Data"):
        data = pd.read_csv("advertising.csv")
        st.dataframe(data, width=1000)  # Adjust the width as per your preference
