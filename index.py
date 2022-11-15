import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('private/raspberry1-d07d8-firebase-adminsdk-4tlwq-68582b8dbd.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
st.title("光線和距離即時監控")
def downloadData():
    print("下載資料")

