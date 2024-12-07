import requests
import json
import time

class OneDrive:
    def __init__(self,client_id = False, client_secret = False, redirect_uri = False, refresh_token = False):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.refresh_token = refresh_token
        self.refresh_api="https://login.microsoftonline.com/common/oauth2/v2.0/token"
        self.drive_api="https://graph.microsoft.com/v1.0/me/drive"
        self.refresh_time = 0

    def refresh_Access_Token(self):
        if time.time()>self.refresh_time:
            if self.client_id and self.client_secret and self.redirect_uri and self.refresh_token:
                data={
                    'client_id':self.client_id,
                    'client_secret':self.client_secret,
                    'redirect_uri':self.redirect_uri,
                    'refresh_token':self.refresh_token,
                    'grant_type':'refresh_token'
                }
                dic=requests.post(self.refresh_api,data=data).json()
                self.refresh_time=time.time()+dic['expires_in']-11
                token='bearer '+dic['access_token']
        

demo = OneDrive()
demo

