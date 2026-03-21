from flask import Flask, jsonify
import db

app = Flask(__name__)

@app.route("/games")
def get_games():
    df = db.get_games()
    return jsonify(df.to_dict(orient="records"))

@app.route("/top10")
def top10():
    df = db.get_top10_by_rating()
    return jsonify(df.to_dict(orient="records"))

@app.route("/stats")
def stats():
    df = db.get_games()

    return jsonify({
        "total_games": int(len(df)),
        "avg_rating": round(df["rating"].mean(), 2),
        "avg_playtime": round(df["playtime_forever"].mean(), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
