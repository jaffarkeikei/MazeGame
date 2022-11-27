# Maze Game
## Inspiration
This game gets inspiration from the reknowned graph traversal techniques: breath-first search and depth-first search. I am utterly intrigued by these two graph traversal methods. Theoretically, it is believed that two thirds of graph interview questions can be solved using these two techniques. Consequently, proficiency in these two algorithms will allow you to solve at least two-thirds of tree and graph problems that you may encounter in real life situations.

## The Game
The game is composed of two players; the computer and the user.

## Player
The player, represented by a green tile, is moved by the user with an aim of reaching the target's location before the computer does. The player moves to the end of a line with a single keyboard press. The movement is limited to straight lines: vertically or horizontally.

## Computer
Computer, which is the opponent, initializes at the centre of the game window. It plays the game using tree traversal methods to get to the target location. The computer makes any possible number of moves based on the algorithm it uses before finding the target.

###  Algorithmic search methods
####  Breadth-First Search
[Breadth-first search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.

####  Depth_First Search
[Depth-first search (DFS)](https://en.wikipedia.org/wiki/Depth-first_search)is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. 

## How to Play 
Once the game loads, identify the shortest route possible, and use keyboard direction keys (up, down, left, right) to move the player to reach the target's location before the computer does, otherwise you lose the game. The winner gains 1 point upon winnig the game and loses 1 point when they lose the game.

## Demo
Below is a sample of the game
