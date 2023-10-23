
Interactive Tic-Tac-Toe Game with MySQL Integration
===


## Introduction
This Python project is a 2-player interactive Tic-Tac-Toe game implemented using Pygame, with results (username, wins, draws, and losses) stored in a MySQL database. The game allows two players to enjoy a classic Tic-Tac-Toe experience while keeping track of their performance.

## Technologies Used
- Pygame
- MySQL


## Game Features
- Interactive game interface
- Two-player gameplay
- Classic Tic-Tac-Toe rules
- Results stored on a database

## Implementation
#### Project Structure
The project is organized into multiple Python modules.
Key modules include:
- TTTdef.py: Contains functions for managing the game board and its display.
- TTTpygame.py: Manages Pygame-related functions for graphics and user interactions.
- TTTmysql.py: Handles interactions with a MySQL database to store user scores.
The main game loop and menu system are implemented in separate modules.

## User Manual
#### Initialization
Download Python, MySQL, and PyGame modules.
In MySQL Command Line, run the following commands : 
```
create database TTT;
use TTT;
create table TTT_scores(username varchar(255) UNIQUE NOT NULL, wins int NOT NULL,  draws int NOT NULL, losses int NOT NULL);
```
Keep all the code files in a single folder and make sure to change pwd variable in `TTTmysql.py` to your MySQL database password.

#### Starting the Game
To start the game, run `TTTmenu.py`
The main menu will be displayed, offering the following options:
- Play Game: Click this to start a new game.
- Check User: Use this option to check your game statistics by entering your username.
- Top Scores: View the top 5 players with the most wins.

Click on the desired option using your mouse.


## Future Enhancements
- Implement an AI opponent for single-player mode.
- Enhance the user interface for a more visually appealing experience.
- Make the game smoother and more user-friendly


## References
- [Pygame documentation](https://pygame.readthedocs.io/en/latest/)
- [MySQL documentation](https://dev.mysql.com/doc/)

## Results

| <img src="https://github.com/ShantanuRenghe/2-Player-TicTacToe-using-RDBMS/assets/128238705/17852f14-36ce-43b6-ae4b-719516d3c9ff" width="width_of_img" height="height" /> | <img src="https://github.com/ShantanuRenghe/2-Player-TicTacToe-using-RDBMS/assets/128238705/0cfbf416-9daa-41f7-b981-d27da8f7b468" width="width_of_img2" height="height2" /> |
| :--: | :--: |
| Menu | Game |
