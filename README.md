# PyColorPalette

PyColorPalette is a tool that is able to pull a list of the top colors, or the color at a specific index, from a given image. Images can be provided either through a direct path or from a URL. Along with the RGB color you have the option to also retreive the percentage of the image that specific color takes up. 

## Dependencies

PyColorPalette uses the Python Imaging Library (PIL).
To Install:
```
pip install Pillow 
```
(Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL if previosuly installed.)

## Usage

```python
from PyColorPalette import ColorPalette

pal = ColorPalette("/Users/user/Pictures/my_image.png")

print(pal.get_top_colors(n=5, ratio=False))
# [(251, 243, 230), (101, 50, 81), (59, 18, 48), (58, 17, 47), (60, 19, 49)]

print(pal.get_color(index=3, ratio=True))
# ((58, 17, 47), 0.1953125)
```

## Installation

Put "PyColorPalette" folder in your project directory.