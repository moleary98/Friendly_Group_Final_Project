# Name: Max O'Leary, Zack Mcquade, Kevin Duritsch
# email: olearymw@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that we can decrypt text files using Python
# Citations:
# Anything else that's relevant:  Thanks for a great semester!

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
    
    
    
        
        
  
