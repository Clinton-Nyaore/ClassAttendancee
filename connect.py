import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-641d2-default-rtdb.firebaseio.com/",
    'storageBucket': 'faceattendancerealtime-641d2.appspot.com'
})
