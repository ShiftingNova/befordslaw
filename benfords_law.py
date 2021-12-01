file_name = str(input("Enter input file:\n"))
file = open(file_name,'r')
numbers = []
amount = {}
for i in file:
    o = i.strip("\n")
    e = o.split(",")
    if e[1].isnumeric():
        numbers.append(float(e[1]))
for i in numbers:
    value = int(str(i)[0])
    if value not in amount:
        amount[value] = 1
    else:
        amount[value] = amount[value]+1
for key in amount:
    count = int((amount[key]/len(numbers))*100)
    print(key,"|","#"*count)
