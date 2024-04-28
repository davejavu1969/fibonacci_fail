import random
import matplotlib.pyplot as plt



b_rolls = []
busts = 0
spins = 0 
max_loss = 0
bank = 5000
wagered = 0 

def plot_array(data):
    plt.figure(figsize=(10, 6))  # Set the size of the plot
    plt.plot(data, marker='o')  # Plot the data with circle markers
    plt.title('Data Visualization')  # Title of the plot
    plt.xlabel('Index')  # X-axis label
    plt.ylabel('Value')  # Y-axis label
    plt.grid(True)  # Show grid
    plt.show()  # Display the plot
    
def roulette_simulation(num_spins):
    global busts, b_rolls, spins, max_loss, wagered, max_losses_in_row, mlr_count
    # Constants and initial conditions
    numbers_bet_on = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    initial_bankroll = bank
    initial_bet = 5
    bankroll = initial_bankroll
    

    # For tracking purposes
    wins_in_row = 0
    losses_in_row = 0
    max_wins_in_row = 0
    max_losses_in_row = 0
    fibonacci_sequence = [5, 5, 10, 15, 25, 40, 65, 105, 170, 275, 455]  # Initial Fibonacci sequence for betting
    fib_index = 0  # Index to keep track of the current position in the Fibonacci sequence
    current_bet = fibonacci_sequence[fib_index]  # Set the current bet to the first element in the Fibonacci sequence
    lose = False
    bank_cum = []
    

    for spin in range(num_spins):
        wagered += current_bet
        spins += 1
        starting_bankroll = bankroll
        spin_result = random.randint(0, 36)
        win = spin_result in numbers_bet_on

        # Calculate win/loss and update bankroll
        if win:
            lose = False
            bankroll += (current_bet * 2)
            wins_in_row += 1
            losses_in_row = 0
        else:
            lose = True
            bankroll -= current_bet
            losses_in_row += 1
            if losses_in_row > max_losses_in_row:
                max_losses_in_row = losses_in_row
            fib_index +=1 
            wins_in_row = 0

            if current_bet > bankroll:
                busts +=1
                break

        if win:
            current_bet = initial_bet
            fib_index = 0
        if lose:
            try:

                current_bet = fibonacci_sequence[fib_index]
            except Exception:
                #print(f"BUST! Final Bankroll: {bankroll}, Required Bet: {current_bet}")
                busts +=1
                break

        bank_cum.append(round(bankroll,3))

    # Final status

    b_rolls.append(round(bankroll,2))
    plot_array(bank_cum)
    

# Example usage
for each in range(0,10): # This is the number of 'sessions' - uncomment the plot_array(bank_cum) line above to plot graph for each session. Close each graph to view the next one. 
    num_spins = 100000  # You can change this number to simulate more or fewer spins
    roulette_simulation(num_spins)
print('BUSTS:', busts)
print('Closing bank rolls:', b_rolls)
pl_roll = []
cumulative = []
cum = bank 
for each in b_rolls:
    check = round(each - bank,2)
    if check < max_loss:
        max_loss = check 
    pl_roll.append(round(each - bank,2))
    cum += (each -bank)
    cumulative.append(round(cum,2))
print('P/L Rolls:', pl_roll)
print('Cumulative:',cumulative)
print('P/L', sum(pl_roll))
print('Spins:',spins)
print('Total wagered:', wagered)
print('Max losses in a row:', max_losses_in_row)
plot_array(cumulative)
