from tkinter import *
from tkinter.messagebox import*
from pickle import*
import os
import sys

def resource_path2(relative_path):
	try:
		base_path=sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path,relative_path)

root = Tk()
root.title("Salary Predictor by Vinesh Ryapak")
root.geometry("500x400+50+50")
f = ("Century", 30, "bold")

def predict():
    try:
        exp = float(ent_exp.get())
        
        # Open the "sal.pkl" file and load the model
        with open(resource_path2("sal.pkl"), "rb") as f:
            model = load(f)
        
        # Use the loaded model to predict salary
        sal = model.predict([[exp]])
        msg = "Salary = " + str(round(sal[0], 2)) + "K"
        showinfo("Prediction", msg)
    except ValueError:
        showerror("Error", "Please enter numbers only")
        ent_exp.delete(0, END)
        ent_exp.focus()
    except FileNotFoundError:
        showerror("Error", "Model file not found")

lab_title = Label(root, text="Salary Predictor", font=f)
lab_exp = Label(root,text="Enter Experience", font=f)
ent_exp = Entry(root,font=f)
btn_predict = Button(root,text="Predict Salary",font=f,command=predict)

lab_title.pack(pady=5)
lab_exp.pack(pady=5)
ent_exp.pack(pady=5)
btn_predict.pack(pady=5)

root.mainloop()

