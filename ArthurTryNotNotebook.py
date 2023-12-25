#print("this is a file.py without cells")
#print("salut Killian")
#from PIL import Image

#imart = Image.new("RGB", (100,100),(100, 200, 15)) #tout doit être des tuples
#imart.show()

#size = imart.size
#color = imart.mode

#print(imart.mode)
#print(imart.format) ##format je devrais mettre png

#imart.save("ImartYes.png")

##changement 

def test_trans_msg_ascII_bin():
    assert trans_msg_ascII_bin("a") == "0b1100001"
    assert trans_msg_ascII_bin("R") == "0b1010010"
    assert trans_msg_ascII_bin("aR") == "0b"
    print("Everything works!")

def trans_msg_ascII_bin(Msg):
    """
    Cette fonction prend comme argument une lettre et return son numéro acsII en binaire
    """
    num_Msg = ord(Msg)
    bin_Msg = bin(num_Msg)
    
    return bin_Msg

test_trans_msg_ascII_bin()

#je vais faire la suite pour une chaîne de caractère

#num = ord("a")
#bin_a = bin(num)
#print(bin_a)
#print(type(bin_a))