from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import platform
from kivy.logger import Logger
from kivymd.uix.screenmanager import MDScreenManager, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton

from kivymd.uix.screen import MDScreen
# Logger.info(f"PLATFORM {kivy.utils.platform}")
if platform == 'android':
    Logger.info("ON ANDROID - REQUESTING PERMISSIONS")
    from android.permissions import Permission, request_permissions
    Logger.info("    imported permission things...")
    perms = [Permission.INTERNET, Permission.CAMERA]
    Logger.info(f"   asking for `{perms}`...")
    res = request_permissions(perms, None)
    Logger.info(f"    permissions requested {res} ...")

MAIN_KV = "./templates/main.kv"

from screens.attendance_screen import AttendanceScreen
class HelloWorldApp(MDApp):
    # One user is the actor of an app
    # user_id attribute

    # ideal time cutoff period automatic logout

    def validate_login(self, username, password, instance):
        if username == "rlad" and password == "admin":
            # JOURNEY BEGINS -- CUE IN ANIMATIONS
            # assign user_id based on login information as an app atribute

            sm = instance.manager
            sm.current = "attendance_screen"

    def user_attendance(self):
        # navigate to attendance journey screen
        pass 

    def build(self):
        # Load the KV string
        return Builder.load_file(MAIN_KV)
  
if __name__ == '__main__':
    HelloWorldApp().run()
