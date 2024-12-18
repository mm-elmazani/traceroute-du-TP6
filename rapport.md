# Probleme survenu
le code ne prenait pas en compte les addresse IPv6


# Rapport : Projet Traceroute

## **1. Contexte et Objectif**

### Contexte
Ce projet a été réalisé dans le cadre du cours **DEV2-PY1** pour valider les compétences en scripting Python. Le but était de créer un script interagissant avec le système informatique via une interface en ligne de commande.

### Objectif
Le script effectue un **traceroute** vers une cible donnée (URL ou adresse IP) et propose les fonctionnalités suivantes :
- **Mode progressif (`-p`)** : Afficher les résultats au fur et à mesure.
- **Mode sauvegarde (`-o`)** : Enregistrer les résultats dans un fichier.

---

## **2. Description du Script**

### Fonctionnalités
- **Entrée utilisateur :**
  - Le script prend une URL ou une adresse IP comme paramètre obligatoire.
  - Deux options supplémentaires : 
    - `-p` ou `--progressive` : Affiche les résultats en temps réel.
    - `-o` ou `--output-file` : Sauvegarde les résultats dans un fichier spécifié.

- **Adaptabilité :**
  - Compatible avec Windows (commande `tracert`) et Linux/macOS (commande `traceroute`).
  - Détection automatique de l'OS pour utiliser la bonne commande système.

- **Robustesse :**
  - Validation des entrées utilisateur.
  - Gestion des erreurs via des exceptions (`try/except`).

---

## **3. Fonctionnement**

### Utilisation du Script
Exécutez le script dans un terminal avec les commandes suivantes :

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
1  192.168.1.1 (192.168.1.1)  2.123 ms
2  10.0.0.1 (10.0.0.1)  3.567 ms
3  172.253.66.10 (172.253.66.10)  5.232 ms
...
```

---

## **4. Validation des Compétences**

### Fonctionnalité validée :
- Le script est fonctionnel et répond aux exigences :
  - Interface en ligne de commande avec options claires.
  - Gestion des erreurs (entrée invalide, commande manquante, etc.).
  - Résultats enregistrés dans un fichier si demandé.

### Gestion des erreurs :
Exemples d'erreurs gérées :
- Entrée invalide :
  ```
  Invalid target: invalid_target. Must be a valid IP or domain.
  ```
- Commande absente :
  ```
  Error: The 'traceroute' command is not available on your system.
  ```

---

## **5. Utilisation d'une IA Générative**

L'IA a été utilisée pour :
- **Générer les bases du script** : Conception des fonctionnalités et gestion des options.
- **Adapter le script** : Intégration de la compatibilité Windows/Linux.
- **Documenter le projet** : Proposer une structure claire pour le rapport.

---

## **6. Conclusion**

Le projet a permis de démontrer les compétences en scripting Python :
- Création d’un script automatisé interactif.
- Utilisation des modules Python (`argparse`, `subprocess`).
- Suivi des bonnes pratiques (validation des entrées, gestion des exceptions).

Le script est fonctionnel, documenté et extensible pour d'autres fonctionnalités si nécessaire.
