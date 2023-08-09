import time


def blogEntry():
    start = time.ctime()
    blogEntry = input("blog>> ")
    end = time.ctime()

    blog = open("blog.txt", "a")
    blog.write(start)
    blog.write("--")
    blog.write(end)
    blog.write(">> ")
    blog.write(blogEntry)
    blog.write("\n")

    blog.close()

def processBlog():
    blog = open("blog.txt", "r")
    allEntries = []
    for line in blog:
        dashDashStart = line.find("--")
        start = line[:dashDashStart]
        gtGtStart = line.find(">>")
        end = line[dashDashStart + 2:gtGtStart]
        entry = line[gtGtStart + 2:].strip()
        myTuple = (start, end, entry)
        allEntries.append(myTuple)
    return allEntries

#blogEntry()
blogEntries = processBlog()
sumOfCharacters = 0
wordCount = 0
for entry in blogEntries:
    sumOfCharacters = len(entry[2]) + sumOfCharacters
    words = entry[2].split(" ")
    wordCount = len(words) + wordCount

print("You have written", sumOfCharacters,"characters and", wordCount, "words")
