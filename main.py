from spotify import Spotify
from appInfo import client_id,client_secret,redirect_uri
def main():
    s = Spotify(client_id,client_secret,redirect_uri)

    while True:
        payload = s.get_current_data()
        name = s.handle_data(payload)

main()