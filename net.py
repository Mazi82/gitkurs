sal = int(input("Ange bruttolön:"))
taxrate = int(input("Ange skatteprocent:"))
rent = int(input("Ange hyra:"))

tax = sal * taxrate/100
net = sal - tax
remains = net - rent

print("Kvar:", remains)

