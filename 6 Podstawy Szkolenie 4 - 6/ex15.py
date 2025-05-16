PESEL_dict = {
    "49168481764" : {"NAME" : "Adam", "LASTNAME" : "Kowalski", "AGE" : 22, "EYES" : "GREEN"},
    "49626281762" : {"NAME" : "Piotr", "LASTNAME" : "Pisarew", "AGE" : 52, "EYES" : "BLUE"},
    "38768764642" : {"NAME" : "Adrian", "LASTNAME" : "Chowanski", "AGE" : 62, "EYES" : "BROWN"},
    "49167252351" : {"NAME" : "Pawel", "LASTNAME" : "Kur", "AGE" : 51, "EYES" : "BLUE"},
    "45268481764" : {"NAME" : "Karolina", "LASTNAME" : "Kolcon", "AGE" : 26, "EYES" : "GREEN"}
}

###############################  TASK 1  ######################################

print(PESEL_dict["49168481764"]) # without mother name

mothers_names = [
    "Natalia",
    "Beata",
    "Anna",
    "Beata",
    "Ada"
]

for i, pesel in enumerate(PESEL_dict.keys()):
    PESEL_dict[pesel]["MOTHER_NAME"] = mothers_names[i]


print(PESEL_dict["49168481764"]) # with mother name


############################  TASK 2 ########################################

print("49167252351" in PESEL_dict.keys()) # presebt pesel ending with 1
pesel_remove = []
for pesel in PESEL_dict.keys():
    if pesel[-1] == "1":
        pesel_remove.append(pesel)

for pesel in pesel_remove:
    del PESEL_dict[pesel]

print("49167252351" in PESEL_dict.keys()) # absent pesel ending with 1


############################  TASK 3 ########################################
desc_line = ""
for pesel in PESEL_dict.keys():
    print("PESEL osoby : ",  pesel)
    print("opis osoby : ")
    for attr in PESEL_dict[pesel].keys():
        desc_line = "".join(str(PESEL_dict[pesel][attr]).replace("\t", ""))
        print(desc_line)
        desc_line = ""

