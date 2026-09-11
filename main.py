from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import platform
from kivy.config import Config

Config.set('graphics', 'fullscreen', 'auto')

PASSWORD = "1230"


class LockerScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 30

        self.label = Label(
            text='ВВЕДИТЕ ПАРОЛЬ',
            font_size='40sp',
            color=(1, 0, 0, 1),
            size_hint=(1, 0.4)
        )
        self.add_widget(self.label)

        self.entry = TextInput(
            password=True,
            font_size='30sp',
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.add_widget(self.entry)

        self.btn = Button(
            text='РАЗБЛОКИРОВАТЬ',
            font_size='24sp',
            size_hint=(1, 0.2),
            background_color=(0.2, 0.2, 0.2, 1)
        )
        self.btn.bind(on_press=self.check_password)
        self.add_widget(self.btn)

        self.timer_label = Label(
            text='Заблокировано: 00:00',
            font_size='16sp',
            color=(0.5, 0.5, 0.5, 1),
            size_hint=(1, 0.2)
        )
        self.add_widget(self.timer_label)

        self.start_time = 0
        Clock.schedule_interval(self.update_timer, 1)
        Clock.schedule_interval(self.keep_focus, 0.5)

    def keep_focus(self, dt):
        Window.fullscreen = 'auto'

    def update_timer(self, dt):
        import time
        if self.start_time == 0:
            self.start_time = time.time()
        elapsed = int(time.time() - self.start_time)
        mins, secs = divmod(elapsed, 60)
        self.timer_label.text = f'Заблокировано: {mins:02d}:{secs:02d}'

    def check_password(self, instance):
        if self.entry.text == PASSWORD:
            App.get_running_app().stop()
        else:
            self.label.text = 'НЕВЕРНЫЙ ПАРОЛЬ!'
            self.entry.text = ''
            Clock.schedule_once(self.reset_label, 2)

    def reset_label(self, dt):
        self.label.text = 'ВВЕДИТЕ ПАРОЛЬ'


class LockerApp(App):
    def build(self):
        self.title = 'System Update'
        Window.clearcolor = (0, 0, 0, 1)
        return LockerScreen()

    def on_pause(self):
        return True


if __name__ == '__main__':
    LockerApp().run()
