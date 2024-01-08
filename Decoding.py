from Pixels import Pixels
from Encoding import Encoding
import string
import random

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
                
                if im.values[i-1,im.height-1][color]%2>0.5:
                    temp_list = list(im.values[i,j])
                    if temp_list[color] != 0:
                        temp_list[color] += -1
                    else:
                        temp_list[color] = 255
                    im.values[i,j] = tuple(temp_list)
            elif (i,j)==(0,1):
                return
            else:
                if im.values[i,j-1][color]%2>0.5:
                    temp_list = list(im.values[i,j])
                    if temp_list[color]!=0:
                        temp_list[color] += -1
                    else:
                        temp_list[color]=255
                    im.values[i,j] = tuple(temp_list)

def func_2_dec(im:Pixels,x:int):
    """
    Inverse de la fonction func_2_enc qui consiste a faire tourner la parite des pixels comme le fait
    func_2_enc mais dans le sense inverse

    Args: l'image et la couleur(ne s'execute seulement si x = 0)

    Returns : None    
    """
    if x == 0:
            for i in range(im.lenght):
                for j in range(im.height):
                    if (i,j)!=(0,0):
                        temp_list= list(im.values[i,j])
                        parity = []
                        for color in range(3):
                            if temp_list[color]%2 == 0:
                                parity.append(0)
                            else:
                                parity.append(1)
                        for color in range(3):
                            if parity[color]==1:
                                if temp_list[color]!=255:
                                    temp_list[color]+=1
                                else :
                                    temp_list[color]=0
                        for color in range(3):
                            if (i+j)%2==1:
                                if parity[color-2]==1:
                                    if temp_list[color]!=0:
                                        temp_list[color]+=-1
                                    else:
                                        temp_list[color]=255
                            else:
                                if parity[color-1]==1:
                                    if temp_list[color]!=0:
                                        temp_list[color]+=-1
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
    while message_in_binairy[-8:]=="00000000":
        message_in_binairy = message_in_binairy[:-8]

        
        
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
    functions =  ["test_func","func_1","func_2"] #ne pas oublieer de mettre a jour
    functions.reverse()
    #print(code_encodage)

    for i,func in enumerate(functions):  
        for color in range(3):      
            if code_encodage[len(functions)-i-1][color]==1:
                   
                   eval(func+"_dec({0})".format("im,"+str(color)))

    
    
    
    #sortir le message en binaire
    message_in_binairy = extract_message(im,encode_layer)
    
    #passer le message en string
    message = translate_to_text(message_in_binairy)
    
    #rend le message
    return message
            




if __name__ == '__main__':
    test = '01010100011001010111001101110100'
    assert (translate_to_text(test) == 'Test')
    #print("bin to text works")
    

    pix = Pixels("encoded_blank.png")
    message = extract_message(pix,[1,0,0])
    encoeded_message = [0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0]
    assert message == "01010100011001010111001101110100"
    #print('extract message works')

    pix2 = Pixels("new_blank.png")
    func_1_dec(pix2,0)
    message2 = extract_message(pix2,[1,0,0])
    assert message == message2
    #print("func_1_dec works")

    test_1 = Encoding("blank.png","new_blank.png","Test")
    test_1.code_encodage[2]=[1,0,0]
    vvalues = []
    for i in range(test_1.pixels.lenght):
        line = []
        for j in range(test_1.pixels.height):
            line.append(test_1.pixels.values[i,j])
        vvalues.append(line)
    test_1.func_2_enc(0)
    func_2_dec(test_1.pixels,0)
    for i in range(test_1.pixels.lenght):
        for j in range(test_1.pixels.height):
            if (i,j)!=(0,0):
                assert test_1.pixels.values[i,j][0]%2==vvalues[i][j][0]%2
                assert test_1.pixels.values[i,j][1]%2==vvalues[i][j][1]%2
                assert test_1.pixels.values[i,j][2]%2==vvalues[i][j][2]%2
    #print("func_2_dec marche")



    #test du systeme complet
    bible = open("bible.txt",'r')
    bible_first_pages = bible.read()
    random = ''.join(random.choices(string.ascii_letters + string.digits, k=100000))
    #https://www.javatpoint.com/python-program-to-generate-a-random-string

    im= Encoding("real_Red_square.png","real_newRed_square.png",message=bible_first_pages)
    #im= Encoding("blank.png","newblank.png",bible_first_pages) # fonction pas tjrs avec la bible

    im.encode()
    im.pixels.save_image(im.new_name)
    
    assert find_signature(Pixels(im.new_name))[0]==im.encode_layer
    assert find_signature(Pixels(im.new_name))[1][:len(im.functions)]==im.code_encodage
    #print("signature found")

        
        
        

    #print(im.code_encodage)
    Decodede_message = Decode(im.new_name)
    #print(im.encode_layer)
    
        
   
    assert Decodede_message == im.message
    print("putain ca marche ")
    
    
    # if Decodede_message == im.message:
    #     print("putain ca marche ")
    #else:
        
    #print(im.code_encodage)
        # for i in range(len(Decodede_message)):
        #     if Decodede_message[i]!=im.message[i]:
        #         print(i)
        #         print(Decodede_message[i],im.message[i])

        #print(Decodede_message)
    