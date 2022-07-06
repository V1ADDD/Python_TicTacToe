from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

X_turn = False


def exit1(instance):
    App.get_running_app().stop()


class MainApp(App):
    def build(self):  # constructor
        self.button = ["", "", "", "", "", "", "", "", ""]
        main_layout = BoxLayout(orientation="vertical", padding=3, spacing=3)  # window
        up_layout = BoxLayout(height=50)  # window in window
        self.label1 = Label(text="O", size_hint=(None, None), height=50, font_size=20,
                            pos_hint={"center_x": 0.1, "center_y": 0.15})  # obj for clicking (button)
        up_layout.add_widget(self.label1)  # add Button on window in window
        self.count_x = Label(text="0", size_hint=(None, None), height=50, width=50, font_size=20,
                             pos_hint={"center_x": 0.1, "center_y": 0.15})  # obj for clicking (button)
        up_layout.add_widget(self.count_x)  # add Button on window in window
        self.count_o = Label(text="0", size_hint=(None, None), height=50, width=50, font_size=20,
                             pos_hint={"center_x": 0.1, "center_y": 0.15})  # obj for clicking (button)
        up_layout.add_widget(self.count_o)  # add Button on window in window
        empty = Label(text=" ", font_size=20, pos_hint={"center_x": 0.1, "center_y": 0.15})  # obj for clicking (button)
        up_layout.add_widget(empty)  # add Button on window in window
        new_button = Button(text="New", font_size=20, size_hint=(None, None), height=50,
                            pos_hint={"center_x": 0.1, "center_y": 0.15})
        new_button.bind(on_press=self.new_game)
        up_layout.add_widget(new_button)
        exit_button = Button(text="Exit", font_size=20, size_hint=(None, None), height=50,
                             pos_hint={"center_x": 0.1, "center_y": 0.15})
        exit_button.bind(on_press=exit1)
        up_layout.add_widget(exit_button)
        main_layout.add_widget(up_layout)  # add window on window to window

        buttons = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]  # mass of button cells
        i = 0
        for row in buttons:
            h_layout = BoxLayout()  # window in window
            for label in row:
                self.button[i] = Button(text=label, font_size=120,
                                        pos_hint={"center_x": 0.5, "center_y": 0.5})  # obj for clicking (button)
                self.button[i].bind(on_press=self.on_button_press)  # bind on press for Button
                h_layout.add_widget(self.button[i])  # add Button on window in window
                i += 1
            main_layout.add_widget(h_layout)  # add window on window to window

        Window.size = (500, 650)  # size for window
        return main_layout

    def new_game(self, instance):
        for the_button in self.button:
            the_button.text = " "
        self.count_x.text = "0"
        self.count_o.text = "0"
        global X_turn
        X_turn = False
        self.label1.text = "O"

    def on_button_press(self, instance):  # bind for buttons
        global X_turn
        if instance.text == " ":
            if X_turn:
                instance.text = "X"
                X_turn = False
                self.label1.text = "O"
            else:
                instance.text = "O"
                X_turn = True
                self.label1.text = "X"
            if (self.button[0].text == "X" and self.button[1].text == "X" and self.button[2].text == "X") or \
                    (self.button[3].text == "X" and self.button[4].text == "X" and self.button[5].text == "X") or \
                    (self.button[6].text == "X" and self.button[7].text == "X" and self.button[8].text == "X") or \
                    (self.button[0].text == "X" and self.button[3].text == "X" and self.button[6].text == "X") or \
                    (self.button[1].text == "X" and self.button[4].text == "X" and self.button[7].text == "X") or \
                    (self.button[2].text == "X" and self.button[5].text == "X" and self.button[8].text == "X") or \
                    (self.button[0].text == "X" and self.button[4].text == "X" and self.button[8].text == "X") or \
                    (self.button[2].text == "X" and self.button[4].text == "X" and self.button[6].text == "X"):
                self.count_x.text = str(1 + int(self.count_x.text))
                for the_button in self.button:
                    the_button.text = " "
            if (self.button[0].text == "O" and self.button[1].text == "O" and self.button[2].text == "O") or \
                    (self.button[3].text == "O" and self.button[4].text == "O" and self.button[5].text == "O") or \
                    (self.button[6].text == "O" and self.button[7].text == "O" and self.button[8].text == "O") or \
                    (self.button[0].text == "O" and self.button[3].text == "O" and self.button[6].text == "O") or \
                    (self.button[1].text == "O" and self.button[4].text == "O" and self.button[7].text == "O") or \
                    (self.button[2].text == "O" and self.button[5].text == "O" and self.button[8].text == "O") or \
                    (self.button[0].text == "O" and self.button[4].text == "O" and self.button[8].text == "O") or \
                    (self.button[2].text == "O" and self.button[4].text == "O" and self.button[6].text == "O"):
                self.count_o.text = str(1 + int(self.count_o.text))
                for the_button in self.button:
                    the_button.text = " "


if __name__ == '__main__':  # main window run
    MainApp().run()
