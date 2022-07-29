#ГРА ШИБЕНИЦЯ
import random

words = ["кіт", "миша", "стіл", "стілець", "будинок", "кімната", "яблуко",
         "груша", "слива", "калина", "машина", "механік", "шибенця", "годиник",
         "голова", "рука", "нога", "око", "вухо", "ніс", "принтер", "журнал"]

def hangman(word):
    wrong = 0
    stages = ["",
              "__________      ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|_______________",
              "|_______________",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Вітаємо на страті!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = """Введіть літеру:
"""
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Молодець Юля! Було загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("""Ви програли! Життя загублене!
Було загадано слово: {}.""".format(word))
wrd = random.choice(words)

hangman(wrd)
