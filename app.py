from flask import Flask, jsonify, request
import scrapetube

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API do YouTube Scrapetube está rodando!"})

@app.route("/channel_videos", methods=["GET"])
def get_channel_videos():
    channel_id = request.args.get("channel_id")
    if not channel_id:
        return jsonify({"error": "Parâmetro 'channel_id' é obrigatório."}), 400

    videos = scrapetube.get_channel(channel_id)
    video_list = [{"videoId": video["videoId"], "title": video["title"]["runs"][0]["text"]} for video in videos]

    return jsonify(video_list)

@app.route("/playlist_videos", methods=["GET"])
def get_playlist_videos():
    playlist_id = request.args.get("playlist_id")
    if not playlist_id:
        return jsonify({"error": "Parâmetro 'playlist_id' é obrigatório."}), 400

    videos = scrapetube.get_playlist(playlist_id)
    video_list = [{"videoId": video["videoId"], "title": video["title"]["runs"][0]["text"]} for video in videos]

    return jsonify(video_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
