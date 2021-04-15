#Cube Number Test... Print out all cubed numbers up to the total value 1000, so if the cubed number is over 1000 break the loop.

i = 0
while True:
    i +=1
    cubed = i**3
    if cubed < 1000:
        print(cubed)
        continue
    else:
        break
        
        
        
#Get first prime numbers up to 100

for num in range(101):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
                print(num)
                
                
 Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
 
age = input("What is your age?")
  if int(age) < 18:
    print("kids")
  elif int(age)<= 65:
    print("adults")
  else:
    print("seniors")
