import customtkinter
from Modules.randomizer import randomizer


class PasswordGenerator:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("400x150")

        self.slider_value: int = 5

        self.button = customtkinter.CTkButton(
            self.app, text='Create', command=self.button_create)
        self.button.pack(padx=20, pady=20)

        self.slider = customtkinter.CTkSlider(
            self.app, from_=5, to=50, command=self.slider_event)
        self.slider.pack(padx=20, pady=20)

    def slider_event(self, value):
        self.slider_value = value

    def button_create(self):
        print(randomizer(self.slider_value))


if __name__ == "__main__":
    my_app = PasswordGenerator()
    my_app.app.mainloop()
