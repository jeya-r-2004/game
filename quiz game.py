def multiple_choice_question(question, choices, correct_answer):
    """
    Function to display a multiple-choice question, its choices, and validate the user's answer.

    Parameters:
        question (str): The question text.
        choices (list of str): A list containing the multiple-choice options.
        correct_answer (int): The index (0-based) of the correct answer in the choices list.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    print(question)
    for idx, choice in enumerate(choices):
        print(f"{idx + 1}. {choice}")

    user_answer = int(input("Enter the number corresponding to your answer: ")) - 1

    return user_answer == correct_answer

score = 0
question_no = 0
playing = input('Do you want to play ? ')
if playing == 'yes':
    question_no += 1
   # Example usage:
    question_text =(f'\n{question_no}.What is the capital of France?')
    choices_list = ["London", "Paris", "Berlin", "Rome"]
    correct_answer_index = 1  # The correct answer index in the choices_list (in this case, 1 corresponds to "Paris")

    is_correct = multiple_choice_question(question_text, choices_list, correct_answer_index)

    if is_correct:
          score += 1
          print("Congratulations! Your answer is correct.")
    
    else:
         print("Oops! Your answer is incorrect.")
question_no += 1 
   # Example usage:
question_text = (f'\n{question_no}.What is the largest internal organ in the human body?')
choices_list = ["Lungs","Heart","Kidneys","Liver"]
correct_answer_index = 3  # The correct answer index in the choices_list (in this case, 1 corresponds to "liver")

is_correct = multiple_choice_question(question_text, choices_list, correct_answer_index)

if is_correct:
    print("Congratulations! Your answer is correct.")
    score += 1
else:
    print("Oops! Your answer is incorrect.")
question_no += 1
   # Example usage:
question_text = (f'\n{question_no}.What is the atomic number of Hydrogen?')
choices_list = ["1","2","3","4"]
correct_answer_index = 0  # The correct answer index in the choices_list (in this case, 1 corresponds to "1")

is_correct = multiple_choice_question(question_text, choices_list, correct_answer_index)

if is_correct:
     print("Congratulations! Your answer is correct.")
     score += 1
else:
     print("Oops! Your answer is incorrect.")

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')


    
