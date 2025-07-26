# Student grading program:

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if 91 <= student_scores[student] <=100:
        student_grades[student] = "Outstanding"
    elif 81 <= student_scores[student] <=90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= student_scores[student] <=80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# to print out Lille:
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
 # to print out D:
print(nested_list[2][1])


# how to print out "Stuttgart"
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])