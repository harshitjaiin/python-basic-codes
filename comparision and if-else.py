
print(3>2)     
print(3==8)                       #boolean return karega
print(3!=8)
print(4<1)
print(3>2 or 3>8)
print(3>2 and 3>8)
print(not(3>2 and 3>8))          #not ko direct not likh do


#now we move to if else

age=input("enter the age ")

if(int(age)>=18):        #colon (:) yeh use karna padta hai isme to tell ki ab hum alag lines likhne wale h for this condtn
    print("you are allowed as you are 18+ " )

elif(int(age)>=16):      #elif likhte haii isme
    print("you will be allowed after " + str(18-int(age)) + " years")
else:
    print("ghar ja bacche!! ")


