helpf = [" ","$","%","*","+","-",".","/",":"]
symbols = [chr(i) for i in range(48,58)]
for i in range(65,91):
    symbols.append(chr(i))
for i in range(len(helpf)):
    symbols.append(helpf[i])
for i in range(len(symbols)):
    print(i,"-",symbols[i])
