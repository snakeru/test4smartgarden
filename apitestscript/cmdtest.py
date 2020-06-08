import datetime
import time
import sys
import requests
import uuid

# account specific values
USERNAME = 'myUserEmail'
PASSWORD = 'myUserPassword'
API_KEY =  'myApplicationApiKey'
SERVICE_ID = '11112222-3333-4444-5555-666677778888'

# other constants
AUTHENTICATION_HOST = 'https://api.authentication.husqvarnagroup.dev'
SMART_HOST = 'https://api.smart.gardena.dev'


def format(response):
    formatted = [response.url, "%s %s" % (response.status_code, response.reason)]
    for k,v in response.headers.items():
        formatted.append("%s: %s" % (k, v))
    formatted.append("")
    formatted.append(r.text)
    return "\n".join(formatted)


if __name__ == "__main__":
    payload = {'grant_type': 'password', 'username': USERNAME, 'password': PASSWORD,
               'client_id': API_KEY}

    print("Logging into authentication system...")

    r = requests.post(f'{AUTHENTICATION_HOST}/v1/oauth2/token', data=payload)
    assert r.status_code == 200, format(r)
    auth_token = r.json()["access_token"]
    print("Logged in auth_token=(%s)" % auth_token)

    headers = {
        "Content-Type": "application/vnd.api+json",
        "x-api-key": API_KEY,
        "Authorization-Provider": "husqvarna",
        "Authorization": "Bearer " + auth_token
    }

    print("### get locations ###")
    r = requests.get(f'{SMART_HOST}/v1/locations', headers=headers)
    assert r.status_code == 200, format(r)
    assert len(r.json()["data"]) > 0, 'location missing - user has not setup system'
    location_id = r.json()["data"][0]["id"]
    print("LocationId=(%s)" % location_id)


    payload = {
      'data': {
          'attributes': {
              'command': 'STOP_UNTIL_NEXT_TASK'
          }, 
          'id': str(uuid.uuid4()),
          'type': 'VALVE_CONTROL'
      }
    }


    print("Sending command with payload:", payload)
    r = requests.put(f'{SMART_HOST}/v1/command/' + SERVICE_ID, json=payload, headers=headers)

    assert r.status_code == 202, format(r)
    print("Success")
    print(format(r))
