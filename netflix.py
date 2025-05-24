import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\games\netflix\netflix_titles.csv", encoding='latin1')

df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

# bar charts for movie and tv shows

type_count = df['type'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(type_count.index, type_count.values, color=['skyblue', 'orange'])
plt.title('Number of Movies Vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# distributed content rating

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Content Ratings')
plt.tight_layout()
plt.show()

# distributed duration of movies

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8, 6))
plt.hist(movie_df['duration_int'],bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.show()

# visualizating release years vs number of shows

release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.scatter(release_count.index, release_count.values, color='red')
plt.title('Release year VS Number of Shows')
plt.xlabel('Release year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.show()

# Number of Shows in top 10 countries

country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries by Number Of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

content_by_year = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# first subplot:movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Released per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Numbers of Movies')

# second subplot:movies

ax[0].plot(content_by_year.index, content_by_year['TV Show'], color='red')
ax[0].set_title('Tv show Released per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Numbers of Movies')

fig.suptitle('Comparison of movies and TV Shows Released Over Years')
plt.tight_layout()
plt.show()