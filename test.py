
from firebase import firebase

firebases = firebase.FirebaseApplication("https://schneider-project.firebaseio.com/")

 firebases.post('/test',{"WW":"WW"})
