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

def main():
    print("Welcome to the CLI Flashcard Quiz Tool.")
    
    while(True):
        print("------- FLASHCARD MENU ------------")
        print("1. Create a New deck of Flashcards")
        print("2. Load Existing Deck of Flashcards")
        print("3. Exit Program")
        
        choice = input("Enter your choice (1 - 3): ")
        
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        