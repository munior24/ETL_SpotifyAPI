# Spotify Data Extractor
This is a Python script that extracts data on artists, albums, and tracks from the Spotify API. It currently supports two genres, Rap and K-Pop.

The script uses the following Python libraries:

Requests: to make API requests to Spotify
JSON: to handle JSON data returned by the API
Base64: to encode the client ID and secret for authentication
## How to Use
Create a Spotify Developer account and register your application to get your client ID and client secret.
Clone the repository to your local machine.
Install the necessary Python libraries by running pip install -r requirements.txt.
Set your client ID and client secret in the config.py file.
Run the script by running python extractor.py.
The script will download data for the specified genres, and save them in separate JSON files in the dashboard/data directory.
## Extract.py Overview :
### Class Overview
Extractor
This class is the main class of the script. It initializes with the client ID, client secret, and genre of the music. The class methods are:

**get_token()** : This method makes a request to the Spotify API to get an access token. It uses the client_id and client_secret to authenticate the request, and stores the access token for future API requests.

**get_artists()** : This method searches for artists in the specified genre using the Spotify API. It uses the access token obtained from get_token(). It returns a list of artists that match the search criteria.

**get_albums()** : This method retrieves the albums for each artist returned by get_artists(). It returns a list of dictionaries, where each dictionary contains the album details for an artist.

**get_song()** : This method retrieves the songs from each album returned by get_albums(). It returns a list of dictionaries, where each dictionary contains the song details for an artist and album.

**store_data()** : This method saves the extracted data to a JSON file.
## Trasnform&load Overview :
The script performs data loading and transformation operations using Python and PostgreSQL. It loads data from JSON files, filters the data to take only the required columns, and inserts the transformed data into a PostgreSQL database using the psycopg2 connector.

The first part of the code loads data from two JSON files that contain information about rap and K-pop artists. The required columns are extracted, and the data is combined and stored in a list. This list is then used to insert data into the PostgreSQL database.

The second part of the code loads data from two JSON files that contain information about rap and K-pop albums. The required columns are extracted, and the data is stored in a Pandas DataFrame. This DataFrame is then used to insert data into the PostgreSQL database.

The code requires a PostgreSQL database to be set up and configured with the correct credentials. The psycopg2 connector is used to connect to the database and perform the insertion of data.
# Dashboard :
## How to use :
### With Docker file : 
Install Docker on your machine if it's not already installed.

1 - Clone this repo 

2 - Open a terminal or command prompt and change directory to the dashboard directory  and run the following command to build the Docker image:

`docker build -t my-image-name` 

3 - Once the image has been built, run the following command to start a Docker container with your Streamlit app:

`docker run -p 8501:8501 my-image-name`


4 - Open a web browser and go to http://localhost:8501 to access the dashboard.

### With Terminal :
1 - Clone this repo 

2 - Open a terminal or command prompt and change directory to the dashboard directory  and run the following command :

`streamlit run Rap.py`

## Overview :
This is a Python code for a Spotify dashboard that uses the Streamlit library to display data about rap artists and their albums. The code imports the required libraries such as Streamlit, Pandas, JSON, and Altair. It loads two JSON files containing information about rap artists and their albums respectively, and extracts the necessary information such as artist name, popularity, followers, album name, total tracks, etc.

The dashboard is divided into two sections: popularity and followers of rap artists, and information about a selected artist and their last 10 albums. The popularity and followers section displays two bar charts using the Altair library, one for popularity and one for followers, with the names of the artists sorted by their respective metrics.

The information about a selected artist and their last 10 albums is displayed below. The user can select an artist from a dropdown menu and the code retrieves the necessary information from the data frames created earlier. It displays the artist's image, number of followers, and popularity, and the names of their last 10 albums along with their respective cover images, total tracks, and artist names.

## The Dasboard :
![Alt text](https://github.com/munior24/ETL_SpotifyAPI/blob/main/dash.png?raw=true)

