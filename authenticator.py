import requests
import json
import config



class Authenticator():
    def __init__(self, client_id : str = None, redirect_uri : str = 'https://127.0.0.1:8080', curr_access_token : str = None):
        
        self.client_id = config.client_id
        
        self.curr_access_token = curr_access_token

    def generate_access_token(self):
        
        resource_url = 'https://api.tdameritrade.com/v1/oauth2/token' # resource url for post access token api
        
        refresh_token = config.refresh_token

        data = {'client_id': self.client_id, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'} # json format data to send to the api server
        
        response = requests.post(resource_url, data=data) # send post request
        json_obj_str = response.json() #collect response from server in json object format
        print(json_obj_str)
        
        
        
        self.curr_access_token = json_obj_str['access_token'] # set Authenticator's curr_access_token to access token from the json object
        print('current access token: ' + self.curr_access_token) 
        return self.curr_access_token
    

authenticator = Authenticator()
authenticator.generate_access_token()



