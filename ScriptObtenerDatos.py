import requests # type: ignore
import csv
import time

def obtener_nombre_liga(league_id):
    league_url = f'https://api.opendota.com/api/leagues/{league_id}'
    response = requests.get(league_url)
    if response.status_code == 200:
        league_data = response.json()
        return league_data.get('name', 'Desconocido')
    else:
        print(f"Error al obtener la liga con ID {league_id}")
        return 'Desconocido'

def obtener_datos_torneo(league_id):
    matches_url = f'https://api.opendota.com/api/leagues/{league_id}/matches'
    teams_url = f'https://api.opendota.com/api/leagues/{league_id}/teams'
    
    matches_response = requests.get(matches_url)
    matches_data = matches_response.json()

    teams_response = requests.get(teams_url)
    teams_data = teams_response.json()

    team_id_to_name = {team['team_id']: team['name'] for team in teams_data}
    
    league_name = obtener_nombre_liga(league_id)
    
    csv_data = []

    for match in matches_data:
        match_id = match.get('match_id')
        duration = match.get('duration')
        start_time = match.get('start_time')
        radiant_team_id = match.get('radiant_team_id')
        dire_team_id = match.get('dire_team_id')
        series_id = match.get('series_id')
        series_type = match.get('series_type')
        radiant_score = match.get('radiant_score')
        dire_score = match.get('dire_score')
        radiant_win = match.get('radiant_win')
        radiant = match.get('radiant')

        radiant_name = team_id_to_name.get(radiant_team_id, 'Unknown')
        dire_name = team_id_to_name.get(dire_team_id, 'Unknown')

        csv_data.append([
            match_id,
            duration,
            start_time,
            radiant_team_id,
            radiant_name,
            dire_team_id,
            dire_name,
            series_id,
            series_type,
            radiant_score,
            dire_score,
            radiant_win,
            radiant,
            league_id,
            league_name
        ])
        time.sleep(0.1)
    
    return csv_data

def main():
    """Función principal para gestionar las ligas específicas"""
    league_ids = [5401, 9870, 10749, 13256, 14268, 15728, 16935]# Corresponde al los codigos de los torneos de dota2 del 2017 al 2024

    all_data = []

    for league_id in league_ids:
        try:
            print(f"Obteniendo datos del torneo con ID: {league_id}")
            league_data = obtener_datos_torneo(league_id)
            all_data.extend(league_data)  
        except Exception as e:
            print(f"Error al obtener datos para la liga {league_id}: {e}")
    
    with open('dota_league_data_selected.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'match_id', 'duration', 'start_time', 'radiant_team_id', 'radiant_name', 
            'dire_team_id', 'dire_name', 'series_id', 'series_type', 'radiant_score', 
            'dire_score', 'radiant_win', 'radiant', 'leagueid', 'name'
        ])
        writer.writerows(all_data)

    print("El archivo CSV ha sido creado correctamente.")
if __name__ == "__main__":
    main()
