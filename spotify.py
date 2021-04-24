import spotipy
from spotipy.oauth2 import SpotifyOAuth
from sound import Sound

class Spotify :
    def __init__(self,client_id,client_secret,redirect_uri):
        #Spotify Authentication
        self.__sp = spotipy.Spotify(auth_manager=SpotifyOAuth (
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope='user-read-currently-playing'))

        self.__current_song = ''  


        '''
            The selected songs and its value 
            e.g :
            'song_name' : 'ideal song volume'
                                               '''    
        self.__songs = {'Brasi Sla7':30,'Blood':10}  

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

        
        ''' 
            we start looking after the letter 4000 so we can catch the song name 
            easly and then we add the 4000 chars then we shift 8 letters so
            we start at the first letter of the song name
            and then start looping the name  
                                                '''     
        start = int(payload[4000:].find('name'))+4008

        name = ''
        while True:
            try:


                                              
                

                '''
                if we hitted " ' " that means we have finished looping the song name
                else we continue        
                
                ''CAUTION'' - THIS MAY NOT WORD ON SOME SONGS THAT CONTAINS ' IN ITS NAME

                    '''

                if payload[start] == "\'":
                    
                    
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
                    
                    name = ''
                    break
                else:
                    name +=payload[start]
                    start+=1
                    
                                                                     
                ''' 
                    If there is nothing on playing then we get IndexError
                    So we display the error
                                                                        '''
            except IndexError:
                print('THERE IS NO SONG PLAYING') 
                break     

    def get_current_data(self):
        '''
        Sending GET request to Spotify API to get the current playing song  
                                                                            '''
        return str(self.__sp.current_user_playing_track())  







