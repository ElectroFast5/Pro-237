import os
# Can rename any folder with a file name containing less than 4 characters (only lowercase letters and numbers)

d1=0
d2=0
d3=0
d4=0
letter=["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
fileNo=1

for i in range(1679616):#456937 is large enough to account for the necessary possilities with 4 digits
    try:
        d1=d1+1
        if d1==len(letter)-1:
            d2=d2+1
            d1=0
        if d2==len(letter)-1:
            d3=d3+1
            d2=0
        if d3==len(letter)-1:
            d4=d4+1
            d3=0
        if d4==len(letter)-1:
            d4=0
        word=(str(letter[d1])+str(letter[d2])+str(letter[d3])+str(letter[d4]))
        os.rename(f"{word}.txt",f"file {fileNo}.txt")
        fileNo=fileNo+1
    except:
        pass

d1=0
d2=0
d3=0

for i in range(46656):#same as before but for 3 digits
    try:
        d1=d1+1
        if d1==len(letter)-1:
            d2=d2+1
            d1=0
        if d2==len(letter)-1:
            d3=d3+1
            d2=0
        if d3==len(letter)-1:
            d3=0
        word=(str(letter[d1])+str(letter[d2])+str(letter[d3]))
        os.rename(f"{word}.txt",f"file {fileNo}.txt")
        fileNo=fileNo+1
    except:
        pass

d1=0
d2=0

for i in range(1296):#but with 2 numbers
    try:
        d1=d1+1
        if d1==len(letter)-1:
            d2=d2+1
            d1=0
        #if d2==len(letter)-1:
            #d2=0
        word=(str(letter[d1])+str(letter[d2]))
        os.rename(f"{word}.txt",f"file {fileNo}.txt")
        fileNo=fileNo+1
    except:
        pass
    if word=="13":
        pass

d1=0

for i in range(36):#now just 1
    try:
        d1=d1+1
        word=str(letter[d1])
        os.rename(f"{word}.txt",f"file {fileNo}.txt")
        fileNo=fileNo+1
    except:
        pass