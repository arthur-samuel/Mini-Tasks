# write a program to find the largest number in a list

#one way of approaching it
#print(max(numbers))

#another way of approaching it

numbers = [1,2,3,4,5,6,7,8,9,10]
max = numbers[0]


for number in numbers:
    if number > max:
        max = number
    print(max)
