import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)




chosen_word = random.choice(word_list)


placeholder = []
word_length = len(chosen_word)
for position in range(word_length):
    placeholder.append("_")
print("".join(placeholder))

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.
lives = 6

guessed_letters = set()  # Track guessed letters

while "_" in placeholder and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue
    guessed_letters.add(guess)
    correct_guess = False
    for position in range(word_length):
        if chosen_word[position] == guess:
            placeholder[position] = guess
            correct_guess = True
    print("".join(placeholder))
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    print(stages[lives])  # Shows the ASCII art for current lives
    if "_" not in placeholder:
        print("You guessed the word!")
        break
    if not correct_guess:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print(f"You have {lives} lives left.")
        if lives == 0:
            print("***********************YOU LOSE**********************")
            print(f"The correct word was: {chosen_word}")
            print(stages[lives])

