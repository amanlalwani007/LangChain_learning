from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI

"""
Steps to replicate this example:
1. Create a firebase account
2. Create a new firebase project    
    - Copy the project ID
3. Create a firestore database in the Firebase  project
4. Install the google cloud cli on your computer
    - https://cloud.google.com/sdk/docs/install
    - Authenticate the google cloud cli with your google account
        - https://cloud.google.com/docs/authentication
        provide-credentials-adc#local-dev
    _ Set your default project to the new Firebase project you created
5.Enable the Firestore API in google  cloud console
    - https://console.cloud.google.com/apis/library/firestore.googleapis.com    
     
"""
load_dotenv()
# setup Firebase Firestore
