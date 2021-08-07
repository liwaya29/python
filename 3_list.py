pets = []
print(pets)
print(type(pets))

pets.append("dog")
print(pets)
pets.append("cat")
print(pets)
pets.append("fish")
print(pets)

pets.append(99)
print(pets)

print(len(pets))

print("length: ", len(pets))

pets.append(44.44)
print(pets)

# to access elements in the list, supply index
print(pets[0])
print(pets[1])

print(pets[4])
print(pets[-1])
print(pets[-2])

# slicing
print(pets[1:])
print(pets[0:4])
print(pets[-2:])


# remove elements
pets.remove("dog")
print(pets)

one = pets.pop(0)
print(one)
print(pets)


school = "CIT"
print(school)
print(school[0])
print(school[-1])
print(school[1:])
