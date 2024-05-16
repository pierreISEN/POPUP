import time
import pygetwindow as gw
from pywinauto import Application

screen_width = 1920
screen_height = 1080

def close_popups():
    while True:
        all_windows = gw.getAllWindows()

        for window in all_windows:
            if window.visible:
                left, top, right, bottom = window.left, window.top, window.right, window.bottom

                if left > screen_width - 400 and top > screen_height - 400:
                    try:
                        app = Application().connect(handle=window._hWnd)
                        app.kill()
                        print(f"Fermé la fenêtre pop-up : {window.title}")
                    except Exception as e:
                        print(f"Erreur en fermant la fenêtre {window.title}: {e}")

        time.sleep(5)

def block_new_popups():
    while True:
        # Obtenir toutes les fenêtres actives sur l'écran
        all_windows = gw.getAllWindows()

        # Filtrer les nouvelles fenêtres qui sont en bas à droite de l'écran
        new_bottom_right_popups = [window for window in all_windows if window.visible and window.left > screen_width - 400 and window.top > screen_height - 400]

        # Fermer les nouvelles fenêtres qui sont des popups en bas à droite de l'écran
        for window in new_bottom_right_popups:
            try:
                app = Application().connect(handle=window._hWnd)
                app.kill()
                print(f"Fermé la fenêtre pop-up : {window.title}")
            except Exception as e:
                print(f"Erreur en fermant la fenêtre {window.title}: {e}")

        time.sleep(2)

if __name__ == "__main__":
    import threading
    thread1 = threading.Thread(target=close_popups)
    thread2 = threading.Thread(target=block_new_popups)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
