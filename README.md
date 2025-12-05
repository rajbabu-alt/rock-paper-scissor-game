# rock-paper-scissor-game
🪨📄✂️ Rock–Paper–Scissors Game (Python)

A simple Python program where you can play Rock, Paper, Scissors against the computer.
The computer makes a random choice each round, and you must try to beat it!

🔧 Features

User-friendly menu

User chooses Rock, Paper, or Scissor

Computer picks a random choice

Game compares both choices

Shows win, lose, or tie

Play as many rounds as you want

Exit anytime

📌 How the Game Works

Run the program

You will see a menu:

1 → Rock

2 → Paper

3 → Scissor

4 → Exit

You choose a number (1–3)

Computer randomly chooses one

Program shows:

Your choice

Computer’s choice

Result (Win / Lose / Tie)
🧠 Game Rules

Rock beats Scissor

Scissor beats Paper

Paper beats Rock

Same choices = Tie

📝 Code Logic (Short Explanation)

A list stores the moves: ["rock", "paper", "scissor"]

User enters 1, 2, or 3

Program converts your number to a word (like "rock")

Computer picks randomly using random.choice()

If/elif checks who wins

Loop repeats until you choose 4 to exit
