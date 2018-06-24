# PyColorPalette

PyColorPalette is a tool that is able to pull a list of the top colors, or the color at a specific index, from a given image through the process of kmeans clustering. Images can be provided either through a direct path or from a URL. Along with the RGB color you have the option to also retreive the percentage of the image that specific color takes up. 

## Dependencies

PyColorPalette uses the Python Imaging Library (PIL) and numpy.
To Install:
```
pip install Pillow 
pip install numpy
```
(Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL if previosuly installed.)

## Usage

```python
from PyColorPalette import ColorPalette

pal = ColorPalette("/Users/user/Pictures/my_image.png")

print(pal.get_top_colors(k=5, ratio=False, rounded=True))
# [(251.0, 243.0, 230.0), (101.0, 50.0, 81.0), (59.0, 18.0, 48.0), (58.0, 17.0, 47.0), (60.0, 19.0, 49.0)]

print(pal.get_color(index=3, ratio=True, rounded=True))
# ((58.0, 17.0, 47.0), 0.1953125)
```

## Examples

![ScreenShot] (/examples/example1.jpg?raw=true)

![ScreenShot] (examples/example1.jpg?raw=true)

![Alt text] (/examples/ex_1_1.png?raw=true)
![Alt text] (/examples/ex_1_2.png?raw=true  "")
![Alt text] (/examples/ex_1_3.png?raw=true  "")
![Alt text] (/examples/ex_1_4.png?raw=true  "")
![Alt text] (/examples/ex_1_5.png?raw=true  "")
![Alt text] (/examples/example2.png?raw=true  "Example 2")
![Alt text] (/examples/ex_2_1.png?raw=true  "")
![Alt text] (/examples/ex_2_2.png?raw=true  "")
![Alt text] (/examples/ex_2_3.png?raw=true  "")
![Alt text] (/examples/example3.jpg?raw=true  "Example 3")
![Alt text] (/examples/ex_3_1.png?raw=true  "")
![Alt text] (/examples/ex_3_2.png?raw=true  "")
![Alt text] (/examples/ex_3_3.png?raw=true  "")
![Alt text] (/examples/ex_3_4.png?raw=true  "")
![Alt text] (/examples/ex_3_5.png?raw=true  "")

## Installation

Put "PyColorPalette" folder in your project directory.