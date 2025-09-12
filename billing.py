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
Q_Namkeen = tk.Entry()
LABLES["Namkeen"]  = [Namkeen, 50, Q_Namkeen]

SoftDrink = tk.Label(text = "SoftDrink", font=("arial", 12, "bold"))
Q_SoftDrink = tk.Entry()
LABLES["SoftDrink"]  = [SoftDrink, 40, Q_SoftDrink]

Chips = tk.Label(text = "Chips", font=("arial", 12, "bold"))
Q_Chips = tk.Entry()
LABLES["Chips"]  = [Chips, 20, Q_Chips]

Chocolates = tk.Label(text = "Chocolates", font=("arial", 12, "bold"))
Q_Chocolates = tk.Entry()
LABLES["Chocolates"]  = [Chocolates, 100, Q_Chocolates]


Lable_position_x = 12
Lable_position_y = 50
increment = 0

for i in LABLES:
    #print(LABLES[i])
    LABLES[i][0].place(x=Lable_position_x, y=Lable_position_y + increment)
    tk.Label(text=f"₹ {LABLES[i][1]}", font=("arial", 10)).place(x=Lable_position_x + 150,  y=Lable_position_y + increment)
    increment += 30

# running the window
root.mainloop()