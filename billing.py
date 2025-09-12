# importing libraries
import tkinter as tk


WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 300
center = WINDOW_SIZE_X//2




def genrate_bill():
    # blank text to print bill
    bill_text = ""

    # total bill 
    total = 0

    # loop to go through all items
    for i in LABLES:
        # getting quantity of each item
        a =  LABLES[i][2].get()
        # creating a place holder - if a =0 or none or error 
        qty = None

        # cheking if quantity is a number
        if str(a).strip().isdigit():

            # if quantity is a number, then assinging it to qty
            qty = int(str(LABLES[i][2].get()).strip())

        # if quantity is blank or error 
        qty = qty or 0

        # generating total bill
        total += LABLES[i][1] * qty

        # adding all the item, their names, price, quantity and total
        bill_text += f'{i} : ₹ {LABLES[i][1]} X {qty}  =  {LABLES[i][1] * qty} \n'

    # grand total
    bill_text += f"Total bill is ₹ {total}"
    print(bill_text)








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





B_Total = tk.Button(text="Calculate Bill", font=("arial", 12), command=genrate_bill)
B_Total.place(x=250, y=250)






Lable_position_x = 12
Lable_position_y = 50
increment = 0

for i in LABLES:
    #print(LABLES[i])
    # LABELS have Lable object at index 0
    # LABELS have price at index 1
    # Lables Have entry at index 2

    # placing the lables at position according to x and y axies
    LABLES[i][0].place(x=Lable_position_x, y=Lable_position_y + increment)

    # placing the price at position accoding to x and y
    tk.Label(text=f"₹ {LABLES[i][1]}", font=("arial", 10)).place(x=Lable_position_x + 150,  y=Lable_position_y + increment)
    
    # placing the Entry at position accoding to x and y
    LABLES[i][2].place(x=Lable_position_x + 250, y=Lable_position_y + increment)
    
    # placing every item after 30 pixels below the preceding 
    increment += 30

# running the window
root.mainloop()