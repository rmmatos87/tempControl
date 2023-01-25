from datetime import datetime
from pymongo import MongoClient

path = "/".join(__file__.split("/")[:-1])
path = "." if len(path) < 1 else path

def connect():
    uri = r"mongodb+srv://cluster0.ptnhbto.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
    uri = "mongodb+srv://pi:pi@cluster0.ptnhbto.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(
        uri,
#         tls=True,
#         tlsCertificateKeyFile=path + '/cert/X509-cert.pem'
    )

    db = client['pi']
    col_measures = db['measures']
    col_status = db['status']
    return col_measures, col_status

def insert_measures(now: datetime, temp: float, umid: float):
    try:
        col_measures, _ = connect()
        col_measures.insert_one({
            "timestamp": now,
            "temperature": temp,
            "umidity": umid
        })
        return True
    except Exception:
        return False

def insert_status(now: datetime, status: bool):
    try:
        _, col_status = connect()
        col_status.insert_one({
            "timestamp": now,
            "status": status
        })
        return True
    except Exception:
        return False

if __name__ == "__main__":
    client = MongoClient("mongodb+srv://pi:raspberry@cluster0.ptnhbto.mongodb.net/?retryWrites=true&w=majority")

    print(client.server_info())
#     col_measures, _ = connect()
#     col_measures.insert_one({
#         "timestamp": datetime.now(),
#         "temperature": 20,
#         "umidity": 80
#     })
