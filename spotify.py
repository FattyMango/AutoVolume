import spotipy 
import sys 

from spotipy.oauth2 import SpotifyOAuth
from sound import Sound

class Spotify :
    def __init__(self,client_id,client_secret,redirect_uri):
        #Spotify Authentication
        self.__sp = spotipy.Spotify(auth_manager=SpotifyOAuth (
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope='user-read-currently-playing'
                ))

        self.__current_song = ''  


        '''
            The selected songs and its value 
            e.g :
            'song_name' : 'ideal song volume'
                                               '''    
        self.__songs = {'High Hopes':99,'':0}  


    def IsInList(self,song):
        if song in self.__songs: 
            return True  
        return False

    def get_current_song(self):
        return self.__current_song

    def change_volume(self,song):
        s = Sound()
        s.volume_set(int(self.__songs[song]))

    
    def exit(self):    
        selection = input("Press Q to quit \n")
        if selection is "Q" or selection is "q":
            print("Quitting")
            sys.exit()   


    
    def handle_data(self,payload):

        
        result = payload
        if result is None:
            print ("NO SONG PLAYING")
        else:  
            name = result["item"]["name"]

        

            ''' 
                Checking if the song changed or not
                                                    '''
            if self.__current_song != name:
                self.__current_song = name
                
                print('NOW PLAYING : ' + self.__current_song)
                if self.IsInList(self.__current_song):
                    print('CHANGING VOLUME TO : ' + str(self.__songs[self.__current_song]))
                    self.change_volume(name)
                else: print('ERROR : SONG DOES NOT EXIST IN YOU LIST') 

    def get_current_data(self):
        '''
        Sending GET request to Spotify API to get the current playing song  
                                                                            '''
        return self.__sp.current_user_playing_track() 







