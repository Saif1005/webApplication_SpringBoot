# Application Web de Gestion de Projet

Ce projet est une **application web de gestion de projet** avec un **back-end** développé en **Spring Boot** et un **front-end** utilisant **HTML**, **CSS**, et **JavaScript**. L'application permet de gérer des produits, de les ajouter, de les rechercher, et de les classer en utilisant un modèle de régression logistique. Une interface interactive est également fournie via **Streamlit** pour visualiser et interagir avec les données.

## Fonctionnalités

- **Gestion de produits** : Ajout, recherche, modification et suppression de produits dans la base de données via une interface web.
- **Régression logistique** : Un script Python analyse les données des produits et applique un modèle de régression logistique pour la classification des produits.
- **Interface Streamlit** : Un dashboard interactif développé avec Streamlit permet d'ajouter de nouveaux produits, de visualiser les résultats du modèle de régression logistique et de gérer la base de données.

## Structure du Projet

1. **Back-end (Spring Boot)** :
   - **Spring Boot** pour la gestion des requêtes HTTP, la logique métier et les opérations CRUD.
   - **JPA/Hibernate** pour l'accès à la base de données et la gestion des entités.
   - Les routes REST sont utilisées pour gérer les produits.
   - API disponible pour l'ajout et la recherche de produits.

2. **Front-end (HTML, CSS, JS)** :
   - Interface web permettant l'ajout et la gestion des produits.
   - Intégration de l'API back-end pour effectuer des requêtes AJAX.
   - Création avec **HTML**, **CSS**, et **JavaScript**.

3. **Python (Régression Logistique et Streamlit)** :
   - Script Python qui interagit avec l'API du back-end, récupère les données et applique un modèle de **régression logistique** pour la classification.
   - Utilisation de **Streamlit** pour créer une interface simple et interactive permettant d'ajouter de nouveaux produits et de visualiser les résultats du modèle.

## Installation

### Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- **Java 17** ou supérieur
- **Maven** pour gérer les dépendances de Spring Boot
- **Python 3.x** pour l'exécution du script Python et Streamlit
- **MySQL** ou tout autre système de gestion de base de données

### Installation du Back-end (Spring Boot)

1. Clonez le dépôt du projet :
   ```bash
   git clone https://github.com/ton-utilisateur/ton-repository.git
   cd ton-dossier
