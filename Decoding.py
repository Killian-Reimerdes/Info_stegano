from Pixels import Pixels
from Encoding import Encoding

def find_signature(im:Pixels):
    """
    Trouve la signature d'une image donc les paramtere selon lesquels le message a ete encoder

    Args : l'image (Classe Pixels)

    Returns : encode_layer ([0,1,1] qui indique si le message a ete enceoder sur des couches
      paires ou impaires) et code_encodage ([[1,0,1],[0,1,1]...] qui indique quel fonction a ete
      applique sur chaque couche)
    """

    byts = im.values[0,0]
    siganture = []
    for color in range(3):
        str = bin(byts[color])
        str= str[2:]
        while len(str) <8:
            str = "0"+str
        for i in str:
            siganture.append(i)
    encode_layer = [int(siganture[i]) for i in range(3)]
    code_encodage = [[int(siganture[3+i+(3*j)])for i in range(3)]for j in range(7)] 
    return encode_layer,code_encodage

"""

Fonctions de décodage


"""


def test_func_dec(im : Pixels ,color:int):
    """
    Inverse de la fonction test_func_enc de la class Encoding 
    consiste a soustraire 1 a la valeur d'une certaines couleur pour chaque pixel

    Args: l'image (class Pixels) et la couleur (int entre 0 et 2)

    Return : None
    """
    for i in range(im.lenght):
        for j in range(im.height):
            temp_list=list(im.values[i,j])
            if temp_list[color] == 0:
                temp_list[color] = 255
            else:
                temp_list[color] += -1
            im.values[i,j] = tuple(temp_list)

def func_1_dec(im : Pixels,color:int):
    """
    Inverse de la fonction func_1_enc de la class Encoding
    consiste a soustraire 1 a la valeur d'une couleur pour
    chaque pixel qui suit un pixel dont la valeur de la couleur est impaire

    Args: limage (class Pixels) et la couleur (int entre 0 et 2)

    Returns : None
    """
    for i in range(im.lenght-1,-1,-1):
        for j in range(im.height-1,-1,-1):
            if j == 0 :
                if i == 0 :
                    return
                if im.values[i-1,im.height-1][color]%2>0.5:
                    temp_list = list(im.values[i,j])
                    if temp_list[color] != 0:
                        temp_list[color] += -1
                    else:
                        temp_list[color] = 255
                    im.values[i,j] = tuple(temp_list)
            else:
                if im.values[i,j-1][color]%2>0.5:
                    temp_list = list(im.values[i,j])
                    if temp_list[color]!=0:
                        temp_list[color] += -1
                    else:
                        temp_list[color]=255
                    im.values[i,j] = tuple(temp_list)


"""

Sortir le message en binaire et le passer en string

"""
def extract_message(im : Pixels,encode_layer):
    """
    sort le message en binaire de l'image

    Args: l'image (class Pixels) et la cle pour les couches d'encodage ([0,1,0])

    Return : le message en str binaire
    """

    #corrige si on encode sur une couche impaire
    color = 0
    
    if encode_layer[color]==1:
        for x in range(im.lenght):
            for y in range(im.height):
                temp_list = list(im.values[x,y])
                if temp_list[color]!= 0:
                    temp_list[color] += -1
                else:
                    temp_list[color]=255
                im.values[x,y] = tuple(temp_list)
    
    message_in_binairy = ""
    zero_counter=0
    x,y = 1,0
    while  zero_counter<24:  #arret la lecture apres 24 zero d'affile
            
        message_in_binairy += str(int(im.values[x,y][color]%2))

        if message_in_binairy[-1]=="0":
            zero_counter += 1
                
        else:
            zero_counter = 0

        if x >= im.lenght-1:
            x = 0
            y += 1
            if y >= im.height-1:
                color += 1
                x,y = 1,0
                if color >= 3 :
                    return message_in_binairy
                if encode_layer[color]==1:
                    for a in range(im.lenght):
                        for b in range(im.height):
                            temp_list = list(im.values[a,b])
                            if temp_list[color]!=0:
                                temp_list[color] += -1
                            else:
                                temp_list[color]= 255
                            im.values[a,b] = tuple(temp_list)
                        
        else:
            x += 1

    #crop les zero inutile            
    message_in_binairy = message_in_binairy [:-16]
    while len(message_in_binairy)%8 > 0.1 :
        
        message_in_binairy = message_in_binairy[:-1]

        
        
    return message_in_binairy

def translate_to_text(message_in_binairy:str):
    """
    prend un message ecrit en binaire(str de 0 et de 1) et rend le text traduit

    Args: str (binaire)

    Return : message decode (str)
    """
    message_in_real_binairy = []
    while message_in_binairy!="":
        byt = ""
        for i in range (8):
            if message_in_binairy != "":
                byt += message_in_binairy[0]
                message_in_binairy = message_in_binairy[1:]
            else:
                break
        message_in_real_binairy.append(byt)
    
    message = ""
    for byt in message_in_real_binairy:
        
        message += chr(eval("0b"+byt))
    
    
    
    return message


"""

Fonction de Décodage

"""

def Decode(image_name):
    """
    prend une image et nous retourne le message encoder

    Args: nom de l'image

    Return: le message
    """
    #ouvrir l'image
    im = Pixels(image_name)

    #trouver le code d'encodage et la parite des couches encoder

    encode_layer, code_encodage = find_signature(im)

    

    #appliquer les foncdtion de decodage
    functions =  ["test_func","func_1"] #ne pas oublieer de mettre a jour
    functions.reverse()
    for color in range(3):
        for i,func in enumerate(functions):
            if code_encodage[i][color]==1:
                   eval(func+"_dec({0})".format("im,"+str(color)))

    
    
    
    #sortir le message en binaire
    message_in_binairy = extract_message(im,encode_layer)
    
    #passer le message en string
    message = translate_to_text(message_in_binairy)
    #print(len(message))
    #rend le message
    return message
            




if __name__ == '__main__':
    test = '01010100011001010111001101110100'
    assert (translate_to_text(test) == 'Test')
    print("bin to text works")


    pix = Pixels("encoded_blank.png")
    message = extract_message(pix,[1,0,0])
    encoeded_message = [0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0]
    assert message == "01010100011001010111001101110100"
    print('extract message works')

    pix2 = Pixels("new_blank.png")
    func_1_dec(pix2,0)
    message2 = extract_message(pix2,[1,0,0])
    assert message == message2
    print("func_1_dec works")



    #test du systeme complet
    bible = open("bible.txt",'r')
    bible_first_pages = bible.read()
    
    #im= Encoding("real_Red_square.png","real_newRed_square.png",bible_first_pages)
    im= Encoding("blank.png","newblank.png",bible_first_pages) # fonction pas tjrs avec la bible
    
    im.encode()
    im.pixels.save_image(im.new_name)
    
    assert find_signature(Pixels(im.new_name))[0]==im.encode_layer
    assert find_signature(Pixels(im.new_name))[1][:2]==im.code_encodage
    print("signature found")

    
    Decodede_message = Decode(im.new_name)
    
    print(Decodede_message)
    
    for i in range(len(Decodede_message)):#7459 pour bible 
       assert Decodede_message[i] == im.message[i]

    print("putain ca marche ")
