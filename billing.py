# importing libraries
import tkinter as tk


WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 300
center = WINDOW_SIZE_X//2











# creating a window 
root = tk.Tk()


#####################################
########### root functions ##########
#####################################
# resizing window
root.geometry(f"{WINDOW_SIZE_X}x{WINDOW_SIZE_Y}")

# changing title
root.title("Billing System")

# no resizing
root.resizable(True, False)

SOFTWARE_TITLE = "BILLING SYSTEM"
myTitle = tk.Label(text=SOFTWARE_TITLE)
myTitle.place(x=center - (len(SOFTWARE_TITLE)*6//2) , y=20)



LABLES = {}


Namkeen = tk.Label(text = "Namkeen", font=("arial", 12, "bold"))
LABLES["Namkeen"]  = [Namkeen, 50]

SoftDrink = tk.Label(text = "SoftDrink", font=("arial", 12, "bold"))
LABLES["SoftDrink"]  = [SoftDrink, 40]

Chips = tk.Label(text = "Chips", font=("arial", 12, "bold"))
LABLES["Chips"]  = [Chips, 20]

Chocolates = tk.Label(text = "Chocolates", font=("arial", 12, "bold"))
LABLES["Chocolates"]  = [Chocolates, 100]


Toothpaste = tk.Label(text = "Toothpaste", font=("arial", 12, "bold"))
LABLES["Toothpaste"]  = [Toothpaste, 100]


Lable_position_x = 12
Lable_position_y = 50
increment = 0

for i in LABLES:
    print(LABLES[i])
    LABLES[i][0].place(x=Lable_position_x, y=Lable_position_y + increment)
    increment += 30

# running the window
root.mainloop()