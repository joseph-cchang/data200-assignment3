#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


fish_df = pd.read_csv('Fish.csv')
toy_df = pd.read_csv("toy_dataset.csv")

st.markdown("""<style>.big-font {font-size:20px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Joseph Chang </p>', unsafe_allow_html=True)
st.markdown("""<style>.big-font {font-size:20px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> DATA 200 Assignment 1</p>', unsafe_allow_html=True)

st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a display of the fish dataframe: </p>', unsafe_allow_html=True)
st.dataframe(fish_df)

if st.button("Click here to see a condensed Dataframe"):
    st.dataframe(fish_df[['Species', 'Weight', 'Height']])
    st.write("This dataframe shows just the columns of Species, Weight, and Height")

# Graph 1
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a histogram: </p>', unsafe_allow_html=True)
n_bins = 10
fig, ax = plt.subplots()
ax.hist(fish_df['Height'], edgecolor = "black")
ax.set_title("Histogram of Height")
ax.set_xlabel('Height Value')
ax.set_ylabel('Count')
st.pyplot(fig)
st.write("This histogram shows the height of the fish. The most common fish height is between the 5.0 - 7.5, with around 40 counts. Overall, the distribution seems skew right.")

# Graph 2
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a scatterplot graph: </p>', unsafe_allow_html=True)
fig, ax = plt.subplots()
ax.scatter(fish_df['Height'], fish_df['Weight'])
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
ax.set_title("Weight vs Height")
st.pyplot(fig)
st.write("This scatterplot is harder to infer, but a exponential graph could be used to infer. After 7.5 in Height, it's more difficult to access.")

# Graph 3
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a bar graph: </p>', unsafe_allow_html=True)
fish_df.groupby(['Species'])['Length1'].mean()
fig, ax = plt.subplots()
species = fish_df['Species'].unique()
mean_ = fish_df.groupby(['Species'])['Length1'].mean()
ax.bar(species, mean_)
ax.set_xlabel('Species')
ax.set_ylabel('Mean of Length1')
ax.set_title('Species by the Mean of Length1')
st.pyplot(fig)
st.write("This bar graph shows the mean of length1 of all the species. Here we can see that on average, Parkki has the highest at around 40. The lowest is Pike at around 11.")

# Graph 4
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a stem plot: </p>', unsafe_allow_html=True)
fig, ax = plt.subplots()
ax.stem(fish_df['Height'], fish_df['Width'])
ax.set_xlabel("Height")
ax.set_ylabel("Width")
ax.set_title("Height vs Width")
st.pyplot(fig)
st.write("This stem plot shows the Height as the x-axis and width as the y-axis. It appears when height is around 10.5-12.5, width is also at the highest at around 8. The graph seems to show a linear trend up until height is 12.")

# Graph 5
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a boxplot: </p>', unsafe_allow_html=True)
fig, ax = plt.subplots()
ax.boxplot(fish_df['Weight'])
ax.set_title("Boxplot of Weight")
ax.set_xlabel('Weight')
ax.set_ylabel('Value')
st.pyplot(fig)
st.write("This shows a boxplot of fish weight. The 25th percetile is around 150. The median or 50th percentile is around 250. The 75th percentile is around 650, and there are some outliers we see as well.")
