## Space Attackers
This repository houses a Space Invaders clone using the modules and game
development tools provided by the pygame library. The goal of the game is
to kill as many aliens as possible without dying (get the highest score),
which requires aim using movement of the player's spaceship.

# Installation and setup

Running the game uses pygame, which can be installed by running `$ pip install pygame`.
The other required dependency is the `random` library. To install it run `$ pip install random`.
With those fulfilled, you should be able to download our code, locate to the space_attackers
folder as a directory, and run `$ python main_class.py`.

# GAME

![game](assets/mass-123.png)

Upon running the game, it should give a black screen and a prompt in the terminal asking you
to select the level. Please type in either of the options given: `easy`, `medium`, or `hard`,
and it should start an instance of the game. Use the arrow keys to move your ship, and the
spacebar to shoot, and as soon as you kill your first enemy in the swarm, the game will begin.
