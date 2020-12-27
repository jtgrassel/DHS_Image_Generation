# DHS_Image_Generation

# Generating an Image
To generate an image using this code 4 steps are required:

    I. Python libraries
    II. Directories
    III. Making a json image parameters file
    IV. Running the "json_image_gen.py" code


### I. Python libraries
The only library that should require installation outside of the default python packages is the Pillow library (a fork of PIL). This library is used to do most of the image processing. Use the following commands to install this library:

For installing:
```python
pip install pip
pip install Pillow
```

For upgrading if previously installed:
```python
pip install --upgrade pip
pip install --upgrade Pillow
```
The other libraries required are listed below:
```python
os
math
random
json
```

### II. Directories
This cloned repository has the directories by default set up, however the important ones are explained here. The default folders are all subfolders of the folder containing the code.

3 Directories are required.

1. MPEG7 folder (Default: "MPEG7/") - This folder should contain all the MPEG7 images in their original downloaded format. The dataset can be dowloaded from the following link: http://www.timeseriesclassification.com/description.php?Dataset=ShapesAll

2. JSON input folder (Default: "Input_JSON/") - This will be the folder that contains the JSON files containing the parameters for all the images you wish to generate. The JSON files will be further explained in the next section.

3. Image/Metadata output folder - (Default: "Output_Images/") This will be the folder that the generated images along the the generated metatdata will be output to.

### III. Making a json image parameters file
The code generates an image based on the parameters set in the JSON files.
In the home folder of this project there is a "template.json" that is an example of a working set of parameters used to generate an image.

The following sections will be used to explain how to change the parameters used in a JSON file.

1. `save_dir`
    This is input will dictate where the generated image will be saved. This can be either an absolute or relative path. See two examples below. The first is the default.
    ```json
    "save_dir": "Image_Ouput/"
    ```
    ```json
    "save_dir": "C:/Users/Joshua/Documents/DHS Project/Image_Output/"
    ```
2. `save_name`
    This input will be the text that is used to name the output files.
    When run three files will be generated.

    1. The image using the input parameters named *"<save_name>.png"*
    2. Another version of the image that makes the specified find image white named *"<save_name>-find.png"*
    3. A .json file that contains the input parameters and additional metadata named *"<save_name>.json"*

3. `background` This section includes 3 inputs. The color, length, and height of the background image. A valid entry will be formatted as follows:
    ```json
    "background": {
        "color": "beige",
        "width": 1080,
        "height": 1080
    }
    ```
    Currently the color is stated by name. In the future this will be updated to an RGB input. The color can currently be set to any of the colors show on the following website: https://www.w3schools.com/colors/colors_names.asp

4. `scale` The scale determines the size that the shapes will generated. The measure is a proportion of the height dimension of the background. For example, if the background is 500x1000 (WxH) and the scale of a shape is 0.25, then the shape will be generated at a 250x250 size. This parameter has two parts. The first is the distribution that will guide the random sampling and the second is the distribution parameters. Currently the triangular and uniform distributions are supported. See two examples below:

    ```json
    "scale": {
            "dist": "T",
            "params": [0.15, 0.2, 0.25]
    }
    ```
    The triangular distribution has parameters set up as [Lower Bound, Peak, Upper Bound].

    ```json
    "scale": {
            "dist": "U", 
            "params": [0.2, 0.3]
    }
    ```
    The uniform distribution has the paramters set as [Lower Bound, Upper Bound]

5. `rotation` The rotation determines what angle of rotation a shape has from the original image. This parameter has the same inputs as the scale. See two examples below:

    ```json
    "rotation": {
            "dist": "U",
            "params": [0, 365]
    }
    ```
    ```json
    "rotation": {
            "dist": "T",
            "params": [-15, 0, 15]
    }
    ```

6. `color` The color input determines the color each shape will be generated as. There are 3 distributions available for this parameter. Uniform, triangular, and mode. Each will be explained below.

    #### Triangular
    

