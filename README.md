# Pygame Workshop

## Workshop Overview
Welcome to the Pygame workshop! In this 1.5-hour session, you'll learn to build 2D games using Python and Pygame.

By the end of the workshop, you'll:
- Understand basic game loops, events, and collision detection
- Build a simple game like **Flappy Bird**
- Gain the skills to create your own 2D games!


## Getting Started
1. Install **Python 3.12** from [here](https://www.python.org/downloads/).
2. Download **Jetbrains PyCharm** IDE from [here](https://www.jetbrains.com/pycharm/download/) or using Jetbrains Toolbox.
3. Install the IDE.
4. Open the IDE and get the **student license** from [here](https://www.jetbrains.com/community/education/#students).
5. Click on "Code" in the GitHub Repository and **copy the ssh link** (if you have an ssh-key pair for GitHub) or **download the zip file**.
6. If you copied the link and have an ssh-key open Pycharm and use the "Get from Version Control" option to **clone the repository**. If you downloaded the zip file, extract it and **open the folder in Pycharm**.
7. Create a **new virtual environment** by clicking in the bottom right corner of the IDE and selecting "Add New Interpreter", then "Add Local Interpreter..."
8. Now a new window is opened where you can create a Virtualenv Environment. You only need to select the **base interpreter** (Python 3.12) and click on "OK". 
9. Now **open the terminal** in python, which can be found in the bottom left corner of the IDE.
10. In the terminal, type the following command to **install the required packages**:
```bash
pip install -r requirements.txt
```

## Files Overview
- ```base_template.py``` – A minimal game template with movement, collisions, and FPS control. Use it to build your own games.
- ```flappy_bird.py``` – A working version of Flappy Bird. It includes gravity, moving upwards, obstacles, and a timer.

## Game Ideas to Build
Here are some game ideas to create during the workshop:
1. Flappy Bird – Fly and avoid obstacles (code provided)
2. Doodle Jump – Jump between platforms and avoid falling
3. Dodge the Blocks – Move to avoid falling blocks
4. Snake Game – Classic snake game with growing tail
5. Tetris – Classic Tetris game with falling blocks

## Hints
### How to connect to GitHub with SSH
Check out the instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
### Where to find the python interpreter to create the virtual environment
#### Windows:
usually the python interpreter is located in the following path:
```angular2html
C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python312\python.exe
```
or
```angular2html
C:\Benutzer\<IhrBenutzername>\AppData\Local\Programs\Python\Python312\python.exe
```

#### macOS:
Use the terminal to find the path of the python interpreter:
```bash
which python3.12
```
It is usually located in:
```angular2html
/usr/local/bin/python3.12
```

#### Linux:
Use the terminal to find the path of the python interpreter:
```bash
which python3.12
```
It is usually located in:
```angular2html
/usr/bin/python3.12
```