# importing libraries
import tkinter as tk


WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 300
center = WINDOW_SIZE_X//2



def getBill():
    
    price = [45, 100, 50, 20]

    a = E_SOFTDRINK.get() or 0
    b = E_CHOCOLATE.get() or 0
    c = E_NAMKEEN.get() or 0
    d = E_CHIPS.get() or 0

    items = [a,b,c,d]
    total = 0
    for i in range(len(items)):
        if str(items[i]).isnumeric():
            total += int(items[i]) * price[i]

    print(total)    













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
myTitle.place(x=center-50 , y=10)










L_SOFTDRINK = tk.Label(root, text= 'SoftDrink', font=("arial")).place(x=20, y=40)
L_PRICE_SOFTDRINK = tk.Label(root, text="₹ 45", font=("arial")).place(x=200, y=40)
E_SOFTDRINK = tk.Entry(root)
E_SOFTDRINK.place(x=300, y=40)


L_CHOCOLATE = tk.Label(root, text= 'Chocolate', font=("arial")).place(x=20, y=70)
L_PRICE_CHOCOLATE = tk.Label(root, text="₹ 100", font=("arial")).place(x=200, y=70)
E_CHOCOLATE = tk.Entry(root)
E_CHOCOLATE.place(x=300, y=70)

L_NAMKEEN = tk.Label(root, text= 'NAMKEEN', font=("arial")).place(x=20, y=100)
L_PRICE_NAMKEEN = tk.Label(root, text="₹ 50", font=("arial")).place(x=200, y=100)
E_NAMKEEN = tk.Entry(root)
E_NAMKEEN.place(x=300, y=100)

L_CHIPS = tk.Label(root, text= 'CHIPS', font=("arial")).place(x=20, y=130)
L_PRICE_CHIPS = tk.Label(root, text="₹ 20", font=("arial")).place(x=200, y=130)
E_CHIPS = tk.Entry(root)
E_CHIPS.place(x=300, y=130)





CalculateBill = tk.Button(text="Calculate Bill", font=("arial"), command=getBill).place(x=300, y=230)



# running the window
root.mainloop()