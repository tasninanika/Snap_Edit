import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import os

# helper function
# convert image to numpy array
def pil_to_np(img): 
    return np.array(img)