import math
import pandas as pd
from PIL import Image

# def get_aspect_ratio_formatted(image_path):

#   img = Image.open(image_path)
#   width, height = img.size

#   # Ensure we don't divide by zero
#   if height == 0:
#     return "Invalid: Height cannot be zero"

#   # Calculate greatest common divisor (GCD) for clean formatting
#   gcd = math.gcd(width, height)

#   # Simplify width and height using GCD
#   width = width // gcd
#   height = height // gcd

#   # Return formatted aspect ratio
#   return f"{width}:{height}"

# image_path = "contest_foodweight/images/IMG_20191003_155933.jpg"
# aspect_ratio = get_aspect_ratio_formatted(image_path)
# print(f"The aspect ratio of {image_path} is: {aspect_ratio}")

def normalizeDatas(csv_file):
    df = pd.read_csv(csv_file)
    
    column_to_norm =  ["meat","veggie","noodle"]
    for col in column_to_norm:
        df[col+"_norm"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    
    df.to_csv(csv_file,index=False)
    
normalizeDatas("contest_foodweight/fried_noodles_dataset.csv")
    