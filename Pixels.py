from PIL import Image
from numpy.random import randint

class Pixels:
    def __init__(self,image_name):
        #string du nom de l'image
        self.image_name = image_name

        #l'image ouverte qu'on peut modifier
        self.image = Image.open(self.image_name)

        #liste a double index des valeurs de chaque pixel (R,G,B)
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
    def set_to_even(self,color:int):
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








if __name__ == '__main__':
    #test class pixel
    pix = Pixels("Red_square.png")
    before=list([[[pix.values[i,j][color] for color in range(3)] for i in range(pix.lenght)]]for j in range(pix.height))
    pix.set_to_even(0)
    pix.set_to_uneven(1)
    pix.set_to_uneven(2)
    after=[[[[pix.values[i,j][color] for color in range(3)] for i in range(pix.lenght)]]for j in range(pix.height)]
    for i in range(pix.height):
        for j in range(pix.lenght):
            assert pix.values[i,j][0]%2==0
            assert pix.values[i,j][1]%2==1
            assert pix.values[i,j][2]%2==1
    # print(before)
    print(after)

    #pix.save_image("newRed_square.png")
    
    
    
        