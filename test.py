class test:
    def __init__(self,number):
        self.number = number
    
    def test_func(self):
        self.number+=2
    
func = "test_func"
tst = test(0)
eval("tst."+func+"()")
print(tst.number)
print(chr(0b1010100))
esgeg="1243251343"
assert esgeg[0] == "1"