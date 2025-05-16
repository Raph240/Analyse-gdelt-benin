Titre :  Extraction et structuration des données du Bénin à partir de GDELT
Description :
Ce projet a pour objectif d’extraire, analyser et structurer les informations relatives au Bénin issues de la base de données GDELT (Global Database of Events, Language, and Tone). 
Le code est entièrement écrit dans un Notebook Jupyter, avec des explications étape par étape dans chaque cellule.

Étapes du notebook :
- Téléchargement automatique de fichiers ZIP contenant les données GDELT (à partir de liens texte)
- Décompression et extraction des fichiers CSV
- Filtrage des données pour ne conserver que les lignes concernant le Bénin
- Nettoyage linguistique des textes associés aux événements (issus de liens web)
- Extraction de tendances thématiques et émotionnelles avec spaCy et Gensim
- Résumés automatiques de textes
- Visualisation des résultats : nuages de mots sur les thématiques les plus abordées, diagramme circulaire sur les organisations les plus actives..

Prérequis : 
- Python 3.11
- Jupyter Notebook ou JupyterLab

Installez les bibliothèques nécessaires avec : 
pip install -r requirements.txt
ou bien manuellement (voir la liste des bibliothèques ci-dessous).

Utilisation :
1-	Lancer jupyter
2-	Ouvrez le fichier : Code_Projet_GDELT.ipynb
3-	Exécutez les cellules dans l'ordre. Chaque cellule contient des instructions claires sur ce qu'elle effectue.
4-	Les résultats incluent :
•	Des fichiers CSV filtrés
•	Des analyses thématiques
•	Des analyses émotionnelles 
•	Des résumés de texte
•	Des visualisations graphiques

Bibliothèques principales
•	pandas
•	requests
•	tqdm
•	spaCy
•	gensim
•	transformers
•	newspaper3k
•	wordcloud
•	matplotlib
•	python-docx

Auteur
Raphaël DAH-LOKONON 

Licence
Ce projet est distribué sous la licence MIT.  
Vous pouvez l'utiliser, le modifier et le partager librement à condition de mentionner l'auteur.
