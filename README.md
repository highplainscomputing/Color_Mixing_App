# Color Mixer Application

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [Keyboard Shortcuts](#keyboard-shortcuts)
## 1. Introduction

The **Color Mixer Application** is a user-friendly and interactive tool designed to facilitate the creation of custom colors by mixing pixel colors from a palette image with a blank canvas. This application is ideal for artists, designers, or anyone who wants to experiment with color blending in a creative and intuitive way.

![Demo Image](https://github.com/highplainscomputing/Color_Mixing_App/blob/main/Demo.png)
### Key Features

- Open two windows: one with a blank white canvas and another with a palette image.
- Mix colors by clicking on the palette image and applying the selected color to the canvas.
- Reset the canvas to its original white color.
- Save the mixed image for further use.

## 2. Getting Started


1. Create Virtual Environment
  ```bash
  python -m venv <your-environment-name>
  ```
  Activate
```bash
<your-environment-name>\Scripts\activate
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Clone or download the Color Mixer Application repository to your local machine.

   ```bash
   git clone https://github.com/highplainscomputing/Color_Mixing_App.git

4. Navigate to the project directory.
  
   ```bash
   cd color-mixer-app
5. Run the Application.
   ```bash
   python color_mix.py
   ```

## 3. Usage

To use the Color Mixer Application,
follow these steps:

Open a terminal or command prompt.

Navigate to the project directory.

Run the application using the following command:

   ```bash
   python color_mixer.py

```
Two windows will open: one with a blank white canvas and another with a palette image.

Click on the palette image to select a color. The selected color will be mixed with the canvas color and displayed on the canvas.

To reset the canvas to its original white color, press the "r" key.

To save the mixed image, press the "s" key. The image will be saved in the project directory.

## 4. Features
The Color Mixer Application offers the following features:

**Interactive Color Mixing**: Click on the palette image to select a color, which is then mixed with the canvas color.

**Canvas Reset**: Press the "r" key to reset the canvas to its original white color, allowing you to start a new creation.

**Image Saving**: Press the "s" key to save the mixed image to your computer for future reference or sharing.

## 5. Keyboard Shortcuts

r: Reset the canvas to its original white color.

s: Save the mixed image to your computer.
