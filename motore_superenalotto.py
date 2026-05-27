import json
import random

def genera_sestina():
    numeri = random.sample(range(1, 91), 6)
    superstar = random.randint(1, 90)
    return sorted(numeri), superstar

def aggiungi_estrazione(nuovo_concorso, file_path='data/estrazioni.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    data.append(nuovo_concorso)
    
    # Ordinamento: il trucco è usare una chiave lambda
    # Ordiniamo prima per anno, poi per numero di concorso
    data.sort(key=lambda x: (x['anno'], x['concorso']))
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)