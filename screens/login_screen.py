from kivymd.uix.screen import MDScreen
# import firebase_admin
from firebase_admin import db
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog


class LoginScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate_login(self, username, password):
        print(username, password)
        ref = db.reference("rlad/users")
        users_db = ref.get()
        if username == '':
            print("here")
            dialog = MDDialog(title="Error", text="Enter Username")
            dialog.open()
            Clock.schedule_once(lambda dt: dialog.dismiss(), 3)
        elif username not in users_db:
            print("here222")
            dialog = MDDialog(title="Error", text="Username does not exist")
            dialog.open()
            Clock.schedule_once(lambda dt: dialog.dismiss(), 3)
        elif users_db[username] != password:
            print("here33")
            dialog = MDDialog(title="Error", text="Password does not match")
            dialog.open()
            Clock.schedule_once(lambda dt: dialog.dismiss(), 3)
        else:
            print("ALL GOOD")