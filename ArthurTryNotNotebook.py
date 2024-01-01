#print("this is a file.py without cells")
#print("salut Killian")
#from PIL import Image

#imart = Image.new("RGB", (100,100),(100, 200, 15)) #tout doit être des tuples
#imart.show()

#size = imart.size
#color = imart.mode

#print(imart.mode)
#print(imart.format) ##format je devrais mettre png

#imart.save("ImartYes.png")

##changement 

def test_trans_msg_ascII_bin():
    assert trans_msg_ascII_bin("a") == "0b1100001"
    assert trans_msg_ascII_bin("R") == "0b1010010"
    print("Everything works!")

def trans_msg_ascII_bin(Msg):
    """
    Cette fonction prend comme argument une lettre et return son numéro acsII en binaire
    """
    num_Msg = ord(Msg)
    bin_Msg = bin(num_Msg)
    
    return bin_Msg

#test_trans_msg_ascII_bin()

## je dois ajouter quelque part un if qui vérifie si le caractere appartient à ascii

def test_trans_loop_str():
    assert trans_loop_str("aR") == ["0b1100001","0b1010010"]
    print("yeah!")

def trans_loop_str(Msglong):
    """
    Cette fonction utilise la fonction déjà créée (trans_msg_ascII_bin) mais applique une boucle sur toutes les lettres de la châine de caractère
    trans_loop_str créer une liste avec toutes les valeurs ascii en binaires qui représente une lettre d'une string
    """
    list_long_bin = []
    for lettre in Msglong:
        x = trans_msg_ascII_bin(lettre)
        list_long_bin.append(x)
    print(list_long_bin)
    return list_long_bin

#test_trans_loop_str()  ## ça fonctionne

#trans_loop_str("Bonjour Killian")



original_string = "Hello, World!"
modified_string = original_string[0] + original_string[0 + 1:]
#print(modified_string[0])



P1_amount_red = 100
P1_amount_green = 50
P1_amount_blue = 120
P2_amount_red = 130
P2_amount_green = 40
P2_amount_blue = 200
P3_amount_red =180
#P3_amount_green = on s'en fou, il n'y aura pas d'info codé dessus
#P3_amount_blue = on s'en fou, il n'y aura pas d'info codé dessus

def test_change_pixel():
    #assert change_pixel("0b1001100") == "1001100"
    #assert change_pixel("0b1001100") == 7
    #assert change_pixel("0b1001100", P1_amount_red, P1_amount_green, P1_amount_blue) == (101, 50, 120) #ça marche
    assert change_pixel("0b1001100",P1_amount_red, P1_amount_green, P1_amount_blue, P2_amount_red, P2_amount_green, P2_amount_blue, P3_amount_red) == (101, 50, 120, 131, 41, 200, 180)
    print("bababooy")

def change_pixel(bin_Msg, Pi1_amount_red, Pi1_amount_green, Pi1_amount_blue, Pi2_amount_red, Pi2_amount_green, Pi2_amount_blue, Pi3_amount_red):
    """
    Cette fonction prend comme argument bin_Msg. (la valeur d'un seul caracter en binaire) exemple ("0b1010011") (c'est un string)
    Elle commence par enlever le "0b" du début
    Puis de droite à gauche additionne le chiffre (0 ou 1) à une variable pour l'instant appelé P1_amount_red, P1_amount_green, ou P1_amount_blue
    la fonction renvoie les nouvelles quantitées de chaque couleurs (int)
    """
    bin_Msg_sans_0b = bin_Msg[2:]

    x = 0 
    while x < len(bin_Msg_sans_0b):

        if x == 0:
            Pi1_amount_red = Pi1_amount_red + int(bin_Msg_sans_0b[x], 2)
        elif x == 1:
            Pi1_amount_green = Pi1_amount_green + int(bin_Msg_sans_0b[x], 2)
        elif x == 2:
            Pi1_amount_blue = Pi1_amount_blue + int(bin_Msg_sans_0b[x], 2)
        elif x == 3:
            Pi2_amount_red = Pi2_amount_red + int(bin_Msg_sans_0b[x],2 ) 
        elif x == 4:
            Pi2_amount_green = Pi2_amount_green + int(bin_Msg_sans_0b[x],2 ) 
        elif x == 5:
            Pi2_amount_blue = Pi2_amount_blue + int(bin_Msg_sans_0b[x],2 ) 
        elif x == 6: 
            Pi3_amount_red = Pi3_amount_red + int(bin_Msg_sans_0b[x],2 )
        
        else:
            print("il y a un problème quelque part")
        x = x + 1

    return Pi1_amount_red, Pi1_amount_green, Pi1_amount_blue, Pi2_amount_red, Pi2_amount_green, Pi2_amount_blue, Pi3_amount_red



test_change_pixel()



