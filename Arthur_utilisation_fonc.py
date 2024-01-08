from PIL import Image

from Arthur_fonctions_Coder_msg import trans_msg_ascII_bin
from Arthur_fonctions_Coder_msg import trans_loop_str
from Arthur_fonctions_Coder_msg import change_pixel
from Arthur_fonctions_Coder_msg import reset_Imart
from Arthur_fonctions_Coder_msg import place_le_pixel

def test_Main_fonc():
    Main_fonc("Bon")

    #assert  == 


def Main_fonc(Message_a_cacher):
    """
    Cette fonction principale permet d'assembler toutes les fonctions du fichier Arthur_fonctions_Coder_msg.py.
    Elle prend comme argument le message (string) qu'on veut cacher et l'encode sur l'image imart.png. 
    """
    Msglong = Message_a_cacher
    list_long_bin = trans_loop_str(Msglong)
    image = Image.open("imart.png")

    for i in range(len(list_long_bin)):
        pixel1 = image.getpixel((i,0))
        pixel2 = image.getpixel((i,1))
        pixel3 = image.getpixel((i,2))
        Pi1_amount_red = pixel1[0]
        Pi1_amount_green = pixel1[1]
        Pi1_amount_blue = pixel1[2]
        Pi2_amount_red = pixel2[0]
        Pi2_amount_green = pixel2[1]
        Pi2_amount_blue = pixel2[2]
        Pi3_amount_red = pixel3[0]
        Pi3_amount_green = pixel3[1]
        Pi3_amount_blue = pixel3[2]
        bin_Msg = list_long_bin[i]
        Tuple_results = change_pixel(bin_Msg, Pi1_amount_red, Pi1_amount_green, Pi1_amount_blue, Pi2_amount_red, Pi2_amount_green, Pi2_amount_blue, Pi3_amount_red, Pi3_amount_green, Pi3_amount_blue)   #returns Tuple_results = (New_color_Pi1, New_color_Pi2, New_color_Pi3)
        place_le_pixel("imart.png",Tuple_results,i)

Main_fonc("Bonjour Killian")

#image = Image.open("imart.png")
#image.show()


#reset_Imart()

#Discution :
#Ces fonctions et méthodes de stéganogrphie n'ont pas été menées jusqu'au boue car l'autre méthode commencé par Killian avait déjà un stade plus avancé. 
#Ces fonctions peuvent être améliorer de plusieur manières:
#
# 1. Pour l'instant la fonction encode seulement sur les trois premières lignes de l'image
# Il faudrait regarder la largeur de l'image et ajouter en système de retour à la ligne quand le nombre de caractères dans la string est plus grand que le nombre de colonne. 
#
# 2. Il faudrait pouvoir utiliser la fonction de Killian qui rend chaque couleur de chaque pixel pair pour qu'on puisse coder sur n'importe quelle image. 
#
# 3. Ajouter la fonction pour décoder le message. 
