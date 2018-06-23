from PIL import Image
import re
import urllib.request
import io

class ColorPalette():

    def __init__(self, path):
        self.path = path
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', path)
        if not urls:
            self.__is_url = False    
        else:
            self.__is_url = True

        self.__color_palette()

    def __color_palette(self):
        if self.__is_url:
            with urllib.request.urlopen(self.path) as url:
                f = io.BytesIO(url.read())
            im = Image.open(f).convert('RGB')
        else:
            im = Image.open(self.path).convert('RGB')
        
        pixels = im.load()
        width, height = im.size
        
        pixel_dict = dict()

        _total_pixels = 0 
        for col in range(width):
            for row in range(height):
                _total_pixels += 1
                cpixel = pixels[col, row]
                if cpixel in pixel_dict:
                    pixel_dict[cpixel] = pixel_dict[cpixel] + 1
                else:
                    pixel_dict[cpixel] = 1
        
        sorted_tups = [(k, float(pixel_dict[k]/_total_pixels) * 100) for k in sorted(pixel_dict, key=pixel_dict.get, reverse=True)]

        self.sorted_tups = sorted_tups
        self._total_pixels = _total_pixels
        self.dict = pixel_dict

    def get_top_colors(self, n=5, ratio=False):
        if n > len(self.sorted_tups):
            raise ValueError("Too many values requested\nMax colors: {}".format(str(len(self.sorted_tups))))
        
        if not ratio:
            return [color[0] for color in self.sorted_tups[:n]]
        else:
            return [color for color in self.sorted_tups[:n]]

    def get_color(self, index, ratio=False):
        if index > len(self.sorted_tups):
            raise ValueError("Index too high\nMax index: {}".format(str(len(self.sorted_tups))))

        if not ratio:
            return self.sorted_tups[index][0]
        else:
            return self.sorted_tups[index]
        