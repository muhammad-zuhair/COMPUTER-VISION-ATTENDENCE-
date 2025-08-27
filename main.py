#import tkinter as tk
#from tkinter import ttk, messagebox as mess, simpledialog as tsd
import cv2
import os
import csv
import numpy as np
import pandas as pd
import datetime
import time
import tkinter as tk
from tkinter import filedialog
import subprocess
from tkinter  import *
from PIL import ImageTk,Image

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title(" AI Attendance System")
window.configure(background='white')
heading=Label(window,text="Welcome to AI Based Attendence System",background="dark blue",fg="white",font=("Time",20))
heading.pack(fill=X,ipady=60)
window.iconbitmap('UI_Image/AMS.ico')
ai = Image.open("UI_Image/0003.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=400, y=158)


button_frame=LabelFrame(window,height=100,width=1550,background="dark blue",text="Please be Patience  to Run Software with in 24 (sec) & Press q to Stop Attendence",fg="white",font=("Time",15))
button_frame.place(x=0,y=600)

window.mainloop()





def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
    faces = []
    ids = []
    for image_path in image_paths:
        img = cv2.imread(image_path, 0)
        # Read images in grayscale
        face_id = int(os.path.split(image_path)[-1].split(".")[0])
        faces.append(img)
        ids.append(face_id)

    return faces, np.array(ids)

def recognize_faces():

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    casc_path = ("C:/Users/muhammad zuhair/Desktop/ffs attendence/haarcascade_frontalface_default.xml")

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces, ids = get_images_and_labels(os.path.join("C:/Users/muhammad zuhair/Desktop/ffs attendence/TrainingImages"))

    recognizer.train(faces, ids)
    recognizer.save("C:/Users/muhammad zuhair/Desktop/ffs attendence/trainer.yml")
    
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    headings = ['ID', 'Name', 'Date', 'Time']
    attendance_file = "C:/Users/muhammad zuhair/Desktop/ffs attendence/Attendance.csv"
    # Data to be written to the CSV file
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
            face_id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if confidence < 50:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                name = "Person " + str(face_id)
                # Sample data: Dictionary of face IDs and corresponding names
                face_id_mapping = {
                    0: 'Muhammad zuhair uddin',
                    2: 'Irshad',
                    3: 'Muhammad zuhair uddin',
                    4: 'hasim',
                    5:'hasnain',
                    6:' Muhammad zuhair uddin',
                    7:'azhar',
                    8:'mujtaba',
                    9:'Muhammad ',
                    10: 'col r Rashid Iqbal ansari',
                    11:'Iqbal',


                    # Add more face IDs and names as needeqd
                }

                # Assume face_id is obtained from your recognition system
                face_id = 0
                face_id = 2
                face_id = 3
                face_id = 4
                face_id = 5
                face_id = 6
                face_id = 7
                face_id = 8
                face_id = 9
                face_id = 10
                face_id = 1

                # Check if the face_id is in the dictionary
                if face_id in face_id_mapping:
                    name = face_id_mapping[face_id]
                    print(f"Person recognized: {name}")
                else:
                    name = f"Person {face_id}"
                    print(f"Person not recognized, defaulting to ID: {face_id}")

                # Now 'name' contains the recognized person's name or a default string if not recognized

                #with open ("C:/Users/Irshad Hussain/Desktop/ffs attendence/Attendance.csv" + date + ".csv", 'a+') as csvFile1:
                #writer = csv.writer(csvFile1)
                # Specify the file name
                file_name = 'Attendance.csv'

                    # Writing the headings to the CSV file
                with open("C:/Users/muhammad zuhair/Desktop/ffs attendence/Attendance.csv" + date + ".csv", mode='w', newline='') as csvFile1:
                    writer = csv.writer(csvFile1)
                        # Write the headings to the CSV file
                    writer.writerow(headings)

                    print(f'Headings {headings} have been written to {file_name}.')




                #with open(attendance_file, 'a+') as csvFile1:
                    #writer = csv.writer(csvFile1)
                    writer.writerow([face_id, name, date, timeStamp])

                cv2.putText(img, str(name), (x, y + h), font, 1, (255, 255, 255), 2)
            else:
                cv2.putText(img, "Unknown", (x, y + h), font, 1, (255, 255, 255), 2)

        cv2.imshow('', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("C:/Users/muhammad zuhair/Desktop/Face detection Attendance System/Attendance/Attendance_" + date + ".csv")
    if exists:
        with open("C:/Users/muhammad zuhair/Desktop/Face detection Attendance System/Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)

        csvFile1.close()
    else:
        with open("C:/Users/muhammad zuhair/Desktop/Face detection Attendance System/Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)

        csvFile1.close()
    with open("C:/Users/muhammad zuhair/Desktop/Face detection Attendance System/Attendance/Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()

    cam.release()
    cv2.destroyAllWindows()
   


if __name__ == "__main__":
    assure_path_exists("C:/Users/muhammad zuhai/ffs attendence/Desktop/TrainingImages")
    recognize_faces()




