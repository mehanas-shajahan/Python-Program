#matchcase_file
file=input("Enter File Extension: ")
match file:
    case 'py':print("Python File")
    case 'c':print("C File")
    case 'c++':print("C++ File")
    case 'html':print("HTML File")
    case 'jpg':print("Image File")
    case _:print("Unknown File Type")
