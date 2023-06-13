# chess_AI_simple_engine
A simple chess engien 
This project involves building a simplified chess playing AI using Python and various libraries. 
As a side project alongside my studies, 
I will explore different algorithms and techniques to create a chess engine 
capable of playing against humans. 
The AI will implement strategies such as the Alpha-Beta pruning algorithm, 
transposition tables, and history heuristics to improve its performance. Additionally, 
This project will allow me to gain practical experience in artificial intelligence 
and enhance my programming skills, 
while also providing a fun and challenging game of chess to play.
code source in : 
(#python , #numpy , #chess , #AI , #chess_engien)
exporing the code : (each function)
evaluate board function:
This code defines a function that evaluates a given chess board and returns the computed score. 
The code consists of two parts:
1. Determining the values for each piece:
   - A dictionary `piece_values` is defined that contains the value for each piece type.
   - A variable `score` is created and initialized to zero.
2. Calculating the material balance:
   - The `piece_map()` function is used to get the piece mapping for each square on the board.
   - The first loop calculates the material balance by adding up the value of the pieces for each color.
   - The second loop adds bonuses/penalties based on the piece locations.
   - The inner loops check the piece type and color, and add the appropriate weight based on the current location of the piece and the threats it exerts.
   - `score` is returned as the evaluation result.

This function can be used to determine the value of the current board in a game of chess
and helps in selecting the best possible moves for both the player and the computer.
#########
alpha beta MinMaxL algorithm function:
This code represents the Alpha-Beta Minimax algorithm with LMR (Late Move Reduction) 
extension for finding the best move in a game of chess. 
The code consists of the following steps:
1. Checking for depth completion or game over:
   - Checking whether the maximum depth limit has been reached or the game is over.
   - If so, returning the evaluation score of the board using the `evaluate_board()` function.
2. Evaluating all legal moves and storing them in a list with their scores:
   - Using a loop to evaluate each legal move by applying the `evaluate_heuristic()` function.
   - Storing each move with its computed score in a list `moves_scores`.
3. Sorting the list of moves based on their scores:
   - Using the `sort()` function to sort the `moves_scores` list based on the computed score, 
     in descending order if the current player is trying to achieve a higher score.
4. Looping through the selected moves and evaluating them using Alpha-Beta Minimax:
   - Using a loop to evaluate each move and applying the Alpha-Beta Minimax algorithm on it with LMR extension.
   - Storing the computed value in the `val` variable.
   - Updating the best score and alpha/beta values.
5. Returning the best score for the current player:
   - Returning the best score that can be achieved for 
     the current player (the player trying to achieve the highest score).
######
valuate heuristic function :  
This code defines a function that evaluates a given chess board using a simple heuristic function
based on the difference in piece counts. 
The code consists of the following steps:
1. Initializing the piece count array:
   - Using numpy to create an array of length 6, one for each type of chess piece.
   - For each piece type, the difference in the count of pieces 
     for each color (white and black) is computed and stored in the corresponding array element.
2. Summing up the piece count array:
   - Using numpy to sum up the element-wise values in the `piece_count` array.
   - The resulting value represents the difference in the total count of pieces for each color on the board.
3. Returning the evaluated score:
   - The computed score is returned as the result of the function.

Overall, this function provides a simple evaluation of the given chess board 
based on the difference in the number of pieces for each color. 
This evaluation can be used to rank the board and help in selecting the best possible move in the game of chess.
#####
alpha beta MinMax best algorithm function : 
This code represents an extension of the Alpha-Beta Minimax algorithm 
that selects the top k moves to explore further. 
The code consists of the following steps:
1. Checking for depth completion or game over:
   - Checking whether the maximum depth limit has been reached or the game is over.
   - If so, returning the evaluation score of the board using the `evaluate_board()` function.
2. Evaluating all legal moves and storing them in a list with their scores:
   - Using a loop to evaluate each legal move by applying the `evaluate_heuristic()` function.
   - Storing each move with its computed score in a list `moves_scores`.
3. Sorting the list of moves based on their scores:
   - Using the `sort()` function to sort the `moves_scores` list based on the computed score, 
     in descending order if the current player is trying to achieve a higher score.
4. Selecting the top k moves to explore further:
   - Reducing the `moves_scores` list to the top k moves based on their scores.
5. Looping through the selected moves and evaluating them using Alpha-Beta Minimax:
   - Using a loop to evaluate each move and applying the Alpha-Beta Minimax algorithm on it.
   - Storing the computed value in the `val` variable.
   - Updating the best score and alpha/beta values.
6. Returning the best score for the current player:
   - Returning the best score that can be achieved 
     for the current player (the player trying to achieve the highest score).
Overall, this function extends the Alpha-Beta Minimax algorithm by selecting the top k moves 
to further explore, which can help in reducing the search space and improving the performance of the algorithm.
######
play FEN function for web based GUI: 
This code defines a function called `play` that plays a game of chess using the Alpha-Beta Minimax algorithm 
with transposition table and history heuristic. 
The code consists of the following steps:
1. Defining a transposition table and a history table:
   - The transposition table is used to store previous evaluations of chess board positions, 
     which helps in reducing the search space and improving the performance of the algorithm.
   - The history table is used to store move history, 
     which helps in ordering moves based on their likelihood of success.
2. Creating a chess board object:
   - Creating a chess board object from the given FEN notation.
3. Setting initial values:
   - Setting the initial value of depth to 2 (the number of moves to look ahead).
   - Setting alpha to negative infinity and beta to positive infinity 
     (the initial values for the Alpha-Beta Minimax algorithm).
4. Choosing the first move:
   - Choosing the first legal move as the initial best move.
5. Looping through the legal moves and evaluating them using Alpha-Beta with move ordering:
   - Using a loop to evaluate each legal move by applying the Alpha-Beta Minimax algorithm with move ordering.
   - Using the transposition table to retrieve previous evaluations of the board.
   - Using the history heuristic to order moves based on their likelihood of success.
   - Updating the best move and score if a better score is found.
6. Making the selected move on the board:
   - Making the selected move on the chess board object.
Overall, this function plays a game of chess by selecting the best possible move 
using the Alpha-Beta Minimax algorithm with transposition table and history heuristic, 
which can help in reducing the search space and improving the performance of the algorithm.
#######
play move by UCI wih alpha beta MinMax best algorithm : 
(and the same way to play with alpha beta MinMaxL algorithm)
This code defines a function called `play_move` that prompts the user for a move 
and plays the chess game against the computer using the Alpha-Beta Minimax algorithm 
with transposition table and history heuristic. 
The code consists of the following steps:
1. Printing the current board position:
   - Printing the current state of the chess board object to the console.
2. Checking if the game is over:
   - Using the `is_game_over()` function to check if the game is over.
   - If so, printing "Game over" and returning from the function.
3. Determining which player's turn it is:
   - Determining the name of the player whose turn it is based on the color of the pieces on the board.
4. Prompting the player for their move:
   - Using the `input()` function to prompt the user for their move in UCI notation.
   - Checking if the move is legal by 
     using the `chess.Move.from_uci()` function and the `legal_moves` attribute of the board object.
   - If the move is invalid, printing "Invalid move" and calling the `play_move()` function recursively.
5. Applying the player's move:
   - Using the `push()` function of the board object to apply the player's move.

6. Checking if the game is over:
   - Using the `is_game_over()` function to check if the game is over.
   - If so, printing the final state of the chess board object and "Game over", 
     and returning from the function.
7. Determining which player's turn it is:
   - Determining the name of the player whose turn it is based on the color of the pieces on the board.
8. Printing the board after the player's move:
   - Printing the state of the chess board object to the console after the player's move.
9. Letting the computer choose its move using Alpha-Beta Minimax:
   - Using a loop to evaluate each legal move by applying the Alpha-Beta Minimax algorithm with move ordering.
   - Using the `push()` and `pop()` functions of the board object to test each move and compute its score.
   - Updating the best move and score if a better score is found.
10. Applying the computer's move:
   - Using the `push()` function of the board object to apply the computer's move.
11. Printing the board after the computer's move:
   - Printing the state of the chess board object to the console after the computer's move.
12. Playing the next move:
   - Calling the `play_move()` function recursively to play the next move.
Overall, this function allows the user to play a game of chess against the computer 
using the Alpha-Beta Minimax algorithm with transposition table and history heuristic. 
The function prompts the user for their move and applies it to the board, 
and then lets the computer choose its move and applies it to the board. 
The function then repeats this process until the game is over.
######
In conclusion, the development of a simple chess-playing AI using Python and various libraries 
has been an exciting and challenging project. 
Through the implementation of different algorithms and techniques, 
I was able to create an AI capable of playing chess against human opponents. 
I used strategies such as the Alpha-Beta pruning algorithm, transposition tables, 
and history heuristics to improve the AI's performance, 
and also explored the use of machine learning techniques. 
This project allowed me to gain a deeper understanding of artificial intelligence 
and to enhance my programming skills. 
I hope to continue to refine and improve the AI in the future, 
and to potentially explore other games and applications of AI.


