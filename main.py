import customtkinter
from .Modules.randomizer import randomizer

def button_create():
    print(randomizer)


app = customtkinter.CTk()
app.geometry("400x150")


button = customtkinter.CTkButton(app, text='Create', command=button_create)
button.pack(padx=20, pady=20)

app.mainloop()
