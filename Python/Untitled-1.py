'''alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

string ="ZNMD"
testString = list(string)
printingTime = 0

if testString[0] == alphabet[0]:
   printingTime = 0
elif alphabet.index(testString[0])-alphabet.index("A")>13:
   printingTime = printingTime + (alphabet.index(testString[0])+alphabet.index("A")+2)%len(alphabet)
else:
   printingTime = printingTime + alphabet.index(testString[0])-alphabet.index("A")

for i in range (len(testString)-1):
   if alphabet.index(testString[i]) < alphabet.index(testString[i+1]):
      if alphabet.index(testString[i+1])-alphabet.index(testString[i])>13:
         print((alphabet.index(testString[i])+alphabet.index(testString[i+1])+1)%len(alphabet))
         printingTime = printingTime + (alphabet.index(testString[i])+alphabet.index(testString[i+1])+2)%len(alphabet)
      else:
         printingTime = printingTime + alphabet.index(testString[i+1])-alphabet.index(testString[i])
   else:
      if alphabet.index(testString[i])-alphabet.index(testString[i+1])>13:
         printingTime = printingTime + (alphabet.index(testString[i])+alphabet.index(testString[i+1])+2)%len(alphabet)
      else:
         printingTime = printingTime + alphabet.index(testString[i])-alphabet.index(testString[i+1])

print (printingTime)'''

def countGroups(related):
    n = len(related)
    elements_index = set(i for i in range(n))
    counter = 0
    while elements_index:
        counter = counter +  1
        node = elements_index.pop()
        neighbor = related[node]
        more_group_members = set()
        for i in elements_index:
            if neighbor[i]:
                more_group_members.add(i)
        elements_index = elements_index - more_group_members
    return counter


# your example:
related_0 = [[1, 1, 0,0,0], [1, 1, 0,0,0], [0, 0,1,0,0], [0, 0,0,1,1], [0, 0,0,1,1]]

print(countGroups(related_0))