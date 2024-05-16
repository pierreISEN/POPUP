import time
import pygetwindow as gw
from pywinauto import Application


screen_width = 1920
screen_height = 1080

# Fonction pour vérifier et fermer les pop-ups en bas à droite
def close_popups():
    while True:
        # Obtenir toutes les fenêtres ouvertes
        all_windows = gw.getAllWindows()

        for window in all_windows:
            if window.visible:
                # Obtenir les coordonnées de la fenêtre
                left, top, right, bottom = window.left, window.top, window.right, window.bottom

                # Vérifier si la fenêtre est en bas à droite (ajuster les marges si nécessaire)
                if left > screen_width - 400 and top > screen_height - 400:
                    try:
                        # Fermer la fenêtre pop-up
                        app = Application().connect(handle=window._hWnd)
                        app.kill()
                        print(f"Fermé la fenêtre pop-up : {window.title}")
                    except Exception as e:
                        print(f"Erreur en fermant la fenêtre {window.title}: {e}")

        # Attendre quelques secondes avant de vérifier à nouveau
        time.sleep(5)

if __name__ == "__main__":
    close_popups()
