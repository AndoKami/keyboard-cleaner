import tkinter as tk
import keyboard


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Clavier ON/OFF")

        # Définir la taille initiale et rendre la fenêtre redimensionnable
        self.root.geometry("400x200")

        self.button = tk.Button(root, text="ON", command=self.toggle_keyboard, width=10, height=2)
        self.button.pack(pady=20)

        self.is_on = True

        # Variables pour le déplacement de la fenêtre
        self._offsetx = 0
        self._offsety = 0

        # Bind les événements de la souris pour le déplacement de la fenêtre
        self.root.bind('<Button-1>', self.click_window)
        self.root.bind('<B1-Motion>', self.drag_window)

    def toggle_keyboard(self):
        if self.is_on:
            self.button.config(text="OFF")
            self.disable_keyboard()
        else:
            self.button.config(text="ON")
            self.enable_keyboard()
        self.is_on = not self.is_on

    def disable_keyboard(self):
        # Bloquer toutes les touches individuelles
        for key in range(150):
            keyboard.block_key(key)

    def enable_keyboard(self):
        keyboard.unhook_all()

    def click_window(self, event):
        self._offsetx = event.x
        self._offsety = event.y

    def drag_window(self, event):
        x = self.root.winfo_pointerx() - self._offsetx
        y = self.root.winfo_pointery() - self._offsety
        self.root.geometry(f'+{x}+{y}')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
