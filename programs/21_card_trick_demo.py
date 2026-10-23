
import random

def build_deck():
    ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    suits = ["♠","♥","♦","♣"]
    return [f"{r}{s}" for s in suits for r in ranks]

def deal_into_columns(cards):
    cols = [[], [], []]
    for i, c in enumerate(cards):
        cols[i % 3].append(c)
    return cols

def gather_with_middle(columns, chosen_col_idx):
    order = [0,1,2]
    left = [i for i in order if i != chosen_col_idx][0]
    right = [i for i in order if i != chosen_col_idx][1]
    return columns[left] + columns[chosen_col_idx] + columns[right]

def format_columns(columns):
    rows = []
    for r in range(7):
        row = []
        for c in range(3):
            val = columns[c][r] if r < len(columns[c]) else ""
            row.append(val.ljust(4))
        rows.append("   ".join(row))
    header = "Col 1".ljust(6) + "Col 2".ljust(8) + "Col 3"
    sep = "-" * 24
    return header + "\n" + sep + "\n" + "\n".join(rows)

def play(seed=None):
    if seed is not None:
        random.seed(seed)
    deck = build_deck()
    random.shuffle(deck)
    cards = deck[:21]

    print("Think of one card from the 21 shown. Remember it silently.\n")

    for round_no in range(1,4):
        columns = deal_into_columns(cards)
        print(f"\nRound {round_no}:")
        print(format_columns(columns))
        while True:
            try:
                col = int(input("Which column is your card in? (1/2/3): ").strip())
                if col in (1,2,3):
                    break
            except ValueError:
                pass
            print("Please enter 1, 2, or 3.")
        cards = gather_with_middle(columns, col-1)

    # After 3 rounds, the chosen card is at position 11 (index 10)
    print("\nI believe your card is:", cards[10])

if __name__ == "__main__":
    # Fix a seed for reproducibility in class, e.g., play(seed=42)
    play()
