import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("Titanic Data Analysis & Visualization")

# Load Dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "titanic1.csv")

a = pd.read_csv(csv_path)

st.title("Titanic Survival Prediction")

st.dataframe(a)
# Data Cleaning
b = a.dropna()

st.subheader("Cleaned Data")
st.dataframe(b)

# 1. Survival Count
st.subheader("Survival Count")

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.countplot(x="Survived", data=a, ax=ax1)
st.pyplot(fig1)

# 2. Gender
st.subheader("Survival by Gender")

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x="Sex", y="Survived", data=a, ax=ax2)
st.pyplot(fig2)

# 3. Passenger Class
st.subheader("Survival by Passenger Class")

fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.barplot(x="Pclass", y="Survived", data=a, ax=ax3)
st.pyplot(fig3)

# 4. Age
st.subheader("Age Distribution")

fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.histplot(data=a, x="Age", bins=20, ax=ax4)
st.pyplot(fig4)

# 5. Correlation
st.subheader("Correlation Matrix")

corr = a.corr(numeric_only=True)

fig5, ax5 = plt.subplots(figsize=(10, 6))

sns.heatmap(
    corr,
    annot=True,
    cmap="YlGnBu",
    linewidths=0.5,
    ax=ax5
)

ax5.set_title("Correlation Matrix - Titanic Dataset")

st.pyplot(fig5)