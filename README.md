# PyColorPalette

PyColorPalette is a Python 3 tool capable of pulling a list of the top colors, or the color at a specific index, from a given image through the process of K-means clustering. Images can be provided either through a direct path or from a URL. Along with the RGB/Hex color value, you have the option to also retreive the percentage of the image that specific color takes up. 

_**See examples below!**_

## Usage

PyColorPalette derives a color palette using K-means clustering to create a cluster map. To see the cluster map use ```show_clustering=True```. (Thank you, ZeevG)

```python
from PyColorPalette import ColorPalette

pal = ColorPalette(r"/Users/user/Pictures/my_image.png", show_clustering=False)
#Use a raw string for Windows paths.

print(pal.get_top_colors(n=5, ratio=False, rounded=True))
# [(251, 243, 230), (101, 50, 81), (59, 18, 48), (58, 17, 47), (60, 19, 49)]

print(pal.get_color(index=3, ratio=True, rounded=True))
# ((58, 17, 47), 14)

'''
Retrieve values in hex.
'''
print(pal.get_color(index=3, ratio=True, to_hex=True, rounded=False))
# ('#3a112f', 14.1953125)
```

## Examples

![Alt text](/examples/example1.jpg)
![Alt text](/examples/ex_1_1.png?raw=true  "")
![Alt text](/examples/ex_1_2.png?raw=true  "")
![Alt text](/examples/ex_1_3.png?raw=true  "")
![Alt text](/examples/ex_1_4.png?raw=true  "")
![Alt text](/examples/ex_1_5.png?raw=true  "")

![Alt text](/examples/example3.jpg)
![Alt text](/examples/ex_3_1.png?raw=true  "")
![Alt text](/examples/ex_3_2.png?raw=true  "")
![Alt text](/examples/ex_3_3.png?raw=true  "")
![Alt text](/examples/ex_3_4.png?raw=true  "")
![Alt text](/examples/ex_3_5.png?raw=true  "")

![Alt text](/examples/example2.png)
![Alt text](/examples/ex_2_1.png?raw=true  "")
![Alt text](/examples/ex_2_2.png?raw=true  "")
![Alt text](/examples/ex_2_3.png?raw=true  "")

## Dependencies

PyColorPalette uses the Python Imaging Library (PIL) and numpy.
To Install:
```
pip install Pillow 
pip install numpy
```
(Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL if previosuly installed.)

## Installation

```pip install PyColorPalette```