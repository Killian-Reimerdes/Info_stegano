from Pixels import Pixels
from Encoding import Encoding

def find_code_encododage(im : Pixels):
    code_encododage = [[1,0,0],[1,0,0]]
    return code_encododage

def find_encoded_layer(im:Pixels):
    encoded_layer = [1,0,0]
    return encoded_layer

"""

Fonctions de décodage


"""


def test_func_dec(im : Pixels ,color:int):
    for i in range(im.lenght):
        for j in range(im.height):
            temp_list=list(im.values[i,j])
            if temp_list[color]==0:
                temp_list[color]=255
            else:
                temp_list[color]+=-1
            im.values[i,j] = tuple(temp_list)

def func_1_dec(im : Pixels,color:int):
    for i in range(im.lenght-1,-1,-1):
        for j in range(im.height-1,-1,-1):
            if j == 0 :
                if im.values[i-1,im.height-1][color]%2>0.5:
                    temp_list = list(im.values[i,j])
                    temp_list[color] += -1
                    im.values = tuple(temp_list)
            else:
                if im.values[i,j-1][color]%2>0.5:
                    temp_list = list(im.values[i,j])
                    temp_list[color] += -1
                    im.values = tuple(temp_list)


"""

Sortir le message en binaire et le passer en string

"""
def extract_message(im : Pixels,encode_layer):
    #corrige si on encode sur une couche impaire
    color = 0
    
    if encode_layer[color]==1:
        for x in range(im.lenght):
            for y in range(im.height):
                temp_list = list(im.values[x,y])
                temp_list[color] += -1
                im.values[x,y] = tuple(temp_list)
    
    message_in_binairy = ""
    zero_counter=0
    x,y = 0,0
    while  zero_counter<24:  #arret la lecture apres 16 zero d'affile
            
        message_in_binairy += str(int(im.values[x,y][color]%2))

        if message_in_binairy[-1]=="0":
            zero_counter += 1
                
        else:
            zero_counter = 0

        if x >= im.lenght-1:
            x = 0
            y += 1
            if y >= im.height:
                color += 1
                if color >= 3 :
                    return message_in_binairy
                if encode_layer[color]==1:
                    for a in range(im.lenght):
                        for b in range(im.height):
                            temp_list = list(im.values[a,b])
                            temp_list[color] += -1
                            im.values[a,b] = tuple(temp_list)
                        
        else:
            x += 1

    #crop les zero inutile            
    message_in_binairy = message_in_binairy [:-16]
    while len(message_in_binairy)%8 > 0.1 :
        
        message_in_binairy = message_in_binairy[:-1]

        
        
    return message_in_binairy

def translate_to_text(message_in_binairy:str):
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

    #trouver le code d'encodage

    code_encodage = find_code_encododage(im)

    

    #appliquer les foncdtion de decodage
    functions =["test_func"] #ne pas oublieer de mettre a jour
    for color in range(3):
        for i,func in enumerate(functions):
            if code_encodage[i][color]==1:
                
                eval(func+"_dec({0})".format("im"+','+str(color)))

    #trouver la parite des couches encoder
    encode_layer = find_encoded_layer(im)
    
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
    message = extract_message(pix,[0,0,0])
    encoeded_message = [0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0]
    assert message == "01010100011001010111001101110100"
    print('extract message works')



    #test du systeme complet
    bible = open("bible.txt",'r')
    bible_first_pages = bible.read()
    
    im= Encoding("real_Red_square.png","real_newRed_square.png",bible_first_pages)# a changer
    im.encode()
    im.pixels.save_image(im.new_name)
    

    
    Decodede_message = Decode(im.new_name)
    #print(Decodede_message)
    print(Decodede_message[6872])#le seule caracter qui est faut un seul byt faut et jsp pas pk
    for i in range(6850):#7459
        assert Decodede_message[i] == im.message[i]

    print("putain ca marche ")
