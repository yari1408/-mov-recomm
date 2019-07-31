import pandas as pd 
import numpy as np 
df1=pd.read_csv('credits.csv')
df2=pd.read_csv('movies.csv')
df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')
b=df2.head(5)
print(b)

#demographic filteringg
C= df2['vote_average'].mean()
print(C) #So, the mean rating for all the movies is approx 6 on a scale of 10

m= df2['vote_count'].quantile(0.9)
print(m)

q_movies = df2.copy().loc[df2['vote_count'] >= m]
a=q_movies.shape
print(a)#We see that there are 481 movies which qualify to be in this list


def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)

#Print the top 15 movies
y=q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10)
print(y)


pop= df2.sort_values('popularity', ascending=False)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,4))

plt.barh(pop['title'].head(6),pop['popularity'].head(6), align='center',
        color='skyblue')
plt.gca().invert_yaxis()
plt.xlabel("Popularity")
plt.title("Popular Movies")
plt.show()





