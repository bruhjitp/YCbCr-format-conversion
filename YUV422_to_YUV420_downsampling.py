#chroma downsampling as explained in readme file

rows=480
columns=640
List=[]
list_new=[]

with open("YUV422_chroma.ppm","r") as file:
  data=file.read()
  List=data.split("\n")

for i in range(0, rows, 2):
  for j in range(0, columns):
    index=(i*columns)+j
    num1=int(List[index],10)+int(List[index+columns], 10)
    num1=num1/2
    List_new.append(num1)

with open("YUV420_chroma.ppm","w") as file:
  for items in List_new:
    file.write('%s\n' %items)
