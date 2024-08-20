from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Define your API keys and URLs
CRICKET_API_URL = 'https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/comm'
API_KEY = 'd3668d28ddmsh899b147fa69e9cdp123fb6jsn03895650f2ed'  # Replace with your actual API key

def format_date(timestamp):
    # Convert timestamp to a human-readable date format
    return datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
    # Fetch data from the API
    try:
        response = requests.get(CRICKET_API_URL, params={'apikey': API_KEY})
        response.raise_for_status()
        data = response.json()
        
        # Check if there are any recent matches
        recent_matches = data.get('recentMatches', [])
        upcoming_matches = data.get('upcomingMatches', [])
        
        # Prepare data for rendering
        recent_matches_data = [
            {
                'matchId': match['matchId'],
                'description': match['matchHeader']['matchDescription'],
                'status': match['matchHeader']['status'],
                'team1': match['matchHeader']['team1']['name'],
                'team2': match['matchHeader']['team2']['name'],
                'score': match['miniscore']['batTeam']['teamScore'],
                'wickets': match['miniscore']['batTeam']['teamWkts']
            }
            for match in recent_matches
        ] if recent_matches else None

        upcoming_matches_data = [
            {
                'matchId': match['matchId'],
                'description': match['matchHeader']['matchDescription'],
                'startDate': format_date(match['matchHeader']['matchStartTimestamp']),
                'team1': match['matchHeader']['team1']['name'],
                'team2': match['matchHeader']['team2']['name']
            }
            for match in upcoming_matches
        ] if upcoming_matches else None

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        recent_matches_data = None
        upcoming_matches_data = None

    return render_template('index.html', recent_matches=recent_matches_data, upcoming_matches=upcoming_matches_data)

if __name__ == '__main__':
    app.run(debug=True)
