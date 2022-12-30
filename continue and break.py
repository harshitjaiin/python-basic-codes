students = ["ram" ,"raju","radhey","jain","hustle"]

for student in students:     #student is the name given here for separate elements under the list students
 if(student=="jain"):
   print(student)
   break
 else: 
   print(student)
   
print("\n")

for student in students:     #student is the name given here for separate elements under the list students
 if(student=="jain"):
   continue
 else: 
   print(student)
