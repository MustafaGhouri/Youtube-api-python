from flask import Flask,request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from waitress import serve
import logging
from flask_cors import CORS

 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def get_transcript():
    try:
        data = request.json
        videoId = data['videoId']
        lang = data['lang']
        transcript = YouTubeTranscriptApi.get_transcript(videoId, languages=[lang])
        return jsonify(transcript)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)