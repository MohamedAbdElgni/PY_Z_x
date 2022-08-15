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
t_otal = []
grades = {"A": 100, "B": 80, "C": 40, "D": 20}
for main_key, main_value in students.items():
    print("-" * 30)
    print(f"-- Student Name => {main_key}")
    print("-" * 30)
    for child_key, child_value in main_value.items():
        print(f"- {child_key} => {grades[child_value]} Points")
        t_otal.append(grades[child_value])

    print(f'Total Points for {main_key} is {sum(t_otal)}'. title())
    t_otal.clear()
