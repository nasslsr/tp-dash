# Image de base
FROM python:3.9-slim-buster

# Définit le répertoire de travail
WORKDIR /LAASRI_NASSER


# Copie le fichier requirements.txt dans l'image
COPY requirements.txt .

# Installe les dépendances
RUN pip install -r requirements.txt

# Copie tous les fichiers de l'application
COPY . .

# Expose le port 8051
EXPOSE 8051


CMD ["python3", "tp_dash.py"]

