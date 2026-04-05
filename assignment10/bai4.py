import json
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

AIRPORTS_FILE = Path(__file__).with_name("airports.json")


def load_airports():
    with AIRPORTS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def find_airport_by_icao(icao):
    airports = load_airports()
    target_icao = icao.upper()

    for airport in airports:
        airport_icao = airport.get("icao") or airport.get("ident")
        if airport_icao and airport_icao.upper() == target_icao:
            return {
                "icao": airport_icao,
                "name": airport.get("name"),
                "city": airport.get("municipality") or airport.get("city"),
                "country": airport.get("iso_country") or airport.get("country"),
            }

    return None


@app.route("/airport/<icao>")
def get_airport(icao):
    try:
        airport = find_airport_by_icao(icao)
    except FileNotFoundError:
        return jsonify({"error": "airports.json not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid airports.json format"}), 500

    if airport is None:
        return jsonify({"error": f"Airport with ICAO '{icao.upper()}' not found"}), 404

    return jsonify(airport)


if __name__ == "__main__":
    app.run(debug=True)