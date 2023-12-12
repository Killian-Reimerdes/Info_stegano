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

    def test_func_enc(self,color:int):
        
        for i in range(self.pixels.lenght):
            for j in range(self.pixels.height):
                self.pixels.values[i,j][color]+=1

    
        

    def encode(self):
        """
        encode le message dans l'image
        """
        for func,i in enumerate(self.functions):
            if self.code_encodage[i]==1:
                eval(func())




if __name__ == '__main__':
    enc = Encoding("Red_square.png","newRed_square.png")
    print(list(enc.code_encodage))