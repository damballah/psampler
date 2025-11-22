import os
import json
import keyboard
import pygame

# Initialiser pygame mixer
pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

current_channel = None
sounds_cache = {}   # Tous les sons préchargés ici

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def preload_sounds(config):
    """Charge tous les sons en mémoire au démarrage."""
    global sounds_cache

    for key_combo, relative_path in config.items():
        full_path = os.path.join(BASE_DIR, relative_path)
        try:
            sound = pygame.mixer.Sound(full_path)
            sounds_cache[key_combo] = sound
            print(f"Préchargé : {relative_path}")
        except Exception as e:
            print(f"Erreur lors du préchargement {relative_path} : {e}")

def stop_current_sound():
    global current_channel
    if current_channel:
        current_channel.stop()

def play_sound(relative_path):
    """Joue un son déjà préchargé en mémoire."""
    global current_channel

    # STOP du son précédent
    stop_current_sound()

    # Retrouver le son dans le cache en utilisant directement le chemin relatif
    for key, path in config.items():
        if path == relative_path:
            sound = sounds_cache[key]
            current_channel = sound.play()
            print(f"Lecture : {relative_path}")
            return

def stop_sound_key():
    stop_current_sound()
    print("Son stoppé (barre espace).")

def main():
    global config
    config = load_config()

    # PRÉCHARGEMENT des sons
    preload_sounds(config)

    print("\nRaccourcis actifs :")
    for key_combo, sound_file in config.items():
        print(f"  {key_combo} → {sound_file}")
        keyboard.add_hotkey(key_combo, play_sound, args=[sound_file])

    keyboard.add_hotkey("space", stop_sound_key)

    print("\nTous les sons sont maintenant en mémoire – lancement instantané.")
    keyboard.wait()

if __name__ == "__main__":
    main()
