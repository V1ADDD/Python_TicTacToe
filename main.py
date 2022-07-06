from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

X_turn = False


class MainApp(App):
    def build(self):  # constructor
        main_layout = BoxLayout(orientation="vertical", padding=3, spacing=3)  # window
        up_layout = BoxLayout()  # window in window
        self.label1 = Label(text="O", size_hint=(None, None), font_size=20)  # obj for clicking (button)
        up_layout.add_widget(self.label1)  # add Button on window in window
        self.count_x = Label(text="O", size_hint=(None, None), font_size=20)  # obj for clicking (button)
        up_layout.add_widget(self.count_x)  # add Button on window in window
        self.count_y = Label(text="O", size_hint=(None, None), font_size=20)  # obj for clicking (button)
        up_layout.add_widget(self.count_y)  # add Button on window in window
        new_button = Button(text="New", font_size=20, size_hint=(None, None), pos_hint={"center_x": 0.5, "center_y": 0.5})
        #new_button.bind(on_press=self.new_game)
        up_layout.add_widget(new_button)
        exit_button = Button(text="Exit", font_size=20, size_hint=(None, None), pos_hint={"center_x": 0.5, "center_y": 0.5})
        #exit_button.bind(on_press=self.exit)
        up_layout.add_widget(exit_button)
        main_layout.add_widget(up_layout)  # add window on window to window

        buttons = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]  # mass of button cells
        for row in buttons:
            h_layout = BoxLayout()  # window in window
            for label in row:
                button = Button(text=label, font_size=120, pos_hint={"center_x": 0.5, "center_y": 0.5})  # obj for clicking (button)
                button.bind(on_press=self.on_button_press)  # bind on press for Button
                h_layout.add_widget(button)  # add Button on window in window
            main_layout.add_widget(h_layout)  # add window on window to window

        Window.size = (500, 650)  # size for window
        return main_layout

    def on_button_press(self, instance):  # bind for buttons
        global X_turn
        if instance.text == " ":
            if X_turn:
                instance.text = "X"
                X_turn = False
            else:
                instance.text = "O"
                X_turn = True


if __name__ == '__main__':  # main window run
    MainApp().run()
