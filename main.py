from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import requests
import json
from workoutbanner import WorkoutBanner
from  kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class SettingsScreen(Screen):
    pass


GUI = Builder.load_file("main.kv")


class MainApp(App):
    my_friend_id = 1
    data = {}

    def build(self):
        return GUI

    def on_start(self):
        result = requests.get("https://manageyourlife-ee2c0-default-rtdb.firebaseio.com/"
                              + str(self.my_friend_id) + ".json")
        self.data = json.loads(result.content.decode())

    def load_home_screen(self):
        avatar_image = self.root.ids["avt_img"]
        avatar_image.source = "img/" + self.data["avatar"]

        self.update_avatar()

        banner_grid = self.root.ids["home_screen"].ids["banner_grid"]
        workouts = self.data["workouts"][1:]
        for workout in workouts:
            for i in range(0,5):
                w = WorkoutBanner(workout_image=workout["workout_image"], description=workout["description"])
                banner_grid.add_widget(w)

    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name

    def update_avatar(self):
        current_avatar = self.root.ids["settings_screen"].ids["id_change_avatar"]
        current_avatar.source = "img/" + self.data["avatar"]

    def login(self, screen_name = "home_screen"):
        user_name = self.root.ids["login_screen"].ids["user_name"].text
        password = self.root.ids["login_screen"].ids["password"].text
        if self.data["username"] == user_name and self.data["password"] == password:
            self.root.ids["screen_manager"].current = screen_name
            print(screen_name)
            self.load_home_screen()
        else: print("sai mk")

MainApp().run()
