import requests
from tabulate import tabulate
import json  # Import json for debugging

def fetch_cricket_scores():
    url = 'https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/comm'
    headers = {
        'x-rapidapi-key': 'd3668d28ddmsh899b147fa69e9cdp123fb6jsn03895650f2ed',
        'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Debugging: Print the structure of the JSON response
        print("JSON Response Structure:")
        print(json.dumps(data, indent=2))
        
        # Initialize matches to None
        matches = None
        
        # Safely extract matches from the JSON data
        if 'typeMatches' in data and isinstance(data['typeMatches'], list) and len(data['typeMatches']) > 0:
            type_matches = data['typeMatches']
            
            if len(type_matches) > 0 and 'seriesMatches' in type_matches[0] and isinstance(type_matches[0]['seriesMatches'], list) and len(type_matches[0]['seriesMatches']) > 0:
                series_matches = type_matches[0]['seriesMatches']
                
                if len(series_matches) > 0 and 'seriesAdWrapper' in series_matches[0] and 'matches' in series_matches[0]['seriesAdWrapper']:
                    matches = series_matches[0]['seriesAdWrapper']['matches']
                    
        if matches is None:
            print("No matches found or structure is incorrect.")
            return
        
        # Process matches if they are defined
        for match in matches:
            table = []
            match_info = match.get('matchInfo', {})
            match_score = match.get('matchScore', {})
            team1_score = match_score.get('team1Score', {}).get('inngs1', {})
            team2_score = match_score.get('team2Score', {}).get('inngs1', {})
            
            # Check for presence of necessary fields
            if 'matchDesc' in match_info and 'team1' in match_info and 'team2' in match_info:
                team1 = match_info['team1'].get('teamName', 'Unknown Team 1')
                team2 = match_info['team2'].get('teamName', 'Unknown Team 2')
                description = f"{match_info['matchDesc']} , {team1} vs {team2}"
            else:
                description = "Description Not Available"
            
            table.append(["Match Description", description])
            table.append(["Match Details", ""])
            table.append(["Series Name", match_info.get('seriesName', 'N/A')])
            table.append(["Match Format", match_info.get('matchFormat', 'N/A')])
            table.append(["Result", match_info.get('status', 'N/A')])
            table.append([match_info.get('team1', {}).get('teamName', 'Unknown Team 1'),
                          f"{team1_score.get('runs', 'N/A')}/{team1_score.get('wickets', 'N/A')} in {team1_score.get('overs', 'N/A')} overs"])
            table.append([match_info.get('team2', {}).get('teamName', 'Unknown Team 2'),
                          f"{team2_score.get('runs', 'N/A')}/{team2_score.get('wickets', 'N/A')} in {team2_score.get('overs', 'N/A')} overs"])
            
            headers = ["Key", "Value"]
            print(tabulate(table, headers=headers, tablefmt="grid"))
            print("\n")
    
    except requests.exceptions.RequestException as e:
        print(f"HTTP Error: {e}")
    except ValueError as e:
        print(f"JSON Decode Error: {e}")
    except KeyError as e:
        print(f"Missing Key Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

fetch_cricket_scores()
