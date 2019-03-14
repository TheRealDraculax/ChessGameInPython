import chess

'Chess Board and the variable used to validate checkmate or not'
board = chess.Board()
checkmatecheck = board.is_game_over()

print("""
        CCCCCCCCCCCCChhhhhhh
     CCC::::::::::::Ch:::::h
   CC:::::::::::::::Ch:::::h
  C:::::CCCCCCCC::::Ch:::::h
 C:::::C       CCCCCC h::::h hhhhh           eeeeeeeeeeee        ssssssssss       ssssssssss
C:::::C               h::::hh:::::hhh      ee::::::::::::ee    ss::::::::::s    ss::::::::::s
C:::::C               h::::::::::::::hh   e::::::eeeee:::::eess:::::::::::::s ss:::::::::::::s
C:::::C               h:::::::hhh::::::h e::::::e     e:::::es::::::ssss:::::ss::::::ssss:::::s
C:::::C               h::::::h   h::::::he:::::::eeeee::::::e s:::::s  ssssss  s:::::s  ssssss
C:::::C               h:::::h     h:::::he:::::::::::::::::e    s::::::s         s::::::s
C:::::C               h:::::h     h:::::he::::::eeeeeeeeeee        s::::::s         s::::::s
 C:::::C       CCCCCC h:::::h     h:::::he:::::::e           ssssss   s:::::s ssssss   s:::::s
  C:::::CCCCCCCC::::C h:::::h     h:::::he::::::::e          s:::::ssss::::::ss:::::ssss::::::s
   CC:::::::::::::::C h:::::h     h:::::h e::::::::eeeeeeee  s::::::::::::::s s::::::::::::::s
     CCC::::::::::::C h:::::h     h:::::h  ee:::::::::::::e   s:::::::::::ss   s:::::::::::ss
        CCCCCCCCCCCCC hhhhhhh     hhhhhhh    eeeeeeeeeeeeee    sssssssssss      sssssssssss
""")

'Player Configurations'
color = input("Is Player One Black Or White?: ")

''' Attempt At Validation (if one of 8 options were not to be typed in)
while not color == "Black" or "black" or "B" or "b" or "White" or "white" or "W" or "w":
print("Choose Either Black Or White Player One")
color = input("Is Player One Black Or White?: ")
'''

if color == "Black" or "black" or "B" or "b":
    print("""
    Player One Is White
    Player Two Is Black
    """)

elif color == "White" or "white" or "W" or "w":
    print("""
    Player One Is Black
    Player Two Is White
    """)

'The Game'
while checkmatecheck == False:
    whitemove = input("Make Your Move White: ")
    board.push_san(whitemove)
    print (board)
    if checkmatecheck == True:
        break
        print("This Game Is Over")

    blackmove = input("Make Your Move Black: ")
    board.push_san(blackmove)
    print (board)
    if checkmatecheck == True:
        break
        print("This Game Is Over")
