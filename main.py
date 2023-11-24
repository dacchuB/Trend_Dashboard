import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV
file_path = "shopping_trends.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)

# Streamlit App
st.title("Customer Shopping Trends Dashboard")

# Gender Distribution
st.subheader("Gender Distribution")
gender_counts = df['Gender'].value_counts()
st.bar_chart(gender_counts)

# Category-wise Sales
st.subheader("Category-wise Sales")
category_counts = df['Category'].value_counts()
st.bar_chart(category_counts)

# Season-wise Sales
st.subheader("Season-wise Sales")
season_counts = df['Season'].value_counts()
st.bar_chart(season_counts)

# Subscription Status Distribution
st.subheader("Subscription Status Distribution")
subscription_counts = df['Subscription Status'].value_counts()
st.bar_chart(subscription_counts)

# Payment Method Distribution
st.subheader("Payment Method Distribution")
payment_counts = df['Payment Method'].value_counts()
st.bar_chart(payment_counts)

# Shipping Type Distribution
st.subheader("Shipping Type Distribution")
shipping_counts = df['Shipping Type'].value_counts()
st.bar_chart(shipping_counts)

# Color Distribution
st.subheader("Color Distribution")
color_counts = df['Color'].value_counts()
st.bar_chart(color_counts)
