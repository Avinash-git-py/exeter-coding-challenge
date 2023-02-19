import csv
import time

d = {}
first = time.time()
output = open("frequency.txt","w")
with open("french_dictionary.csv") as fcsv:
     rcsv = csv.reader(fcsv, delimiter=',')
     for row in rcsv:
        d[row[0]] = row[1]
find=open("find_words.txt","r")
for z in find:
    #print(find.read())
    text = open("t8.shakespeare.txt","r")
    for x in text:
        #print(text.read())
        a=[]
        b=[]
for i in text:
    a.append(i)
c=str(a).split()
##for i in range(len(a)):
show=[]
word=[]
for i in d:
    if i in a:
       word.append(i)
       word.append(dic[i])
       word.append(a.count(i))
       show.append(word)
       word=[]
for i in show:
    show.write(str(i))
    show.write("\n")
if x == z:
   x.replace(row[1],z)
   print(x)
end = time.time()
print("Time",end-first)
