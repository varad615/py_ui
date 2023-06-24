import pyrebase

# Config/Setup
# -------------------------------------------------------------------------------
firebaseConfig = {
    "apiKey":  "AIzaSyB-MLPyckIgRqgBQ4zPrg1wOXsf177Ko5c",
    "authDomain": "info-c1887.firebaseapp.com",
    "projectId": "info-c1887",
    "databaseURL": "https://info-c1887-default-rtdb.firebaseio.com/",
    "storageBucket":  "info-c1887.appspot.com",
    "messagingSenderId": "231830430213",
    "appId": "1:231830430213:web:373acde8a4c07a06bab26c",
    "measurementId": "G-TD52CZE66X"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


data = {"Age": 21, "Name": "Jenna", "Employed": True}
# -------------------------------------------------------------------------------
# Create Data
db.push(data)
db.child("Users").child("FirstPerson").set(data)
