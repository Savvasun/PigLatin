text = input("Type your message in english: ")
num = int(input("How many of the first letters of the word do you want moved?: "))
textad = input("What text do you want ot be added at the end of each word?: ")
words = text.split()
answer = ""

for i in range(len(words)):
    ans = words[i]
    answer += ans[num:] + ans[:num] + textad + " "

print(answer)