
# **Rapport : Projet Traceroute (Version corrigée)**

---

## **1. Contexte et Objectif**

### Contexte  
Ce projet a été réalisé dans le cadre du cours **DEV2-PY1** pour valider les compétences en scripting Python. Le but était de concevoir un script interactif en ligne de commande permettant d'effectuer un **traceroute** automatisé.

### Objectif  
Le script permet de réaliser un **traceroute** vers une cible donnée (URL ou adresse IP) et propose les fonctionnalités suivantes :
- **Mode progressif (`-p`)** : Afficher les résultats au fur et à mesure.
- **Mode sauvegarde (`-o`)** : Enregistrer les résultats dans un fichier spécifié.

---

## **2. Description du Script**

### Fonctionnalités  
- **Entrée utilisateur :**  
   - Le script prend en paramètre obligatoire une URL ou une adresse IP.  
   - Deux options supplémentaires :  
      - `-p` ou `--progressive` : Affiche les résultats en temps réel.  
      - `-o` ou `--output-file` : Sauvegarde les résultats dans un fichier spécifié.

- **Adaptabilité :**  
   - Compatible avec **Windows** via la commande `tracert`.  
   - Le script utilise `subprocess` pour interagir avec la commande système.

- **Robustesse :**  
   - Prise en charge des erreurs via des exceptions (`try/except`).  
   - Extraction précise des adresses IP (IPv4 et IPv6).

---

## **3. Changements par rapport à l'ancienne version**

### Problèmes identifiés dans la version précédente  
- **Affichage incorrect** :  
   - Les sorties brutes de `tracert` incluaient des caractères indésirables comme des lettres ou des chiffres isolés.  
   - L'expression régulière n'extrayait que les adresses IPv4, ignorant les adresses IPv6.  

- **Fichier de sortie** :  
   - Les résultats sauvegardés dans un fichier étaient vides ou incorrects.

### Améliorations apportées  
1. **Extraction des adresses IPv4 et IPv6** :  
   - Une nouvelle expression régulière a été implémentée pour capturer à la fois les adresses **IPv4** (ex: `192.168.1.1`) et **IPv6** (ex: `2a02:a000:1:fff3::1`).  

2. **Filtrage des résultats** :  
   - Les lignes de sortie inutiles sont ignorées.  
   - Suppression des doublons pour n’afficher que les adresses IP uniques.

3. **Compatibilité renforcée** :  
   - Prise en compte des spécificités de l’encodage **Windows (`cp850`)** pour éviter les erreurs liées à `subprocess`.  

---

## **4. Fonctionnement**

### Utilisation du Script  
Exécutez le script dans un terminal Windows avec les commandes suivantes :

#### Traceroute simple  
```bash
python traceroute_script.py example.com
```

#### Traceroute avec affichage progressif  
```bash
python traceroute_script.py example.com -p
```

#### Traceroute avec sauvegarde des résultats  
```bash
python traceroute_script.py example.com -o results.txt
```

#### Traceroute avec affichage progressif et sauvegarde  
```bash
python traceroute_script.py example.com -p -o results.txt
```

---

### Exemple de Résultats

#### Commande exécutée :  
```bash
python traceroute_script.py google.com -p -o google_traceroute.txt
```

#### Résultats affichés :  
```
2a00:1450:400e:801::200e
fdaa:bbcc:ddee:0:46d4:54ff:fef6:b1e3
2a02:a000:1:fff3::1
2a02:a000:1:fffb::2
2001:4860:0:1::471b
```

#### Contenu du fichier `google_traceroute.txt` :  
```
2a00:1450:400e:801::200e
fdaa:bbcc:ddee:0:46d4:54ff:fef6:b1e3
2a02:a000:1:fff3::1
2a02:a000:1:fffb::2
2001:4860:0:1::471b
```

---

## **5. Validation des Compétences**

### Fonctionnalité validée  
Le script répond aux exigences du projet :  
- Interface en ligne de commande avec des options claires.  
- Extraction précise des adresses IPv4 et IPv6.  
- Affichage progressif des résultats et sauvegarde dans un fichier.

### Gestion des erreurs  
Exemples d’erreurs gérées :  
- Entrée invalide :  
   ```  
   Invalid target: invalid_target. Must be a valid IP or domain.  
   ```  
- Commande introuvable ou échec de `tracert` :  
   ```  
   Error: 'tracert' command failed or is unavailable.  
   ```

---

## **6. Utilisation d'une IA Générative**

L'IA a été utilisée pour :  
- **Identifier et corriger les problèmes** : Adaptation du script pour inclure les adresses IPv6 et filtrer les sorties incorrectes.  
- **Améliorer la robustesse** : Gestion des encodages Windows et suppression des doublons.  
- **Documenter le projet** : Structuration claire du rapport et ajout des comparaisons entre les versions.  

---

## **7. Conclusion**

Le projet a permis de démontrer les compétences suivantes :  
- Création d'un script Python robuste utilisant `subprocess` et `argparse`.  
- Extraction et affichage précis des adresses IP (IPv4/IPv6).  
- Gestion des exceptions et sauvegarde des résultats.  

Grâce aux améliorations apportées, le script est désormais fonctionnel, fiable et prêt à être utilisé dans différents contextes réseau.  
