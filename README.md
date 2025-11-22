# PSampler

PSampler est un petit programme Python qui permet de jouer des sons avec des raccourcis clavier.
Les sons sont définis dans `config.json` et doivent être placés dans le dossier `sounds/`.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python psampler.py
```

Le programme écoute les raccourcis définis dans `config.json`.

## Configuration

Exemple de `config.json` utilisant les combinaisons **CTRL+ALT** :

```json
{
  "ctrl+alt+1": "sounds/son1.mp3",
  "ctrl+alt+2": "sounds/son2.mp3",
  "ctrl+alt+3": "sounds/son3.mp3"
}
```

Les fichiers audio doivent être placés dans :

```
sounds/
```

## Structure du projet

```
psampler.py
config.json
requirements.txt
sounds/
```

## Fonctionnalités

* Charge les fichiers audio en mémoire pour une exécution **instantanée**
* Appuyer sur **ESPACE** coupe immédiatement le son en cours de lecture

## Dépendances

* pygame
* keyboard
