import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import os

# helper function
# convert images to numpy arrays
def pil_to_np(img): 
    return np.array(img)

# convert numpy arrays to images
def np_to_pil(arr):
    return Image.fromarray(np.uint8(arr))

# convert images to RGB
def ensure_rgb(img): 
    return img.convert("RGB") if img.mode != "RGB" else img
