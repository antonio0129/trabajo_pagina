from pymongo import MongoClient
import certifi
MONGO_URI = 'mongodb+srv://antllanos012:1081790478@cluster0.7swdmc0.mongodb.net/'

ca = certifi.where()

# definimos el método de conexión
def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_baseD_app"]
    except ConnectionError:
     print('Error de conexión con la bdd')
    return db