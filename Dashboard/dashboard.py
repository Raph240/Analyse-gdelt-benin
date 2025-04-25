
import streamlit as st
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="Analyse GDELT - Bénin", layout="wide")

st.title("🌍 Analyse des Thèmes et Organisations dans les articles sur le Bénin")

# Chargement du fichier CSV
uploaded_file = st.file_uploader("📂 Téléversez votre fichier CSV (doit contenir les colonnes 'Thèmes' et 'Organisations')", type="csv")

if uploaded_file:
    df_2 = pd.read_csv(uploaded_file)

    if "Thèmes" in df_2.columns and "Organisations" in df_2.columns:

        st.success("Fichier chargé avec succès ✅")

        st.header("1️⃣ Nuage de mots des thèmes fréquents")

        # Extraire et compter les thèmes
        all_themes = df_2["Thèmes"].dropna().str.split(';').sum()
        theme_counts = Counter(all_themes)
        top_themes = theme_counts.most_common()
        frequent_themes = [theme for theme, count in top_themes if count >= 5]

        if frequent_themes:
            text = " ".join(frequent_themes)
            wordcloud = WordCloud(width=1200, height=800, background_color='white').generate(text)

            fig1, ax1 = plt.subplots(figsize=(12, 8))
            ax1.imshow(wordcloud, interpolation='bilinear')
            ax1.axis("off")
            ax1.set_title("Nuage de mots des thèmes fréquents", fontsize=20)
            st.pyplot(fig1)
        else:
            st.warning("Aucun thème fréquent trouvé (fréquence ≥ 5).")

        st.header("2️⃣ Diagramme circulaire des organisations les plus citées")

        # Fonction pour extraire les noms d'organisations
        def extract_organization_names(org_series):
            org_names = []
            for row in org_series.dropna():
                items = row.split(';')
                for item in items:
                    parts = item.split(',')
                    if parts:
                        org_names.append(parts[0].strip())
            return org_names

        all_org = extract_organization_names(df_2["Organisations"])
        org_counts = Counter(all_org)
        top_n = 15
        top_org = org_counts.most_common(top_n)

        if top_org:
            labels = [org for org, count in top_org]
            values = [count for org, count in top_org]

            fig2, ax2 = plt.subplots(figsize=(8, 8))
            ax2.pie(values, labels=labels, autopct='%1.1f%%', startangle=180)
            ax2.set_title(f"Top {top_n} des organisations les plus citées", fontsize=16)
            ax2.axis('equal')
            st.pyplot(fig2)
        else:
            st.warning("Aucune organisation trouvée dans les données.")

    else:
        st.error("Le fichier doit contenir les colonnes 'Thèmes' et 'Organisations'.")
