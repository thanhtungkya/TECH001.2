a = list([])
while(True):
    tmp = input("Enter your number: ")
    try:
        tmp = int(tmp)
    except:
        break
    a.append(tmp)

a.sort(reverse=True)
if(len(a) >= 5):
    print(a[:5])
else:
    print("Amount of numbers don't have more than 5 numbers")
