from PIL import Image


def test_trans_msg_ascII_bin():
    assert trans_msg_ascII_bin("a") == "0b1100001"
    assert trans_msg_ascII_bin("R") == "0b1010010"
    print("Everything works!")




def trans_msg_ascII_bin(Msg): #"hello"
    """
    Cette fonction prend comme argument une lettre et return son numéro acsII en binaire
    """
    num_Msg = ord(Msg)
    bin_Msg = bin(num_Msg)
    
    return bin_Msg



#test_trans_msg_ascII_bin()


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
    #print(list_long_bin)
    return list_long_bin

#test_trans_loop_str()  ## ça fonctionne 
#trans_loop_str("Bonjour Killian")



P1_amount_red = 100
P1_amount_green = 50
P1_amount_blue = 120
P2_amount_red = 130
P2_amount_green = 40
P2_amount_blue = 200
P3_amount_red =180
P3_amount_green = 40 #on s'en fou, il n'y aura pas d'info codé dessus
P3_amount_blue = 160  #on s'en fou, il n'y aura pas d'info codé dessus

def test_change_pixel():
    #assert change_pixel("0b1001100") == "1001100"
    #assert change_pixel("0b1001100") == 7
    #assert change_pixel("0b1001100", P1_amount_red, P1_amount_green, P1_amount_blue) == (101, 50, 120) #ça marche
    assert change_pixel("0b1001100",P1_amount_red, P1_amount_green, P1_amount_blue, P2_amount_red, P2_amount_green, P2_amount_blue, P3_amount_red, P3_amount_green, P3_amount_blue) == ((101, 50, 120) , (131, 41, 200) , (180, P3_amount_green, P3_amount_blue))
    print("bababooy")

def change_pixel(bin_Msg, Pi1_amount_red, Pi1_amount_green, Pi1_amount_blue, Pi2_amount_red, Pi2_amount_green, Pi2_amount_blue, Pi3_amount_red, Pi3_amount_green, Pi3_amount_blue):
    """
    Cette fonction prend comme argument bin_Msg. (la valeur d'un seul caracter en binaire) exemple ("0b1010011") (c'est un string)
    Elle commence par enlever le "0b" du début
    Puis de droite à gauche additionne le chiffre (0 ou 1) à une variable pour l'instant appelé P1_amount_red, P1_amount_green, ou P1_amount_blue
    la fonction renvoie les nouvelles quantitées de chaque couleurs (int)
    """
    bin_Msg_sans_0b = bin_Msg[2:]


    Pi1_amount_red_N = Pi1_amount_red + int(bin_Msg_sans_0b[0], 2)
    Pi1_amount_green_N = Pi1_amount_green + int(bin_Msg_sans_0b[1], 2)
    Pi1_amount_blue_N = Pi1_amount_blue + int(bin_Msg_sans_0b[2], 2)
    Pi2_amount_red_N = Pi2_amount_red + int(bin_Msg_sans_0b[3],2 ) 
    Pi2_amount_green_N = Pi2_amount_green + int(bin_Msg_sans_0b[4],2 ) 
    Pi2_amount_blue_N = Pi2_amount_blue + int(bin_Msg_sans_0b[5],2 ) 
    if len(bin_Msg_sans_0b) > 6:
        Pi3_amount_red_N = Pi3_amount_red + int(bin_Msg_sans_0b[6],2 )
    else:
        Pi3_amount_red_N = Pi3_amount_red
    Pi3_amount_green_N = Pi3_amount_green
    Pi3_amount_blue_N = Pi3_amount_blue

    New_color_Pi1 = (Pi1_amount_red_N, Pi1_amount_green_N, Pi1_amount_blue_N)
    New_color_Pi2 = (Pi2_amount_red_N, Pi2_amount_green_N, Pi2_amount_blue_N)
    New_color_Pi3 = (Pi3_amount_red_N, Pi3_amount_green_N, Pi3_amount_blue_N)

    Tuple_results = (New_color_Pi1, New_color_Pi2, New_color_Pi3)
    #print(Tuple_results, len(bin_Msg_sans_0b))
    return Tuple_results

#test_change_pixel()

#change_pixel("0b1001100",P1_amount_red, P1_amount_green, P1_amount_blue, P2_amount_red, P2_amount_green, P2_amount_blue, P3_amount_red, P3_amount_green, P3_amount_blue)

#def test_fonction_J():
#    assert fonction_J("salut") == ['0b1110011', '0b1100001', '0b1101100', '0b1110101', '0b1110100']
#    print("la fonction_J fonction")         #Cettre fonction sert un peu à rien




def reset_Imart():
    """
    comme son nom l'indique, cette fonction reset l'image à sa version vierge
    """
    imart = Image.new("RGB", (100,100),(250, 250, 250))
    imart.save("imart.png")
    #imart.show()
    imart.close()
reset_Imart()

def place_le_pixel(fichier_img, Tuple_results, nieme_pix):
    """
    Cette fonction prend comme argument le str du nom du fichier png, la tuple qui représente 3 pixels, ces 3 pixels représentent un charactère.
    En troisième la fonction prend la position du charactère du message initial.
    """
    imart2 = Image.open(fichier_img)
    imart2.putpixel((nieme_pix, 0), Tuple_results[0])
    imart2.putpixel((nieme_pix, 1), Tuple_results[1])
    imart2.putpixel((nieme_pix, 2), Tuple_results[2])
    #imart2.show()
    imart2.save("imart.png")
    imart2.close()   
    return imart2


#nouvel_variable_img = place_le_pixel("imart.png", ((101, 50, 120) , (131, 41, 200) , (180, 40, 160)), 0)
#nouvel_variable_img.show()
#pixel_value = nouvel_variable_img.getpixel((0,0))
#print(pixel_value)

#image = Image.open(fichier_img)











