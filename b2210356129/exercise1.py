

N = int(input("Write a integer number N "))

evenS = 0 
oddS = 0
evenTotal = 0
for i in range(1,N+1):
    if i%2 == 0:
        evenS +=i
        evenTotal +=1
    else:
        oddS +=i
print("Average of even numbers starting from 1 up to and including N: ", evenS/evenTotal)
print("The sum of odd numbers  starting from 1 up to and including N: ", oddS)
        

