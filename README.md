# Maze Game
## Inspiration
This game gets inspiration from the reknowned graph traversal techniques: breath-first search and depth-first search. I am utterly intrigued by these two graph traversal methods. Theoretically, it is believed that two thirds of graph interview questions can be solved using these two techniques. Consequently, proficiency in these two algorithms will allow you to solve at least two-thirds of tree and graph problems that you may encounter in real life situations.

## The Game
This game is for a Python program that uses the turtle module to implement a simple game in which the player tries to find a treasure in a maze while being chased by an opponent. The player and opponent start at predetermined positions in the maze, and the treasure is randomly placed within the maze. The player can move around the maze using the arrow keys, and the opponent will try to follow the player using one search algorithm: depth-first search (DFS) or breadth-first search (BFS). The game can be reset and different search algorithms can be selected using buttons on a graphical user interface (GUI) created using the tkinter module. The game also keeps track of the scores of the player and opponent, and the game can be started or paused using another button on the GUI.

## Player
The player's goal in this game is to navigate the maze and reach the treasure before the opponent does. The player can move around the maze using the arrow keys on their keyboard, and their score is incremented each time they successfully reach the treasure. The opponent is also moving around the maze and trying to reach the treasure, and the player has to try to outmaneuver the opponent in order to reach the treasure first. It is also possible for the player to choose a search algorithm for the opponent to use, by selecting a different algorithm from the controls on the game screen. This would allow the player to see how different search algorithms perform in the maze and compare their efficiency.

## Computer
The opponent is also trying to navigate the maze and reach the treasure. The opponent's movements are determined by a search algorithm, which is specified by the player using the controls on the game screen. The opponent moves according to the chosen search algorithm, trying to find the shortest path to the treasure. The opponent's score is also incremented each time they reach the treasure. The player and the opponent both start at predetermined positions in the maze, and they move around the maze trying to reach the treasure, which is also placed at a random location in the maze. The player and the opponent move simultaneously, so the player has to try to outmaneuver the opponent and reach the treasure first in order to win the game.

###  Algorithmic search methods
####  Breadth-First Search
[Breadth-first search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.

####  Depth_First Search
[Depth-first search (DFS)](https://en.wikipedia.org/wiki/Depth-first_search) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. 

## How to Play 
To play the game, you would need to run the code that defines the MazeGUI class and create an instance of the class. This would create the game window and display the maze and game objects on the screen. You can then use the arrow keys on your keyboard to move the player around the maze, trying to reach the treasure before the opponent does. You can also use the controls on the game screen to select a different search algorithm for the opponent to use, and see how the different algorithms perform in the maze.

The player's score is incremented each time they successfully reach the treasure, and the opponent's score is incremented each time they reach the treasure. The game continues until either the player or the opponent reaches a certain number of points, at which point the game is over and a winner is declared.

You can also press the "Reset" button on the game screen to reset the game to its initial state, with the player and opponent returning to their starting positions and the treasure being placed at a new random location in the maze. This allows you to play multiple rounds of the game and try out different search algorithms.

## Future Improvemts
Below are some ways to potentially improve this game, depending on the goals and the resources you have available.

-Add more search algorithms: Currently, the game only allows the player to choose between two search algorithms (depth-first search and breadth-first search) for the opponent to use. You could add more search algorithms, such as A* search or Dijkstra's algorithm, to give the player more options and allow them to compare the performance of different algorithms in the maze.

-Improve the AI: You could also try to improve the opponent's AI by implementing more advanced search algorithms or using machine learning techniques to make the opponent's movements more strategic.

-Add more game elements: You could add more game elements, such as power-ups or obstacles, to make the game more interesting and challenging.

-Add a level system: You could add a level system to the game, with each level featuring a different maze layout and increasing in difficulty as the player progresses.

-Improve the graphics: You could also try to improve the graphics of the game, for example by using more advanced graphics libraries or by adding more visual effects to the game.

-Multiplayer support: You could also add multiplayer support to the game, allowing multiple players to play against each other online.

