'''
1. Display welcome message
2. Main menu: 1. Create New Deck  2. Load Existing Deck  3. Exit
3. Invalid choice → flag, ask again

4. Create New Deck:
   - Ask for deck name (used as filename)
   - Loop: ask for a question, then its answer
   - Type "done" to stop adding cards
   - If fewer than 1 card added, show error, keep looping
   - Save deck to JSON file
   - Confirm "Deck saved successfully"
   - Return to main menu

5. Load Existing Deck:
   - List available deck files
   - If none exist, show "No decks found", return to menu
   - Ask user to choose a deck by number
   - Ask: Sequential or Shuffled?
   - If shuffled, randomize the card order
   
6. Run the Quiz:
   - Track: score = 0, missed_questions = []
   - Loop through each card in the deck (in chosen order):
       - Display the question
       - Get user's answer
       - Normalize both stored answer and user answer (lowercase, strip whitespace)
       - If match: score += 1
       - If no match: append this card to missed_questions
   - After all cards shown, display final score (e.g. "7/10")

7. End of Quiz Menu:
   - If missed_questions is empty: show "Perfect score!" 
   - If not empty: display list of missed questions
   - Ask: 1. Retry missed questions  2. Back to main menu
   - If retry: run Step 6 again using only missed_questions as the deck
   - If back to menu: return to Step 2
'''

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
                    
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main()