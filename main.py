import customtkinter
from Modules.randomizer import randomizer


class PasswordGenerator:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("400x250")

        self.slider_value: int = 10
        self.alpha_maj: bool = True
        self.nums: bool = True
        self.special_chars = True
        self.word: str = ''

        self.button = customtkinter.CTkButton(
            self.app, text='Create', command=self.button_create)
        self.button.pack(padx=20, pady=20)

        self.slider = customtkinter.CTkSlider(
            self.app, from_=10, to=50, number_of_steps=40,
            command=self.slider_event)
        self.slider.set(10)
        self.slider.pack(padx=20, pady=20)

        self.label_len = customtkinter.CTkLabel(
            self.app, text=str(self.slider_value)
        )
        self.label_len.pack()

        self.text_box = customtkinter.CTkTextbox(
            self.app, width=400, height=25
        )

        self.text_box.pack(padx=20, pady=20)
        self.text_box.insert('0.0', str(randomizer(10)))
        self.text_box.configure(state="disabled")

    def slider_event(self, value: float):
        v = int(value)
        self.slider_value = v
        self.label_len.configure(text=str(v))

    def button_create(self):
        print(randomizer(self.slider_value))
        self.word = randomizer(self.slider_value)
        self.text_box.configure(state="normal")
        self.text_box.delete("0.0", 'end')
        self.text_box.insert("0.0", str(self.word))
        self.text_box.configure(state="disabled")


if __name__ == "__main__":
    my_app = PasswordGenerator()
    my_app.app.mainloop()
