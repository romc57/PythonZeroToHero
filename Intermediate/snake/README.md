# Snake (Turtle)

A simple Snake game built with Python's `turtle` module.

## Requirements
- Python 3.12+ (tested)
- No external dependencies

## Run
```bash
python Intermediate/snake/main.py
```

## Controls
- Arrow keys: Move snake (Up/Down/Left/Right)
- R: Restart after Game Over
- Q: Quit at any time

## Gameplay
- Eat red food to grow and increase score
- Avoid hitting the walls or your own body
- Score is shown at the top

## Notes
- The game uses a timer-driven loop (`ontimer`) for smoother updates
- Food spawns on a 20px grid within safe bounds

## Files
- `main.py`: Entry point
- `Game.py`: Game loop, input handling, collisions
- `SnakeObj.py`: Snake segments, movement, growth
- `Food.py`: Food spawning
- `Scoreboard.py`: Score display and controls hint
