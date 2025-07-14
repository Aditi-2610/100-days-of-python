student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# sum of a list 
total_exam_score = sum(student_scores)
print(total_exam_score)

# which is the same as:

total_score =0
for score in student_scores:
    total_score += score

print(total_score)

# maximum of a list
max_student_score = max(student_scores)
print(max_student_score)

# which is same as:

max_score = 0
for score in student_scores:
    if max_score < score:
        max_score = score

print(max_score)

# range function in for loop
for num in range(1, 11, 2): #start, end, step
    print(num)

total = 0
for num in range(1, 101):
    total +=num
    
print(total)