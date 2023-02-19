import streamlit as st 
import pandas as pd 
import json
import altair as alt


with open('data/artists_k-pop.json', 'r') as f:
    data = json.load(f)
res = []
for artist in data['artists_k-pop'] :
        spotify_id = artist['id']
        name = artist['name']
        popularity = artist['popularity']
        followers = artist['followers']['total']
        genre =  'k-pop'
        image = artist['images'][0]['url']
        res += [(spotify_id, name, genre, followers, popularity, image)]

with open('data/albums_rap.json', 'r') as f2:
    data2 = json.load(f2)
res2 = []
for album_ar in data2['albums_rap']:
    artist_id = album_ar['artist_id']
    for album in album_ar['items'] :
        name = album['name']
        total_tracks = album['total_tracks']
        art = []
        for ar in album['artists']:
            art.append(ar['name'])
        release_date = album['release_date']
        image = album['images'][0]['url']
        res2.append([artist_id ,name, release_date, art, total_tracks, image])


df = pd.DataFrame(res, columns=['spotify_id', 'name', 'genre', 'followers', 'popularity', 'image']).iloc[:20, :]
df2 = pd.DataFrame(res2, columns=['artist_id' ,'name', 'release_date', 'art', 'total_tracks', 'image'])
df2 = df2.drop_duplicates(subset='name')
st.sidebar.image('./data/Spotify_icon.svg.png', width=40)
st.sidebar.title("My Spotify App")

st.title("My Spotify Dashboard")
st.subheader("Popularity and Followers of RAP genre")

col1, col2 = st.columns(2)


chart1 = alt.Chart(df).mark_bar().encode(
    x='popularity:Q',
    y=alt.Y('name:N', sort='-x')
)


chart = alt.Chart(df).mark_bar().encode(
    x='followers:Q',
    y=alt.Y('name:N', sort='-x')
)

with col1:
    st.altair_chart(chart1, use_container_width=True)
with col2:
    st.altair_chart(chart, use_container_width=True)



ar = st.selectbox("Choose an artists", options=list(df.name))
st.subheader(f"{ar} information")


# df2 = df2.drop_duplicates(subset='name')
# st.dataframe(df2)

i = df[df['name']==ar].spotify_id.iloc[0]
col1, col2 = st.columns(2)
with col1:
     st.image(df[df['name']==ar].image.iloc[0],width=200)

with col2:
     st.write("\n")
     st.write("\n")
     st.write("\n")
     st.write("\n")
     st.write(f"Number of followers : {df[df['name']==ar].followers.iloc[0]}")
     st.write(f"Popularity : {df[df['name']==ar].popularity.iloc[0]}")
     

selected_artist_albims = df2[df2['artist_id']==i]
if len(selected_artist_albims)>=10:
    j=10
else :
    j=len(selected_artist_albims)   

st.subheader(f"Last {j} album : ")

for k in range(j):
     st.write("\n")
     st.write("\n")
     col1, col2, col3= st.columns(3)
     with col2:
        st.image(selected_artist_albims.image.iloc[k],width=150)
     with col3:
        st.write(f"Name of the album : {selected_artist_albims.name.iloc[k]}")
        st.write("Artists : " + ', '.join(selected_artist_albims.art.iloc[k]))
        st.write(f"Total tracks : {selected_artist_albims.total_tracks.iloc[k]}")

