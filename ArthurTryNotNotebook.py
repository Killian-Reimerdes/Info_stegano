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
    #assert trans_msg_ascII_bin("aR") == "0b"
    print("Everything works!")

def trans_msg_ascII_bin(Msg):
    """
    Cette fonction prend comme argument une lettre et return son numéro acsII en binaire
    """
    num_Msg = ord(Msg)
    bin_Msg = bin(num_Msg)
    
    return bin_Msg

#test_trans_msg_ascII_bin()

#je vais faire la suite pour une chaîne de caractère

#num = ord("a")
#bin_a = bin(num)
#print(bin_a)
#print(type(bin_a))
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
        #vérfier que le caractère appartient à ascii mais après
        x = trans_msg_ascII_bin(lettre)
        list_long_bin.append(x)
    print(list_long_bin)
    return list_long_bin

test_trans_loop_str()  ## ça fonctionne

#trans_loop_str("Bonjour Killian")

