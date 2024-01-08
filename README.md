# Projet de Stéganographie

## Résumé

Le but de ce projet est de pouvoir cacher un message dans une image, de pouvoir le récuperer et de rendre ceci le plus compliqué possible pour quelqun qui ne sait pas comment nous l'avons caché. Pour faire cela nous allons écrire un message dans les valeurs RGB de chaque pixel de l'image, puis utiliser des algorithmes qui modifient légèrement ces valeurs pour rendre le message illisble au yeux de ceux qui ne connaissent pas l'algorithme. Mais que nous pouvons encore lire grâce à un algorithme de décodage.


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
            -func_2 qui transmet la parité de chaque couleur à une autre, le sens de cette rotataion change selon la position du pixel (selon un damier)
        
        - Pose la signature comme valeur du premier pixel

        - Sauvegarde l'image avec son nouveau nom

Pour le Décodage :

    - la fonction Decode :
        -find-signature : trouve la signature utilisé lors de l'encodage
        -Les fonctions de décodage : font l'inverse de leur homologues d'encodage
        -extract_message : sort le message en binaire de l'image
        -translate_to_text : transforme le message binaire en une chaîne de caractères 



## Les Algorithmes

Le choix des fonctions utilisées est aléatoire et leur couleur d'application aussi (une fonction peut 
être appliquée à plusieurs couleurs), lors du choix chaque couple fonction-couleur a 50% de chance d'être choisi mais il doit y avoir au moins 4 couples choisi sinon le tirage des couples se fera à nouveau.

Chaque fonction prend en argument l'image et une couleur.

test_func : Ajoute 1 à la valeur de la couleur donnée en argument de chaque pixel.

func_1 : Pour chaque pixel ajoute 1 à la valeur de la couleur donnée en argument si la valeur du pixel précedant était impaire (parcouru par colonne de haut en bas et de droite à gauche).

func_2 : Si la couleur donnée en argument est 0, fait tourner la parité des valeurs des couleurs entre elles, pour chaque pixel. Le sens de la rotation dépend de la position du pixel, si la somme des numéros de sa colonne et de sa ligne est paire, le sens de roation est R -> B -> G -> R et l'invere si la somme est impaire.

##  Implémentation Technique


Pour l'ensemble du code nous utilisons des objets de la class Pixels que nous avons crée, cela nous simplifie la plus part des opération sur la valeur des pixels. Cette class aurait pu 
être un plus complète, notament avec une fonction ajouter 1 à la valeur d'une couleur d'un pixel et son homologue pour la soustraction, ce qui aurait simplifié le code à plusieurs reprise (de même pour une fonction qui regarde la partié d'une valeur).

Nous avons aussi crée une class Encoding qui n'a pas énormément d'utilité autre que rendre le transfert des variables plus propres. Nous ne l'avons pas fait pour le décodage car les étapes se suivent d'une manière plus linéaire.

Au niveau de la granularité des fonctions, nous avons essayé de faire subdivise par ce que nous considérons des étapes sans non plus en abuser en faisant des fonctions qui ne contiennent qu'une seule ligne de code et qui ne vont qu'être utilisé une ou deux fois.

## Les Fonctions d'Arthur

Les petites fonctions ainsi que tous les tests sont dans le fichier (Arthur_fonctions_Coder_msg.py).
Dans le fichier (Arthur_utilisation_fonc.py) se situe la fonction principale qui permet de cacher le message dans l'image (imart.png). Cette fonction assemble toutes les plus petites fonctions.

Explication générale:
Cette méthode de sténographie marche de la manière suivante. 
Pour qu'une image puisse héberger un message est doit être "vierge". Pour qu'elle soit "vierge", chaque valeur R G et B de chaque pixel doit être pair.
Chaque du string qu'on veut cacher est caché dans 3 pixels car la représentation binaire de chaque caractère comporte 7 bits. Les trois pixels se situe dans la même colonne les uns au desssus des autres. 

Exemple: Message : "Yo" -> [1011001, 1101111]
Pour le représenter le Y :
"1" "0" "1" seront situé sur  pixel 1 (le coin en haut à gauche)(respectivement rouge, vert, bleu). "1" "0" "0" seront situé sur pixel 2 (le pixel juste au dessous). Les dernier "1" est ajouter au rouge du pixel 3. (encore au dessous) 

pixel en position (0,0) (num_pair + 1, num_pair + 0, num_pair + 1)      pixel en position (1,0)  .....  les chiffres binaires qui représent "o"
pixel en position (0,1) (num_pair + 1, num_pair + 0, num_pair + 0)      pixel en position (1,1)   .....     ""
pixel en position (0,2) (num_pair + 1, num_pair, num_pair)              pixel en position (1,2)   .....     ""

Ainsi le premier caractère est caché sur les trois premiers pixels de la première colonne, le deuxième caractère sur les trois premiers pixels de la deuxième colonne, le troisième caractère sur les trois premiers pixels de la troisième colonne et ainsi de suite. 

La fonction "Main_fonc" prend comme argument le message que l'on veut cacher (str)



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
    - Notebook cesar 1 décodage bien compris (j'estime que le notebook cryptage est une étape nécessaire pour comprendre la stegano)

--> 24 Décembre, Arthur:
	- fonction qui prend une lettre (str) et return (str) son ascii en binaire

--> 26 Décembre, Arthur: 
	- fonction qui prend comme argument une string et return pour chaque lettre, l'ascii (str) en binaire. Toutes ces valeurs ascii en binaire 
	forment une liste qui se fait return à la fin de la fonction.

--> 27-28 Décembre Arthur: 
    - Nouvelle fonction change_pixel:
    Cette fonction prend un string binaire exemple ("0b1010010"). Enlève le "0b" du début, puis ajoute chaque chiffre (0 ou 1) à une varaible qui représente la quantité de R, G ou B sur un pixel.
    Pour l'instant je donne des chiffre arbitraire à chaque quantité de couleur. Mais plustard P1_amount_red deviendra -> la fonction qui demande les valeurs d'un pixel

--> 3 janvier , Killian:
    - finit les fonction d'écriture et de lecture
    - premiere fonction d'encodage et de décodage
    - écriture et lecture sur toute les couleurs
    - test sur plus grand echantillons et decouverte d'un porbleme concernant les pixels de valeur 0 

--> 5 janvier, Killian:
    - correction dans le code au niveau de quelques cas limite

--> 6 janvier, Killian:
    -correction du bug avec les pixels de valeurs 0 
    -correction au niveau des couches d'encodage (on peu mtn encoder sur des couches pair ou impair)
    -systeme de choix et de lecture des couches d'encodage et des codes dencodage

--> 6 janvier, Arthur : 
    -appel avec Killian, discution du fonctionnement des fonctions de chacun
    -recherche fonctionnement objets/classes

-- > 7 janvier, Arthur: 
    -nouveau fichier avec fonction globale qui met toutes les fonctions jusqu'à maintenant créé ensemble
    -import fonctions de l'autre fichier

--> 7 janvier, Killian:
    -corrections des bugs 
    -test suplementaires et plus extensif
    -code fonctionel sans bug observé
    -ajout func_2 encodage et décodage
    -ajout d'un seuil minimum de fonction d'encodage
    -ajout des scripts
    -cas ou aucun nom de nouvelle image est donée

--> 8 janvier, Killian :
    -Fichier README : Résumé, Mode d'emploi, Fonction principale, les Algorithme et Implémentation Technique


-- > 8 janvier, Arthur:
    -Fichier README
    -corrections
    -ajouter docstring
        