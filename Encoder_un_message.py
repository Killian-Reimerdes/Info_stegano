from Encoding import Encoding

name_image = input("Entrez le nom de l'image dans laquel vous voulez cacher un message : ")
new_name = input("Entrez le nom de la nouvelle image (optionel) : ")
message = input("Entrez le message : ")

if new_name != "":
    if message != '':
        enc = Encoding(name_image,new_name,message)
    else:
        enc = Encoding(name_image,new_image_name=new_name)
else:
    if message != '':
        enc = Encoding(name_image,message=message)
    else:
        enc = Encoding(name_image)
enc.encode()
