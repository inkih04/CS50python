name = input("File name: ")
name = name.lower()
name = name.split(".")
if "png" == [-1]:
    print("image/png")
elif "gif" == name[-1]:
    print("image/gif")
elif "jpg" == name[-1]:
    print("image/jpeg")
elif "jpeg" == name[-1]:
    print("image/jpeg")
elif "zip" == name[-1]:
    print("application/zip")
elif "pdf" == name[-1]:
    print("application/pdf")
elif "txt" == name[-1]:
    print("application/txt")
else:
    print("application/octet-stream")