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
def extract_message(im : Pixels):

    return message_in_binairy

def translate_to_text(message_in_binairy)
    
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

    code_enodage=find_code_encododage()

    

    #appliquer les foncdtion de decodage
    functions =["test_func"] #ne pas oublieer de mettre a jour
    
    for func,i in enumerate(functions):
        if code_encodage[i]==1:
            eval(func+"_dec")

    #trouver la parite des couches encoder
    encode_layer = find_encoded_layer
    
    #sortir le message en binaire
    message_in_binairy = extract_message(im)
    
    #passer le message en string
    message = translate_to_text(message_in_binairy)
    
    #rend le message
    return message
            




if __name__ == '__main__':
    
    im= Encoding("Red_square.png","newRed_square.png","abc")# a changer
    im.encode()
    im.pixels.save_image(im.new_name)
    decodede_message = Decode(im.new_name)
    assert decodede_message == im.message
