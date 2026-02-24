from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def compute_score(points: int, multiplier: int) -> int:
    if points < 0 or multiplier < 0:
        raise ValueError("points and multiplier must be non-negative")
    return points * multiplier

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/score")
def score():
    name = (request.form.get("name") or "").strip()
    points_raw = request.form.get("points") or "0"
    mult_raw = request.form.get("multiplier") or "1"

    try:
        points = int(points_raw)
        multiplier = int(mult_raw)
        result = compute_score(points, multiplier)
        message = f"{name or 'Player'} scored {result}!"
        return render_template("index.html", result=message, name=name, points=points, multiplier=multiplier)
    except Exception as e:
        return render_template("index.html", error=f"Invalid input: {e}", name=name, points=points_raw, multiplier=mult_raw), 400

@app.get("/api/health")
def health():
    return jsonify(status="ok")

@app.get("/api/score")
def api_score():
    # Example: /api/score?points=10&multiplier=2
    points_raw = request.args.get("points", "0")
    mult_raw = request.args.get("multiplier", "1")
    points = int(points_raw)
    multiplier = int(mult_raw)
    result = compute_score(points, multiplier)
    return jsonify(points=points, multiplier=multiplier, score=result)

if __name__ == "__main__":
    # Dev server
    app.run(host="0.0.0.0", port=5000, debug=False)