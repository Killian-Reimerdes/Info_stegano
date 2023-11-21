from PIL import Image

class Pixels:
    def __init__(self,image_name):
        self.image_name = image_name
        self.image = Image.open(self.image_name)
        self.values = self.image.load()
        self.lenght,self.height = self.image.size   


    def save_image(self):
        self.image.save("new"+self.image_name )

    def change_value(self,x,y,new_value):
         self.values[x,y] = new_value



if __name__ == '__main__':
    pix = Pixels("Red_square.png")
    pix.save_image()
    
        