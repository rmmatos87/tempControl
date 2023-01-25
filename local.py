from datetime import datetime
import json

path = "/".join(__file__.split("/")[:-1])

def save(now: datetime, temp: float, umid: float):
    try:
        with open(path + "/local_backup", "a") as f:
            f.write(str({
                "timestamp": now.isoformat(),
                "temperature": temp,
                "umidity": umid
            }))
            f.write("\n")
    except Exception:
        with open(path + "/local_backup", "w") as f:
            f.write(str({
                "timestamp": now.isoformat(),
                "temperature": temp,
                "umidity": umid
            }))
            f.write("\n")
    return True

def load():
    now = []
    umid = []
    temp = []
    try:
        with open(path + "/local_backup") as f:
            for line in f:
                d = json.loads(line.replace("'", '"'))
                now.append(datetime.fromisoformat(d["timestamp"]))
                temp.append(float(d["temperature"]))
                umid.append(float(d["umidity"]))
        return now, temp, umid
    except Exception as e:
        return [], [], []

if __name__ == "__main__":
    now, temp, umid = load()
    for i, j, k in zip(now, temp, umid):
        print(i, j, k)