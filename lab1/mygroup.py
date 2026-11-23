groupmates = [
    {
        "name": "Анна",
        "surname": "Иванова",
        "exams": ["Математика", "Физика", "Информатика"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Сергей",
        "surname": "Павлов",
        "exams": ["Математика", "Физика", "Информатика"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Мария",
        "surname": "Соколова",
        "exams": ["Математика", "Физика", "Информатика"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Орлов",
        "exams": ["Математика", "Физика", "Информатика"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Елена",
        "surname": "Волкова",
        "exams": ["Математика", "Физика", "Информатика"],
        "marks": [5, 4, 4]
    },
]

def print_filtered_students(students, threshold):
    for student in students:
        marks = student["marks"]
        average = sum(marks) / len(marks)
        if average > threshold:
            print(student["name"], student["surname"], average)


threshold = float(input("Введите порог среднего балла: "))
print_filtered_students(groupmates, threshold)
