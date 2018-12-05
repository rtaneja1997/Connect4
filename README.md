# Connect4
Created an ai for connect 4 utilizing minimax algorithm (with alpha-beta pruning). 




Done:
- Implemented random player
- Implemented minimax player 
- Fixed bug where player wins but game crashes

To do: 
- Noticed that the game allows someone to make an 'illegal move', i.e. if a player chooses a full column, the game skips his turn. It might be good if we fix this. (optional) 
- debug alpha beta 
- get ai's to vs each other 
- incorporate more randomness when ai chooses moves with same value


Notes:
- minimax was acting kinda weird with numpy so i rewrote a small portion of connect4.py without using numpy. minimax seems fine now but we should still check for bugs by playtesting. 


