#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats

df = pd.read_csv("/airbnb-ratings-dataset/LA_Listings.csv", encoding="ISO-8859-1")
df.head()

# Read the NY_Listings.csv

df2 = pd.read_csv("/airbnb-ratings-dataset/NY_Listings.csv", encoding="ISO-8859-1")
df2.head()

# Read the airbnb_ratings_new.csv

df3 = pd.read_csv(
    "/airbnb-ratings-dataset/airbnb_ratings_new.csv", encoding="ISO-8859-1"
)
pd.set_option("display.max_columns", None)
df3.head()

df_filtered = df3[df3["Country"] == "United States"]

df_filtered.head()

df.describe()

df2.describe()

df_filtered.describe()

combinedDf = df.append(df2)
df_final = combinedDf.append(df_filtered)

df_final.describe()

# Density Plot and Histogram of variable "Price"

sns.distplot(
    df_final["Price"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Filter the Price to below 500

PriceFilteredData = df_final[df_final["Price"] < 500]

# Density Plot and Histogram of variable "Price"

sns.distplot(
    PriceFilteredData["Price"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Density Plot and Histogram of variable "Bedrooms"

sns.distplot(
    df_final["Bedrooms"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Filter the Bedrooms to below 6

BedroomsFilteredData = df_final[df_final["Bedrooms"] < 6]

# Density Plot and Histogram of variable "Price"

sns.distplot(
    PriceFilteredData["Bedrooms"],
    hist=True,
    kde=False,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Filter the Bathrooms to below 6

BedroomsFilteredData = df_final[df_final["Bathrooms"] < 6]

# Density Plot and Histogram of variable "Bathrooms"

sns.distplot(
    BedroomsFilteredData["Bathrooms"],
    hist=True,
    kde=False,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Density Plot and Histogram of variable "Bedrooms"

sns.distplot(
    df_final["Availability 365"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Density Plot and Histogram of variable "Review Scores Value"

sns.distplot(
    df_final["Review Scores Value"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Density Plot and Histogram of variable "Review Scores Value"

sns.distplot(
    df_final["Reviews per month"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Filter the Bathrooms to below 6

ReviewsFilteredData = df_final[df_final["Reviews per month"] < 10]

# Density Plot and Histogram of variable "Review Scores Value"

sns.distplot(
    ReviewsFilteredData["Reviews per month"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Density Plot and Histogram of variable "Review Scores Value"

sns.distplot(
    df_final["Number of reviews"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

# Filter the Bathrooms to below 6

ReviewsFilteredData = df_final[df_final["Number of reviews"] < 60]

# Density Plot and Histogram of variable "Review Scores Value"

sns.distplot(
    ReviewsFilteredData["Number of reviews"],
    hist=True,
    kde=True,
    bins=int(180 / 5),
    color="darkblue",
    hist_kws={"edgecolor": "black"},
    kde_kws={"linewidth": 1},
)

BedroomsFilteredData = PriceFilteredData[PriceFilteredData["Bedrooms"] < 6]
BathroomsFilteredData = BedroomsFilteredData[BedroomsFilteredData["Bathrooms"] < 6]
filteredData = BedroomsFilteredData[BedroomsFilteredData["Reviews per month"] < 10]
filteredData.corr(method="spearman")

# From the result table, we found that *'Price'* and *'Accommodates'* have a correlation coefficient of 0.55, which indicates they are *moderately* correlated, and *'number of Bedrooms'* has a correlation coefficient of 0.46 with *'Price'*, which is the second highest value in all variables, which can be understand, because more bedrooms a house has, the higher the price can be, and more people a house can accommodates, more expensive it will be.
