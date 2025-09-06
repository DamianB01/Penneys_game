# 🟡 Penney’s Game Simulation in Python

This project implements **Penney’s game** (a classic problem in probability theory) in Python.  
Two players choose their own coin flip sequences (for example `R O R O`), sequences can't be the same, and then random coin tosses are simulated until one of the chosen sequences appears.  
The player whose sequence appears first wins the game.

-----------------------------------------------------------------------------------------

## 📌 How it works

1. Each player chooses a sequence of 4 coin flips:
   - `R` for tails  
   - `O` for heads  
2. The program simulates random coin flips
3. Results are stored in a `deque`, which acts as a sliding window of the last flips
4. If the current sequence matches one of the players sequences → that player wins
5. The program repeats the simulation for as many games as the user specifies and counts wins

-----------------------------------------------------------------------------------------

## 🛠️ Technologies used

- **Python**
- **Standard libraries**:
  - `collections.deque` – for efficient sliding window management
  - `random` – for coin toss simulation

-----------------------------------------------------------------------------------------

## 📊 Example usage  

Please first player enter 1 coin (only big letters 'R' or 'O': R  
Please first player enter 2 coin (only big letters 'R' or 'O': O  
Please first player enter 3 coin (only big letters 'R' or 'O': R  
Please first player enter 4 coin (only big letters 'R' or 'O': O  
...  

How many simulations do you want to run? 100  

First player won and he needed for this 8 throws  
Second player won and he needed for this 11 throws  
...  

We simulated 100 games  
First player won 53 of them  
Second player won 47 of them  
