from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import platform
from kivy.logger import Logger
from kivymd.uix.screenmanager import MDScreenManager, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
# Logger.info(f"PLATFORM {kivy.utils.platform}")
if platform == 'android':
    Logger.info("  ON ANDROID - REQUESTING PERMISSIONS")
    from android.permissions import Permission, request_permissions
    Logger.info("    imported permission things...")
    perms = [Permission.INTERNET]
    Logger.info(f"   asking for `{perms}`...")
    res = request_permissions(perms, None)
    Logger.info(f"    permissions requested {res} ...")

# KV string that describes the layout
KV = '''
MDScreenManager:
    MDScreen:
        spacing: "15px"
        MDBoxLayout:
            adaptive_height: True
            orientation: "vertical"
            MDTextField:
                hint_text: "username"
            MDTextField:
                hint_text: "password"
            MDFlatButton:
                text: "login"
        Widget:
'''
MAIN_KV = "./templates/main.kv"
class HelloWorldApp(MDApp):
    def build(self):
        # Load the KV string
        return Builder.load_file(MAIN_KV)

if __name__ == '__main__':
    HelloWorldApp().run()
