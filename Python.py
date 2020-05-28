mode = input("Do you want classic Pig Latin (classic) or custom pig latin (custom)?: ")

if (mode == "custom"):
    text = input("Type your message in english: ")
    num = int(input("How many of the first letters of the word do you want moved?: "))
    textad = input("What text do you want to be added at the end of each word?: ")
    words = text.split()
    answer = ""

    for i in range(len(words)):
        ans = words[i]
        answer += ans[num:] + ans[:num] + textad + " "

    print(answer)

if (mode == "classic"):
    text = input("Type your message in english: ")
    words = text.split()
    answer = ""

    for i in range(len(words)):
        ans = words[i]
        answer += ans[2:] + ans[:2] + "ay" + " "

    print(answer)