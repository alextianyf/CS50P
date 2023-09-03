media_type = {
    ".gif": "image/gif",
    ".jpg": "image/jpg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

fileName = input("File name: ")

# check if the name ends is completed
# if enter "cat.", rfind returns -1
# if enter "cat.jpg", rfind returns 3
# if enter "Alex.gif", rfind returns 4
# rfind returns the number of characters before "."
fileExtension = fileName.rfind('.')

if fileExtension != -1:
    # the input is actually a string, and can be manipulate easily
    fileEnding = fileName[fileExtension:]
else:
    print("application/octet-stream")

get_MediaType = media_type.get(fileEnding, "application/octet-stream")
print(get_MediaType)