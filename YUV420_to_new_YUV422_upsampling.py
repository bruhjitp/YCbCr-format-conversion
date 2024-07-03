#chroma upsampling as explained in readme file

List=[]
List_new=[]

with open("YUV420_chroma.ppm","r") as file:
  data=file.read()
  List=data.split("\n")
  List.remove('') #somehow List has one empty element, removing that
num=len(List)

for i in range(0, num-2, 2):
  num1=int(List[i], 10)+int(List[i+2], 10)
  num1=num1/2
  List_new.append(num1)
  num2=int(List[i+1], 10)+int(List[i+3], 10)
  num2=num2/2
  List_new.append(num2)
  num3=int(List[i],10)
  List_new.append(num3)
  num4=int(List[i+1],10)
  List_new.append(num4)
  index=i

List_new.append(List[index+2]) #last 4 pixels will be missing as per the conversion, so we need to interpolate in this fashion
List_new.append(List[index+3])
List_new.append(List[index+2])
List_new.append(List[index+3])

with open("YUV420_chroma_new.ppm","w") as file:
  for new_line in List_new:
    file.write(str(new_line)+'\n')
