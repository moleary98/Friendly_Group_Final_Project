from PIL import Image, ImageFilter, ImageDraw, ImageFont
import numpy as np
import pandas as pd
import json


# Function for decrypting location 
def decrypt_location(json_file, key):
    
    with open(json_file, 'r') as f:
        # Load the JSON data
        data = json.load(f)

    # Check if the key exists in the JSON data
    if key in data:
        # If the key exists this prints the corresponding values
        values = data[key]
        
    
    with open('english.txt', 'r') as t:
        lines = t.readlines()
    for index in values:
        word = lines[int(index) - 1].strip()
        print(word)
        
# Function for image processing
def display_image(file_path):
   img = Image.open(file_path)
   img.show()
    
    
    
        
        
  
