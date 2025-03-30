
# app.py
import cv2
import numpy as np
from model import load_model, apply_ghibli_style

def main():
    model = load_model("models/animeganv2")
    input_path = "input.jpg"
    output_path = "output.jpg"
    
    image = cv2.imread(input_path)
    stylized_image = apply_ghibli_style(model, image)
    cv2.imwrite(output_path, stylized_image)
    print(f"Saved Ghibli-style image at: {output_path}")

if __name__ == "__main__":
    main()

