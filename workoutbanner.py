from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import kivy.utils


class WorkoutBanner(GridLayout):
    rows = 1

    def __init__(self, **kwargs):
        super(WorkoutBanner, self).__init__()

        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#67697")))
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_background, size=self.update_background)

        left = FloatLayout()
        left_image = Image(source="img" + kwargs['workout_image'], size_hint=(1, .8), pos_hint={"top": 1, "right": 1})
        left_label = Label(text=kwargs['description'], size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        left.add_widget(left_image)
        left.add_widget(left_label)

        # middle = FloatLayout()
        # middle_image = Image(source="img/" + kwargs['workout_image'])
        # middle_label = Label(text=kwargs['description'])
        # middle_label.add_widget(middle_image)
        # middle.add_widget(middle_label)


        self.add_widget(left)
        # self.add_widget(middle)

    def update_background(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
