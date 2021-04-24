from spotify import Spotify

def main():
    s = Spotify(client_id="YOUR_client_id",
            client_secret="YOUR_client_secret",
            redirect_uri="YOUR_redirect_uri")

    while True:
        payload = s.get_current_data()
        name = s.handle_data(payload)

main()