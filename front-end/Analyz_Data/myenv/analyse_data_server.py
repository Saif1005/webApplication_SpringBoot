import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Fonction pour récupérer les données depuis l'API
def fetch_data():
    url = "http://localhost:8081/api/produits"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        data = response.json()  # Convertir la réponse en JSON
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la récupération des données : {e}")
        return pd.DataFrame()  # Retourne un DataFrame vide en cas d'erreur

# Fonction pour traiter les données
def preprocess_data(df):
    # Enlever les lignes avec des valeurs manquantes
    df = df.dropna()

    # Exemple de conversion : catégorie en fonction du prix
    bins = [0, 10, 100, 500, 1000, 10000]
    labels = ['Très bon marché', 'Bon marché', 'Moyenne gamme', 'Haut de gamme', 'Très haut de gamme']
    df['categorie'] = pd.cut(df['prix'], bins=bins, labels=labels, right=False)

    # Classification selon l'utilité
    utilite_mapping = {
        'eau': 'Nutrition',
        'cafe': 'Nutrition',
        'pc': 'Travail',
        'smart_phone': 'Communication',
        'parfum': 'Esthétique'
    }
    df['utilite'] = df['nom'].map(utilite_mapping).fillna('Autre')

    return df

# Fonction pour entraîner le modèle
def train_and_predict(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"Accuracy : {accuracy:.2f}")

    return model, scaler

# Fonction principale
def main():
    st.title("Classification des Produits")

    # Initialiser les données dans session_state si ce n'est pas fait
    if 'data' not in st.session_state:
        st.session_state['data'] = fetch_data()

    st.write("Données actuelles :")
    st.dataframe(st.session_state['data'])

    # Formulaire d'ajout de produit
    with st.form("Ajouter un produit"):
        nom_produit = st.text_input("Nom du produit")
        prix_produit = st.number_input("Prix du produit", min_value=0.0)
        submit_button = st.form_submit_button("Ajouter")

    # Ajouter le produit si le formulaire est soumis
    if submit_button:
        if nom_produit and prix_produit > 0:
            new_product = {"nom": nom_produit, "prix": prix_produit}
            try:
                response = requests.post("http://localhost:8081/api/produits", json=new_product)
                response.raise_for_status()
                st.success(f"Produit '{nom_produit}' ajouté avec succès !")

                # Ajouter le nouveau produit au DataFrame local
                new_data = pd.DataFrame([new_product])
                st.session_state['data'] = pd.concat([st.session_state['data'], new_data], ignore_index=True)

            except requests.exceptions.RequestException as e:
                st.error(f"Erreur lors de l'ajout du produit : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")

    # Prétraitement des données
    df = preprocess_data(st.session_state['data'])
    st.write("Données prétraitées :")
    st.dataframe(df)

    # Visualisation des catégories
    st.write("Visualisation des catégories :")
    fig, ax = plt.subplots()
    sns.countplot(x='categorie', data=df, ax=ax)
    st.pyplot(fig)

    # Division des données en ensembles d'entraînement et de test
    X = df[['prix']]
    y = df['categorie']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraînement du modèle
    st.write("Entraînement du modèle...")
    model, scaler = train_and_predict(X_train, X_test, y_train, y_test)

    # Prédiction sur de nouvelles données
    st.write("Prédiction sur de nouvelles données :")
    new_data_input = st.number_input("Entrez un prix pour prédire la catégorie", min_value=0.0)
    if st.button("Prédire"):
        new_data_scaled = scaler.transform([[new_data_input]])
        prediction = model.predict(new_data_scaled)
        st.write(f"Catégorie prédite : {prediction[0]}")

if __name__ == "__main__":
    main()
