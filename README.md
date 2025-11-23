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
sounds/Ardisson/BEN_HUR.mp3
sounds/Ardisson/JINGLE_PUB.mp3
sounds/Ardisson/MAGNETO_SERGE.mp3
sounds/Ardisson/ON_NE_BOUGE_PAS_PENDANT_LE_JINGLE.mp3
sounds/Ardisson/SACREE_SOIREE.mp3
sounds/Ardisson/SILENCIEUX.mp3
sounds/Ardisson/WITHIN_YOU.mp3
sounds/Ardisson/RED_ALERT.mp3
sounds/Ardisson/CABANIS.mp3
sounds/Ardisson/20_TH_CENTURY.mp3
sounds/Ghostbuster/ES_TU_UN_DIEU.mp3
sounds/Ghostbuster/ON_EST_VENU_ON_L_A_VUE.mp3
sounds/Ghostbuster/RACCOURCI_TON_RAYON.mp3
sounds/Ghostbuster/RDV_SUR_L_AUTRE_RIVE.mp3
sounds/Ghostbuster/SALAUD_QUI_M_A_ENGLUE.mp3
sounds/Retour_vers_le_futur/BONNE_NUIT_VISITEUR_DU_FUTUR.mp3
sounds/Retour_vers_le_futur/C_EST_TOI_QUI_L_A_FERRE_JE_DIS_MOI.mp3
sounds/Retour_vers_le_futur/CIRCUIT_BRANCHE_CONVERTER_TEMPOREL.mp3
sounds/Retour_vers_le_futur/JITSU_NE_DECOUVRIRA_JAMAIS_LE_POT_AU_ROSE.mp3
sounds/Retour_vers_le_futur/PAR_TOUS_LES_PEPINS_DE_LA_POMME_DE_NEWTON.mp3
sounds/Retour_vers_le_futur/T_ES_SOURD_MCFLAN.mp3
sounds/Retour_vers_le_futur/TOUT_LE_MONDE_S_AMUSE.mp3
sounds/Terminator/ALORS_QUI_S_EST_LA_MERDE.mp3
sounds/Terminator/BELLE_SOIREE_POUR_UNE_BALADE.mp3
sounds/Terminator/IL_S_APPELLE_JOHN_CONNOR.mp3
sounds/Terminator/SUIS_MOI_SI_TU_NE_VEUX_PAS_MOURIR.mp3
sounds/Terminator/TU_ES_LA_CIBLE_DU_TERMINATOR.mp3
sounds/Bruitages/CHUCHOTTEMENT.mp3
sounds/Bruitages/EPEE_FEND_L_AIR.mp3
sounds/Bruitages/FANTOME.mp3
sounds/Bruitages/HELICOPTERE_PASSAGE.mp3
sounds/Bruitages/MODEM_56K.mp3
sounds/Bruitages/PAQUEBOT.mp3
sounds/Bruitages/PET_SOUPLE.mp3
sounds/Bruitages/RADIO_GRESILLEMENT.mp3
sounds/Bruitages/ZOMBIE.mp3
```
