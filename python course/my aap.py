import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class SpartanGrid(GridLayout) :
    def __init__(self,**kwargs) -> object:
        super(SpartanGrid, self).__init__()
        self.cols = 2
        self.aad_widget (Label(text="student Name:"))


        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="STUDENT MARKS"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="STUDENT GENDER"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text="click me")
        self.add_widget(self.press)


class SpartanApp(App):
    def build(self):
        return SpartanGrid()


if __name__ =="__main__":
    SpartanApp().run()

