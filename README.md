# Image UTF 8 Generator

This program is useful for creating an image with multiple char. It's usable for OCR learning (like, Tesseract-OCR, open-CV, etc...).

It's possible to return a dict of characters generated. In this dict, the key is the character and the value is a list of all position of characters.

In this above extract , charactrers "A","B" with diferent positions in values.

```python
dict = { 'a' : [
                     [0,1] , 
                     [0,2] ,
                     [0,3] 
                 ] ,
         'b' : [
                     [1,1] , 
                     [2,2] ,
                     [3,3] 
               ]
      }
```

If debug is active you will learn about every generation step.
