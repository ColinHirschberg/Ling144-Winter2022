# Fun with list comprehensions

# ============================  1 ============================
# ---- From class slides ----

germanAnimals = ["Katze", "Hund", "Igel", "Kröte", "Nachtigall", "Bär","Krokodil", "Delfin", "Kamel", "Fuchs"]

k_animals = []

for animal in germanAnimals:
  if animal[0] == 'K':
    k_animals.append(animal)

print(k_animals)

# ----  list comprehension syntax of the above --------------

k_animals2 = [animal for animal in germanAnimals if animal[0] == 'K']

print(k_animals2)


# ============================  2 ============================
# ---- Another for loop ------

e_animals = []

for animal in germanAnimals:
  if 'e' in animal:
    e_animals.append(animal + " has an 'e'")

# ---- write as a list comprehension ----




# ============================  3 ============================
# ---- Here's a list comprehension----

turkish_verbs = ["geliyorum", "anlamıyorum", "içiyoruz", "seviyorum", "yiyorlar", "öğretiyorum"]

first_sg = [word + " is 1st sing" for word in turkish_verbs if word[-2:] == "um"]

# ---- write it as a loop! ----




# ============================  4 ============================
 

complementizers = ["that", "whether", "if", "for", "Ø"]

annotated_Cs = []

for word in complementizers:
  if word == "whether" or word == "if":
    annotated_Cs.append(word + "[+wh]")
  else:
    annotated_Cs.append(word + "[-wh]")

print(annoatated_Cs)


# ---- write as a list comprehension ----
