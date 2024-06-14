"""
8. Admission to a professional course is subject to the following conditions:
a) Marks in mathematics >=60
b) Marks in physics >=50
c) Marks in chemistry >=40
d) Total in all three subjects >=200
Or
Total in mathematics and physics>=150
Given the marks in three subjects, write a program to process the applications to list eligible
candidates.
"""

def check_eligibility(math_marks, physics_marks, chemistry_marks):
    total_marks = math_marks + physics_marks + chemistry_marks
    if math_marks >= 60 and physics_marks >= 50 and chemistry_marks >= 40 and total_marks >= 200:
        return True
    elif math_marks + physics_marks >= 150:
        return True
    else:
        return False

num_applicants = int(input("Enter the number of applicants: "))
eligible_candidates = []

for i in range(num_applicants):
    print("\nApplicant", i+1)
    math_marks = int(input("Enter marks in Mathematics: "))
    physics_marks = int(input("Enter marks in Physics: "))
    chemistry_marks = int(input("Enter marks in Chemistry: "))

    if check_eligibility(math_marks, physics_marks, chemistry_marks):
        eligible_candidates.append((i+1, math_marks, physics_marks, chemistry_marks))

print("\nEligible candidates:")
if eligible_candidates:
    for candidate in eligible_candidates:
        print("Applicant", candidate[0], "with marks in Math:", candidate[1], ", Physics:", candidate[2], ", Chemistry:", candidate[3])
else:
    print("No eligible candidates found.")
