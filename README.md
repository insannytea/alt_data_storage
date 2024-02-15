# Alternative Data Storage
A project looking into alternative ways of storing data online (currently .txt files only).

## Description
The program reads a text file, converts it into binary representation (unicode) and draws frames of black and white pixels which correspond to 0s and 1s. These are then combined to make a video which is saved into an output folder. The program can do the opposite too, converting a video file into a text file.

## Getting Started
**Prerequisites**

Libraries:
numpy
PIL
imageio
imageio\[ffmpeg\]

Optional(highly recommended):
A virtual environment of your choice

Installation:
1. Copy this repository
2. Setup your virtual environment (optional)
3. Install prerequisites
4. Store a .txt that you want to convert into *\alt_data_storage\input_data\input_text\
5. Run main.py (currently *\alt_data_storage\alt_data_storage_pack\main.py)

## Acknowledgments
[BK Binary](https://www.youtube.com/@brendancodes) has an interesting video on the subject. They are the inspiration behind this project. [Video in question](https://www.youtube.com/watch?v=_w6PCHutmb4&ab_channel=BKBinary)

## Troubleshooting
At this point in development there may be some difficulty getting the program to run on command line or other terminals, though the best way to avoid any errors is to run the program using an IDE (ex. VSCode, pycharm)