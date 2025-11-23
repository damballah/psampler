# PSampler

PSampler est un petit programme Python qui permet de jouer des sons avec des raccourcis clavier.
Les sons sont définis dans `config.json` et doivent être placés dans le dossier `sounds/`. 
Il est fourni avec 74 sons de test (Sons du sampler de Thierry Ardisson, 3 blockbusters des années 80-90 et des bruitages divers)

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
Vous pouvez aussi utiliser la touche "shift", exemple : "shift+1" ou bien "ctrl+shift+1"

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

## Sons fournis : 
```
  Ctrl + Alt + 0  -->  sounds/Ardisson/BEN_HUR.mp3
  Ctrl + Alt + 1  -->  sounds/Ardisson/JINGLE_PUB.mp3
  Ctrl + Alt + 2  -->  sounds/Ardisson/MAGNETO_SERGE.mp3
  Ctrl + Alt + 3  -->  sounds/Ardisson/ON_NE_BOUGE_PAS_PENDANT_LE_JINGLE.mp3
  Ctrl + Alt + 4  -->  sounds/Ardisson/SACREE_SOIREE.mp3
  Ctrl + Alt + 5  -->  sounds/Ardisson/SILENCIEUX.mp3
  Ctrl + Alt + 6  -->  sounds/Ardisson/WITHIN_YOU.mp3
  Ctrl + Alt + 7  -->  sounds/Ardisson/RED_ALERT.mp3
  Ctrl + Alt + 8  -->  sounds/Ardisson/CABANIS.mp3
  Ctrl + Alt + 9  -->  sounds/Ardisson/20_TH_CENTURY.mp3
  Ctrl + Alt + a  -->  sounds/Ghostbuster/ES_TU_UN_DIEU.mp3
  Ctrl + Alt + z  -->  sounds/Ghostbuster/ON_EST_VENU_ON_L_A_VUE.mp3
  Ctrl + Alt + e  -->  sounds/Ghostbuster/RACCOURCI_TON_RAYON.mp3
  Ctrl + Alt + r  -->  sounds/Ghostbuster/RDV_SUR_L_AUTRE_RIVE.mp3
  Ctrl + Alt + t  -->  sounds/Ghostbuster/SALAUD_QUI_M_A_ENGLUE.mp3
  Ctrl + Alt + y  -->  sounds/Retour_vers_le_futur/BONNE_NUIT_VISITEUR_DU_FUTUR.mp3
  Ctrl + Alt + u  -->  sounds/Retour_vers_le_futur/C_EST_TOI_QUI_L_A_FERRE_JE_DIS_MOI.mp3
  Ctrl + Alt + i  -->  sounds/Retour_vers_le_futur/CIRCUIT_BRANCHE_CONVERTER_TEMPOREL.mp3
  Ctrl + Alt + o  -->  sounds/Retour_vers_le_futur/JITSU_NE_DECOUVRIRA_JAMAIS_LE_POT_AU_ROSE.mp3
  Ctrl + Alt + p  -->  sounds/Retour_vers_le_futur/PAR_TOUS_LES_PEPINS_DE_LA_POMME_DE_NEWTON.mp3
  Ctrl + Alt + q  -->  sounds/Retour_vers_le_futur/T_ES_SOURD_MCFLAN.mp3
  Ctrl + Alt + s  -->  sounds/Retour_vers_le_futur/TOUT_LE_MONDE_S_AMUSE.mp3
  Ctrl + Alt + d  -->  sounds/Terminator/ALORS_QUI_S_EST_LA_MERDE.mp3
  Ctrl + Alt + f  -->  sounds/Terminator/BELLE_SOIREE_POUR_UNE_BALADE.mp3
  Ctrl + Alt + g  -->  sounds/Terminator/IL_S_APPELLE_JOHN_CONNOR.mp3
  Ctrl + Alt + h  -->  sounds/Terminator/SUIS_MOI_SI_TU_NE_VEUX_PAS_MOURIR.mp3
  Ctrl + Alt + j  -->  sounds/Terminator/TU_ES_LA_CIBLE_DU_TERMINATOR.mp3
  Ctrl + Alt + k  -->  sounds/Bruitages/CHUCHOTTEMENT.mp3
  Ctrl + Alt + l  -->  sounds/Bruitages/EPEE_FEND_L_AIR.mp3
  Ctrl + Alt + m  -->  sounds/Bruitages/FANTOME.mp3
  Ctrl + Alt + w  -->  sounds/Bruitages/HELICOPTERE_PASSAGE.mp3
  Ctrl + Alt + x  -->  sounds/Bruitages/MODEM_56K.mp3
  Ctrl + Alt + c  -->  sounds/Bruitages/PAQUEBOT.mp3
  Ctrl + Alt + v  -->  sounds/Bruitages/PET_SOUPLE.mp3
  Ctrl + Alt + b  -->  sounds/Bruitages/RADIO_GRESILLEMENT.mp3
  Ctrl + Alt + n  -->  sounds/Bruitages/ZOMBIE.mp3

```
