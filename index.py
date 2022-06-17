from dataclasses import dataclass
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

conn = credentials.Certificate('accountKey.json')

firebase_admin.initialize_app(conn, {
    'databaseURL' : 'https://pythonconnection-a4e4f-default-rtdb.firebaseio.com'
})


data = {
    "name" : "Tom",
     "surname" : "Cruise",
     "movie" : "Top Gun",
     "age" : 58,
     "good actor" : True
}

reference = db.reference()
user = reference.set(data)


#connect data

# conn = {
#     "apiKey": "AIzaSyD4jQ0OtAd4_4ypRVgABo8YiKteWlLOkg4",
#     "authDomain": "pythonconnection-a4e4f.firebaseapp.com",
#     "projectId": "pythonconnection-a4e4f",
#     "storageBucket": "pythonconnection-a4e4f.appspot.com",
#     "messagingSenderId": "689573772605",
#     "appId": "1:689573772605:web:bbdab71b14d43bb21a1954",
#     "measurementId": "G-9HZ1J5W045",
#     "databaseURL": "https://pythonconnection-a4e4f-default-rtdb.firebaseio.com"
# }

#database link
#https://console.firebase.google.com/project/pythonconnection-a4e4f/database/pythonconnection-a4e4f-default-rtdb/data/~2F