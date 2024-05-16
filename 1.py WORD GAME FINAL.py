# updated word guessing game final project
import random
personal = "self attempts"
person = "self"
players = 0

#QuestionAnswer

personal_word_bank = ""
hidden_word = "" 
assumed_letters = ()
attempts = 0
word_estimations = 0
class Person:
    

    def __init__(self): 
        self.personal_word_bank = personal_word_bank
        self.hidden_word = self.choice(person.personal_word_bank)
        self.assumed_letters = ()
        self.attempts = 0
        self.word_estimations = 5 
        players += 1 


def add_another_player(person, player_tag):
    player_tag = 'name tag'
    score = 0
    remaining_word_guesses = 4

def another_player(person):
    person.playing = (person.current_player + 1)+ len(person.players)
    return person.players [person.playing]

def guess_the_letter(person, letter):
    person.tries = 1
    person.assumed_letters.add (letter)
    return person.hidden_word.count (letter)

def assume_the_word(person, word):
    player = person.players [person.playing]
    player ['amount_of_guesses_left'] = 1
    person.word_guesses = 1
    if word == person.hidden_word:
        person['score'] = personal.attempts
        return True
    return False
    

def determine_status_in_game(person):
    person = 'person.players [person.playing]'
    return person

def main():
    personal_word_bank = ["earth", "mars", "jupiter", "saturn", "uranus"]
    hidden_word = random.choice (self.personal_word_bank)
    assumed_letters = set()
    game_over = False
    print("Welcome to the game!")
    players = []

    amount_of_players = int(input("insert amount of players: "))

    for   _   in range (amount_of_players):
        player_tag = input ("enter player tag: ")
        players.append(player_tag)
        add_another_player(person, player_tag)
        add_another_player(person, player_tag)

    for player in players:
        print(f"\n{player}, it's your turn to play!")
        play_game(player)

def play_game(person_playing):
    if not game_over:
        status = determine_status_in_game ()
        print(f"\nCurrent player: {status['current_player']}")
        print("guessed letter: ", ' '.join (status['guessed_letters']))
        print(f"Amount of Termms Remaining: {status['amount_of_guesses_remaining##']}")
        letter = input ("guess the letter: ")
        occurences = guess_the_letter(letter)
        print(f"The letter'(letter)' pops up (2) times.")

    if input ("can you guess the term? (yes or no)") == 'y':
        guess_word = input ("guess the word: ")
        if guess_word(guess_word):
            print(f"Congrats! {status['current_player']}, you made the right guess!!")
            print(f"Your score (complete letter guesses): {players[person_playing]['score']}")
            game_over = True

        else:
            print ("Sorry wrong guess ):")
            # if the term is wrong, add another word to the guess to add to original amount of words in bank
            hidden_word = random.choice (personal_word_bank)
            guesses_remaining += 1
            print("Lets try a different word")

    while not game_over:
        for player in self.players: 
            print ( f"\n Current player: {player.name}")
            print ("Guessed letters:" , ' ' )
            print (f" Remaining word guesses: {player.remaining_word_guesses}")

            letter = input ("guess a letter: ")
            guess_the_letter(letter)

            if input ("Can you guess the word? (yes or no)").lower() == 'yes':
                word = input ("Enter your word guess: ").lower()
                guess_the_letter (word, player)
                if game_over:
                    break
                
        if players[person_playing]['amount_of_guesses_left'] == 0:
            print(f"status '{status['current_player']} has no more word guesses left and is removed from the game.")
                    
        if not game_over: 
            another_player()

        if __name__ == "__main__":
            game = Diceround(["Player 1", "Player 2" ])
            game.play_game()
