# Projet de Stéganographie

## Résumé

Le but de ce projet est de pouvoir cacher un message dans une image, de pouvoir le récuperer et de rendre ceci le plus complique possible pour quelqun qui ne sait pas comment nous l'avons caché. Pour faire cela nous allons écrire un message dans les valeurs RGB de chaque pixel de l'image, puis utiliser des algorithme qui modifie légèrement ces valeurs pour rendre le message illisble au yeux de ceux qui ne connaissent pas l'algorithme. Mais que nous pouvons encore lire grâce à un algorithme de décodage.


## Mode d'emploi

### Script

Pour cacher un message dans une image : 
    -Exécuter le fichier Encoder_un_message.py en tant que script
    -Donner le nom de l'image dans laquel vous voulez cacher le message, le message et le nom de la nouvelle image quand le script vous le demande

Pour extraire le message d'une image :
    -Exécuter le fichier Decode_un_message.py 
    - Donner le nom de l'image dont vous voulez extraire l'image

### Fonctions principales

Pour l'encodage:

    - L'initialisation de la class Encoding:
        -Génère aléatoirement un code d'encodage (clé définissant quelles fonctions vont être utilisées sur quelles couches) et une clé pour les couches d'encodage (qui définit si on écrit sur une couche paire ou impaire pour chaque couleur).
        -Prépare pour l'écriture en mettant toutes les valeurs d'une couche à la même parité (tous pair ou impair dépendant de la clé).
        -Création d'une signature : clé sous forme de couleur qui contient la clé pour les couches d'encodage et le code d'encodage.

    -La fonction Encode:
         -message_to-bin : transforme le message d'une chaîne de caractères à du binaire (suite de 0 et de 1)

        -write_message : écrit le message en binaire sur l'image en aditionant le binaire au valeur des pixels

        - Les fonctions d'encodage : 
            -test_func qui aditionne 1 à la valeur d'une couleur pour chaque pixel
            -func_1 qui aditionne 1 à la valeur d'une couleur pour chaque pixel si la valeur de la même couleur du pixel précedant était impaire
            -func_2 qui transmet la parité de chaque couleur à une autre, le sens de cette roataion change selon la position du pixel (selon un damier)
        
        - Pose la signature comme valeur du premier pixel

        - Sauvegarde l'image avec son nouceau nom

Pour le Déodage :

    - la fonction Decode :
        -find-signature : trouve la signature utilisé lors de l'encodage
        -Les fonctions de decodage : font l'inverse de leur homologues d'encodage
        -extract_message : sort le message en binaire de l'iamge
        -transalte_to_text : transforme le message binaire en une chaîne de caractères 



## Les ALgorithmes

Le choix de des fonction utilisées est aléatoire et leur couleur d'application aussi (une fonction peut 
être aplliquée à plusieurs couleurs), lors du choix chaque couple fonction-couleur a 50% de chance d'être choisi mais il doit y avoir au moins 4 couple choisi sinon le tirage des couples se fera à nouveau.

Chaque fonction prend en argument l'image et une couleur.

test_func : Ajoute 1 à la valeur de la couleur donnée en argument de chaque pixel.

func_1 : Pour chaque pixel ajoute 1 à la valeur de la couleur donnée en argument si la valeur du pixel précedant était impaire (parcouru par colonne de haut en bas et de droite à gauche).

func_2 : Si la couleur donnée en argument est 0, fait tourner la parité des valeurs des couleurs entre elles, pour chaque pixel. Le sens de la rotation dépend de la position du pixel, si la somme des numéros de sa colonne et de sa ligne est paire, le sens de roation est R -> B -> G -> R et l'invere si la somme est impaire.

##  Implémentation Technique



## Journal de Bord 

-->12 Décembre, Killian:
    -class pixels
    -base des fonction Encoding et Decoding (surtout de la structure pas vraiment du code)

--> 18 Décembre, Arthur: 
    - premier commit d'Arthur, mini testes comment changer pixels d'image 

--> 21 Décembre, Arthur:
    - En salle info, Emilien m'explique la base de quelques fonction for(width x height):
    - tjrs changer tuple en liste puis denouveau tuple  

--> 22 Décembre, Arthur:
    - Notebook cesar 1 decodage bien compris (j'estime que le notebook cryptage est une étape nécessaire pour comprendre la stegano)

--> 24 Décembre, Arthur:
	- fonction qui prend une lettre (str) et return (str) son ascii en binaire

--> 26 Décembre, Arthur: 
	- fonction qui prend comme argument une string et return pour chaque lettre, l'ascii (str) en binaire. Toutes ces valeurs ascii en binaire 
	forment une liste qui se fait return à la fin de la fonction.

--> 27-28 Décembre Arthur: 
    - 

--> 3 janvier , Killian:
    - finit les fonction d'écriture et de lecture
    - premiere fonction d'encodage et de decodage
    - écriture et lecture sur toute les couleurs
    - test sur plus grand echantillons et decouverte d'un porbleme concernant les pixels de valeur 0 

--> 5 janvier, Killian:
    - correction dans le code au niveau de quelques cas limite

--> 6 janvier, Killian:
    -correction du bug avec les pixels de valeurs 0 
    -correction au niveau des couches d'encodage (on peu mtn encoder sur des couches pair ou impair)
    -systeme de choix et de lecture des couches d'encodage et des codes dencodage

--> 7 janvier, Killian:
    -corrections des bugs 
    -test suplementaires et plus extensif
    -code fonctionel sans bug observé
    -ajout func_2 encodage et decodage
    -ajout d'un seuil minimum de fonction d'encodage
    -ajout des scripts
    -cas ou aucun nom de nouvelle image est donée

--> 8 janvier, Killian :
    -Fichier README