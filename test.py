# class test:
#     def __init__(self,number):
#         self.number = number
    
#     def test_func(self):
#         self.number+=2
    

# func = "test_func"
# tst = test(0)
# eval("tst."+func+"()")
# print(tst.number)



bins="0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100"
num = int(bins, 2)
str1 = num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('ascii')
print("The normal string is :", str1)
type(str1)


