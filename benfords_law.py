file_name = str(input("Data file name:\n"))
file = open(file_name,'r')
numbers = []
amount = {}
law = True
check = {1:30, 2:17,3:12,4:9,5:7,6:6,7:5,8:5,9:4}
for i in file:
    o = i.strip("\n")
    e = o.split(",")
    if e[1].isnumeric():
        numbers.append(float(e[1]))
for i in numbers:
    value = int(str(i)[0])
    if value == 0:
        value = int(str(i)[1])
    if value not in amount:
        amount[value] = 1
    else:
        amount[value] = amount[value]+1
print()
for key in amount:
    count = int((amount[key]/len(numbers))*100)
    print(key,"|","#"*count)
for key in amount:
    count = int((amount[key] / len(numbers)) * 100)
    if count > check[key]+10 or count < check[key]-5:
        law = False
        print(key,"false", amount[key])
print(law)
if law:
    print("\nFollows Benford's Law")
else:
    print("\nDoes not follow Benford's Law")
