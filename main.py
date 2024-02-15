from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import platform
from kivy.logger import Logger

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
Screen:
    MDLabel:
        text: "Hello, World!"
        halign: 'center'
        valign: 'center'
'''

class HelloWorldApp(MDApp):
    def build(self):
        # Load the KV string
        return Builder.load_string(KV)

if __name__ == '__main__':
    HelloWorldApp().run()
