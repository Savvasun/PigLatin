text = input("Type your message in english: ")
words = text.split()
mode = input("Do you want simple Pig Latin (simple), custom Pig Latin (custom), or classic Pig Latin? (classic): ")
vow = "aeiou"
cons = "bcdfghjklmnpqrstvxz"
vowels = list(vow)
consonants = list(cons)
moveLet = 0
answer = ""

if (mode == "custom"):
    num = int(input("How many of the first letters of the word do you want moved?: "))
    textad = input("What text do you want to be added at the end of each word?: ")

    for i in range(len(words)):
        word = words[i]
        answer += word[num:] + word[:num] + textad + " "

    print(answer)

if (mode == "simple"):
    for i in range(len(words)):
        word = words[i]
        answer += word[2:] + word[:2] + "ay" + " "

    print(answer)

if (mode == "classic"):
    for i in range(len(words)):
        word = words[i]
        
        for i in range(len(word)):
            if (any(x in word[i] for x in consonants) == True and any(x in word[i + 1] for x in vowels) == True):
                moveLet = word.find(word[i]) - 1
        
        answer += word[moveLet:] + word[:moveLet] + "ay" + " "
    
    print(answer)

input("Press ENTER to exit the program: ")

