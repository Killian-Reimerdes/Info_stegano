from PIL import Image
from numpy.random import randint

class Pixels:
    def __init__(self,image_name):
        #string du nom de l'image
        self.image_name = image_name

        #l'image ouverte qu'on peut modifier
        self.image = Image.open(self.image_name)

        #liste a double index des valeurs de chaque pixel (x,y,z)
        self.values = self.image.load()

        #les diensions de l'image en pixels
        self.lenght,self.height = self.image.size   


    def save_image(self,new_image_name):
        """
        Cette fonction sauvegarde la nouvelle image

        Args:
        self : l'image

        Returns:
        none
        """
        self.image.save(new_image_name)

    def change_value(self,x,y,new_value):
        """
        Surement inutile
                 
        """                  
        self.values[x,y] = new_value
    
        """
        Cette fonction arondie toutes les valeurs des pixels au chiffre paire le plus proche vers le bas
        """
        for i in range(self.lenght):
            for j in range(self.height):
                if self.values[i,j][color]%2 != 0:
                    list_temp = list(self.values[i,j])
                    list_temp[color] += -1
                    self.values[i,j] = tuple(list_temp)

    def set_to_uneven(self,color:int):
        """
        Cette fonction arondie toutes les valeurs des pixels au chiffre impaire le plus proche vers le bas
        """
        for i in range(self.lenght):
            for j in range(self.height):
                if self.values[i,j][color]%2 != 1:
                    list_temp = list(self.values[i,j])
                    list_temp[color] += -1
                    self.values[i,j] = tuple(list_temp)

class Encoding:
    def __init__(self,image_name,new_image_name):
        
        #cree un objet de la class pixles de l'image 
        self.pixels = Pixels(image_name)
        #decide si on encode sur une base pair ou impair (une valuer par couleur)
        self.encode_layer = ([randint(0,2)]for i in range(3))
        #met tout nos pixel a la valuer pair ou impair voulu
        for i in range(3):
            if self.encode_layer[i]==1:
                self.pixels.set_to_uneven()
            else:
                self.pixels.set_to_even()


        #liste de toute les cellules d'encodage possible
        self.functions =["test_func","another_function"]
        #decide quel module d'encryptage vont etre utiliser (1 veut dire que le module est utilise)
        self.code_encodage = ([randint(0,2)] for i in range(len(self.functions)))

    def test_func(self,color:int):
        for color in rnage(3):
            for i in range(self.pixels.lenght):
                for j in range(self.pixels.height):
                    self.pixels.values[i,j][color]+=1
    def encode(self):
        """
        encode le message dans l'image
        """
        for func,i in enumerate(self.functions):
            if self.code_encodage[i]==0:
                eval(func)


def Decoding(image_name):
    """
    prend une image et nous retourne le message encoder

    Args: nom de l'image

    Return: le message
    """



if __name__ == '__main__':
    # #test class pixel
    # pix = Pixels("Red_square.png")
    # before=list([[[pix.values[i,j][color] for color in range(3)] for i in range(pix.lenght)]]for j in range(pix.height))
    # pix.set_to_even()
    # after=list([[[pix.values[i,j][color] for color in range(3)] for i in range(pix.lenght)]]for j in range(pix.height))
    
    # print(before)
    # print(after)

    # pix.save_image("newRed_square.png")
    # print("jh")
    enc = Encoding("Red_square.png","newRed_square.png")
    print(list(enc.code_encodage))
    
    
        