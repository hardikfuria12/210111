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

import firebase_admin
from firebase_admin import initialize_app, db, credentials

CRED = credentials.Certificate("djwines-a4c3d-firebase-adminsdk-rqi2m-51f2fcc835.json")
FIREBASE_URL = 'https://djwines-a4c3d-default-rtdb.asia-southeast1.firebasedatabase.app/.firebaseio.com/'
MAIN_KV = "./templates/main.kv"

try:
    firebase_admin.get_app()
except ValueError:
    firebase_app = initialize_app(CRED,{
      'databaseURL': FIREBASE_URL
    }
)
# from screens.attendance_screen import AttendanceScreen
from screens.login_screen import LoginScreen
# from screens.gps_screen import GPSScreen
class HelloWorldApp(MDApp):
    # One user is the actor of an app
    # user_id attribute

    # ideal time cutoff period automatic logout

    def user_attendance(self):
        # navigate to attendance journey screen
        pass 

    def build(self):
        # Load the KV string
        return Builder.load_file(MAIN_KV)
  
if __name__ == '__main__':
    HelloWorldApp().run()
