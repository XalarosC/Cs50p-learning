#ask for file name

name = input("File name: ")

#take the .something and change it to /something (.gif .jpg .jpeg .png .pdf .txt .zip)


name1 = name.lower().strip()

if ".gif" in name1 :
    print("image/gif")

elif ".jpg" in name1 :
    print("image/jpeg")
elif ".jpeg" in name1 :
    print("image/jpeg")
elif ".png" in name1 :
    print("image/png")
elif ".pdf" in name1 :
    print("application/pdf")
elif ".txt" in name1 :
    print("text/plain")
elif ".zip" in name1 :
    print("application/zip")
else :
    print("application/octet-stream")
