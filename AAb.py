punktid = 0
print("Kes on USA president?")
vastus1 = input()
õige1 = "Trump"
if vastus1 == õige1:
    punktid += 1
print("Mitu jalga on elevandil?")
vastus2 = input()
õige2 = "4"
if vastus2 == õige2:
    punktid += 1
print("Kas väljas sajab?")
vastus3 = input()
õige3 = "Jah"
if vastus3 == õige3:
    punktid += 1
print (punktid," punkti, tubli")