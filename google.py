from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']

def main():
    '''Test task for the vacancy "Novice system administrator"
                        in the Mindbox
    '''
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('admin', 'directory_v1', credentials=creds)
    #User insert
    adduser = { 'name':
           {'familyName': 'Kudrin', 'givenName': 'Igor'},
             'password': 'EcnfkLtuhflbhjdfnm!',
             'primaryEmail': 'admin@mindbox.ru',
           }
    # Call the Admin SDK Directory API https://developers.google.com/admin-sdk/directory/v1/get-start/getting-started
    results = service.users().list(query="email:adduser['primaryEmail']*").execute()
    user = results.get('users', [])

    if not user:
        user_insert = service.users().insert(body=adduser).execute()
    else:
        print('User already exists.')

if __name__ == '__main__':

    main()
