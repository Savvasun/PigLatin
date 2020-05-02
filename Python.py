text = input("Type your message in english: ")
num = int(input("How many of the first letters of the word do you want encrypted?: "))
words = text.split()
answer = ""

for i in range(len(words)):
    ans = words[i]
    answer += ans[num:] + ans[:num] + "ay" + " "

print(answer)