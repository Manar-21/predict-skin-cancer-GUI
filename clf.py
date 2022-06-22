import math
import os
import cv2
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import keras
from tkinter import messagebox
from PIL import ImageTk, Image
import pickle
from tensorflow.keras.models import load_model

class AI:
    
    def Classification(self):
        if self.m=='ML':
            
            df1 = pd.DataFrame()
            self.img = cv2.resize(self.img, (224,224))
            img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            img_one_column_arr = img_gray.reshape((self.img.shape[0]*self.img.shape[1]), 1)
            df1[str(0)] = img_one_column_arr[:,0]   
            loaded_model = pickle.load(open(self.model, 'rb'))
            result = loaded_model.predict(df1.T)
            
            if result==0:
                messagebox.showinfo("Classification", "Benign")
            else :
                messagebox.showinfo("Classification", "Malignant")

        elif self.m=='CNN':
            model = load_model(self.model)
            img = cv2.resize(self.img,(224,224))
            img = np.reshape(img,[1,224,224,3])
            result = model.predict(img)
            
            if result[0][0]<=.4:
                messagebox.showinfo("Classification", "Benign")
            else :
                messagebox.showinfo("Classification", "Malignant")
            
        else :
            model = load_model(self.model)
            img = cv2.resize(self.img,(224,224))
            img = np.reshape(img,[1,224*224,3])
            result = model.predict(img)
            
            if result[0][0]<=.4:
                messagebox.showinfo("Classification", "Benign")
            else :
                messagebox.showinfo("Classification", "Malignant")

            
    def knn(self):
        self.m = 'ML'
        self.model = "knn.sav"

    def svm(self):
        self.m = 'ML'
        self.model = "svm.sav"

    def dt(self):
        self.m = 'ML'
        self.model = "decision_tree.sav"

    def cnn(self):
        self.m = 'CNN'
        self.model = "CNN"

    def fc(self):
        self.m = 'FC'
        self.model = "FC"


    def Show(self, img):
        self.img = img
        img = np.array(self.img, dtype=np.uint8)
        img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_AREA)
        image_tk = ImageTk.PhotoImage(image=Image.fromarray(img))
        canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        window.mainloop()

    
        
    def Browse(self):
        global canvas, image_tk
        canvas = tk.Canvas(window, width=400, height=400)
        canvas.place(x=300, y=130)
        IMG = filedialog.askopenfilename()
        self.img = cv2.imread(IMG)
        image = Image.open(IMG)
        image_tk = ImageTk.PhotoImage(image)
        image = image.resize((400, 400), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

    def __init__(self):
        global window
        window = tk.Tk()
        window.title('AI')
        window.geometry("1000x650+100+20")
        bk = Image.open("back.jpg")
        bk = bk.resize((1000, 650), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(bk)
        label1 = tk.Label(window, image=bg)
        label1.place(x=0, y=0)        
        self.store_filters = []
        self.flag = False

        try:
            Btn6 = tk.Button(window, text="KNN", font=("Helvetice", 15), width=20, activebackground="#b3b3b3",
                              command=self.knn).place(x=30, y=270)
            Btn7 = tk.Button(window, text="SVM", font=("Helvetice", 15), width=20, activebackground="#b3b3b3",
                              command=self.svm).place(x=30, y=320)
            Btn8 = tk.Button(window, text="DT", font=("Helvetice", 15), width=20, activebackground="#b3b3b3",
                              command=self.dt).place(x=30, y=370)
            Btn8 = tk.Button(window, text="ANN", font=("Helvetice", 15), width=20, activebackground="#b3b3b3",
                              command=self.fc).place(x=740, y=300)
            Btn8 = tk.Button(window, text="CNN", font=("Helvetice", 15), width=20, activebackground="#b3b3b3",
                              command=self.cnn).place(x=740, y=350)

            Btn29 = tk.Button(window, text="Browse", font=("Helvetice", 15), width=20, activebackground="#b3b3b3",
                               command=self.Browse).place(x=270, y=600)
            Btn30 = tk.Button(window, text="Classification", font=("Helvetice", 15), width=20, activebackground="#b3b3b3",
                               command=self.Classification).place(x=510, y=600)
        except:
            pass


        window.mainloop()

if __name__ == '__main__':
    AI()




