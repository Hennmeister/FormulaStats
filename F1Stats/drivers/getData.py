import requests
from typing import Dict
def test():
    print("WORKS")

def getData(last_name: str) -> Dict:
    url = 'https://ergast.com/api/f1/current/drivers/' + last_name + '/results.json'
    response = requests.get(url)
    race_data = response.json()
    total = race_data.get('MRData').get('total')
    index = max(int(total) - 5, 1)
    recent_results = []
    recent_races = []
    test()
    while index < int(total):
        recent_results.append(race_data.get('MRData').get('RaceTable').get('Races')[index].get('Results')[0].get('position'))
        recent_races.append(race_data.get('MRData').get('RaceTable').get('Races')[index].get('raceName'))
        index += 1
    return {'results': recent_results, 'names': recent_races}


getData('norris')


