rock=2
sccisor=1
paper=3
player1=str(input("player1 say your choice:"))
print("player 1 said:" +player1)
player2=str(input("player2 say your choice:"))
print("player2 said:" +player2)
if rock < sccisor:
    print("player 1 win")
else:
    print("player 2 win")
