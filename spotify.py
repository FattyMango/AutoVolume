import spotipy
import sys
from spotipy.oauth2 import SpotifyOAuth
from sound import Sound
def handle_song(song):
    '''
    The selected songs and its value 
    e.g :
    'song_name' : 'song_name'
    
                                         '''

    songs = {
        'SONG_NAME':100,
    }


    '''
    Checking if the song registered in the list
                                                '''
    if song in songs: 
        s = Sound
        s.volume_set(int(songs[song]))
    else:
        print('ERROR : SONG DOES NOT EXIST IN YOU LIST')
        #  flag = input('DO YOU WANT TO ADD THE SONG TEMPORARY (y/n) : ')
        #  if flag != 'n':
        #     vol = int(input('INTER VOLUME 0 - 100 : '))
        #     if vol > 100:
        #         vol = 100
        #     elif vol < 0:
        #         vol = 0    
        #     songs[song] = vol    
        #     print(songs)

'''
    Spotify Authentication   
        You can choose and website it used to get the Token
                                    '''
sp = spotipy.Spotify(auth_manager=SpotifyOAuth (
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri="YOUR_WEBSITE",
        scope="user-read-currently-playing"))

# Varibale to track the current song        
current_song = ''

while True:

    '''
    Sending GET request to Spotify API to get the recent playing song  
    And continue looping if the song changed
                                            '''
    result = str(sp.current_user_playing_track())
    ''' 
    we start looking after the letter 4000 so we can catch the song name 
    easly and then we add the 4000 chars then we shift 8 letters so
     we start at the first letter of the song name
    and then start looping the name  
                                                '''

    start = int(result[4000:].find('name'))+4008 

    name = ''
    while True:
        try:
            '''
            if we hitted " ' " that means that we finished looping the song name
            else we continue
                                                '''
            if result[start] == "\'":
                # Calling  the function to handle the song
                handle_song(name)
                ''' 
                Checking if the song changed or not
                                                        '''
                if current_song != name:
                    current_song = name
                    print('NOW PLAYING : ' + current_song)
                    handle_song(name)
                name = ''
                break
            else:
                name +=result[start]
                start+=1
                ''' 
                If there is nothing on playing then we get IndexError
                So we display the error
                                                                    '''

        except IndexError:
            print('THERE IS NO SONG PLAYING') 
            break    

     # The option to leave the program     
    selection = input("Press Q to quit \n")
    if selection is "Q" or selection is "q":
        print("Quitting")
        sys.exit()        
            