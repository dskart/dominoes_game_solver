# Dominoes game Solver

This is the code of an AI for a dominoes game in which two players take turns placing 1×2 dominoes on a rectangular grid. One player must always place his dominoes vertically, and the other must always place his dominoes horizontally. The last player who successfully places a domino on the board wins.

This was done as an exercise to implement a Minimax search algorithm with Alpha-Beta pruning from scratch and use it in a game. So please take in account that this code was written in a few days without any professional review/standard.

## Getting Started

The game AI is written inside the ["dominoes_game.py"](dominoes_game.py) file.

The other file ["dominoes_game_gui.py"](dominoes_game_gui.py) contains the game logic and a gui for the use to test the AI and/or plaly against it.

### Prerequisites

- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [Numpy](https://numpy.org/)

## Running the game

The following command will launch the gui for you to play the game and interact with the AI.

```[python]
python3 dominoes_game_gui.py rows cols
```

The arguments rows and cols are positive integers designating the size of the board.

## Authors

- **Raphael Van Hoffelen** - [github](https://github.com/dskart) - [website](https://www.raphaelvanhoffelen.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
