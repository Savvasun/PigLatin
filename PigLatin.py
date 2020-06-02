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
    #This mode runs if "custom" is chosen.
    #These prompt you to chose how many letters you want moved and what to add at the end.
    num = int(input("How many of the first letters of the word do you want moved?: "))
    textad = input("What text do you want to be added at the end of each word?: ")

    for i in range(len(words)):
        #Here is the loop that generates the words.
        word = words[i]
        answer += word[num:] + word[:num] + textad + " "

if (mode == "simple"):
    #This mode runs if "simple" is chosen
    #It simply moves two letters and adds an "ay"
    for i in range(len(words)):
        word = words[i]
        answer += word[2:] + word[:2] + "ay" + " "

if (mode == "classic"):
    #This mode runs if "classic" is chosen.
    for i in range(len(words)):
        #This loop iterates through each word.
        word = words[i]
        print(word)

        for e in range(len(word)):
            #This loop iterates through each letter of the word.
            print(word[e])

            if (word[e] in cons and word[e + 1] in vows):
                moveLet = word.find(word[e]) - 1
                print("MoveLet is: " + word[moveLet])
            else:
                continue

        answer += word[moveLet:] + word[:moveLet] + "ay" + " " 

print(answer)

input("Press ENTER to exit the program.")