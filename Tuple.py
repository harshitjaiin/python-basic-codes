marks= (9,4,5,5,6,7,8,9,9)       #this is a tuple and you cannot modify it after making it uses () instead of [] which is used in list

print(marks[0])

# marks.insert(0,99)     this will throw an error

print(marks.count(9))         #this will tell the total number of occurences of 9 in marks

print(marks.index(7))         #this will return the index where 7 is present 1st time

print(marks.index(5))
