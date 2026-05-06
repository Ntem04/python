# --- Correction du Projet 1 : Log Parser ---

# Chemins des fichiers
fichier_source = "cours_exercices/projets scraping/access.log"
fichier_destination = "cours_exercices/projets scraping/alerte_erreurs.txt"

try:
    # 1. Ouverture du fichier source en mode lecture ('r')
    with open(fichier_source, "r") as flux_entree:
        # 2. Ouverture (ou création) du fichier destination en mode écriture ('w')
        with open(fichier_destination, "w") as flux_sortie:
            
            flux_sortie.write("RAPPORT DES ERREURS DETECTEES\n")
            flux_sortie.write("="*30 + "\n\n")
            
            compteur_erreurs = 0
            
            # 3. Lecture ligne par ligne
            for ligne in flux_entree:
                # On retire les espaces inutiles en fin de ligne
                ligne = ligne.strip()
                
                # On saute la ligne si elle est vide
                if not ligne:
                    continue
                
                # 4. Extraction des données avec split()
                elements = ligne.split()
                
                # Selon le format de access.log :
                # Index 0 : IP | Index 5 : Chemin | Index 7 : Code Statut
                ip = elements[0]
                chemin = elements[5]
                code_statut = elements[7]
                
                # 5. Filtrage des erreurs (Codes 400 à 599)
                # On transf orme le code en entier pour plus de flexibilité
                if int(code_statut) >= 400:
                    compteur_erreurs += 1
                    message = f"ALERTE : IP {ip} -> Erreur {code_statut} sur {chemin}\n"
                    
                    # 6. Écriture dans le fichier de destination
                    flux_sortie.write(message)
                    print(f"Erreur trouvée et enregistrée : {code_statut}")

            flux_sortie.write(f"\nTotal des erreurs trouvées : {compteur_erreurs}")

    print(f"\nAnalyse terminée. {compteur_erreurs} erreurs ont été extraites dans '{fichier_destination}'.")

except FileNotFoundError:
    print(f"Erreur : Le fichier '{fichier_source}' est introuvable. Assure-toi de l'avoir créé.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")