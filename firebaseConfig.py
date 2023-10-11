import firebase_admin
from firebase_admin import credentials, db

#carga del certificado del proyecto
cred = credentials.Certificate("credentials/crud-clientes-8acf7-firebase-adminsdk-w8cuy-2f0db1323c.json")

#referencia a la base de datos en tiempo real
firebase_admin.initialize_app(cred,{'databaseURL':'https://crud-clientes-8acf7-default-rtdb.firebaseio.com/'})
