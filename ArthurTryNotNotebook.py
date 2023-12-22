#print("this is a file.py without cells")
#print("salut Kylian")
from PIL import Image

imart = Image.new("RGB", (100,100),(100, 200, 15)) #tout doit être des tuples
imart.show()

size = imart.size
color = imart.mode

print(imart.mode)
print(imart.format) #format je devrais mettre png

imart.save("ImartYes.png")

#changement 


