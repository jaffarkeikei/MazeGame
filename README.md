# Maze Game

## Table of Contents
- [Inspiration](#inspiration)
- [The Game](#the-game)
- [Player](#player)
- [Computer](#computer)
  - [Algorithmic Search Methods](#algorithmic-search-methods)
    - [Breadth-First Search](#breadth-first-search)
    - [Depth-First Search](#depth-first-search)
- [How to Play](#how-to-play)
- [Future Improvements](#future-improvements)

## Inspiration
This game draws inspiration from the renowned graph traversal techniques: breadth-first search and depth-first search. Proficiency in these algorithms can empower you to solve a majority of tree and graph problems in real-life situations.

## The Game
The game is a Python program that employs the turtle module to create an interactive maze game. The player's objective is to find a treasure in the maze while being pursued by an opponent. Key features of the game include:
- Player and opponent starting at predetermined positions
- Random placement of the treasure within the maze
- Player navigation using arrow keys
- Opponent following player using search algorithms
- Graphical User Interface (GUI) with controls for reset and algorithm selection
- Scoring for both player and opponent

## Player
The player aims to navigate the maze and reach the treasure before the opponent. Use arrow keys for movement and earn points by successfully reaching the treasure.

## Computer
The opponent uses search algorithms to reach the treasure. Algorithm options are available for the player to choose from, providing an opportunity to compare different search strategies.

### Algorithmic Search Methods
#### Breadth-First Search
- [Breadth-first search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search) explores nodes at the present depth level before moving to the next depth level.

#### Depth-First Search
- [Depth-first search (DFS)](https://en.wikipedia.org/wiki/Depth-first_search) explores nodes as far as possible along each branch before backtracking.

## How to Play
1. Run the code to instantiate the MazeGUI class.
2. Use arrow keys to navigate the player through the maze.
3. Select opponent search algorithm using controls.
4. Earn points by reaching the treasure before the opponent.
5. Reset the game or change algorithms as desired.

## Future Improvements
- Expand available search algorithms (e.g., A* search, Dijkstra's algorithm).
- Enhance opponent's AI with advanced search or machine learning techniques.
- Introduce power-ups or obstacles for added complexity.
- Implement a level system with increasing difficulty.
- Improve graphics and visual effects.
- Add multiplayer support for online gameplay.

Thank you for checking out!!
