students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

A = 100
B = 80
C = 40
D = 20

for student_name, student_degree in students.items():
    print("-" * 30)
    print(f"-- Student Name => {student_name}")
    print("-" * 30)
    for subject, degree in student_degree.items():
        if degree == "A":
            print(f"{degree} => {A} ")
            total_marks += A
        if degree == "B":
            print(f"{degree} => {B} ")
            total_marks += B
        if degree == "C":
            print(f"{degree} => {C} ")
            total_marks += C
        if degree == "D":
            print(f"{degree} => {D} ")
            total_marks += D
    print(f"Total Marks For {student_name} Is {total_marks}")
    total_marks = 0
