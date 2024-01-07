from Pixels import Pixels
from random import randint
# class test:
#     def __init__(self,number):
#         self.number = number
    
#     def test_func(self):
#         self.number+=2
    

# func = "test_func"
# tst = test(0)
# eval("tst."+func+"()")
# print(tst.number)

blank = Pixels("real_newRed_square.png")
for i in range(blank.height):
    for j in range(blank.lenght):
        for x in range(3):
            blank.values[j,i]=(0,0,0)
blank.save_image("blank.png")

bins="0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100"
num = int(bins, 2)
str1 = num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('ascii')
print("The normal string is :", str1)
type(str1)


tst = "0200000000"
tst = tst[:-8]
print(tst)

print(str(int(255%2)))
print([randint(0,1)for i in range(3)])

print(blank.height,blank.lenght)

