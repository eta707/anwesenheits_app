import threading
import os
from frontend.app import AttendanceApp

# Backend (Flask API) starten
def start_api():
    os.system("python backend/api.py")  # Führt api.py aus

# Thread starten, um Backend parallel laufen zu lassen
api_thread = threading.Thread(target=start_api)
api_thread.daemon = True  # Beendet den Thread, wenn das Hauptprogramm stoppt
api_thread.start()

# Frontend (Kivy-App) starten
if __name__ == "__main__":
    AttendanceApp().run()
