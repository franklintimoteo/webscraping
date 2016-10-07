import requests
import json

def urlshortener(longUrl):
    api_url = 'https://www.googleapis.com/urlshortener/v1/url'
    api_key = 'AIzaSyC3s3mlq9NPTzDjp2MCyp-KXgzRfGmbJSU' 
    url = '{0}?key={1}'.format(api_url, api_key)
    
    
    headers = {'content-type': 'application/json'}
    params = json.dumps({'longUrl': longUrl})
    response = requests.post(url, data=params, headers=headers)
    
    if response.ok:
        return response.json()['id']
    else:
        return None