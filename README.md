# gameoflife

A simple Python implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using Pygame.

As per the Wikipedia article, the following rules are applied to the game:

- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Controls

- A generation occurs every game frame. To increase the frames and generations per second, press the period [.] key on your keyboard. The comma key [,] can be used to decrease the FPS/GPS. There is a minimum value of 1.

- Press [r] to reset with a new random seed.

## Seed

The seed is the randomly decided starting state. During initialization, all positions are either set to alive or dead through a random choice (20% chance of it being alive.) To change this, edit line 31.

The game is a 1000x1000 window. If you want to change this edit line 60. Although you will also need to update both the populate and generation functions (loops should be range of 0 to (height or width / 10) + 1)
