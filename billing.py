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
myTitle.place(x=center-50 , y=10)










L_SOFTDRINK = tk.Label(root, text= 'SoftDrink')
L_SOFTDRINK.place(x=15, y=20)


L_PRICE_SOFTDRINK = tk.Label(root, text="₹ 25")
L_PRICE_SOFTDRINK.place(x=100, y = 20)


L_CHIPS = tk.Label(root, text= 'SoftDrink')
L_CHIPS.place(x=15, y=35)

L_NAMKEEN = tk.Label(root, text= 'SoftDrink')
L_NAMKEEN.place(x=15, y=55)

L_CHOCOLATE = tk.Label(root, text= 'SoftDrink')
L_CHOCOLATE.place(x=15, y=75)





# running the window
root.mainloop()