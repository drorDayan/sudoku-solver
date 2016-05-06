import time


def is_valid_block(block):
    for i in range(1, 10):
        if block.count(i) > 1:
            return False
    return True


def is_valid_board(sudoku_board):
    for i in range(9):#rows
        if not is_valid_block(sudoku_board[i]):
            return False
    block = []
    for i in range(9):#cols
        block.clear()
        for j in range(9):
            block.append(sudoku_board[j][i])
        if not is_valid_block(block):
            return False
    for i in range(3):#squares
        for j in range(3):
            block.clear()
            for w in range(3):
                block.extend(sudoku_board[3*i+w][3*j:3*j+3])
            if not is_valid_block(block):
                return False
    return True


def solve_board(sudoku_board,num_of_sol_to_print):
    printed_num = 0
    print("start time "+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+":"+str(time.localtime(time.time()).tm_sec))
    for board in solve_board_h(sudoku_board, 0):
        if printed_num < num_of_sol_to_print:
            printed_num += 1
            print("solution num "+str(printed_num)+":")
            print_board(board[0])
        else:
            break
    print("end time " + str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min) + ":" + str(time.localtime(time.time()).tm_sec))


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


def print_board(board):
    for i in range(9):
        print(board[i])


my_sudoku_board=[
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]
print("lets start")
print("call solve_board(sudoku_board)")
solve_board(my_sudoku_board, 100000)
print("all done")

