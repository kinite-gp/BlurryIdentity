# BlurryIdentity
 Crystallize your identity on the webcam

![GitHub User's stars](https://img.shields.io/github/stars/kinite-gp%2FBlurryIdentity?style=for-the-badge&logo=star)
![Static Badge](https://img.shields.io/badge/Language-python-gold?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Library-opencv_%26_pyvirtualcam-green?style=for-the-badge)


## Demo
<img width='50%' src="https://github.com/kinite-gp/BlurryIdentity/blob/main/res/gif.gif?raw=true" alt="Camera Preview"/>

## run


- run without argument ```python blurry_identity.py```
- run with preview ```python blurry_identity.py --preview```
- run with custom text ```python blurry_identity.py --text "kinite_gp"```
- run without text ```python blurry_identity.py --dont-show-text```

> After running you will have a "OBS Virtual Camera" in obs

<img width='50%' src="https://github.com/kinite-gp/BlurryIdentity/blob/main/res/obs.png?raw=true" alt="OBS Video Capture Device"/>

> To exit, just press Ctrl+C 

## install requirements
- install opencv with ```pip install opencv-python```
- install pyvirtualcam with ```pip install pyvirtualcam```


## You can change the following values in the program

```python
fps = 15 # Change if quantity is low or you need
camera_index = 0 # Change if your camera has a different index
scale_factor = 1.2 # Change if you don't like the default sensitivity value
padding = 30 # Change if you want to increase or decrease the crystal window size
blur_value = (99,11) # Change if you want more or less crystal amount
frame_text = "blured face" # Change the default face text value
frame_title = 'Camera Preview' # Change the default value of the preview window
```

