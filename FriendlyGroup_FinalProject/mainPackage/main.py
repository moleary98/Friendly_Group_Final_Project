# Name: Max O'Leary, Zack Mcquade, Kevin Duritsch
# email: olearymw@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that we can decrypt text files using Python
# Citations:
# Anything else that's relevant:  Thanks for a great semester!

from functionsPackage.functions import *
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import numpy as np
import pandas as pd
import json



solution = decrypt_location('EncryptedGroupHints Spring 2023 Section 002.json', 'Friendly Group')
print(solution)

display_image('friendly_group.jpg')





