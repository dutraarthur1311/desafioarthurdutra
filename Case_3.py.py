import pandas as pd
import pymysql

connection = pymysql.connect(
    host="35.199.115.174",
    user="looqbox-challenge",
    password="looq-challenge",
    database="looqbox-challenge"
)

# Case 3

# table IMDB_movies
# Generate table and graphic format
# Explain why you chose the visualization(s) 

import matplotlib.pyplot as plt

df_IMDB = pd.read_sql("SELECT * FROM IMDB_movies", connection)

#print(df_IMDB.columns)
# Columns: 'Id', 'Title', 'Genre', 'Director', 'Actors', 'Year', 'Runtime',
# 'Rating', 'Votes', 'RevenueMillions', 'Metascore'

#print(df_IMDB.info()) 
# str: 'Title', 'Genre', 'Director', 'Actors'
# int: 'Id', 'Year', 'Runtime', 'Votes'
# float: 'Rating', 'RevenueMillions', 'Metascore'

#print(df_IMDB.head())
# We can see that the column "Genre" is a list of strings separated with ","

#print(df_IMDB.shape)
# The dataset contains 1000 rows

# Seeing the columns and the original table, I choose 3 ideas of visualizations:
# - Revenue of Horror films over the Years - because I love horror movies
# - Rating X Revenue - to evaluate the relationship between movie ratings and their revenues
# - Top 10 Genres by Average Movie Revenue - to identify which genres generate more revenue in this industry

# 1) Revenue of Horror films over the Years

df_horror = df_IMDB[df_IMDB["Genre"].str.contains("Horror", case=False, na=False)]

revenue_by_year = (df_horror.groupby("Year")["RevenueMillions"].sum().reset_index().sort_values("Year"))

plt.figure(figsize=(10, 5))
plt.plot(
    revenue_by_year["Year"],
    revenue_by_year["RevenueMillions"],
    marker="o"
)
plt.title("Revenue of Horror Movies Over the Years")
plt.xlabel("Year")
plt.ylabel("Revenue (Millions USD)")
plt.grid(True)
plt.show()

# I chose this line visualization because it's easy to see the flow of the revenue over the years,
# and we can see more clearly when it goes up or down


# 2) Rating X Revenue

# To drop null information to not affect the analyses
df_Ratings = df_IMDB.dropna(subset=["Rating", "RevenueMillions"])

plt.figure(figsize=(10, 6))
plt.scatter(df_Ratings["Rating"],df_Ratings["RevenueMillions"])

plt.title("Movie Rating vs Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue in Millions")
plt.grid(True)
plt.show()

# I choosed this scatter plot because it allows us to identify more clearly the relationship of the two variables 


# 3) Top 10 Genres by Average Movie Revenue

# To drop null information to not affect the analyses
df_Revenue = df_IMDB.dropna(subset=["RevenueMillions"]).copy()

# To separate the column "Genre" and to see put in a structure more easy to work with (in lines)
df_Revenue["Genre"] = df_Revenue["Genre"].str.split(",")
df_Revenue = df_Revenue.explode("Genre")
df_Revenue["Genre"] = df_Revenue["Genre"].str.strip()

genre_revenue = (df_Revenue.groupby("Genre")["RevenueMillions"].mean().sort_values(ascending=False).head(10))

plt.figure(figsize=(10, 6))
genre_revenue.sort_values().plot(kind="barh")

plt.title("Top 10 Genres by Average Movie Revenue")
plt.xlabel("Average Revenue in Millions")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

# I choosed this horizontal bar because it allows us to identify see the difference of revenue performance of each genre