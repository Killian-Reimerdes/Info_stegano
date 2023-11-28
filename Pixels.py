from PIL import Image

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


    def save_image(self):
        """
        Cette fonction sauvegarde l'image

        Args:
        self : l'image

        Returns:
        none
        """
        self.image.save("new"+self.image_name )

    def change_value(self,x,y,new_value):
        """
        Surement inutile
                 
        """                  
        self.values[x,y] = new_value
    
    def set_to_even(self):
        """
        Cette fonction arondie toutes les valeurs des pixels au chiffre paire le plus proche vers le bas
        """
        for i in range(self.lenght):
            for j in range(self.height):
                for color in range(3):
                    if self.values[i,j][color]%2 != 0:
                        print("a")
                        list_temp = list(self.values[i,j])
                        list_temp[color] += -1
                        self.values[i,j] = tuple(list_temp)
        




if __name__ == '__main__':
    pix = Pixels("Red_square.png")
    before=list([[[pix.values[i,j][color] for color in range(3)] for i in range(pix.lenght)]]for j in range(pix.height))
    pix.set_to_even()
    after=list([[[pix.values[i,j][color] for color in range(3)] for i in range(pix.lenght)]]for j in range(pix.height))
    #temp=([[pix.values[i,j][color] for color in range(3)] for i in range(pix.lenght)] for j in range(pix.height))
    print(before)
    print(after)

    pix.save_image()

    
        