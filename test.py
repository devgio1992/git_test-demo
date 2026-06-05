import json


def load_data():
    with open("students.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def show_students():
    data = load_data()
    print(data["students"])


def add_student():
    data = load_data()

    student = {
        "id": int(input("ID: ")),
        "name": input("Name: "),
        "grade": int(input("Grade: ")),
    }

    data["students"].append(student)
    save_data(data)


def find_student():
    search = int(input("შეიყვანე ID: "))
    data = load_data()

    for student in data["students"]:
        if student["id"] == search:
            print("ნაპოვნია:", student)
            return

    print("ვერ მოიძებნა")


def change_point():
    search = int(input("ID ქულის შესაცვლელად: "))
    data = load_data()

    for student in data["students"]:
        if student["id"] == search:
            student["grade"] = int(input("ახალი ქულა: "))
            save_data(data)
            print("შეიცვალა")
            return

    print("ვერ მოიძებნა")


def delete_student():
    search = int(input("ID წასაშლელად: "))
    data = load_data()

    new_list = []

    for student in data["students"]:
        if student["id"] != search:
            new_list.append(student)

    data["students"] = new_list
    save_data(data)

    print("წაშლილია")


# MAIN MENU
while True:
    print("\n--- STUDENT SYSTEM ---")
    print("1. ნახვა")
    print("2. დამატება")
    print("3. ქულის შეცვლა")
    print("4. წაშლა")
    print("5. ძებნა")
    print("0. გამოსვლა")

    choice = int(input("აირჩიე: "))

    if choice == 1:
        show_students()

    elif choice == 2:
        add_student()

    elif choice == 3:
        change_point()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        find_student()

    elif choice == 0:
        break

    else:
        print("არასწორი არჩევანი")
