text = input("Type your message in english: ")
words = text.split()
answer = ""

for i in range(len(words)):
    ans = words[i]
    answer += ans[2:] + ans[:2] + "ay" + " "

print(answer)