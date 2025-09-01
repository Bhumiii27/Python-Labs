from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CombinedApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # -------- Counter Section --------
        self.counter = 0
        self.counter_label = Label(text="Count: 0", font_size=32)
        main_layout.add_widget(self.counter_label)

        counter_button = Button(text="Increment Counter", font_size=24)
        counter_button.bind(on_press=self.increment_counter)
        main_layout.add_widget(counter_button)

        # -------- Text Input Section --------
        self.text_input = TextInput(hint_text="Enter something...", font_size=20)
        main_layout.add_widget(self.text_input)

        text_button = Button(text="Display Text", font_size=24)
        text_button.bind(on_press=self.display_text)
        main_layout.add_widget(text_button)

        self.display_label = Label(text="", font_size=28)
        main_layout.add_widget(self.display_label)

        return main_layout

    def increment_counter(self, instance):
        self.counter += 1
        self.counter_label.text = f"Count: {self.counter}"

    def display_text(self, instance):
        user_input = self.text_input.text
        self.display_label.text = f"You typed: {user_input}"


if __name__ == '__main__':
    CombinedApp().run()
