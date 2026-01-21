# Silent Auction – Python (Day 9)

This project is a **console-based Silent Auction application** built in Python as part of my *100 Days of Code – Python Bootcamp* (Day 9).

The program allows multiple users to place bids anonymously and determines the highest bidder using core Python concepts such as functions, dictionaries, loops, and conditional logic.

The project is structured into multiple files to demonstrate **basic modularization and imports**.

---

## 📂 Project Structure

day-9-silent-auction/
│
├── silent_bidding.py
├── art.py
└── README.md

- **silent_bidding.py** – Main application logic  
- **art.py** – ASCII art used for program display  
- **README.md** – Project documentation  

---

## 🧠 Concepts & Skills Demonstrated

- Writing and calling functions with parameters and arguments  
- Using dictionaries to store and process dynamic user data  
- Loop control (`while`, `for`) for repeated user input  
- Conditional logic to control program flow  
- Variable scope and data passed into functions  
- Separating code into multiple files using `import`  

---

## ⚙️ How the Program Works

1. The program prompts users to enter:
   - Their name
   - Their bid amount
2. Each bid is stored in a dictionary where the key is the bidder name and the value is the bid amount.
3. Users can continue adding bidders until they choose to stop.
4. A function iterates through the collected bids to determine and display the highest bidder.

---

## ▶️ How to Run

1. Clone the repository or download this folder.
2. Ensure ` silent_bidding.py` and `art.py` are in the same directory.
3. Run the program from the terminal:

```bash
python  silent_bidding.py
