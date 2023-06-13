# Smooth Mouse Mover

Python script that allows to control the mouse smoothly and provides methods for moving the mouse to specific coordinates, as well as moving the mouse relative to its current position.

I thank all people who use this for their project. I love to contribute to the community. However, please credit me by using the GitHub project link.

## Usage

To use this, you need Python 3.6+ and all of the required packages installed.
To install the required packages, run: 
<br>`pip3 install keyboard pynput` or `pip3 install requirements.txt`

### Importing the script
1. Place `mousemover.py` and `config.json` into your directory
2. Import the `MouseMover` class like this: `from mousemover import MouseMover`

### Move the mouse to a specified position
1. Import the script following the steps above
2. Creating a new instance of the class `MouseMover`: `mover = MouseMover()`
3. Use the `mover.move_to(x, y, duration_of_movement)` function to move the mouse to the specified position

I provided an [example script](https://github.com/markrzv/Smoth-Mouse-Mover/blob/main/examplescript.py).

### Move the mouse relativly to its current position
1. Import the script following the steps above
2. Creating a new instance of the class `MouseMover`: `mover = MouseMover()`
3. Use the `mover.rel_move(dx, dy, duration_of_movement)` relativly to its current position

I provided an [example script](https://github.com/markrzv/Smoth-Mouse-Mover/blob/main/examplescript.py).

### Changing the keybind to terminate the script
The user has the possibility to exit the script at any time by pressing a key on the keyboard. This key is specified in config.json.
1. Open the config.json file
2. Change the value of "keybind" to the new key

<br> If you don't want to have a key that terminates the script, set the string `"none"` as the value.
<br> In case the location or name of the JSON file is changed, an adjustment for finding the JSON file must be made in the `_terminate()` function

## Aditional methods

-  `mover.get_mouse_position()`
-  `mover.set_mouse_position(x, y)`
