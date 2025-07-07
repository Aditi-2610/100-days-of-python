print("Hello"[-1])
print(123_456_789)

# check data type of a data:
print(type("hello"))
print(type(123))
print(type(45.77))
print(type(True))

# to change data type :
# change str to int
int("123")
print(int("123") + int("345"))

# concatenation

print("Number of letters in your name: " + str(len(input("Enter your name"))))


# Change the code so it outputs 3?
print(3 * 3 + 3 / 3 - 3)

print(3 * ( 3 + 3 ) / 3 - 3)


# Calculate BMI:
height = 1.65 
weight = 84

bmi = weight/(height**2)

print(bmi)

# Number manipulation:
Score = 0
Score +=1
Score /=1

# f strings
print(f"Your score is = {Score}") # use instead of type converting a variable

