#random yuv444 chroma component generated for the conversions
import random

file=open("yuv444_chroma.ppm","w")
for i in range(0,256): #8 bit data
  num=random.randrange(0,640*480/2) #resolution 480p
  file.write(str(num)+'\n')
file.close
