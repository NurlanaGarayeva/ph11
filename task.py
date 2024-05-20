#   #task1
# def tutdugu_yer(topladigi_xal):
   
#     index_goster = list(enumerate(topladigi_xal))
    

#     index_goster.sort(reverse=True, key=lambda x: x[1])
    
#     yerler = [0] * len(topladigi_xal)
    
#     for index, (idx, xal) in enumerate(index_goster):
#         yerler[idx] = f"{index + 1}-ci"
    
#     return yerler


# topladigi_xal = [4, 7, 1, 3, 2, 5, 6]
# print(tutdugu_yer(topladigi_xal))
 
#task2
# import os 

# os.mkdir("Example")

# os.mkdir ("Example/subdirect")

# with open ("Example/subdirect/download.jpg", "w") as img_file:
#     img_file.write("tttt")
     
# with open ("Example/subdirect/metn.txt", "w") as txt_file: 
#     txt.file.write("Pandalar haqqinda melumat.")




import os
import shutil


os.mkdir("Example")


os.mkdir("Example/subdirect")


with open("Example/subdirect/download.jpg", "w") as img_file:
    img_file.write("tttt")


with open("Example/subdirect/metn.txt", "w") as txt_file:
    txt_file.write("Pandalar haqqinda melumat.")


for filename in os.listdir("Example/subdirect"):
    if filename.endswith(".txt"):
        shutil.move(f"Example/subdirect/{filename}", f"Example/{filename}")


print("Example qovluğundakı fayllar:", os.listdir("Example"))
print("Subdirect qovluğundakı fayllar:", os.listdir("Example/subdirect"))

     