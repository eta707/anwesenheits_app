import sqlite3

def create_connection():
    return sqlite3.connect("anwesenheit.db")

def setup_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Tabelle für Mitarbeiter
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mitarbeiter (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT,
        abteilung TEXT
    )
    """)

    # Tabelle für Arbeitsdaten
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS arbeitsdaten (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mitarbeiter_id INTEGER NOT NULL,
        datum DATE NOT NULL,
        arbeitsbeginn TIME NOT NULL,
        arbeitsende TIME NOT NULL,
        mittagspause INTEGER,
        arbeitsinhalte TEXT,
        ueberstunden INTEGER,
        FOREIGN KEY (mitarbeiter_id) REFERENCES mitarbeiter(id)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Datenbank erfolgreich erstellt!")
