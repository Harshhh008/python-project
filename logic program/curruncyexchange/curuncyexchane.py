with open('curuncyexchange.txt') as f:
    lines = f.readlines()
# print(line)

CurruncyDict = {}

for line in lines:
    parshed = line.split("\t")
    CurruncyDict[parshed[0]] = parshed[1]     #parshed 0 = country name parshed 1
# print(CurruncyDict)

amount = int(input("Enter amount for Exchange: "))
[print(item) for item in CurruncyDict.keys()]
curruncy = input("Enter country for exchange curruncy : ")
print(f"{amount} INR is equal to {amount * float(CurruncyDict[curruncy])} {curruncy}")

