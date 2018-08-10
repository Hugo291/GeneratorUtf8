# GeneratorUtf8

This program is useful for creating an image with multiple char. It's usable for OCR learning (like, Tesseract-OCR, open-CV, etc...).

It's possible to return a dict of characters generated.
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
