marks = [5,7,9]     #this is called a list in python (I personally think it is )

print(len(marks))   # this tells the lenghth of the list marks

print(marks[0])
print(marks[1])     #aage se 
print(marks[2])
print(marks[-1])    #peeche se print karna hai to -1 -2 -3 and so onn
print(marks[-2])
print(marks[-3])

print(marks[0:2])   #marks print hoga index 0 and 1 onlyy
print(marks[1:3])   #1st me jo likhoge wo index use hoga but 2nd wale se 1 phele tak hi include hoga4
print(marks[-3:-1]) 
print(marks[-1:-2])

# for loop se bhi kar sake agr linearly chalna hai!!
for index in marks:
 print( index )

 
marks.append(11)    # to add 11 to last of this list
print(marks[3])

print("\n")       #this is to add new line

marks.insert(0,16)         # to insert 16 to 0th index we do this
for index in marks:
 print( index )

marks.insert(2,19)      # to insert 19 at the 2nd index ie the 3rd place

print("\n")
for index in marks:
 print( index )
 
print(9 in marks)      # to check ki 9 hai ya nhi isme
print(0 in marks)

print("marks before clearing is ") 
print(marks[0:len(marks)])  #this is also one way to print all elements of a list

marks.clear()         # puri clear out kar dega list
print("marks after clearing is ") 
print(marks[0:len(marks)])  #list is empty in this case )
