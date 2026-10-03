# Python Beginner Assignments

This project contains small, command-line Python programs designed for
beginner assignments. Python 3.8 or later is required; no external packages
are needed.

## Task 3: JPG File Organizer

`file_organizer.py` moves all `.jpg` and `.JPG` files from a source folder to
a destination folder. It creates the destination folder when needed, reports
invalid folders, and protects existing files by adding a number to duplicate
filenames instead of overwriting them.

### Run Task 3

From this folder, run:

```powershell
python file_organizer.py
```

### Task 3 Example

```text
JPG File Organizer
Source folder path: C:\Users\Student\Pictures\ToSort
Destination folder path: C:\Users\Student\Pictures\JPGs
Moved: beach.jpg
Moved: sunset.JPG

Files moved: 2
```

## Task 4: Basic Chatbot

`chatbot.py` is a simple rule-based chatbot. It responds to greetings, answers
"how are you", gives a friendly fallback for unknown messages, and ends when
the user types `bye`, `goodbye`, `exit`, or `quit`. Matching ignores letter
case and extra spaces.

### Run Task 4

From this folder, run:

```powershell
python chatbot.py
```

### Task 4 Example

```text
Basic Chatbot
Type 'bye', 'goodbye', 'exit', or 'quit' to end the chat.
You: HELLO
Bot: Hello! How can I help you?
You: how are you
Bot: I'm fine, thanks!
You: goodbye
Bot: Goodbye!
```

## Existing Project: Stock Portfolio Tracker

A beginner-friendly Python command-line application that calculates the value
of stock holdings using hardcoded prices. It does not use live stock APIs.

## Run the program

From this folder, run:

```powershell
python stock_portfolio_tracker.py
```

Enter one of the displayed tickers, then a positive quantity. Repeat for each
holding and enter `DONE` to view the portfolio summary. At the end, you can
optionally export the summary as `portfolio_summary.csv`.

## Example

```text
Ticker (or DONE): AAPL
Quantity: 2
Added AAPL.

Ticker (or DONE): TSLA
Quantity: 1.5
Added TSLA.

Ticker (or DONE): DONE

Portfolio Summary
--------------------------------------------------------------
Ticker       Quantity           Price        Investment Value
--------------------------------------------------------------
AAPL                 2         $180.00                 $360.00
TSLA               1.5         $250.00                 $375.00
--------------------------------------------------------------
Total portfolio value: $735.00
```
