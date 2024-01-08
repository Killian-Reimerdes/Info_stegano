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

### 

## Les ALgorithmes

##  Implémentation Technique

## Fonctions d'Arthur

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
    - Notebook cesar 1 decodage bien compris (j'estime que le notebook cryptage est une étape nécessaire pour comprendre la stegano)

--> 24 Décembre, Arthur:
	- fonction qui prend une lettre (str) et return (str) son ascii en binaire

--> 26 Décembre, Arthur: 
	- fonction qui prend comme argument une string et return pour chaque lettre, l'ascii (str) en binaire. Toutes ces valeurs ascii en binaire 
	forment une liste qui se fait return à la fin de la fonction.

--> 27-28 Décembre Arthur: 
    - Nouvelle fonction change_pixel:
    Cette fonction prend un string binaire exemple ("0b1010010"). Enlève le "0b" du début, puis ajoute chaque chiffre (0 ou 1) à une varaible qui représente la quantité de R, G ou B sur un pixel.
    Pour l'instant je donne des chiffre arbitraire à chaque quantité de couleur. Mais plustard P1_amount_red deviendra -> la fonction qui demande les valeurs d'un pixel.

--> 3 janvier , Killian:
    - finit les fonction d'écriture et de lecture
    - premiere fonction d'encodage et de decodage
    - écriture et lecture sur toute les couleurs
    - test sur plus grand echantillons et decouverte d'un porbleme concernant les pixels de valeur 0 

--> 5 janvier, Killian:
    - correction dans le code au niveau de quelques cas limite

--> 6 janvier, Arthur:
    - appel avec Killian, discution du fonctionnement des fonctions de chacun
    - recherche fonctionnement objets/classes 
    
--> 6 janvier, Killian:
    -correction du bug avec les pixels de valeurs 0 
    -correction au niveau des couches d'encodage (on peu mtn encoder sur des couches pair ou impair)
    -systeme de choix et de lecture des couches d'encodage et des codes dencodage

-- > 7 janvier, Arthur: 
    - nouveau fichier avec fonction globale qui met toutes les fonctions jusqu'à maintenant créé ensemble
    - import fonctions de l'autre fichier

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

-- > 8 janvier, Arthur:
    -Fichier README