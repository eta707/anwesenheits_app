from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def create_connection():
    return sqlite3.connect("anwesenheit.db")

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.json
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mitarbeiter (name, position, abteilung) VALUES (?, ?, ?)", 
                   (data['name'], data['position'], data['abteilung']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Mitarbeiter hinzugefügt!"})

@app.route('/add_work_data', methods=['POST'])
def add_work_data():
    data = request.json
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO arbeitsdaten (mitarbeiter_id, datum, arbeitsbeginn, arbeitsende, mittagspause, arbeitsinhalte, ueberstunden)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (data['mitarbeiter_id'], data['datum'], data['arbeitsbeginn'], data['arbeitsende'], 
          data['mittagspause'], data['arbeitsinhalte'], data['ueberstunden']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Arbeitsdaten hinzugefügt!"})

@app.route('/get_work_data/<int:mitarbeiter_id>/<string:monat>', methods=['GET'])
def get_work_data(mitarbeiter_id, monat):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT datum, arbeitsbeginn, arbeitsende, mittagspause, arbeitsinhalte, ueberstunden
    FROM arbeitsdaten
    WHERE mitarbeiter_id = ? AND strftime('%m', datum) = ?
    """, (mitarbeiter_id, monat))
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
