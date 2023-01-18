<h1 align="center"> 🎵 Lyric Sync Game 🎵</h1>


<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify">
  Spotify has a playlist dedicated to the top 50 weekly songs and these songs can be found on YouTube as well. This project uses creates a song guessing game using apis from both services.
</p>


<!-- OVERVIEW -->
<h2 id="overview"> :cloud: Overview</h2>

<p align="justify"> 
  In this project, the objective is to correctly guess the song given the YouTube official music video. Choices will be limited to the Spotify's Top 50 playlist.
</p>


<!-- PROJECT FILES DESCRIPTION -->
<h2 id="project-files-description"> :floppy_disk: Project Files Description</h2>

<ul>
  <li><b>SongGame.py</b> - Flask back-end. REST API implementation of game logic.</li>
  <li><b>UI_SongGame.py</b> - Simple command-line user interface. </li>
  <li><b>top50.json</b> - File containing the Spotify Top 50 Playlist as of a certain date. Mainly used for testing without calling Spotify API.</li>
  <li><b>db.json</b> - Text file representing a database where song data is written to from Spotify API or top50.json.</li>
</ul>


<!-- GETTING STARTED -->
<h2 id="getting-started"> :book: Getting Started</h2>

You will first need to generate your own [Spotify API Bearer Token](https://developer.spotify.com/documentation/web-api/quick-start/) and [YouTube Data API Key](https://developers.google.com/youtube/v3/getting-started).

Then, change token inside the <b>getSpotifyTopFifty</b> method and change API_Key inside the <b>generateGame</b> method:
<pre><code> token = "spotify api token"</code></pre>
<pre><code> API_Key = "&key=youtube data api"</code></pre>

You will also need to install Flask and the requests library:

Mac:
<pre><code>$ pip install requests</code></pre>
<pre><code>$ pip install Flask</code></pre>

Windows:
<pre><code>$ python3 -m pip install requests</code></pre>
<pre><code>$ python3 -m pip install Flask</code></pre>

<p>First, run the application locally with:</p>
<pre><code>$ python3 SongGame.py</code></pre>

<p>Then, start the game by typing the following commands in the command line:</p>
<pre><code>$ python3 UI_SongGame.py</code></pre>


<h2 id="project-files-description"> 🏗️ Roadmap </h2>
<ol>
  
 <b><li>Implement database.</li></b>
 <ul><li>Currently the song data is written into a json file.</li></ul>
  
 <b><li>Implement React web UI.</li></b>
 <ul><li>The music game gives a link to the music video rather than playing the actual video.</li> </ul>
 
 <b><li>Host on a server like Heroku or AWS.</li></b>
 <ul><li>Currently runs locally.</li> </ul>
</ol>
