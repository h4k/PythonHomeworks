numbers = [6,5,3,8,4,2,5,4,11]
sum1 = 0

for val in numbers:
    sum1 = sum1 + val

print("Sum is  ", sum1)

# ======================================

print(range(10))

print(list(range(10)))

# ======================================

genre = ['pop', 'rock', 'jazz']

for i in range(len(genre)):
    print("I like ", genre[i])

# ======================================

digits = [0,1,5]
for i in digits:
    print(i)
else:
    print("Nothing more")

# ======================================

student_name = "Test"
marks = {'James' : 90, "Arthur" : 50, "Jules" : 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print("Student without marks.")

# ======================================

n = 10
sum = 0
i2 = 1

while i2 <=n:
    sum = sum + i2
    i2 = i2+1

print("The sum is ", sum)


# ======================================

counter = 0

while counter < 3:
    print("loop on")
    counter = counter +1
else:
    print("loop off")




# ======================================
# ======================================
# ======================================
# ======================================
# ======================================
# ======================================
