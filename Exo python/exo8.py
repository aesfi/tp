from datetime import datetime, timedelta
from json import loads
import requests

timezone = input("Entrez une capitale pour connaître l'heure locale : ")
url = f'https://worldtimeapi.org/api/timezone/{timezone}'

response = requests.get(url)

if response.status_code != 200:
    raise ValueError('Fuseau horaire inconnu')

response_json = loads(response.text)

# Utilisez l'heure UTC et ajoutez l'offset
utc_time = datetime.fromisoformat(response_json['datetime'])
local_time = utc_time #+ offset

print(f"Heure locale à {timezone}: {local_time}")
