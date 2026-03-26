import sqlite3
import openpyxl

def export_to_excel(mitarbeiter_id):
    conn = sqlite3.connect("anwesenheit.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT datum, arbeitsbeginn, arbeitsende, mittagspause, arbeitsinhalte, ueberstunden
    FROM arbeitsdaten
    WHERE mitarbeiter_id = ?
    """, (mitarbeiter_id,))
    rows = cursor.fetchall()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Datum", "Arbeitsbeginn", "Arbeitsende", "Mittagspause", "Arbeitsinhalte", "Überstunden"])
    for row in rows:
        ws.append(row)

    wb.save("arbeitsbericht.xlsx")
    print("Bericht exportiert!")
    conn.close()

if __name__ == "__main__":
    export_to_excel(1)
