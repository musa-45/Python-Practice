import random

def display_menu():
    print("\n" + "="*40)
    print("🎮 WELCOME TO NUMBER GUESSING GAME 🎮")
    print("="*40)
    print("Choose Difficulty Level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-1000, 10 attempts)")
    print("4. View Statistics")
    print("5. Exit")
    print("="*40)

def play_game(difficulty, stats):
    # Set parameters based on difficulty
    if difficulty == 1:
        num_range = 10
        attempts = 5
        level_name = "Easy"
    elif difficulty == 2:
        num_range = 100
        attempts = 7
        level_name = "Medium"
    elif difficulty == 3:
        num_range = 1000
        attempts = 10
        level_name = "Hard"
    
    secret_number = random.randint(1, num_range)
    guess_count = 0
    score = 100
    
    print(f"\n🎯 {level_name} Mode Started!")
    print(f"Guess a number between 1 and {num_range}")
    print(f"You have {attempts} attempts\n")
    
    while guess_count < attempts:
        try:
            guess = int(input(f'Attempt {guess_count + 1}/{attempts} - Enter your guess: '))
            
            # Validate input
            if guess < 1 or guess > num_range:
                print(f"❌ Please enter a number between 1 and {num_range}!")
                continue
            
            guess_count += 1
            score -= 10  # Deduct points for each guess
            
            if guess == secret_number:
                print(f"\n🎉 You Won! The number was {secret_number}!")
                print(f"Score: {max(score, 0)} points")
                stats['wins'] += 1
                stats['total_games'] += 1
                stats['scores'].append(max(score, 0))
                return
            elif guess < secret_number:
                print(f"📈 Too low! Try a higher number.")
            else:
                print(f"📉 Too high! Try a lower number.")
        
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue
    
    print(f"\n😞 Game Over! The number was {secret_number}")
    print(f"Better luck next time!")
    stats['losses'] += 1
    stats['total_games'] += 1

def show_statistics(stats):
    print("\n" + "="*40)
    print("📊 GAME STATISTICS 📊")
    print("="*40)
    print(f"Total Games: {stats['total_games']}")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    if stats['total_games'] > 0:
        win_rate = (stats['wins'] / stats['total_games']) * 100
        print(f"Win Rate: {win_rate:.1f}%")
    if stats['scores']:
        print(f"Best Score: {max(stats['scores'])} points")
        print(f"Average Score: {sum(stats['scores']) / len(stats['scores']):.1f} points")
    print("="*40)

# Main Game Loop
stats = {
    'wins': 0,
    'losses': 0,
    'total_games': 0,
    'scores': []
}

while True:
    display_menu()
    choice = input('Enter your choice (1-5): ')
    
    if choice == '1':
        play_game(1, stats)
    elif choice == '2':
        play_game(2, stats)
    elif choice == '3':
        play_game(3, stats)
    elif choice == '4':
        show_statistics(stats)
    elif choice == '5':
        print("\nThanks for playing! 👋")
        break
    else:
        print("❌ Invalid choice! Please try again.")