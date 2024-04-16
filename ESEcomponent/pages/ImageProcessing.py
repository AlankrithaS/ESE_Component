import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

st.subheader("Image Processing")

image = cv2.imread("image2.jpg", 1)

gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Define the rotation angle and the scaling factor
angle = 45
scale_factor = 1.0

# Get the image dimensions
(h, w) = image.shape[:2]

# Get the center point for rotation
center = (w // 2, h // 2)

# Create an affine transformation matrix for rotation
M = cv2.getRotationMatrix2D(center, angle, scale_factor)

# Apply the affine transformation matrix to rotate the image
rotated_image = cv2.warpAffine(image, M, (w, h))

# Load the grayscale image
gray_image = cv2.imread('image2.jpg')

# Define the coordinates for the top-left corner of the ROI
top_left_x = 0
top_left_y = 0

# Define the dimensions of the ROI
roi_width = 200
roi_height = 200

# Crop the grayscale image to the specified ROI
cropped_image = gray_image[top_left_y:top_left_y + roi_height, top_left_x:top_left_x + roi_width]

st.subheader('Original Image')
st.image(image)

st.subheader('Resized Image')
st.image(gray_image1)

st.subheader('Cropped Image')
st.image(cropped_image)

st.subheader('Rotated Image')
st.image(rotated_image)

st.subheader('Gray Image')
st.image(gray_image)