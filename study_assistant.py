def show_menu():
    print("\n=== Personal Study Assistant ===")
    print("1. Flashcard Quiz")
    print("2. Study Timer")
    print("3. Exit")


def flashcard_quiz():
    questions = {
        "What is the capital of India?": "Delhi",
        "What does CPU stand for?": "Central Processing Unit",
        "What is 5 + 7?": "12"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer is:", answer)

    print("Your score:", score)


def study_timer():
    import time
    minutes = int(input("Enter study time in minutes: "))
    print("Focus time started...")

    time.sleep(minutes * 60)
    print("Time's up! Take a break.")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        flashcard_quiz()
    elif choice == "2":
        study_timer()
    elif choice == "3":
        print("Goodbye! Happy studying 😊")
        break
    else:
        print("Invalid choice. Try again.")
