import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("📊 Sample Streamlit App")

# Sidebar
st.sidebar.header("User Input")

num_points = st.sidebar.slider("Number of random points", min_value=10, max_value=1000, value=100)

# Generate random data
x = np.random.randn(num_points)
y = np.random.randn(num_points)
data = pd.DataFrame({'X': x, 'Y': y})

# Show DataFrame
st.subheader("🔍 Randomly Generated Data")
st.write(data.head())


# Plot
st.subheader("📈 Scatter Plot")
fig, ax = plt.subplots()
ax.scatter(x, y, color='green', alpha=0.6)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
st.pyplot(fig)

# User input
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👋")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Uploaded Data")
    st.write(df)







