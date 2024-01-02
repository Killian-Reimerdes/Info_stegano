from Pixels import Pixels
from Encoding import Encoding

def find_code_encododage(im : Pixels):
    code_encododage = [1]
    return code_encododage

def find_encoded_layer(im:Pixels):
    encoded_layer = [0,0,0]
    return encoded_layer

"""

Fonctions de décodage


"""


def test_func_dec(im : Pixels ,color:int):
    for i in range(im.lenght):
        for j in range(im.height):
            im.values[i,j][color]+=-1


"""

Sortir le message en binaire et le passer en string

"""
def extract_message(im : Pixels,color,encode_layer):
    
    if encode_layer[color]==1:
        for x in range(im.lenght):
            for y in range(im.height):
                im.values[x,y]+=-1
    message_in_binairy = "0b"
    zero_counter=0
    for i in range(im.lenght):
        for j in range(im.height):
            
            if im.values[i,j][color]%2<0.001:
                
                message_in_binairy+="0"
                zero_counter+=1
                if zero_counter>15:
                    return message_in_binairy
            else:
                message_in_binairy+="1"
                zero_counter=0

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
    
    for i,func in enumerate(functions):
        if code_encodage[i]==1:
            eval(func+"_dec")

    #trouver la parite des couches encoder
    encode_layer = find_encoded_layer(im)
    
    #sortir le message en binaire
    message_in_binairy = extract_message(im,0,encode_layer)
    
    #passer le message en string
    message = translate_to_text(message_in_binairy)
    print(len(message))
    #rend le message
    return message
            




if __name__ == '__main__':
    test = '01010100011001010111001101110100'
    assert (translate_to_text(test) == 'Test')



    im= Encoding("real_Red_square.png","real_newRed_square.png","Test")# a changer
    im.encode()
    im.pixels.save_image(im.new_name)
    message_in_binairy = extract_message(im.pixels,0,[0,0,0])
    print(message_in_binairy[:10])
    decodede_message = Decode(im.new_name)
    

    encode_layer = find_encoded_layer(im)
    message_in_binairy = extract_message(im.pixels,0,encode_layer)
    print(message_in_binairy[:50])
    assert decodede_message == im.message
    
    print("putain ca marche ")
    # decodede_message = Decode(im.new_name)
    # print(decodede_message)
    # assert decodede_message == im.message
