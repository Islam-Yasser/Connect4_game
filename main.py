import math
import random
import sys
import pygame


ROWS = 6
COLS = 7
BOARD_SIZE = 100

FPS = 60
RADIUS = BOARD_SIZE / 2 - 10


def create_board():
    board = [[0] * COLS for i in range(ROWS)]
    return board


def isvalid(board, column):
    return board[0][column] == 0


def available_row(board, column):
    for i in range(5, -1 , -1):
        if board[i][column] == 0:
            return i


def play(board, row, column, type):
    board[row][column] = type


def print_board(board):
    for i in board:
        print(*i)


dx8 = [+0, +0, -1, +1, +1, +1, -1, -1]
dy8 = [-1, +1, +0, +0, +1, -1, +1, -1]

def get_valid_locations(board):
    valid_locations = []
    for col in range(7):
        if isvalid(board, col):
            valid_locations.append(col)
    return valid_locations

def checkking(board, row, col, OR,OC):
    return row < ROWS and row >= 0 and col < COLS and col >= 0 and board[row][col] == board[OR][OC]

def check_winner(board, type):
    for row in range(0,6):
        for col in range(0,7):
            ans = 0
            if board[row][col] == 0 or board[row][col]!=type:
                continue
            for moves in range(8):
                ans = 1
                nx = row + dx8[moves]
                ny = col + dy8[moves]
                oldrow = row
                oldcol = col
                while checkking(board, nx, ny, oldrow, oldcol):
                    ans += 1
                    if ans == 4:
                        return True
                    oldrow = nx
                    oldcol = ny
                    nx = nx + dx8[moves]
                    ny = ny + dy8[moves]

    return False


def moves(board):
    for i in range(0, 7):
        if board[0][i] == 0: return False
    return True


def checkinput(col):
    return col >= 0 and col <= 6


def is_terminal_node(board):
    return check_winner(board, 1) or check_winner(board, 2) or moves(board) == 1


def score_evaluation(board):
    score = 0
    window=[]
    for i in range(0, 6):
        for j in range(0, 4):
            window.clear()
            for k in range(0,4):
              window.append(board[i][j + k])
            if window.count(1) == 4:
                score += 100
            if window.count(1) == 3 and window.count(0) == 1:
                score += 50
            if window.count(1) == 2 and window.count(0) == 2:
                score += 5
            if window.count(2) == 3 and window.count(0) == 1:
                score += -100


    for i in range(0, 7):
        for j in range(0, 2):
            window.clear()
            for k in range(0, 4):
                window.append(board[j + k][i])
            if window.count(1) == 4:
                score += 100
            if window.count(1) == 3 and window.count(0) == 1:
                score += 50
            if window.count(1) == 2 and window.count(0) == 2:
                score += 5
            if window.count(2) == 3 and window.count(0) == 1:
                score += -100

    for i in range(0, 2):
        for j in range(0, 3):
            window.clear()
            for k in range(0, 4):
                window.append(board[i + k][j + k])
            if window.count(1) == 4:
                score += 100
            if window.count(1) == 3 and window.count(0) == 1:
                score += 50
            if window.count(1) == 2 and window.count(0) == 2:
                score += 5
            if window.count(2) == 3 and window.count(0) == 1:
                score += -100

    for i in range(0, 2):
        for j in range(0, 3):
            window.clear()
            for k in range(0, 4):
                window.append(board[i + 3 - k][j + 3 - k])
            if window.count(1) == 4:
                score += 100
            if window.count(1) == 3 and window.count(0) == 1:
                score += 50
            if window.count(1) == 2 and window.count(0) == 2:
                score += 5
            if window.count(2) == 3 and window.count(0) == 1:
                score += -100

    return score


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_winner(board, 1):
                return (None, 100000000000000)
            elif check_winner(board, 2):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            return (None, score_evaluation(board))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = available_row(board, col)
            play(board, row, col, 1)
            new_score = minimax(board, depth - 1, alpha, beta, False)[1]
            play(board, row, col, 0)
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = available_row(board, col)
            play(board, row, col, 2)
            new_score = minimax(board, depth - 1, alpha, beta, True)[1]
            play(board, row, col, 0)
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value




board = create_board()
print("\n")


