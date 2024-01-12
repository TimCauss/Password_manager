import customtkinter
from Modules.PasswordCreator import randomizer


class PasswordGeneratorWindow:
    def __init__(self):
        self.pass_gen = customtkinter.CTk()
        self.pass_gen.geometry("500x350")

        self.slider_value: int = 10
        self.alpha_maj: bool = customtkinter.BooleanVar(value=True)
        self.nums: bool = customtkinter.BooleanVar(value=True)
        self.special_chars: bool = customtkinter.BooleanVar(value=True)
        self.word: str = ''

        self.text_box = customtkinter.CTkTextbox(
            self.pass_gen, width=400, height=25
        )

        self.text_box.pack(padx=20, pady=20)
        self.text_box.insert('0.0', str(randomizer(10)))
        self.text_box.configure(state="disabled")

        self.button = customtkinter.CTkButton(
            self.pass_gen, text='Create', command=self.button_create)
        self.button.pack(padx=20, pady=20)

        self.alpha_maj_checkbox = customtkinter.CTkCheckBox(
            self.pass_gen, text="Maj.", variable=self.alpha_maj,
        )
        self.alpha_maj_checkbox.pack()

        self.nums_checkbox = customtkinter.CTkCheckBox(
            self.pass_gen, text="Numbers", variable=self.nums,
        )
        self.nums_checkbox.pack()

        self.spec_chars_checkbox = customtkinter.CTkCheckBox(
            self.pass_gen, text="Spec", variable=self.special_chars,
        )
        self.spec_chars_checkbox.pack()

        self.slider = customtkinter.CTkSlider(
            self.pass_gen, from_=10, to=50, number_of_steps=40,
            command=self.slider_event)
        self.slider.set(10)
        self.slider.pack(padx=20, pady=20)

        self.label_len = customtkinter.CTkLabel(
            self.pass_gen, text=str(self.slider_value)
        )
        self.label_len.pack()

    def slider_event(self, value: float):
        v = int(value)
        self.slider_value = v
        self.label_len.configure(text=str(v))

    def button_create(self):
        self.word = randomizer(self.slider_value, self.alpha_maj.get(),
                               self.nums.get(), self.special_chars.get())

        self.text_box.configure(state="normal")
        self.text_box.delete("0.0", 'end')
        self.text_box.insert("0.0", str(self.word))
        self.text_box.configure(state="disabled")


if __name__ == "__main__":
    my_app = PasswordGeneratorWindow()
    my_app.pass_gen.mainloop()
