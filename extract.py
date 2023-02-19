import requests
import json
import base64
from config import client_id, client_secret


class Extractor:
    
    def __init__(self, client_id, client_secret, genre):
       
        self.client_id = client_id
        self.client_secret = client_secret
        self.genre = genre
        self.token = ""

    def get_token(self):
        auth_string = self.client_id + ":" + self.client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode (auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"

        headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
        }

        data  = {"grant_type": "client_credentials"}

        result = requests.post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        self.token  = json_result["access_token"]

    def get_artists(self):
        print(f"Begin download Artists from genre : {self.genre}")
        self.get_token()

        url = 'https://api.spotify.com/v1/search'
        headers = {'Authorization': f'Bearer {self.token}'}
        limit = 50
        params = {'q': f'genre:{self.genre}', 'type': 'artist',  'limit': limit , 'offset' : 0}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
        # Parse the JSON response
            data = response.json()
            artists = data["artists"]["items"]

        # Repeat the API request to get the next pages of results
        while len(artists) < 100:
            params['offset'] += 50
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                artists += data["artists"]["items"]
            else:
                break
        print("Download completed")
        self.artists = artists
        # self.artists = artists
        return artists

   
    
    
    def get_albums(self) :
        print("Begin download Albums for every Rapper given")
        albums = []
        
        for artist in self.artists :
            
            artist_id = artist['id']
            headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
            }

            
            endpoint = "https://api.spotify.com/v1/artists/{artist_id}/albums".format(artist_id=artist_id)

            
            response = requests.get(endpoint, headers=headers)

            
            if response.status_code == 200:
                album = { 
                        'items' : response.json()['items'],
                        'artist_id' : artist_id 
                        }

                albums.append(album)
               
            else:
                
                break
        print("Download completed")
        self.albums = albums
        return self.albums
    
    def get_song(self) :
        tracks = []
        print("Begin download Songs from every album ")
        traks_alb = []
        for art_album in self.albums:
            artist_id = art_album['artist_id']
            for album in art_album['items'] :
                album_id = album['id']

                headers = {
                    "Authorization": "Bearer " + self.token
                }
                
                url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"

                response = requests.get(url, headers=headers)

                # Check that the request was successful
                if response.status_code == 200:
                    # Load the JSON data from the response
                    data = json.loads(response.text)
                    # Get the list of tracks from the response
                    track = data["items"]
                    traks_alb.append({'album_id' : album_id, 'traks' : track})
                else:
                    # Print the error message from the API
                    print("Could not get tracks:", response.text)
                tracks.append({'artist_id' : artist_id, 'tracks' : traks_alb})
        self.tracks = tracks
        print("Download completed")
        return self.tracks

    def store_data(self, file_name, data):
        
       
        with open(f"./dashboard/data/{file_name}.json", "w") as f:
            js = {file_name : data}
            json.dump(js, f)
    






#main
for genre in ['rap', 'k-pop']:
    sp = Extractor(client_id, client_secret, genre )
    sp.get_token()
    artists = sp.get_artists()
    sp.store_data(f"artists_{genre}", artists)
    albums = sp.get_albums()
    sp.store_data(f"albums_{genre}", albums)



