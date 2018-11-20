# Connect4
Created an ai for connect 4 utilizing minimax algorithm (with alpha-beta pruning). 




Done:
- Implemented random player
- Implemented minimax player 

To do: 
- Test minimax player (currently tested at depth of 4, higher depths cause exponential rise in time computations) 
- Noticed that the game allows someone to make an 'illegal move', i.e. if a player chooses a full column, the game skips his turn. It might be good if we fix this.
- alpha beta pruning possibly
- fix bug when player wins
- incorporate more randomness when ai chooses moves with same value


Notes:
- minimax was acting kinda weird with numpy so i rewrote a small portion of connect4.py without using numpy. minimax seems fine now but we should still check for bugs by playtesting. 


Bugs:
- If a human wins, it seems the game takes some time to break out of the running loop. Therefore, ai tries to run minimax but gets a terminal state. It should be the case that when anyone wins, the game immediately terminates.
