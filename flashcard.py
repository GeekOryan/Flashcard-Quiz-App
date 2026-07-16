import random
import json
import os

def main():
    print("Welcome to the CLI Flashcard Quiz Tool.")
    
    while(True):
        print("------- FLASHCARD MENU ------------")
        print("1. Create a New deck of Flashcards")
        print("2. Load Existing Deck of Flashcards")
        print("3. Exit Program")
        
        choice = input("Enter your choice (1 - 3): ")
        
        if choice == '1':
            deck = []
            
            deck_name = input("Enter the name of your deck: ")
                
            filename = f"{deck_name.strip().replace(' ', '_')}.json"
            
            while True:
            
                question = input("Enter the question (or 'done' to finish): ")
        
                if question == "done":
                    if len(deck) < 1:
                        print("You need at least one card before finishing. Try again.")
                    else:
                        break
        
                answer = input("Enter the answer to the question: ")
        
                card = {"question": question, "answer": answer}
                deck.append(card)
                
            with open(filename, "w", encoding="utf-8") as file:
                    json.dump(deck, file, indent=4)
                    
            print(f"Successfully saved! Deck name is '{filename}'")
            
        elif choice == '2':
            all_files = os.listdir(".")
            
            deck_files = [file for file in all_files if file.endswith(".json")]
            
            if not deck_files:
                print("No saved decks found.")
                continue
            else:
                print("Available decks: ")
                for index, file in enumerate(deck_files, 1):
                    proper_name = file.replace(".json", "")
                    print(f"{index}. {proper_name}")
                
                deck_data = None
                number_choice = input("Enter the number: ")
                    
                try:
                    deck_number = int(number_choice)
                        
                    if 1 <= deck_number <= len(deck_files):
                        selected_file = deck_files[deck_number - 1]
                        print(f"Success! You chose: {selected_file}")
                        
                        with open(selected_file, "r", encoding="utf-8") as file:
                            deck_data = json.load(file)
                            
                        print(f"Loaded {len(deck_data)} cards from '{selected_file}'!")
                    else:
                        print(f"Error: Please choose a number between 1 and {len(deck_files)}.")
                            
                except ValueError:
                    print("Error: Invalid input. You must type a whole number.")
                    
            # Debug line
            # print("\nFirst card sample data: ", deck_data[0] if deck_data else "No data")
            
            if deck_data and len(deck_data) > 0:
                while True:
                    print("\nHow would you like to play?")
                    print("Shuffled (Random order)")
                    print("Sequential (Original order)")
                    
                    
                    order_choice = input("Sequential or Shuffled? (s/sh): ").strip()
                    
                    if order_choice.lower() == "sh":
                        random.shuffle(deck_data)
                        print("Deck successfully shuffled!")
                        break
                    elif order_choice.lower() == "s":
                        print("Deck kept in sequential order.")
                        break
                    else:
                        print("Error: Invalid choice. Please enter s or sh.")
            while True:            
                score = 0
                missed_questions = []
                total_questions = len(deck_data)
                        
                for current_card in deck_data:
                    print(f"\nQuestion: {current_card['question']}")
                    
                    user_answer = input("Your Answer: ").strip()
                            
                    correct_answer = str(current_card["answer"]).strip()
                            
                    if user_answer.lower() == correct_answer.lower():
                        print("Correct!!")
                        score += 1
                    else:
                        print(f"Incorrect. The right answer was: {correct_answer}")
                        missed_questions.append(current_card)
                                
                print("\n--- Quiz Finished! ---")
                print(f"Your Final Score: {score} / {total_questions}")
                            
                if total_questions > 0:
                    percentage = (score / total_questions) * 100
                    print(f"Percentage: {percentage:.1f}%")
                    
                if not missed_questions:
                    print("Perfect score! You got every question right!")
                    break
                else:
                    print("\nQuestions you missed: ")
                    for missed_question in missed_questions:
                        print(f"\nMissed Question: {missed_question['question']}")
                        
                    retry = input("Do you want to retry?\n1. Retry missed questions\n2. Back to main menu\nEnter your choice: ")
                    if retry == '1':
                        deck_data = missed_questions
                        continue
                    else:
                        break
                    
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main()
