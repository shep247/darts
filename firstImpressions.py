from game import Game

if __name__ == "__main__":
    numOfPlayers = int(raw_input("How many players?\n"))
    rounds = int(raw_input("How many rounds?\n"))

    outputStr = "We're going to play {rds} rounds with {numpl} players"
    print outputStr.format(numpl=numOfPlayers, rds=rounds)

    game = Game(rounds, numOfPlayers)
    game.play()
    print "-------------"
    game.print_score()
    print "-------------"
