#from termcolor import colored
from tkinter import *
import math
def inversia(el):
    if el==1:
        return int(0)
    if el==0:
        return int(1)
def printf(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print()
def size_of_qr(size):
    arr = [128,224,352]
    for i in range(len(arr)):
        if size<arr[i]:
            return i
def create_symbols():
    global symbols
    helpf = [" ","$","%","*","+","-",".","/",":"]
    symbols = [chr(i) for i in range(48,58)]
    for i in range(65,91):
        symbols.append(chr(i))
    for i in range(len(helpf)):
        symbols.append(helpf[i])


def inp(text):
    arr =[]
    typ = []
    pos = 0
    for i in range(len(text)//2):
        s = ""
        for j in range(2):
            s+=text[pos]
            pos+=1
        arr.append(s)
    if (pos<len(text)):
        arr.append(text[pos])
    mas = []
    for i in range(len(arr)):
        x = 0
        if len(arr[i])==2:
            for j in range(len(symbols)):
                if arr[i][0]==symbols[j]:
                    x+=j*45
                if arr[i][1]==symbols[j]:
                    x+=j
            typ.append(2)
        if len(arr[i])==1:
            for j in range(len(symbols)):
                if arr[i][0]==symbols[j]:
                    x+=j
            typ.append(1)
        mas.append(x)
    x=0
    for i in range(len(mas)):
        arr[i] = 0
        while mas[i]>0:
            arr[i] += int(mas[i]%2*(10**x))
            mas[i]=int(mas[i]/2)
            x+=1
        x=0
        arr[i] = str(arr[i])
    for i in range(len(arr)):
        if typ[i]==2:
            arr[i] = arr[i][::-1]
            for j in range(11-len(arr[i])):
                arr[i] = arr[i]+"0"
            arr[i] = arr[i][::-1]
        if typ[i]==1:
            arr[i] = arr[i][::-1]
            for j in range(6-len(arr[i])):
                arr[i] = arr[i]+"0"
            arr[i] = arr[i][::-1]
    s=""
    for i in range(len(arr)):
        s+=arr[i]
    return s
def length_text(l):
    print("length = ",l)
    length = ""
    while l>0:
        length+=str(l%2)
        l//=2
    for i in range(9-len(length)):
        length+="0"
    length = length[::-1]
    return length
def dop_stroki(string,size,t):
    if (len(string)%8!=0 and t==0):
        while len(string)%8!=0:
            string+="0"
    if (len(string)<size and t==1):
        for i in range((size-len(string))//8):
            if (i%2==0):
                string += "11101100"
            if (i%2==1):
                string += "00010001"
    return string
def find_yzor(arr,startx,starty):
    arr[starty + 3][startx + 3] = 1
    for i in range(3):
        for j in range(0,7-2*i):
            if i%2==0:
                arr[starty][startx+j] = 1
            else:
                arr[starty][startx+j] = 0
        for j in range(0,7-2*i):
            if i%2==0:
                arr[starty+6-2*i][startx+j] = 1
            else:
                arr[starty+6-2*i][startx+j] = 0
        for j in range(0,7-2*i):
            if i%2==0:
                arr[starty+j][startx] = 1
            else:
                arr[starty+j][startx] = 0
        for j in range(0,7-2*i):
            if i%2==0:
                arr[starty+j][startx+6-2*i] = 1
            else:
                arr[starty+j][startx+6-2*i] = 0
        startx+=1
        starty+=1

def find_yzor_line(arr,x,y):
    for i in range(len(arr)-22):
        if i%2==0:
            arr[y][x] = 0
        else:
            arr[y][x] = 1
        y-=1
    x+=1
    for i in range(len(arr)-22):
        if i%2==0:
            arr[y][x] = 0
        else:
            arr[y][x] = 1
        x+=1
def ygol(arr):
    for i in range(2):
        for j in range(8):
            if i==0:
                arr[11][j+4] = 0
            if i==1:
                arr[j+4][11] = 0
    for i in range(2):
        for j in range(8):
            if i==0:
                arr[11][len(arr)-12+j] = 0
            if i==1:
                arr[j+4][len(arr)-12] = 0
    for i in range(2):
        for j in range(8):
            if i==0:
                arr[len(arr)-12][j+4] = 0
            if i==1:
                arr[len(arr)-12+j][11] = 0
def aligning_yzor(arr,pos):
    arr[pos][pos] = 1
    arr[pos][pos+1] = 0
    arr[pos][pos-1] = 0
    for i in range(3):
        arr[pos+1][pos-1+i] = 0
    for i in range(3):
        arr[pos-1][pos-1+i] = 0

    for i in range(5):
        arr[pos-2][pos-2+i] = 1
    for i in range(5):
        arr[pos+2][pos-2+i] = 1

    for i in range(3):
        arr[pos-1+i][pos-2] = 1
    for i in range(3):
        arr[pos-1+i][pos+2] = 1

def mask(arr,m):
    pos = 0;
    for i in range(8):
        if i!=7:
            arr[len(arr)-5-i][12] = int(m[pos])
            pos+=1
        else:
            arr[len(arr)-5-i][12] = 1
    for i in range(8):
        arr[12][len(arr)-12+i] = int(m[pos])
        pos += 1
    pos = 0
    for i in range(2):
        for j in range(9):
            if i==0 and arr[12][j+4]!=0 and arr[12][j+4]!=1:
                arr[12][j+4] = int(m[pos])
            elif (i==0 and (arr[12][j+4]==0 or arr[12][j+4]==1)):
                continue
            if i==1 and arr[12-j][12]!=0 and arr[12-j][12]!=1:
                arr[12-j][12] = int(m[pos])
            elif (i==1 and (arr[12-j][12]==0 or arr[12-j][12]==1)):
                continue
            pos+=1
def in_qr(arr,infi):
    pos = 0
    x = len(arr)-5
    y = len(arr)-5
    let = [0,1]
    level = 0
    for f in range(len(arr)-8//2):
        if pos>len(infi):
            print(pos,"==",len(arr))
            continue
        if f % 2 == 0 and pos < len(infi):
            y = len(arr)-1
            for i in range(len(arr)):
                if (arr[y][x]!=let[0] and arr[y][x]!=let[1] and arr[y][x-1]!=let[0] and arr[y][x-1]!=let[1]):
                    for j in range(2):
                        if pos<len(infi):
                            if mask_f[level](x-j,y)==0:
                                arr[y][x-j] = inversia(int(infi[pos]))
                                pos+=1
                            else:
                                arr[y][x-j] = int(infi[pos])
                                pos += 1
                        else:
                            if mask_f[level](x-j,y)==0:
                                arr[y][x-j] = 1
                            else:
                                arr[y][x-j] = 0
                            arr[y][x-j]=" "
                    y -= 1
                    continue
                if ((arr[y][x]==let[0] or arr[y][x]==let[1]) and (arr[y][x-1]==let[0] or arr[y][x-1]==let[1])):
                    y -= 1
                    continue
            x -= 3
        if f % 2==1 and pos<len(infi):
            y = 0
            for i in range(len(arr)):
                if ((arr[y][x] != let[0] and arr[y][x] != let[1]) and (arr[y][x + 1] == let[0] or arr[y][x + 1] == let[1])):
                    x-=1
                if (arr[y][x] != let[0] and arr[y][x] != let[1] and arr[y][x+1]!=let[0] and arr[y][x+1]!=let[1]):
                    for j in range(2):
                        if pos<len(infi):
                            if mask_f[level](x-j+1,y)==0:
                                arr[y][x-j+1] = inversia(int(infi[pos]))
                                pos+=1
                            else:
                                arr[y][x-j+1] = int(infi[pos])
                                pos+=1
                        else:
                            if mask_f[level](x-j+1,y)==0:
                                arr[y][x-j+1] = 1
                            else:
                                arr[y][x-j+1] = 0
                            arr[y][x - j+1] = " "
                    y += 1
                    continue
                if ((arr[y][x]==let[0] or arr[y][x]==let[1]) and (arr[y][x+1]==let[0] or arr[y][x+1]==let[1])):
                    y += 1
                    continue
            x -= 1

def ramka(arr):
    for i in range(4):
        for j in range(len(arr)):
            arr[i][j]=0
    for i in range(4):
        for j in range(len(arr)):
            arr[len(arr)-1-i][j]=0
    for i in range(len(arr)):
        for j in range(4):
            arr[i][j]=0
    for i in range(len(arr)):
        for j in range(4):
            arr[i][len(arr)-1-j]=0
def XOR(x):
    arr = [0 for i in range(9)]
    const = [1, 0, 0, 0, 1, 1, 1, 0, 1]
    res = [0 for i in range(9)]
    ch = 8
    while x>0:
        arr[ch] = x%2
        x//=2
        ch-=1
    for i in range(9):
        if (const[i]==1 and arr[i]==1) or (const[i]==0 and arr[i]==0):
            res[i] = 0
        elif (const[i]!=0 or arr[i]!=0):
            res[i] = 1
    result = 0
    for i in range(9):
        result+=res[i]*(2**(8-i))
    return result
def bit_sum(x1,x2):
    arr1 = [0 for i in range(8)]
    arr2 = [0 for i in range(8)]
    result = [0 for i in range(8)]
    ch = 7
    while x1>0:
        arr1[ch] = x1%2
        x1//=2
        ch-=1
    ch = 7
    while x2>0:
        arr2[ch] = x2%2
        x2//=2
        ch-=1
    for i in range(8):
        if arr1[i]==1 and arr2[i]==1:
            result[i] = 0
            continue
        if arr1[i]==0 and arr2[i]==0:
            result[i] = 0
        else:
            result[i] = 1
    res = 0
    for i in range(8):
        res+=result[i]*(2**(7-i))
    return res
def byte_correction(arr,level):
    print("\n\n\t\tByte correction Start")
    yr_kor = [13,22,18]
    pol = {
        13:[74, 152, 176, 100, 86, 100, 106, 104, 130, 218, 206, 140, 78],
        22:[210, 171, 247, 242, 93, 230, 14, 109, 221, 53, 200, 74, 8, 172, 98, 80, 219, 134, 160, 105, 165, 231],
        18:[215, 234, 158, 94, 184, 97, 118, 170, 79, 187, 152, 148, 252, 179, 5, 98, 96, 153]
    }
    rev_pol_gaysa = ["-" for j in range(256)]
    pol_gays = [1]

    for i in range(255):
        x = pol_gays[len(pol_gays)-1]*2
        if x<256:
            pol_gays.append(x)
        else:
            pol_gays.append(XOR(x))

    for i in range(255):
        rev_pol_gaysa[pol_gays[i]] = i
    arr1 = [0 for i in range(yr_kor[level])]
    for i in range(len(arr)):
        arr1[i] = arr[i]
    
    print("yr_kor=",yr_kor[level])
    print("arr1=", arr1)

    gen_mn = [pol[yr_kor[level]][i] for i in range(yr_kor[level])]
    for i in range(len(arr)):
        a = arr1[0]
        del arr1[0]
        arr1.append(0)
        if a!=0:
            for j in range(len(gen_mn)):
                arr1[j] = bit_sum(arr1[j],pol_gays[(gen_mn[j]+rev_pol_gaysa[a])%255])
            
    print("arr1[result]=",arr1)
    print("\n\t\tByte correction end")
    new_arr = [arr1[i] for i in range(13)]
    return new_arr
def from_bit(arr):
    arr1 = ["" for i in range(len(arr)//8)]
    for i in range(len(arr)//8):
        for j in range(8):
            arr1[i]+=str(arr[i*8+j])
    res = 0
    for i in range(len(arr1)):
        for j in range(8):
            res+=int(arr1[i][j])*2**(7-j)
        arr1[i] = res
        res = 0
    return arr1
def to_bit(arr):
    try:
        arr1 = ["" for i in range(len(arr))]
        for i in range(len(arr)):
            for j in range(8):
                arr1[i]+=str(arr[i]%2)
                arr[i]//=2
            arr1[i] = arr1[i][::-1]
        return ''.join(arr1)
    except:
        r = ""
        for i in range(8):
            r+=str(arr%2)
            arr//=2
        return r[::-1]

correct_q = [104, 176,  272]
pos_align = [18,22,26,30]

masks = ["011010101011111","011000001101000","011111100110001","011101000000110","010010010110100"]
mask_f = [lambda x,y: (x+y) % 2,lambda x,y: y%2, lambda x,y: x%3,lambda x,y: (x+y)%3,lambda x,y:(x/3 + y/2) % 2]
type_code = "0010"
create_symbols()

texti = "ID444-12346"

text = inp(texti)
print("text len=",len(text))
level = size_of_qr(len(text))
size = correct_q[level]
qr = [[" " for i in range(pos_align[level+1]+7)] for j in range(pos_align[level+1]+7)]

length = length_text(len(texti))
print("length=",length)
type_code+=length+text

type_code = dop_stroki(type_code,size,0)
type_code = dop_stroki(type_code,size,1)

ltext = to_bit(byte_correction(from_bit(type_code),level))
print("ltext=",ltext)
type_code+=ltext
print("type_code = ",len(type_code))

ramka(qr)
find_yzor(qr,4,4)
find_yzor(qr,len(qr)-11,4)
find_yzor(qr,4,len(qr)-11)

find_yzor_line(qr,10,len(qr)-12)

ygol(qr)

mask(qr,masks[0])
ch=0
for i in range(len(qr)):
    for j in range(len(qr)):
        if qr[i][j]==" ":
            ch+=1

in_qr(qr,type_code)

root = Tk()
root.geometry("500x500")
root.title("QR_CODE")
size = 500//(pos_align[level+1]+7)
for i in range(len(qr)):
    for j in range(len(qr)):
        if qr[i][j]==1:
            lab = Label(bg="black")
        if qr[i][j]==0:
            lab = Label(bg="white")
        if qr[i][j]==" ":
            lab = Label(bg="gray")
        lab.place(x=size*j,y=size*i,width=size,height=size)

root.mainloop()
#arr = [64,196,132,84,196,196,242,194,4,132,20,37,34,16,236,17];
#byte_correction(arr)
