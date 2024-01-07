from Pixels import Pixels
from random import randint
import copy


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
        self.encode_layer = [randint(0,1)for i in range(3)]
        
        #met tout nos pixel a la valuer pair ou impair voulu
        for i in range(3):
            if self.encode_layer[i]==1:
                self.pixels.set_to_uneven(i)
            else:
                self.pixels.set_to_even(i)


        #liste de toute les cellules d'encodage possible
        self.functions =["test_func","func_1","func_2"]  
        #decide quel module d'encryptage vont etre utiliser (1 veut dire que le module est utilise)
        self.code_encodage = [[randint(0,1) for j in range(3)] for i in range(len(self.functions))]
        
        
        
         #ecrit les parametere d'enodage
        signature = []
        for i in range(3):
            signature.append(str(self.encode_layer[i]))
        for i in range(len(self.functions)):
            for j in range(3):
                signature.append(str(self.code_encodage[i][j]))
        if len(signature)>24:
            return SystemError #attention si on depasse 7 fonction on doit agrandir la signature
        while len(signature)<24:
            signature.append("0")
        
        x = 0
        self.signature=[]
        for i in range(3):
            byt = ''
            for i in range(8):
            
                byt += signature[x]
                x += 1
            byt = int(byt,2)
            self.signature.append(byt)
        
        

        
    def test_func_enc(self,color:int):
        """
        Fonction d'encodage qui consiste a additione 1 a la valeur de chaque pixel sur une couleur

        Args : l'image (self) et la couleur (int entre 0 et 2)

        Returns : None 
        """
        
        for i in range(self.pixels.lenght):
            for j in range(self.pixels.height):
                
                temp_list =list(self.pixels.values[i,j])
                if temp_list[color]==255:
                    temp_list[color]=0
                else:
                    temp_list[color]+=1
                self.pixels.values[i,j]=tuple(temp_list)
    
    def func_1_enc(self,color:int):
        """
        Fonction d'encodage qui consiste a additioner un 1 a la valeur d'uen couleur de chauqe pixel 
        qui est preceder d'un pixel ayant une valeur impaire pour cette couleur

        Args : l'image (self) et la couleur (int entre 0 et 2)

        returns : None

        """
        last_value=0
        for i in range(self.pixels.lenght):
            for j in range(self.pixels.height):
                if (i,j)!=(0,0):
                    if last_value < 0.01:
                        if self.pixels.values[i,j][color]%2 >0.1:
                            last_value = 1
                    else:
                        temp_list = list( self.pixels.values[i,j])
                        if temp_list[color]!=255:
                            temp_list[color]+=1
                        else:
                            temp_list[color]=0
                        self.pixels.values[i,j]=tuple(temp_list) 
                        if self.pixels.values[i,j][color]%2 < 0.1 :
                            last_value = 0
                        

    def func_2_enc(self,color:int):
        """
        Fonction d'encodage qui consite a passer la parite de chaque couleur a la prochaine (pour chaque pixel)

        Args : l'image (self) et couleur (la fonction ne sexecute seulement si color = 0)

        returns : None
        """
        if color == 0:
            for i in range(self.pixels.lenght):
                for j in range(self.pixels.height):
                    
                    temp_list= list(self.pixels.values[i,j])
                    parity = []
                    for color in range(3):
                        if temp_list[color]%2 == 0:
                            parity.append(0)
                        else:
                            parity.append(1)
                    for x in range(3):
                        if parity[x]==1:
                            if temp_list[x]!=255:
                                temp_list[x]+=1
                            else :
                                temp_list[x]=0
                    for x in range(3):
                        if parity[x-1]==1:
                            if temp_list[x]!=0:
                                temp_list[x]+=-1
                            else:
                                temp_list[x]=255
                    self.pixels.values[i,j] = tuple(temp_list)
                    



    def message_to_bin(self):
        """
        Converti le message du text a un string binaire

        Args : le message (self)

        returns : le message en binaire
        """
        mess_bin = []
        
        for letter in self.message:
            mess_bin.append(bin(ord(letter)))
        self.message_bin = mess_bin
        return mess_bin
    
    def write_message(self):
        """
        Ecerit le message dans l'image

        Args : l'image (self) et le message en binaire (self)

        Returns : None
        """
       

        
        if self.message_bin != []:
            if len(self.message)>=(self.pixels.height * self.pixels.lenght * 3):
                print("message too long")
            else:
                color = 0
                code= []
                for byt in self.message_bin:
                    bits = byt[2:]
                    while len(bits)<8:
                        bits = "0"+ bits
                    for bit in bits:
                        code.append(bit)
                x,y = 1,0    
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
                        if y >= self.pixels.height-1:
                            color +=1 
                            y = 0
                    else:
                        x += 1 
        else:
            print("pas de message en binaire")
                    



    
        

    def encode(self):
        """
        converti en binaire, ecrit, encode le message dans l'image  et sauvegarde

        Args : l'image, le message, les parametre d'encodage (cles)

        Return : None

        """
        self.message_to_bin()
        self.write_message()
        
        for color in range(3):
            for i,func in enumerate(self.functions):
                if self.code_encodage[i][color]==1:
                    eval("self."+func+"_enc("+str(color)+")")
        
        self.pixels.values[0,0] = tuple(self.signature)

        self.pixels.save_image(self.new_name)
        
        




if __name__ == '__main__':
    #test ne fonctionne plus a cause des fonctionalite ajouter apres coup
    
    # #test ecriture
    # enc = Encoding("blank.png","new_blank.png","Test")
    # assert enc.message_to_bin()==['0b1010100','0b1100101','0b1110011','0b1110100']
    # print("message_to_bin marche")
    # enc.write_message()
    # encoeded_message = [255,0,255,0,255,0,255,255,255,0,0,255,255,0,255,0,255,0,0,0,255,255,0,0,255,0,0,0,255,0,255,255]
    # for i in range(32):
    #     assert enc.pixels.values[i+1,0][0]==encoeded_message[i]
    
    # print("l'ecriture marche ")
    
    

    # enc.func_1_enc(0)
    # for i in range(32):
    #     #print(enc.pixels.values[i,0])
    #     assert enc.pixels.values[i+1,0][0]== [255,0,0,1,255,0,0,0,0,1,0,0,0,1,255,0,0,1,0,1,255,255,0,1,255,0,1,0,0,1,255,255][i]
                                           
       
    # print("func 1 fonctionne")

    test_1 = Encoding("blank.png","new_blank.png","Test")
    vvalues = []
    for i in range(test_1.pixels.lenght):
        line = []
        for j in range(test_1.pixels.height):
            line.append(test_1.pixels.values[i,j])
        vvalues.append(line)
    test_1.func_2_enc(0)
    for i in range(test_1.pixels.lenght):
        for j in range(test_1.pixels.height):
            assert test_1.pixels.values[i,j][0]%2==vvalues[i][j][2]%2
            assert test_1.pixels.values[i,j][1]%2==vvalues[i][j][0]%2
            assert test_1.pixels.values[i,j][2]%2==vvalues[i][j][1]%2
    

    print("func_2_enc marche")

   
    
    print("ca marche pour l'instant")