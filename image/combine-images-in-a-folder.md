# combine images in a folder


## 1. natural sort


```
import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)
```


## 2.combine image

```
from PIL import Image

def combine_images(columns, images, space = 0, name = 'image.png' ):
	rows = len(images) // columns
	if len(images) % columns:
		rows += 1
	width_max = max([Image.open(image).width for image in images])
	height_max = max([Image.open(image).height for image in images])
	background_width = width_max*columns + (space*columns)-space
	background_height = height_max*rows + (space*rows)-space
	background = Image.new('RGBA', (background_width, background_height), (255, 255, 255, 255))
	x = 0
	y = 0
	for i, image in enumerate(images):
		img = Image.open(image)
		x_offset = int((width_max-img.width)/2)
		y_offset = int((height_max-img.height)/2)
		background.paste(img, (x+x_offset, y+y_offset))
		x += width_max + space
		if (i+1) % columns == 0:
			y += height_max + space
			x = 0	
	background.save(name)

```


## 3. get all images from one directory

```
fp_in = "figs/*.png"
    
images = natural_sort(glob.glob(fp_in))
```

use the functions above to combine images


ref:

- [Is there a built in function for string natural sort?](https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort)
- [How to combine several images to one image in a Grid structure in Python?](https://stackoverflow.com/questions/72723928/how-to-combine-several-images-to-one-image-in-a-grid-structure-in-python)
- [Importing images from a directory (Python) to list or dictionary](https://stackoverflow.com/questions/26392336/importing-images-from-a-directory-python-to-list-or-dictionary)