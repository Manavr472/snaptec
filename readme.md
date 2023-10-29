# SnapTEC - Snap and Detect Faces!

SnapTEC is a simple yet powerful application that allows you to capture images and detect faces in them. Whether you want to automate attendance tracking or simply have fun with face recognition, SnapTEC has you covered.

## Installation

### Step 1: Clone the Repository

First, clone the SnapTEC repository into your local machine:

```bash
git clone <repository_url>
```

### Step 2: Prepare Training Images

Create a new folder named 'Training_images' in your SnapTEC directory. This is where you'll store images of individuals you want to recognize. Label these images with the individual's name, for example, "Manav.jpg".

### Step 3: Install Requirements

Install the necessary Python packages by running the following command in your terminal (make sure you're in the SnapTEC directory):

```bash
pip install -r requirements.txt
```

This might take a little time, so feel free to make yourself a coffee!

### Step 4: Run the Face Encoding Script

Now, it's time to generate encodings of the faces from the 'Training_images'. Run all the code blocks in "face.ipynb". After running this file, a new file named 'encoded_faces.pkl' will be automatically added to your folder. This file stores the facial data and will be used for face detection.

### Step 5: Launch the SnapTEC Web App

In your terminal, run the following command:

```bash
python -m streamlit run app.py
```

This will launch a local web application that allows you to upload images and detect faces in them.

## Usage

- Visit the provided local web address in your browser.
- Upload an image.
- Click the "Show Attendance" button to detect faces.
- Watch as SnapTEC identifies faces and marks attendance.
- Explore the output, which includes a CSV file with attendance records.

Enjoy using SnapTEC for various applications, from tracking attendance to having fun with face recognition!

Happy snapping! 📸👤