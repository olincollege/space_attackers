# Introduction
This is the repository hosting the game 'Space Attackers' by Gibson and Conan.

The goal of 'Space Attackers' was to create a Space Invaders clone using the modules
and game development tools provided by the pygame library. We chose to make a
game in the Arcade Space Shooter genre, as we thought that it would not be as
often-chosen as something like a platformer or isometric RPG, and we were fans
of the aesthetic associated with games in the genre.

# Preview
![Gif_Space_Trim](https://user-images.githubusercontent.com/50885520/117381100-411c1e80-aea9-11eb-87a5-0caea49eb165.gif)

# [Link to our GitHub Repository](https://github.com/olincollege/space_attackers)

# [Download Link for our Game](https://github.com/olincollege/space_attackers/archive/refs/heads/main.zip)

# Installation and Setup

Running the game uses pygame, which can be installed by running `$ pip install pygame`.
The other required dependency is the `random` library. To install it run `$ pip install random`.
With those fulfilled, you should be able to download our code, locate to the space_attackers
folder as a directory, and run `$ python main_class.py`.

# Game

Upon running the game, it should give a black screen and a prompt in the terminal
asking you to select the level of difficulty. Please type in either of the options
given: `easy`, `medium`, or `hard`, and it should start an instance of the game.
Use the arrow keys to move your ship, and the spacebar to shoot, and as soon as you
kill your first enemy in the swarm, the game will begin.

# File Structure
Our file structure consists of five major files and flaticon assets.
* `mainClass.py` : This file runs the game
* `player.py`   :This file contains the player Class
* `score.py`    : This file contains the score Class 
* `spaceship.py`: This file contains the spaceship Class
* `enemy.py`    : This file contains the enemy Class
* assets      : This folder contains all the assets in the game

# Assets
All our assets were drawn from [flaticon](https://www.flaticon.com/).

Spaceship Asset:
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
Alien Asset:
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
Bullet Asset:
<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
