# Updated Final Project for Tupled Out!
import random
class Player:
    def __init__(self, name):
        self.name = name 
        self.score = 0

class DiceRound:
    def __init__(self, players, max_score=20, max_turns=3):
        self.players = [Player(name) for name in players]
        self.max_score = max_score
        self.max_turns = max_turns

    def dice_roll(self):
        return [random.randint(1, 6) for _ in range(3)]

    def turn_to_play(self, player):
        print(f"{player.name}'s turn:")
        rolls = self.dice_roll()
        print(f"Rolls of dice: {rolls}")
        
        if len(set(rolls)) == 3:
            print("Tupled Out!")
            return 0
        
        fixed = []
        for i in range(2):
            if rolls.count(rolls[i]) >= 2:
                fixed.append(i)

        if len(fixed) == 2: 
            print("Three dice are in place:", [rolls[i] for i in fixed])
            return 0
        
        choice = input("Would you like to roll again? (y/n): ").lower()
        if choice == 'n':
            return 0

        for i in range(2):
            if i not in fixed: 
                rolls[i] = random.randint(1, 6)
        print(f"New roll: {rolls}")

        turn_score = sum([rolls[i] for i in range(3) if i not in fixed])
        print(f"{player.name} scored {turn_score} points this round!")
   
    # Check if any player needs to give a point to the player with the lowest score 
        lowest_score = min([p.score for p in self.players])
        if player.score == lowest_score:
            for p in self.players:
                if p != player:
                    print(f"{p.name} gives 1 point to {player.name}!")
                    p.score -= 1
                    player.score += 1
   
    # return turn_score
    
    def display_scores(self):
        print("\nCurrent Scores Available:")
        for player in self.players:
            print(f"{player.name}: {player.score} points")

    def play_game(self): 
        for _ in range(self.max_turns):
            for player in self.players:
                turn_score = self.turn_to_play(player)
                if turn_score == 0:
                    player.score = 0
                else:
                    player.score += turn_score
                    self.display_scores()
                    if player.score >= self.max_score:
                        print(f"\n{player.name} won!")
                        return
        print("\nGAME OVER! No winners this round.")
