# DHS_Image_Generation

# Generating an Image
To generate an image using this code 4 things are required:
1. Python libraries
2. Setting up directories
3. Making a json image parameters file
4. Running the "json_image_gen.py" code

### 1. Python libraries
The only library that should require installation outside of the python packages is the Pillow library (a fork of PIL).This library is used to do most of the image processing. Use the following command to install this library:

```python
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
The other libraries required are listed below:
```python
os
math
random
json
```

### 2. Setting up directories
Three folders will need to be created. For convenience, these folders can be subfolders of the folder that contains the python code.

1. The first will be where the MPEG7 images are stored. All the images should retain their original names.

2. The second will be used to hold the json files that will be used to generate images. 

3. The third will be used to hold the generated images and the additional metadata.

### 3. Making a json image parameters file







# Programs Key

# Setting the Image Parameters
The code generates an image based on the parameters set in the JSON files.
In the home folder of this project there is a "template.json" that is an example of a working set of parameters used to generate an image.

The following sections will be used to explain how to change the parameters used in a JSON file.

1. `save_dir`
    This is input will dictate where the generated image will be saved. This can be either an absolute or relative path. See two examples below.

    ```json
    "save_dir": "C:/Users/Joshua/Documents/DHS Project/Image_Output/"
    ```
    ```json
    "save_dir": "/Image_Ouput/"
    ```
2. `save_name`
    This input will be the text that is used to name the output files.
    When run three files will be generated.

    1. The image using the input parameters named "<save_name>.png"
    2. Another version of the image that makes the specified find image white named "<save_name>-find.png"
    3. A .json file that contains the input parameters and additional metadata named "<save_name>.json"

3. `background`
    This section includes 3 inputs. The color, length, and height of the background image. A valid entry will be formatted as follows:

    ```json
        "background": {
            "color": "beige",
            "width": 1080,
            "height": 1080
        }
    ```