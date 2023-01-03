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
Once the game loads, identify the shortest route possible, and use keyboard direction keys (up, down, left, right) to move the player to reach the target's location before the computer does, otherwise you lose the game. The winner gains 1 point upon winning the game and loses 1 point when they lose the game.

## Demo
Below is a sample of the game
