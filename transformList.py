#Matthew Chu
#Reads a list of words from a text file and modify capitalization
n = open('wordList.txt','w')
with open('GenerationList.txt', 'r+') as f:
    for line in f:
        l=line.capitalize()
        n.write(l)
n.close()



