import time  # Importer le module time pour la gestion du temps
import pygetwindow as gw  # Importer pygetwindow pour la gestion des fenêtres
from pywinauto import Application  # Importer Application depuis pywinauto pour interagir avec les fenêtres

# Dimensions de l'écran
screen_width = 1920
screen_height = 1080

def close_popups():
    # Fonction pour fermer les popups
    while True:  # Boucle infinie pour surveiller en permanence les fenêtres

        # Obtenir toutes les fenêtres actives sur l'écran
        all_windows = gw.getAllWindows()

        # Parcourir toutes les fenêtres
        for window in all_windows:
            if window.visible:  # Vérifier si la fenêtre est visible à l'écran

                # Obtenir les coordonnées de la fenêtre
                left, top, right, bottom = window.left, window.top, window.right, window.bottom

                # Vérifier si la fenêtre est en bas à droite de l'écran
                if left > screen_width - 400 and top > screen_height - 400:
                    try:
                        # Se connecter à l'application associée à la fenêtre
                        app = Application().connect(handle=window._hWnd)
                        # Fermer la fenêtre
                        app.kill()
                        # Afficher un message de confirmation
                        print(f"Fermé la fenêtre pop-up : {window.title}")
                    except Exception as e:
                        # Afficher une erreur s'il y a un problème lors de la fermeture de la fenêtre
                        print(f"Erreur en fermant la fenêtre {window.title}: {e}")

        # Attendre pendant 5 secondes avant de vérifier à nouveau les fenêtres
        time.sleep(5)

# Exécuter la fonction close_popups() si le script est exécuté directement
if __name__ == "__main__":
    close_popups()
