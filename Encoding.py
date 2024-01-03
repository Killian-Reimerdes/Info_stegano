from Pixels import Pixels


class Encoding:
    def __init__(self,image_name,new_image_name,message):
        
        #message à cacher dans l'image
        self.message = message
        self.message_bin = []
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
        #self.code_encodage = ([[randint(0,2)] for j in range(3)] for i in range(len(self.functions)))
        self.code_encodage = [[1,0,1]]

    def test_func_enc(self,color:int):
        
        for i in range(self.pixels.lenght):
            for j in range(self.pixels.height):
                temp_list =list(self.pixels.values[i,j])
                if temp_list[color]==255:
                    temp_list[color]=0
                else:
                    temp_list[color]+=1
                self.pixels.values[i,j]=tuple(temp_list)
    
    def message_to_bin(self):
        mess_bin = []
        
        for letter in self.message:
            mess_bin.append(bin(ord(letter)))
        self.message_bin = mess_bin
        return mess_bin
    
    def write_message(self,color):
        if self.message_bin != []:
            if len(self.message)>(self.pixels.height * self.pixels.lenght):
                print("message too long")
            else:
                code = []
                for byt in self.message_bin:
                    bits = byt[2:]
                    while len(bits)<8:
                        bits = "0"+ bits
                    for bit in bits:
                        code.append(bit)
                x,y = 0,0    
                for i in code:
                    
                    if i == "1":
                        if self.pixels.values[x,y][color]==255:
                            temp_list = list(self.pixels.values[x,y])
                            temp_list[color] = 0
                            self.pixels.values[x,y]=tuple(temp_list)
                            
                        else:
                            temp_list = list(self.pixels.values[x,y])
                            temp_list[color] +=1
                            self.pixels.values[x,y]=tuple(temp_list)
                            
                    if x == self.pixels.lenght-1:
                        x=0
                        y += 1
                    else:
                        x += 1 
        else:
            print("pas de message en binaire")
                    



    
        

    def encode(self):
        """
        ecrit et encode le message dans l'image 
        """
        self.message_to_bin()
        self.write_message(0)
        
        for color in range(3):
            for i,func in enumerate(self.functions):
                if self.code_encodage[i][color]==1:
                    eval("self."+func+"_enc("+str(color)+")")
        
        




if __name__ == '__main__':
    #unchanged = Encoding("blank.png","new_blank","no message")
    enc = Encoding("blank.png","new_blank.png","Test")
    assert enc.message_to_bin()==['0b1010100','0b1100101','0b1110011','0b1110100']
    print("message_to_bin marche")
    enc.write_message(0)
    encoeded_message = [0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0]
    for i in range(16):
        #print(enc.pixels.values[i,0][0])
        assert enc.pixels.values[i,0][0]==encoeded_message[i]
    enc.pixels.save_image("encoded_blank.png")
    print("l'ecriture marche ")
    
    enc2 = Encoding("blank.png","new_blank.png","Test")
    enc2.encode()

    print("ca marche pour l'instant")