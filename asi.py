#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Titanic Dataset")
#import dataset
df = pd.read_csv('titanic.csv')
#First thirty rows
tips = df.head(10)
#Display the table
st.table(tips)

#bar plot
st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()
################
#pairplot
st.subheader("Pairplot")
sns.pairplot(tips,palette='rainbow')
st.pyplot()
#######
st.subheader("Heatmap")
sns.heatmap(tips.corr)
st.pyplot()