# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
df=pd.read_csv("Unfiltered_Movies.csv")
df = df.drop('overview', axis=1)


# %%
df = df.drop('tagline', axis=1)

# %%
df = df.drop('homepage', axis=1)

# %%
df = df.drop('id', axis=1)

# %%
director_name = input("Enter the director's name: ")
result = df[df['director'] == director_name]


# %%
print("\nAvailable columns:")
print(list(df.columns))

# %%
fields = input("\nEnter the columns you want to display (comma-separated): ")
fields = [f.strip() for f in fields.split(',')]
df = result[fields]
df


# %%
df['release_date'] = df['release_date'].apply(lambda x: pd.to_datetime(x, format='%m/%d/%y').strftime('%Y-%m-%d') if isinstance(x, str) and '/' in x else x)
df

# %%
df.to_csv("filtered_movies.csv", index=False)

# %%
df = df.sort_values(by='release_date', ascending=True)
df.plot(kind= 'line', xlabel='release_date', ylabel='popularity')



# %%



