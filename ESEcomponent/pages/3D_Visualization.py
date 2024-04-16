import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.subheader("3D Visualization for the given data")
df = pd.read_csv('new.csv')
st.dataframe(df)
fig = plt.figure(figsize=(10, 10))
# fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Use different colors for each variable
ax.scatter(df['Age'], df['Rating'], df['Positive Feedback Count'], c=df['Age'], cmap='viridis')
ax.scatter(df['Age'], df['Rating'], df['Positive Feedback Count'], c=df['Rating'], cmap='hot')
ax.scatter(df['Age'], df['Rating'], df['Positive Feedback Count'], c=df['Positive Feedback Count'], cmap='cool')

ax.set_xlabel('Age')
ax.set_ylabel('Rating')
ax.set_zlabel('Positive Feedback Count')

st.pyplot(fig)