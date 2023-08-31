#input=input("enter number")
file = open("Route001.docx","rt")
data = file.read()
list=data.replace('\n','').split(".")

print(list)