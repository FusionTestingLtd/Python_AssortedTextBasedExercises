# Pig Latin is a game of alterations played on the
# English language game. To create the Pig Latin
# form of an English word the initial consonant
# sound is transposed to the end of the word and an ay is
# affixed (Ex.: "banana" would yield anana-bay).

text = input("Please Enter some text").split(' ')
i = 0
pig_latin = []

while i < len(text):
    if len(text[i]) > 3:
        pig_latin.append("{}{}{}".format(text[i][1:], text[i][:1], "ay"))
    else:
        pig_latin.append(text[i])
    i = i + 1

print(str(pig_latin).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))
