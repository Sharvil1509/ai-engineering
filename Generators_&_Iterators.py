#Lesson 1: Iterators
#What is an Iterator?
#An iterator is an object that remembers its current position while you loop through it.

l = [1,2,3,4]
it = iter(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print("-------------------------------------------------------------------")

fruits =["Apple", "Banana", "Orange"]
it = iter(fruits)
print(next(it))
print(next(it))
for fruit in it:
    print(fruit)

print("-------------------------------------------------------------------")

l1= [1,2,3]
it=iter(l1)
print(list(it))
print(list(it))

print("-------------------------------------------------------------------")

nums = [10, 20, 30, 40]
it = iter(nums)
print(next(it))
print(list(it))
print(next(iter(nums)))

print("-------------------------------------------------------------------")

# Lesson 2: Generators (yield)
# A generator is a special function that pauses instead of finishing.

def count():
    yield 1
    yield 2
    yield 3
gen = count()
print(next(gen))
print(next(gen))
print(next(gen))

def count1():
    print("Do u know")
    yield 1
    print("no u dont know (●'◡'●)")
    yield 2
    print(" u r f boy ヾ(＠⌒ー⌒＠)ノ ")
    yield 3
gen = count1()

print(next(gen))
print(next(gen))
print(next(gen))

print("-------------------------------------------------------------------")

def even_numbers():
    for i in range(1,20):
        
        if i%2==0 :
            yield i

gen =  even_numbers() 

for x in gen:
    print(x)

print("-------------------------------------------------------------------")    

def fibonacci(n):
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


gen = fibonacci(7)

for num in gen:
    print(num)

print("-------------------------------------------------------------------")    

#Lesson 3: Generator Expressions

squares = [x * x for x in range(5)] #already know list comprehension
print(squares)

squares = (x * x for x in range(5))#Just replace [] with ().
for num in squares:
    print(num)