text = input("Type your message in english: ")
words = text.split()
print(words)
mode = input("Do you want simple Pig Latin (simple), custom Pig Latin (custom), or classic Pig Latin? (classic): ")
vowels = "aeiou"
vows = list(vowels)
consonants = "bcdfghjklmnpqrstvwxyz"
cons = list(consonants)
moveLet = 0
answer = ""

if (mode == "custom"):
    num = int(input("How many of the first letters of the word do you want moved?: "))
    textad = input("What text do you want to be added at the end of each word?: ")

    for i in range(len(words)):
        word = words[i]
        answer += word[num:] + word[:num] + textad + " "

if (mode == "simple"):
    for i in range(len(words)):
        word = words[i]
        answer += word[2:] + word[:2] + "ay" + " "

if (mode == "classic"):
    for i in range(len(words)):
        word = words[i]

        for e in range(len(word)):
            if (word[e] in cons and word[e + 1] in vows):
                moveLet = word.find(word[e]) - 1
            else:
                continue

        answer += word[moveLet:] + word[:moveLet] + "ay" + " " 

print(answer)

input("Press ENTER to exit the program.")