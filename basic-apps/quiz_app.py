import re
from questions import QUESTIONS

def ask_question(question_data, question_number):
    print(f'\nQuestion {question_number}')
    print(question_data["question"])

    for option in question_data["options"]:
        print(option)

    while True:
        user_answer = input("Your answer: ").strip().upper()

        if user_answer in ['A', 'B', 'C', 'D']:
            return user_answer

        print("Please enter A, B, C or D.")

def run_quiz():
    pass


def test_regex():
    print("\n=== Regex Tester ===")
    pass

def main():
    pass

if __name__ == "__main__":
    pass

