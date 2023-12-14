from Pixels import Pixels


class Encoding:
    def __init__(self,image_name,new_image_name,message):
        
        #message à cacher dans l'image
        self.message = message
        
        #nom de la nouvelle image
        self.new_name = new_image_name
        #cree un objet de la class pixles de l'image 
        self.pixels = Pixels(image_name)
        #decide si on encode sur une base pair ou impair (une valuer par couleur)
        #self.encode_layer = ([randint(0,2)]for i in range(3))
        self.encode_layer = [0,0,0]
        #met tout nos pixel a la valuer pair ou impair voulu
        for i in range(3):
            if self.encode_layer[i]==1:
                self.pixels.set_to_uneven(i)
            else:
                self.pixels.set_to_even(i)


        #liste de toute les cellules d'encodage possible
        self.functions =["test_func"]
        #decide quel module d'encryptage vont etre utiliser (1 veut dire que le module est utilise)
        #self.code_encodage = ([randint(0,2)] for i in range(len(self.functions)))
        self.code_encodage = [1]

    def test_func_enc(self,color:int):
        
        for i in range(self.pixels.lenght):
            for j in range(self.pixels.height):
                temp_list =list(self.pixels.values[i,j])
                temp_list[color]+=1
                self.pixels.values[i,j]=tuple(temp_list)


    
        

    def encode(self):
        """
        encode le message dans l'image 
        """
        for color in range(3):
        
            for i,func in enumerate(self.functions):
                if self.code_encodage[i]==1:
                    eval("self."+func+"_enc("+str(color)+")")




if __name__ == '__main__':
    enc = Encoding("Red_square.png","newRed_square.png")
    print(list(enc.code_encodage))