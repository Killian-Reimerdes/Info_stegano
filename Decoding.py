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
def extract_message(im : Pixels,encode_layer:list):
    for color in range(3):
        if encode_layer[color]==1:
            for x in range(im.lenght):
                for y in range(im.height):
                    im.values[x,y]+=-1
    message_in_binairy = "0b"
    
    for color in range(3):
        for i in range(im.lenght):
            for j in range(im.height):
                if im.values[i,j][color]%2==0:
                    message_in_binairy+="0"
                else:
                    
                    message_in_binairy+="1"

    return message_in_binairy

def translate_to_text(message_in_binairy):
    #https://www.askpython.com/python/built-in-methods/convert-binary-string-to-normal-string
    num = int(message_in_binairy, 2)
    str1 = num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('ascii')
    
    return str1


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
    message_in_binairy = extract_message(im,encode_layer)
    
    #passer le message en string
    message = translate_to_text(message_in_binairy)
    print(len(message))
    #rend le message
    return message
            




if __name__ == '__main__':
    
    im= Encoding("Red_square.png","newRed_square.png","abc")# a changer
    im.encode()
    im.pixels.save_image(im.new_name)
    decodede_message = Decode(im.new_name)
    print(decodede_message)
    assert decodede_message == im.message
