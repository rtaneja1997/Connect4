# Connect4
ai stuff 




Done:
- Implemented random player
- Implemented minimax player 

To do: 
- Test minimax player (currently tested at depth of 4, no pr
- Noticed that the game allows someone to make an 'illegal move', i.e. if a player chooses a full column, the game skips his turn. It might be good if we fix this.


Notes:
- minimax was acting kinda weird with numpy so i rewrote a small portion of connect4.py without using numpy. minimax seems fine now but we should still check for bugs by playtesting. 


Bugs:
- If a human wins, it seems the game takes some time to break out of the running loop. Therefore, ai tries to run minimax but gets a terminal state. It should be the case that when anyone wins, the game immediately terminates.
