import streamlit as st
import cv2
import face_recognition
from datetime import datetime
from PIL import Image
import io
import os
import numpy as np
import pandas as pd
import joblib

# Load the saved model (PKL file) for face encoding
model = joblib.load('encoded_faces.pkl')


path = 'Training_images'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

# Create or load an attendance CSV file
attendance_file = 'attendance.csv'
def mark_attendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')

        # Check if the name is not in the list and mark attendance
        if name not in nameList:
            f.writelines(f'\n{name},{dtString}')
# Streamlit UI
st.title("Face Recognition Attendance System")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Check if an image has been uploaded
if uploaded_image is not None:
    # Read the uploaded image data
    image_data = uploaded_image.read()
    pil_image = Image.open(io.BytesIO(image_data))
    # Convert the PIL Image to a NumPy array
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2RGB)

if st.button("Show Attendance"):
    facesCurFrame = face_recognition.face_locations(image, model='cnn')
    encodesCurFrame = face_recognition.face_encodings(image, facesCurFrame)

    for faceLoc in facesCurFrame:
            y1, x2, y2, x1 = faceLoc
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(model, encodeFace)
            faceDis = face_recognition.face_distance(model, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                mark_attendance(name)

    st.success("Attendance marked successfully!")
    st.image(image, channels="BGR")
    df = pd.read_csv(attendance_file)
    st.write(df)
    
    csv_file = df.to_csv(index=False)
    st.download_button(
    label="Download CSV",
    data=csv_file,
    key="csv_download",
    file_name="attendance.csv",
    )
