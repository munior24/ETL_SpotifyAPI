# Spotify Genre Extractor
This is a Python script that extracts data from the Spotify API for a specified genre of music, and saves the extracted data as JSON files.

## Requirements
To run this script, you will need to have the following installed:

Python 3
requests
json
base64
Spotify API credentials (client ID and client secret)
## How to Use
To use this script, follow these steps:

Open the script in a Python environment.
Replace the client_id and client_secret variables with your Spotify API credentials.
Choose the genre of music you want to extract by modifying the genre variable in the Extractor class.
Run the script.
The script will extract data for the specified genre, and save the extracted data as JSON files in the ./dashboard/data/ directory.
The script will extract data for two genres of music: rap and k-pop. If you want to extract data for a different genre, you can modify the genre variable in the Extractor class.