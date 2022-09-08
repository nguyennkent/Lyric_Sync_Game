from flask import Flask
import json, requests, random, time

app = Flask(__name__)

@app.route('/testupdate')
def getSongList():
    """
    Generate song list from collected song data.
    """
    song_file = open("top50.json")
    content = json.load(song_file)
    write(content)
    song_file.close()
    return content

@app.route('/update')
def getSpotifyTopFifty():
    """
    Generate song list from Spotify Web Api. Makes a GET reqest for song data from the US Top 50 playlist.
    Updates the current song list with the data retrieved.
    """
    uri = "https://api.spotify.com/v1/playlists/37i9dQZEVXbLRQDuF5jeBp?fields=tracks(items(track(name%2C%20artists(name))))"
    # REQUIRES SPOTIFY API BEARER TOKEN
    token = ""
    headers = {"Authorization": "Bearer " + token}

    response = requests.get(uri, headers=headers)
    response_json = response.json()
    write(response_json["tracks"])
    return response_json["tracks"]

def write(content):
    db = open("db.json", "w")
    j = json.dumps(content, indent=4)
    db.write(j)
    db.close

@app.route('/game')
@app.route('/game/<int:size>')
def generateGame(size=3):
    """
    Creates the game object with specified number of questions (default 3). 
    Chooses songs randomly from the song list and makes a request to Youtube API to generate links for music videos.
    """
    # REQUIRES YOUTUBE DATA API KEY
    API_Key = "&key="
    search = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&q="

    db = open("db.json")
    song_list = json.load(db)
    db.close()

    x = random.sample(song_list["items"], k = size)

    game= []

    for item in x:
        title = item["track"]["name"]
        artist = item["track"]["artists"][0]["name"]
        query = artist + " " + title
        query.replace(" ", "%20")
        response = requests.get(search + query + API_Key)
        response_json = response.json()
        time.sleep(3)
        video_Id = response_json["items"][0]["id"]["videoId"]
        
        question = {"artist":artist, "title":title, "id":video_Id}
        game.append(question)

    return {"items": game }

@app.route('/testgame')
def testGame():
    return {
        'items': [
            {'artist': 'Arctic Monkeys', 'title': '505', 'id': '1Jd2DysfCW8'}, 
            {'artist': 'Kanye West', 'title': 'Bound 2', 'id': 'BBAtAM7vtgc'}, 
            {'artist': 'Future', 'title': 'WAIT FOR U (feat. Drake & Tems)', 'id': 'Y2QpQP8wPG8'}
            ]
        }
        
if __name__ == "__main__":
    app.run(debug=True)