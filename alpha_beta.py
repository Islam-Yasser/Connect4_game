import bsl
import pygame
import math
def playEasy():
    pygame.display.update()
    board = bsl.create_board()
    print("\n")

    bsl.draw_board(board)
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 100)

    NO_Winner = False
    turn = "ai"

    while NO_Winner == 0:

        clock = pygame.time.Clock()
        clock.tick(bsl.FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bsl.sys.exit()


    # print_board(board)
        if bsl.moves(board) == True:
            print("Game ended with tie ")
            break
        print("\n")
        if turn == "ai":
            pygame.time.wait(400)
            turn = "computer"
            print("Agent turn \n")
            b_col, alphaBeta_score = bsl.alpha_beta(board, 2, -math.inf, math.inf, True)
            if bsl.isvalid(board, b_col):
                row = bsl.available_row(board, b_col)
                bsl.play(board, row, b_col, 1)

                if bsl.check_winner(board, 1):
                    print("Agent has won \n")
                    NO_Winner = False
                    text = myfont.render("AI wins", 1, bsl.RED)
                    bsl.WINDOW.blit(text, (143, 5))
                    pygame.display.update()
                    gui = False

            bsl.print_board(board)
            bsl.draw_circle(board,row,b_col)
            pygame.display.update()
            print("\n")


        else:
            pygame.time.wait(400)
            turn = "ai"
            print("computer turn ")
            column = bsl.random.randint(0,6)

            if bsl.isvalid(board,column) :
                row = bsl.available_row(board,column)
                bsl.play(board,row,column,2)

                if bsl.check_winner(board,2) :
                    print("computer wins")
                    bsl.print_board(board)
                    NO_Winner = False
                    text = myfont.render("Computer wins", 1, bsl.YELLOW)
                    bsl.WINDOW.blit(text, (143, 5))
                    pygame.display.update()

            bsl.print_board(board)
            bsl.draw_circle(board, row, column)
            pygame.display.update()
            print("\n")


        if NO_Winner == True :
            pygame.time.wait(10000)

def playNormal():
    pygame.display.update()
    board = bsl.create_board()
    print("\n")

    bsl.draw_board(board)
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 100)

    NO_Winner = False
    turn = "ai"

    while NO_Winner == 0:

        clock = pygame.time.Clock()
        clock.tick(bsl.FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bsl.sys.exit()


    # print_board(board)
        if bsl.moves(board) == True:
            print("Game ended with tie ")
            break
        print("\n")
        if turn == "ai":
            pygame.time.wait(400)
            turn = "computer"
            print("Agent turn \n")
            b_col, alphaBeta_score = bsl.alpha_beta(board, 4, -math.inf, math.inf, True)
            if bsl.isvalid(board, b_col):
                row = bsl.available_row(board, b_col)
                bsl.play(board, row, b_col, 1)

                if bsl.check_winner(board, 1):
                    print("Agent has won \n")
                    NO_Winner = False
                    text = myfont.render("AI wins", 1, bsl.RED)
                    bsl.WINDOW.blit(text, (143, 5))
                    pygame.display.update()
                    gui = False

            bsl.print_board(board)
            bsl.draw_circle(board,row,b_col)
            pygame.display.update()
            print("\n")


        else:
            pygame.time.wait(400)
            turn = "ai"
            print("computer turn ")
            column = bsl.random.randint(0,6)

            if bsl.isvalid(board,column) :
                row = bsl.available_row(board,column)
                bsl.play(board,row,column,2)

                if bsl.check_winner(board,2) :
                    print("computer wins")
                    bsl.print_board(board)
                    NO_Winner = False
                    text = myfont.render("Computer wins", 1, bsl.YELLOW)
                    bsl.WINDOW.blit(text, (143, 5))
                    pygame.display.update()

            bsl.print_board(board)
            bsl.draw_circle(board, row, column)
            pygame.display.update()
            print("\n")


        if NO_Winner == True :
            pygame.time.wait(10000)


def playHard():
    pygame.display.update()
    board = bsl.create_board()
    print("\n")

    bsl.draw_board(board)
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 100)

    NO_Winner = False
    turn = "ai"

    while NO_Winner == 0:

        clock = pygame.time.Clock()
        clock.tick(bsl.FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bsl.sys.exit()


    # print_board(board)
        if bsl.moves(board) == True:
            print("Game ended with tie ")
            break
        print("\n")
        if turn == "ai":
            pygame.time.wait(400)
            turn = "computer"
            print("Agent turn \n")
            b_col, alphaBeta_score = bsl.alpha_beta(board, 6, -math.inf, math.inf, True)
            if bsl.isvalid(board, b_col):
                row = bsl.available_row(board, b_col)
                bsl.play(board, row, b_col, 1)

                if bsl.check_winner(board, 1):
                    print("Agent has won \n")
                    NO_Winner = False
                    text = myfont.render("AI wins", 1, bsl.RED)
                    bsl.WINDOW.blit(text, (143, 5))
                    pygame.display.update()
                    gui = False

            bsl.print_board(board)
            bsl.draw_circle(board,row,b_col)
            pygame.display.update()
            print("\n")


        else:
            pygame.time.wait(400)
            turn = "ai"
            print("computer turn ")
            column = bsl.random.randint(0,6)

            if bsl.isvalid(board,column) :
                row = bsl.available_row(board,column)
                bsl.play(board,row,column,2)

                if bsl.check_winner(board,2) :
                    print("computer wins")
                    bsl.print_board(board)
                    NO_Winner = False
                    text = myfont.render("Computer wins", 1, bsl.YELLOW)
                    bsl.WINDOW.blit(text, (143, 5))
                    pygame.display.update()

            bsl.print_board(board)
            bsl.draw_circle(board, row, column)
            pygame.display.update()
            print("\n")


        if NO_Winner == True :
            pygame.time.wait(10000)
