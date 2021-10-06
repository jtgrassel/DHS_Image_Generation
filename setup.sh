# Setup the virtual environment
#virtualenv -p $(which python3) .venv
#source .venv/bin/activate
#pip install - requirements.txt

# Download the MPEG7 dataset
curl -o MPEG7.zip https://dabi.temple.edu/external/shape/MPEG7/MPEG7dataset.zip
unzip MPEG7.zip && mv original MPEG7 && rm MPEG7.zip

#Remove unwanted files from MPEG7 download
rm MPEG7/confusions.eps && rm MPEG7/confusions.fig && rm MPEG7/confusions.gif
rm MPEG7/rat-09.gif && rm MPEG7/shapedata.eps && rm MPEG7/shapedata.fig && rm MPEG7/shapedata.gif

# Create directory for generated images
mkdir Output_Images
mkdir Output_Images/Positive
mkdir Output_Images/Negative
mkdir Output_Images/White
