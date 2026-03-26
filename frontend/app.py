from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AttendanceApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Eingabe für Mitarbeiter
        self.name_input = TextInput(hint_text="Name des Mitarbeiters")
        layout.add_widget(self.name_input)

        self.position_input = TextInput(hint_text="Position")
        layout.add_widget(self.position_input)

        self.dept_input = TextInput(hint_text="Abteilung")
        layout.add_widget(self.dept_input)

        add_employee_btn = Button(text="Mitarbeiter hinzufügen")
        add_employee_btn.bind(on_press=self.add_employee)
        layout.add_widget(add_employee_btn)

        # Arbeitsdaten-Eingabe
        self.work_date_input = TextInput(hint_text="Datum (YYYY-MM-DD)")
        layout.add_widget(self.work_date_input)

        self.start_time_input = TextInput(hint_text="Arbeitsbeginn (HH:MM)")
        layout.add_widget(self.start_time_input)

        self.end_time_input = TextInput(hint_text="Arbeitsende (HH:MM)")
        layout.add_widget(self.end_time_input)

        self.pause_input = TextInput(hint_text="Mittagspause (Minuten)")
        layout.add_widget(self.pause_input)

        self.work_desc_input = TextInput(hint_text="Arbeitsinhalte")
        layout.add_widget(self.work_desc_input)

        self.overtime_input = TextInput(hint_text="Überstunden (Stunden)")
        layout.add_widget(self.overtime_input)

        add_work_data_btn = Button(text="Arbeitsdaten hinzufügen")
        add_work_data_btn.bind(on_press=self.add_work_data)
        layout.add_widget(add_work_data_btn)

        return layout

    def add_employee(self, instance):
        print(f"Mitarbeiter: {self.name_input.text}, {self.position_input.text}, {self.dept_input.text}")

    def add_work_data(self, instance):
        print(f"Arbeitsdaten: {self.work_date_input.text}, {self.start_time_input.text}, "
              f"{self.end_time_input.text}, {self.pause_input.text}, {self.work_desc_input.text}, "
              f"{self.overtime_input.text}")

if __name__ == "__main__":
    AttendanceApp().run()
