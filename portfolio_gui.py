import tkinter as tk

root = tk.Tk()

logo = tk.PhotoImage(file='portfolio_image.png')

w1 = tk.Label(root, image=logo).pack(side='right')

intro = '''Welcome to the Portfolio Manager.
           Pick an option.
        '''

w2 = tk.Label(root, justify=tk.LEFT, padx=10, text=intro).pack(side='left')



root.mainloop()