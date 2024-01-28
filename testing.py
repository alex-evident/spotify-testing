# %% SETUP
import os

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


# %% AUTH
# write a POST request to get an access token
def get_auth() -> str:
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    resp = requests.post(url="https://accounts.spotify.com/api/token", data=data)

    if resp.status_code != 200:
        raise Exception(f"Could not authenticate client: Error {resp.status_code}")

    return resp.json()["access_token"]


access_token = get_auth()

# %%
base_uri = f"https://api.spotify.com/v1/"


def get_artist_info(artist_id: str) -> dict:
    """Get artist info from Spotify API.

    Args:
        artist_id (str): Spotify artist ID
    """
    artists_uri = f"{base_uri}artists/"
    r = requests.get(
        url=f"{artists_uri}{artist_id}",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    if r.status_code != 200:
        raise Exception(f"Could not get artist info: Error {r.status_code}")

    return r.json()


# id for Lemaitre
test_id = "4CTKqs11Zgsv8EZTVzx764"
print(get_artist_info(test_id))

# %%
