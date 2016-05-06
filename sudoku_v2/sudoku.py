import time  # used only for the printing of start and finish time


def is_valid_block(block):
    for i in range(1, 10):
        if block.count(i) > 1:
            return False
    return True


def is_valid_board(sudoku_board):
    for i in range(9):  # rows
        if not is_valid_block(sudoku_board[i]):
            return False
    block = []
    for i in range(9):  # cols
        block.clear()
        for j in range(9):
            block.append(sudoku_board[j][i])
        if not is_valid_block(block):
            return False
    for i in range(3):  # squares
        for j in range(3):
            block.clear()
            for w in range(3):
                block.extend(sudoku_board[3*i+w][3*j:3*j+3])
            if not is_valid_block(block):
                return False
    return True


def solve_board(sudoku_board, num_of_sol_to_print):
    printed_num = 0
    print("start time "+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+":" +
          str(time.localtime(time.time()).tm_sec))
    for board in solve_board_h(sudoku_board, 0):
        if printed_num < num_of_sol_to_print:
            if board[1]:
                printed_num += 1
                print("solution num "+str(printed_num)+":")
                print_board(board[0])
            else:
                break
        else:
            break
    print("end time " + str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min) + ":" +
          str(time.localtime(time.time()).tm_sec))


# returns (board,is_valid)
def solve_board_h(sudoku_board, location):
    if location == 81:
        yield sudoku_board, True
    else:
        if sudoku_board[location // 9][location % 9] == 0:
            for val in range(1, 10):
                sudoku_board[location // 9][location % 9] = val
                if is_valid_board(sudoku_board):
                    for res in solve_board_h(sudoku_board, location+1):
                        if res[1]:
                            yield res
            sudoku_board[location // 9][location % 9] = 0
            yield [], False
        else:
            if is_valid_board(sudoku_board):
                for res in solve_board_h(sudoku_board, location + 1):
                    if res[1]:
                        yield res


# prints the board in a more readable format
def print_board(board):
    for j in range(3):
        # print 3 lines
        for i in range(3):
            print_line(board[i+3*j])
        if j < 2:
            print("---------------------")


def print_line(line):
    for i in range(3):
        for j in range(3):
            print(line[j+3*i], end=" ")
        if i < 2:
            print("|", end=" ")
        else:
            print("")

my_sudoku_board = [
    [0, 1, 2, 3, 0, 0, 8, 0, 0],
    [0, 6, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 4, 0],
    [0, 0, 0, 0, 2, 3, 5, 0, 0],
    [6, 0, 0, 0, 4, 0, 0, 0, 9],
    [0, 0, 1, 5, 7, 0, 0, 0, 0],
    [0, 7, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 0, 0, 2, 3, 5, 0]
    ]
print("lets start")
print("call solve_board(sudoku_board, num_of_sol_to_print)")
solve_board(my_sudoku_board, 2)
print("all done")
