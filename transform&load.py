import json
import psycopg2
import pandas as pd




"""
    << transform >>
    load json data from local directory 
    filter the data and take the columns that we need

"""


file_names = ['artists_rap', 'artists_k-pop', 'albums_rap','albums_k-pop']
results = {}

for file_name in file_names:
    with open(f"./dashboard/data/{file_name}.json", "r") as f :
        results[file_name] = json.load(f)

 #load artists   
data = {}
for i in ['artists_rap', 'artists_k-pop']:
    data[i] = []
    result = results[i]
    for artist in result[i] :
        spotify_id = artist['id']
        name = artist['name']
        popularity = artist['popularity']
        followers = artist['followers']['total']
        genre =  i.split('_')[1]
        
        data[i] += [(spotify_id, name, genre, followers, popularity)]

final_data = data['artists_rap']+data['artists_k-pop']


"""
    << Load >>
    load the data into a postgres database using psycopg2 connector    
"""

conn = psycopg2.connect(
    host="localhost", 
    database='postgres',
    user='postgres',
    password='mounir',
    port='5431'
)
cur = conn.cursor()
for row in final_data :
    cur.execute("INSERT INTO artists (spotify_id, name, genre, followers, popularity) VALUES (%s, %s, %s, %s, %s)", row)


conn.commit()

# Close the cursor and connection
cur.close()
conn.close()





"""
    << transform >>
    load json data from local directory 
    filter the data and take the columns that we need

"""

data1= {}
for i in ['albums_rap', 'albums_k-pop']:
    data1[i] = []
    result = results[i]
    for album in result[i] :
        artist_id = album['artist_id']
        for ab in album['items']:
            album_id = ab['id']
            name = ab['name']
            artists = ", ".join([i['name'] for i in ab['artists'] ])
            release_date = ab['release_date']
            image = ab['images'][0]['url']
            total_tracks = ab['total_tracks']
            
            data1[i] += [(artist_id, album_id, name, artists, release_date, image, total_tracks)]

final_data = data1['albums_rap']+data1['albums_k-pop']
df = pd.DataFrame(final_data)
df.columns = ['artist_id', 'album_id', 'name', 'artists', 'release_date', 'image', 'total_tracks']

df = df.drop_duplicates(subset=['name'])
df['total_tracks'] = df['total_tracks'].astype('int')




"""
    << Load >>
    load the data into a postgres database using psycopg2 connector    
"""

conn = psycopg2.connect(
    host="localhost", 
    database='postgres',
    user='postgres',
    password='mounir',
    port='5431'
)
cur = conn.cursor()



for i in range(len(df)) :
    artist_id = df.iloc[i, 0]
    album_id = df.iloc[i, 1]
    name = df.iloc[i, 2]
    artists = df.iloc[i, 3]
    release_date = df.iloc[i, 4]
    image = df.iloc[i, 5]
    total_tracks = int(df.iloc[i, 6])
    row = (artist_id, album_id, name, artists, release_date, image, total_tracks)
    cur.execute("INSERT INTO albums (artist_id, album_id, name, artists, release_date, image, total_tracks) VALUES (%s, %s, %s, %s, %s, %s, %s)", row)


conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
