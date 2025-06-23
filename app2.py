
from kivy.app import App
from kivy.uix.label import Label

class NameMatcherApp(App):
    def build(self):
        return Label(text="تطبيق مطابقة الأسماء والأقسام")

if __name__ == "__main__":
    NameMatcherApp().run()
