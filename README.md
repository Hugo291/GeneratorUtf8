# Image UTF 8 Generator

This program is useful for creating an image with multiple char. It's usable for OCR learning (like, Tesseract-OCR, open-CV, etc...).

It's possible to return a dict of characters generated. In this dict, the key is the character and the value is a list of all position of characters.

In this example , the generation is between 103 and 105. 
You find in this link all value 

### Example 
```python
from  generator import draw

dict = draw(103, 105)

dict = {
    'g': [(32, 0), (73, 0), (114, 0)], 
    'h': [(32, 70), (73, 70), (114,70)],
    'i': [(32, 140), (73, 140), (114, 140)]
}
```

If debug is active you will know each generation step.

In Output your find a file 'PNG' that contains all character generated. A output example is available above

#### Example 

<img src="https://github.com/Hugo291/Image-Char-UTF-8-Generator/blob/master/image.png" alt="Image Example">

A documentation of this class is available <a href=#>here</a>.

