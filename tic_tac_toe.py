
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # بررسی سطرها
    for row in board:
        if all(cell == player for cell in row):
            return True
    # بررسی ستون‌ها
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # بررسی قطرها
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("\n خوش آمدید به Tic-Tac-Toe!")
    print("بازیکن 1: X | بازیکن 2: O")
    print_board(board)

    while True:
        try:
            move = input(f"بازیکن {current_player}, حرکت خود را وارد کنید (ردیف و ستون، مثال: 1 2): ")
            row, col = map(int, move.split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("لطفاً عددی بین 1 تا 3 وارد کنید.")
                continue
            if board[row - 1][col - 1] != " ":
                print("این خانه قبلاً گرفته شده است. لطفاً جای دیگری را انتخاب کنید.")
                continue

            board[row - 1][col - 1] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"🏆 بازیکن {current_player} برنده شد!")
                break
            elif is_draw(board):
                print("🤝 بازی مساوی شد!")
                break

            # تغییر نوبت بازیکن
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("ورودی نامعتبر! لطفاً دو عدد با فاصله وارد کنید.")

# اجرای بازی
play_game()
