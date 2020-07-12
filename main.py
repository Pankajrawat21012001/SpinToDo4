from random import randrange

import plyer
from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex


class HomePage(FloatLayout):
    angle = NumericProperty(0)
    animation_rotate = True
    loop_for_time = True
    black = ListProperty([0, 0, 0, 1])
    white = ListProperty([1, 1, 1, 0])
    day = StringProperty('sun_black_64.png')
    night = StringProperty('moon_white_64.png')
    menu_day = StringProperty('black_menu_64.png')
    menu_night = StringProperty('white_menu_64.png')
    white_without_opacity = ListProperty([1, 1, 1, 1])
    add_white = StringProperty('add_white.png')
    sub_white = StringProperty('sub_white.png')
    add_black = StringProperty('add_black.png')
    sub_black = StringProperty('sub_black.png')
    theme = 0
    start_stop = ObjectProperty
    wheel3 = StringProperty('wheel3.png')
    wheel4 = StringProperty('wheel4.png')
    wheel5 = StringProperty('wheel5.png')
    wheel6 = StringProperty('wheel6.png')
    wheel7 = StringProperty('wheel7.png')
    wheel8 = StringProperty('wheel8.png')
    wheel9 = StringProperty('wheel9.png')
    wheel10 = StringProperty('wheel10.png')
    wheel11 = StringProperty('wheel11.png')
    wheel12 = StringProperty('wheel12.png')

    save_black = StringProperty('save_black_64.png')
    save_white = StringProperty('save_white_64.png')

    reminder_white = StringProperty("reminder_white_64.png")
    reminder_black = StringProperty("reminder_black_64.png")

    orientation_white = StringProperty("orientation_white_64.png")
    orientation_black = StringProperty("orientation_black_64.png")

    drop_down_button_theme_black_background_normal = StringProperty("middle_black_64.png")
    drop_down_button_theme_black_background_down = StringProperty("boundary_white_64.png")
    drop_down_button_theme_white_background_normal = StringProperty("middle_white_64.png")
    drop_down_button_theme_white_background_down = StringProperty("boundary_black_64.png")

    height_indicator = 0.77 * Window.height
    center_height = 0.46 * Window.height
    center_width = Window.width / 2
    height_confirm = 0.08 * Window.height
    width_confirm = 0.2 * Window.width
    width_textbox_confirm = 0.6 * Window.width

    icon=StringProperty("icon_16.png")

    indicator_white = StringProperty('white_yellow_256.png')
    indicator_black = StringProperty('black_yellow_arrow_256.png')
    indicator = Image(source="white_yellow_256.png", pos=(0, 450))
    textinput_3_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 100, center_height + 100), keyboard_suggestions=True,
                              background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1], height=60,
                              width=200)
    textinput_3_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 100, center_height - 250), keyboard_suggestions=True,
                              background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_3_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 300, center_height + 100), keyboard_suggestions=True,
                              background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_4_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 100, center_height + 120), keyboard_suggestions=True,
                              background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_4_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 100, center_height - 200), keyboard_suggestions=True,
                              background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_4_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 300, center_height - 200), keyboard_suggestions=True,
                              background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_4_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 300, center_height + 120), keyboard_suggestions=True,
                              background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_5_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 100, center_height + 200), keyboard_suggestions=True,
                              background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_5_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 150, center_height - 100), keyboard_suggestions=True,
                              background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_5_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 100, center_height - 300), keyboard_suggestions=True,
                              background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_5_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 350, center_height - 100), keyboard_suggestions=True,
                              background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_5_5 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 300, center_height + 200), keyboard_suggestions=True,
                              background_color=[0.604, 0.447, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_6_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 50, center_height + 200), keyboard_suggestions=True,
                              background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_6_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 150, center_height - 30), keyboard_suggestions=True,
                              background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_6_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 50, center_height - 260), keyboard_suggestions=True,
                              background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_6_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 250, center_height - 260), keyboard_suggestions=True,
                              background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_6_5 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 350, center_height - 30), keyboard_suggestions=True,
                              background_color=[0.604, 0.447, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_6_6 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 250, center_height + 200), keyboard_suggestions=True,
                              background_color=[0, 0.690, 0.313, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_7_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 50, center_height + 260), keyboard_suggestions=True,
                              background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_7_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 200, center_height), keyboard_suggestions=True,
                              background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_7_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 150, center_height - 200), keyboard_suggestions=True,
                              background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_7_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 100, center_height - 320), keyboard_suggestions=True,
                              background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_7_5 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 350, center_height - 200), keyboard_suggestions=True,
                              background_color=[0.604, 0.447, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_7_6 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 400, center_height), keyboard_suggestions=True,
                              background_color=[0, 0.690, 0.313, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_7_7 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 250, center_height + 260), keyboard_suggestions=True,
                              background_color=[0.560, 0.666, 0.863, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_8_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 20, center_height + 250), keyboard_suggestions=True,
                              background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_8_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 150, center_height + 70), keyboard_suggestions=True,
                              background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_8_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 150, center_height - 130), keyboard_suggestions=True,
                              background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_8_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 20, center_height - 310), keyboard_suggestions=True,
                              background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_8_5 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 220, center_height - 310), keyboard_suggestions=True,
                              background_color=[0.604, 0.447, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_8_6 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 350, center_height - 130), keyboard_suggestions=True,
                              background_color=[0, 0.690, 0.313, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_8_7 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 350, center_height + 70), keyboard_suggestions=True,
                              background_color=[0.560, 0.666, 0.863, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_8_8 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 220, center_height + 250), keyboard_suggestions=True,
                              background_color=[1, 1, 0, 0.3], foreground_color=[0, 0, 0, 1], height=60, width=200)
    textinput_9_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 20, center_height + 300), keyboard_suggestions=True,
                              background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_9_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 150, center_height + 100), keyboard_suggestions=True,
                              background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_9_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 200, center_height - 70), keyboard_suggestions=True,
                              background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_9_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width + 120, center_height - 280), keyboard_suggestions=True,
                              background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_9_5 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 100, center_height - 400), keyboard_suggestions=True,
                              background_color=[0.604, 0.447, 0, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_9_6 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 320, center_height - 280), keyboard_suggestions=True,
                              background_color=[0, 0.690, 0.313, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_9_7 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 400, center_height - 70), keyboard_suggestions=True,
                              background_color=[0.560, 0.666, 0.863, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_9_8 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 350, center_height + 100), keyboard_suggestions=True,
                              background_color=[1, 1, 0, 0.3], foreground_color=[0, 0, 0, 1], height=60, width=200)
    textinput_9_9 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                              pos=(center_width - 220, center_height + 300), keyboard_suggestions=True,
                              background_color=[0.560, 0.765, 0.419, 0.3], foreground_color=[0, 0, 0, 1],
                              height=60, width=200)
    textinput_10_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 10, center_height + 320), keyboard_suggestions=True,
                               background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=200)
    textinput_10_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 150, center_height + 120), keyboard_suggestions=True,
                               background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=200)
    textinput_10_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 200, center_height - 30), keyboard_suggestions=True,
                               background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=200)
    textinput_10_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 160, center_height - 230), keyboard_suggestions=True,
                               background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=200)
    textinput_10_5 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 10, center_height - 390), keyboard_suggestions=True,
                               background_color=[0.604, 0.447, 0, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=200)
    textinput_10_6 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 210, center_height - 390), keyboard_suggestions=True,
                               background_color=[0, 0.690, 0.313, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=200)
    textinput_10_7 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 360, center_height - 230), keyboard_suggestions=True,
                               background_color=[0.560, 0.666, 0.863, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=200)
    textinput_10_8 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 400, center_height - 30), keyboard_suggestions=True,
                               background_color=[1, 1, 0, 0.3], foreground_color=[0, 0, 0, 1], height=60, width=200)
    textinput_10_9 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 350, center_height + 120), keyboard_suggestions=True,
                               background_color=[0.560, 0.765, 0.419, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=200)
    textinput_10_10 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                                pos=(center_width - 210, center_height + 320), keyboard_suggestions=True,
                                background_color=[0.847, 0.349, 0.051, 0.3], foreground_color=[0, 0, 0, 1],
                                height=60, width=200)
    textinput_11_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 10, center_height + 320), keyboard_suggestions=True,
                               background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=180)
    textinput_11_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 160, center_height + 170), keyboard_suggestions=True,
                               background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=180)
    textinput_11_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 180, center_height), keyboard_suggestions=True,
                               background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=180)
    textinput_11_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 180, center_height - 150), keyboard_suggestions=True,
                               background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=180)
    textinput_11_5 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 100, center_height - 320), keyboard_suggestions=True,
                               background_color=[0.604, 0.447, 0, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=180)
    textinput_11_6 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 90, center_height - 400), keyboard_suggestions=True,
                               background_color=[0, 0.690, 0.313, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=180)
    textinput_11_7 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 280, center_height - 320), keyboard_suggestions=True,
                               background_color=[0.560, 0.666, 0.863, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=180)
    textinput_11_8 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 380, center_height - 150), keyboard_suggestions=True,
                               background_color=[1, 1, 0, 0.3], foreground_color=[0, 0, 0, 1], height=60, width=180)
    textinput_11_9 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 380, center_height), keyboard_suggestions=True,
                               background_color=[0.560, 0.765, 0.419, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=180)
    textinput_11_10 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                                pos=(center_width - 350, center_height + 170), keyboard_suggestions=True,
                                background_color=[0.847, 0.349, 0.051, 0.3], foreground_color=[0, 0, 0, 1],
                                height=60, width=180)
    textinput_11_11 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                                pos=(center_width - 210, center_height + 320), keyboard_suggestions=True,
                                background_color=[0.776, 0.627, 0, 0.3], foreground_color=[0, 0, 0, 1],
                                height=60, width=180)
    textinput_12_1 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 20, center_height + 330), keyboard_suggestions=True,
                               background_color=[0.266, 0.447, 0.768, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=170)
    textinput_12_2 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 150, center_height + 180), keyboard_suggestions=True,
                               background_color=[1, 0.753, 0, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=170)
    textinput_12_3 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 220, center_height + 30), keyboard_suggestions=True,
                               background_color=[0.439, 0.678, 0.278, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=170)
    textinput_12_4 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 220, center_height - 90), keyboard_suggestions=True,
                               background_color=[0.749, 0.749, 0.749, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=170)
    textinput_12_5 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 150, center_height - 260), keyboard_suggestions=True,
                               background_color=[0.604, 0.447, 0, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=170)
    textinput_12_6 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width + 20, center_height - 390), keyboard_suggestions=True,
                               background_color=[0, 0.690, 0.313, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=170)
    textinput_12_7 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 190, center_height - 390), keyboard_suggestions=True,
                               background_color=[0.560, 0.666, 0.863, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=170)
    textinput_12_8 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 320, center_height - 260), keyboard_suggestions=True,
                               background_color=[1, 1, 0, 0.3], foreground_color=[0, 0, 0, 1], height=60, width=170)
    textinput_12_9 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                               pos=(center_width - 390, center_height - 90), keyboard_suggestions=True,
                               background_color=[0.560, 0.765, 0.419, 0.3], foreground_color=[0, 0, 0, 1],
                               height=60, width=170)
    textinput_12_10 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                                pos=(center_width - 390, center_height + 30), keyboard_suggestions=True,
                                background_color=[0.847, 0.349, 0.051, 0.3], foreground_color=[0, 0, 0, 1],
                                height=60, width=170)
    textinput_12_11 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                                pos=(center_width - 320, center_height + 180), keyboard_suggestions=True,
                                background_color=[0.776, 0.627, 0, 0.3], foreground_color=[0, 0, 0, 1],
                                height=60, width=170)
    textinput_12_12 = TextInput(multiline=False, hint_text="Add here", hint_text_color=[0, 0, 0, 1], text="",
                                pos=(center_width - 190, center_height + 330), keyboard_suggestions=True,
                                background_color=[0.5725, 0.8156, 0.313, 0.3], foreground_color=[0, 0, 0, 1],
                                height=60, width=170)

    button_confirm = Button(text="", pos=(width_confirm, height_confirm), bold=True,
                            background_color=[0, 0, 0, 0], color=[1, 1, 1, 1], font_size=45,
                            height=60, width=width_textbox_confirm)
    delete_1_point = 0
    delete_2_point = 0
    delete_3_point = 0

    list_for_detail=[]
    list_for_save_wheel_1=[]
    list_for_save_wheel_2=[]
    list_for_save_wheel_3=[]

    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.ids.wheel_number.source = self.wheel3
        self.add_textbox_for_3()
        self.add_widget(self.indicator)
        self.ids.between_add_sub.add_widget(self.button_confirm)
        detail=open("detail.txt","r")
        for line in detail:
            self.list_for_detail.append(line[:-1])
        print(self.list_for_detail)
        detail.close()


        save_wheel_1 = open("save_wheel_1.txt", "r")
        for line in save_wheel_1:
            self.list_for_save_wheel_1.append(line[:-1])
        print(self.list_for_save_wheel_1)
        save_wheel_1.close()


        save_wheel_2 = open("save_wheel_2.txt", "r")
        for line in save_wheel_2:
            self.list_for_save_wheel_2.append(line[:-1])
        print(self.list_for_save_wheel_2)
        save_wheel_2.close()


        save_wheel_3 = open("save_wheel_3.txt", "r")
        for line in save_wheel_3:
            self.list_for_save_wheel_3.append(line[:-1])
        print(self.list_for_save_wheel_3)
        save_wheel_3.close()

    def refresh(self):
        # self.list_for_detail.clear()
        # detail = open("detail.txt", "r")
        # for line in detail:
        #     self.list_for_detail.append(line[:-1])
        # print(list_for_detail)
        a=self.list_for_detail[0]
        b=self.list_for_detail[1]
        c=self.list_for_detail[2]
        # print(a)
        # print(b)
        # print(c)
        # detail.close()
        if a != "No item saved" and self.delete_1_point == 0:
            if a == "3rd slot added":
                self.ids.save_wheel_1.text = "3rd slot added"
                pass
            elif a == "4th slot added":
                self.ids.save_wheel_1.text = "4th slot added"
                pass
            elif a == "5th slot added":
                self.ids.save_wheel_1.text = "5th slot added"
                pass
            elif a == "6th slot added":
                self.ids.save_wheel_1.text = "6th slot added"
                pass
            elif a == "7th slot added":
                self.ids.save_wheel_1.text = "7th slot added"
                pass
            elif a == "8th slot added":
                self.ids.save_wheel_1.text = "8th slot added"
                pass
            elif a == "9th slot added":
                self.ids.save_wheel_1.text = "9th slot added"
                pass
            elif a == "10th slot added":
                self.ids.save_wheel_1.text = "10th slot added"
                pass
            elif a == "11th slot added":
                self.ids.save_wheel_1.text = "11th slot added"
                pass
            elif a == "12th slot added":
                self.ids.save_wheel_1.text = "12th slot added"
                pass
            else:
                pass
        else:
            # print("last1")
            pass

        if b != "No item saved" and self.delete_2_point == 0:
            if b == "3rd slot added":
                self.ids.save_wheel_2.text = "3rd slot added"
                pass
            elif b == "4th slot added":
                self.ids.save_wheel_2.text = "4th slot added"
                pass
            elif b == "5th slot added":
                self.ids.save_wheel_2.text = "5th slot added"
                pass
            elif b == "6th slot added":
                self.ids.save_wheel_2.text = "6th slot added"
                pass
            elif b == "7th slot added":
                self.ids.save_wheel_2.text = "7th slot added"
                pass
            elif b == "8th slot added":
                self.ids.save_wheel_2.text = "8th slot added"
                pass
            elif b == "9th slot added":
                self.ids.save_wheel_2.text = "9th slot added"
                pass
            elif b == "10th slot added":
                self.ids.save_wheel_2.text = "10th slot added"
                pass
            elif b == "11th slot added":
                self.ids.save_wheel_2.text = "11th slot added"
                pass
            elif b == "12th slot added":
                self.ids.save_wheel_2.text = "12th slot added"
                pass
            else:
                pass
        else:
            # print("last2")
            pass

        if c != "No item saved" and self.delete_3_point == 0:
            if c == "3rd slot added":
                self.ids.save_wheel_3.text = "3rd slot added"
                pass
            elif c == "4th slot added":
                self.ids.save_wheel_3.text = "4th slot added"
                pass
            elif c == "5th slot added":
                self.ids.save_wheel_3.text = "5th slot added"
                pass
            elif c == "6th slot added":
                self.ids.save_wheel_3.text = "6th slot added"
                pass
            elif c == "7th slot added":
                self.ids.save_wheel_3.text = "7th slot added"
                pass
            elif c == "8th slot added":
                self.ids.save_wheel_3.text = "8th slot added"
                pass
            elif c == "9th slot added":
                self.ids.save_wheel_3.text = "9th slot added"
                pass
            elif c == "10th slot added":
                self.ids.save_wheel_3.text = "10th slot added"
                pass
            elif c == "11th slot added":
                self.ids.save_wheel_3.text = "11th slot added"
                pass
            elif c == "12th slot added":
                self.ids.save_wheel_3.text = "12th slot added"
                pass
            else:
                pass
        else:
            # print("last3")
            pass

    def animation_show(self):
        angle_rand = randrange(35, 70)
        self.anim = Animation(angle=angle_rand, duration=0.001)
        for i in range(angle_rand, 361, angle_rand):
            self.anim += Animation(angle=i, duration=0.001)
        self.anim.repeat = True
        self.anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

    def animation_correction(self):
        if self.start_stop.text == "[size=60]Start[/size]":
            self.anim = Animation(angle=0)
            self.anim.repeat = False
            self.anim.start(self)
        else:
            self.button_confirm.text = "Can't ORIENT while wheel is spinning"
            if self.theme == 0:
                self.animate_the_confirm_white_to_black_text()
            else:
                self.animate_the_confirm_black_to_white_text()

    def start(self):
        if self.animation_rotate:
            self.animation_rotate = not self.animation_rotate
            self.start_stop.text = "[size=60]Stop[/size]"
            self.start_stop.background_normal = "red_circle_64.png"
            self.start_stop.background_down = "red_circle_64.png"
            return self.animation_show()
        else:
            self.anim.cancel(self)
            self.start_stop.text = "[size=60]Start[/size]"
            self.start_stop.background_normal = "blue_circle_64.png"
            self.start_stop.background_down = "blue_circle_64.png"
            self.animation_rotate = not self.animation_rotate

    def add(self):
        if int(self.ids.slot_number.text) < 12:
            if self.start_stop.text == "[size=60]Start[/size]":
                self.ids.slot_number.text = str(int(self.ids.slot_number.text) + 1)
                self.animation_correction()
                if int(self.ids.slot_number.text) == 3:
                    self.ids.wheel_number.source = self.wheel3
                    self.add_textbox_for_3()
                elif int(self.ids.slot_number.text) == 4:
                    self.ids.wheel_number.source = self.wheel4
                    self.add_textbox_for_4()
                elif int(self.ids.slot_number.text) == 5:
                    self.ids.wheel_number.source = self.wheel5
                    self.add_textbox_for_5()
                elif int(self.ids.slot_number.text) == 6:
                    self.ids.wheel_number.source = self.wheel6
                    self.add_textbox_for_6()
                elif int(self.ids.slot_number.text) == 7:
                    self.ids.wheel_number.source = self.wheel7
                    self.add_textbox_for_7()
                elif int(self.ids.slot_number.text) == 8:
                    self.ids.wheel_number.source = self.wheel8
                    self.add_textbox_for_8()
                elif int(self.ids.slot_number.text) == 9:
                    self.ids.wheel_number.source = self.wheel9
                    self.add_textbox_for_9()
                elif int(self.ids.slot_number.text) == 10:
                    self.ids.wheel_number.source = self.wheel10
                    self.add_textbox_for_10()
                elif int(self.ids.slot_number.text) == 11:
                    self.ids.wheel_number.source = self.wheel11
                    self.add_textbox_for_11()
                elif int(self.ids.slot_number.text) == 12:
                    self.ids.wheel_number.source = self.wheel12
                    self.add_textbox_for_12()
                return
            return
        return

    def sub(self):
        if int(self.ids.slot_number.text) > 3:
            if self.start_stop.text == "[size=60]Start[/size]":
                self.ids.slot_number.text = str(int(self.ids.slot_number.text) - 1)
                self.animation_correction()
                if int(self.ids.slot_number.text) == 3:
                    self.ids.wheel_number.source = self.wheel3
                    self.add_textbox_for_3()
                elif int(self.ids.slot_number.text) == 4:
                    self.ids.wheel_number.source = self.wheel4
                    self.add_textbox_for_4()
                elif int(self.ids.slot_number.text) == 5:
                    self.ids.wheel_number.source = self.wheel5
                    self.add_textbox_for_5()
                elif int(self.ids.slot_number.text) == 6:
                    self.ids.wheel_number.source = self.wheel6
                    self.add_textbox_for_6()
                elif int(self.ids.slot_number.text) == 7:
                    self.ids.wheel_number.source = self.wheel7
                    self.add_textbox_for_7()
                elif int(self.ids.slot_number.text) == 8:
                    self.ids.wheel_number.source = self.wheel8
                    self.add_textbox_for_8()
                elif int(self.ids.slot_number.text) == 9:
                    self.ids.wheel_number.source = self.wheel9
                    self.add_textbox_for_9()
                elif int(self.ids.slot_number.text) == 10:
                    self.ids.wheel_number.source = self.wheel10
                    self.add_textbox_for_10()
                elif int(self.ids.slot_number.text) == 11:
                    self.ids.wheel_number.source = self.wheel11
                    self.add_textbox_for_11()
                elif int(self.ids.slot_number.text) == 12:
                    self.ids.wheel_number.source = self.wheel12
                    self.add_textbox_for_12()
                return
            return
        return

    def change_background(self):
        if self.theme == 0:
            Window.clearcolor = get_color_from_hex("#FFFFFF")  # window color change to white
            self.ids.day_night.source = self.day  # sun/moon ka image change kartay hai
            # self.ids.menu.source = self.menu_day  # menu ka image change to black
            self.ids.add_image.background_color = self.white  # plus sign
            self.ids.add_image.color = self.black  # plus sign
            self.ids.sub_image.background_color = self.white  # minus sign
            self.ids.sub_image.color = self.black  # minus sign
            self.ids.slot_number.color = self.black  # screen top may 3 ka color change
            self.ids.slot_number.background_color = self.white  # screen top may 3 ka bg color change
            self.ids.slots.color = self.black  # text writtern slots uska color change
            self.ids.slots.background_color = self.white  # ismay uska background white nahi hai uska opacity 0
            # hai iskay liyeah window color dikta hai
            self.indicator.source = self.indicator_black  # indicator ka source change
            self.ids.save.source = self.save_black  # save button ka source change
            # self.ids.menu_name.color = self.black  # text menu ka color change karta hai
            # self.ids.menu_name.background_color = self.white  # textmenu ka bg color change karta hai
            self.ids.day_night_name.color = self.black  # day/night text ka color change karta hai
            self.ids.day_night_name.background_color = self.white  # day/night ka bg color change karta hai

            self.ids.reminder.source = self.reminder_black  # reminder button  ka source change karta hai

            self.ids.save_name.color = self.black  # save text ka text color change karta hai
            self.ids.save_name.background_color = self.white  # save text name ka bg color change karta hai

            self.ids.reminder_name.color = self.black  # reminder text ka text color change karta hai
            self.ids.reminder_name.background_color = self.white  # reminder text name ka bg color change karta hai

            self.ids.save_wheel_1.background_down = self.drop_down_button_theme_white_background_down
            self.ids.save_wheel_1.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.save_wheel_1.color = self.black

            self.ids.save_wheel_2.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.save_wheel_2.background_down = self.drop_down_button_theme_white_background_down
            self.ids.save_wheel_2.color = self.black

            self.ids.save_wheel_3.background_down = self.drop_down_button_theme_white_background_down
            self.ids.save_wheel_3.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.save_wheel_3.color = self.black

            self.ids.delete_1.background_down = self.drop_down_button_theme_white_background_down
            self.ids.delete_1.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.delete_1.color = self.black

            self.ids.delete_2.background_down = self.drop_down_button_theme_white_background_down
            self.ids.delete_2.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.delete_2.color = self.black

            self.ids.delete_3.background_down = self.drop_down_button_theme_white_background_down
            self.ids.delete_3.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.delete_3.color = self.black

            self.ids.save_wheel.background_down = self.drop_down_button_theme_white_background_down
            self.ids.save_wheel.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.save_wheel.color = self.black

            self.ids.minute_0_off.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_0_off.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_0_off.color = self.black

            self.ids.minute_5.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_5.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_5.color = self.black

            self.ids.minute_10.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_10.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_10.color = self.black

            self.ids.minute_15.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_15.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_15.color = self.black

            self.ids.minute_20.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_20.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_20.color = self.black

            self.ids.minute_30.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_30.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_30.color = self.black

            self.ids.minute_45.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_45.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_45.color = self.black

            self.ids.minute_60.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_60.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_60.color = self.black

            self.ids.minute_90.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_90.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_90.color = self.black

            self.ids.minute_120.background_down = self.drop_down_button_theme_white_background_down
            self.ids.minute_120.background_normal = self.drop_down_button_theme_white_background_normal
            self.ids.minute_120.color = self.black

            self.button_confirm.background_color = [1, 1, 1, 0]
            self.button_confirm.color = [0, 0, 0, 1]
            self.button_confirm.text = ""

            self.ids.orientation_of_wheel.source = self.orientation_black
            self.ids.orientation_of_wheel_name.color = self.black
            self.ids.orientation_of_wheel_name.background_color = self.white

            self.theme = 1
        else:
            Window.clearcolor = get_color_from_hex("#000000")  # window color change to black
            self.ids.day_night.source = self.night  # sun/moon ka image change kartay hai
            # self.ids.menu.source = self.menu_night  # menu ka image change to black
            self.ids.add_image.background_color = self.black  # plus sign
            self.ids.add_image.color = self.white_without_opacity  # plus sign
            self.ids.sub_image.background_color = self.black  # minus sign
            self.ids.sub_image.color = self.white_without_opacity  # minus sign
            self.ids.slot_number.color = self.white_without_opacity  # screen top may 3 ka color change
            self.ids.slot_number.background_color = self.black  # screen top may 3 ka bg color change
            self.ids.slots.color = self.white_without_opacity  # text writtern slots uska color change
            self.ids.slots.background_color = self.black  # text writtern slots uska bg color change
            self.indicator.source = self.indicator_white  # indicator color change kiyeah hai
            self.ids.save.source = self.save_white  # save button ka source change
            # self.ids.menu_name.color = self.white_without_opacity  # text menu ka color change karta hai
            # self.ids.menu_name.background_color = self.black  # textmenu ka bg color change karta hai
            self.ids.day_night_name.color = self.white_without_opacity  # day/night text ka color change karta hai
            self.ids.day_night_name.background_color = self.black  # day/night ka bg color change karta hai
            # reminder ka image change based on the theme
            self.ids.reminder.source = self.reminder_white  # reminder button  ka source change karta hai
            # "Save" written below save button uska color change w.r.t theme
            self.ids.save_name.color = self.white_without_opacity  # without opacity means without transparance
            # of its background
            self.ids.save_name.background_color = self.black  # save text ka bg color change karta hai
            # "Reminder" written below reminder button uska color change w.r.t theme
            self.ids.reminder_name.color = self.white_without_opacity  # reminder name ka text color change karta hai
            self.ids.reminder_name.background_color = self.black  # here background of reminder is changed

            self.ids.save_wheel_1.background_down = self.drop_down_button_theme_black_background_down
            self.ids.save_wheel_1.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.save_wheel_1.color = self.white_without_opacity

            self.ids.save_wheel_2.background_down = self.drop_down_button_theme_black_background_down
            self.ids.save_wheel_2.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.save_wheel_2.color = self.white_without_opacity

            self.ids.save_wheel_3.background_down = self.drop_down_button_theme_black_background_down
            self.ids.save_wheel_3.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.save_wheel_3.color = self.white_without_opacity

            self.ids.delete_1.background_down = self.drop_down_button_theme_black_background_down
            self.ids.delete_1.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.delete_1.color = self.white_without_opacity

            self.ids.delete_2.background_down = self.drop_down_button_theme_black_background_down
            self.ids.delete_2.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.delete_2.color = self.white_without_opacity

            self.ids.delete_3.background_down = self.drop_down_button_theme_black_background_down
            self.ids.delete_3.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.delete_3.color = self.white_without_opacity

            self.ids.save_wheel.background_down = self.drop_down_button_theme_black_background_down
            self.ids.save_wheel.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.save_wheel.color = self.white_without_opacity

            self.ids.minute_0_off.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_0_off.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_0_off.color = self.white_without_opacity

            self.ids.minute_5.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_5.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_5.color = self.white_without_opacity

            self.ids.minute_10.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_10.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_10.color = self.white_without_opacity

            self.ids.minute_15.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_15.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_15.color = self.white_without_opacity

            self.ids.minute_20.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_20.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_20.color = self.white_without_opacity

            self.ids.minute_30.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_30.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_30.color = self.white_without_opacity

            self.ids.minute_45.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_45.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_45.color = self.white_without_opacity

            self.ids.minute_60.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_60.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_60.color = self.white_without_opacity

            self.ids.minute_90.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_90.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_90.color = self.white_without_opacity

            self.ids.minute_120.background_down = self.drop_down_button_theme_black_background_down
            self.ids.minute_120.background_normal = self.drop_down_button_theme_black_background_normal
            self.ids.minute_120.color = self.white_without_opacity

            self.button_confirm.background_color = [0, 0, 0, 0]
            self.button_confirm.color = [1, 1, 1, 1]
            self.button_confirm.text = ""

            self.ids.orientation_of_wheel.source = self.orientation_white
            self.ids.orientation_of_wheel_name.color = self.white_without_opacity
            self.ids.orientation_of_wheel_name.background_color = self.black

            self.theme = 0

        pass

    def add_textbox_for_3(self):
        self.ids.wheel_number.add_widget(self.textinput_3_1)
        self.ids.wheel_number.add_widget(self.textinput_3_2)
        self.ids.wheel_number.add_widget(self.textinput_3_3)
        wheel_3_non_widget = [self.textinput_4_1, self.textinput_4_2, self.textinput_4_3, self.textinput_4_4,
                              self.textinput_5_1, self.textinput_5_2, self.textinput_5_3, self.textinput_5_4,
                              self.textinput_5_5, self.textinput_6_1, self.textinput_6_2, self.textinput_6_3,
                              self.textinput_6_4, self.textinput_6_5, self.textinput_6_6, self.textinput_7_1,
                              self.textinput_7_2, self.textinput_7_3, self.textinput_7_4, self.textinput_7_5,
                              self.textinput_7_6, self.textinput_7_7, self.textinput_8_1, self.textinput_8_2,
                              self.textinput_8_3, self.textinput_8_4, self.textinput_8_5, self.textinput_8_6,
                              self.textinput_8_7, self.textinput_8_8, self.textinput_9_1, self.textinput_9_2,
                              self.textinput_9_3, self.textinput_9_4, self.textinput_9_5, self.textinput_9_6,
                              self.textinput_9_7, self.textinput_9_8, self.textinput_9_9, self.textinput_10_1,
                              self.textinput_10_2, self.textinput_10_3, self.textinput_10_4, self.textinput_10_5,
                              self.textinput_10_6, self.textinput_10_7, self.textinput_10_8, self.textinput_10_9,
                              self.textinput_10_10, self.textinput_11_1, self.textinput_11_2, self.textinput_11_3,
                              self.textinput_11_4, self.textinput_11_5, self.textinput_11_6, self.textinput_11_7,
                              self.textinput_11_8, self.textinput_11_9, self.textinput_11_10, self.textinput_11_11,
                              self.textinput_12_1, self.textinput_12_2, self.textinput_12_3, self.textinput_12_4,
                              self.textinput_12_5, self.textinput_12_6, self.textinput_12_7, self.textinput_12_8,
                              self.textinput_12_9, self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_3_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_4(self):
        self.ids.wheel_number.add_widget(self.textinput_4_1)
        self.ids.wheel_number.add_widget(self.textinput_4_2)
        self.ids.wheel_number.add_widget(self.textinput_4_3)
        self.ids.wheel_number.add_widget(self.textinput_4_4)
        wheel_4_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_5_1,
                              self.textinput_5_2, self.textinput_5_3, self.textinput_5_4, self.textinput_5_5,
                              self.textinput_6_1, self.textinput_6_2, self.textinput_6_3, self.textinput_6_4,
                              self.textinput_6_5, self.textinput_6_6, self.textinput_7_1, self.textinput_7_2,
                              self.textinput_7_3, self.textinput_7_4, self.textinput_7_5, self.textinput_7_6,
                              self.textinput_7_7, self.textinput_8_1, self.textinput_8_2, self.textinput_8_3,
                              self.textinput_8_4, self.textinput_8_5, self.textinput_8_6, self.textinput_8_7,
                              self.textinput_8_8, self.textinput_9_1, self.textinput_9_2, self.textinput_9_3,
                              self.textinput_9_4, self.textinput_9_5, self.textinput_9_6, self.textinput_9_7,
                              self.textinput_9_8, self.textinput_9_9, self.textinput_10_1, self.textinput_10_2,
                              self.textinput_10_3, self.textinput_10_4, self.textinput_10_5, self.textinput_10_6,
                              self.textinput_10_7, self.textinput_10_8, self.textinput_10_9, self.textinput_10_10,
                              self.textinput_11_1, self.textinput_11_2, self.textinput_11_3, self.textinput_11_4,
                              self.textinput_11_5, self.textinput_11_6, self.textinput_11_7, self.textinput_11_8,
                              self.textinput_11_9, self.textinput_11_10, self.textinput_11_11, self.textinput_12_1,
                              self.textinput_12_2, self.textinput_12_3, self.textinput_12_4, self.textinput_12_5,
                              self.textinput_12_6, self.textinput_12_7, self.textinput_12_8, self.textinput_12_9,
                              self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_4_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_5(self):
        self.ids.wheel_number.add_widget(self.textinput_5_1)
        self.ids.wheel_number.add_widget(self.textinput_5_2)
        self.ids.wheel_number.add_widget(self.textinput_5_3)
        self.ids.wheel_number.add_widget(self.textinput_5_4)
        self.ids.wheel_number.add_widget(self.textinput_5_5)
        wheel_5_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_4_1,
                              self.textinput_4_2, self.textinput_4_3, self.textinput_4_4,
                              self.textinput_6_1, self.textinput_6_2, self.textinput_6_3, self.textinput_6_4,
                              self.textinput_6_5, self.textinput_6_6, self.textinput_7_1, self.textinput_7_2,
                              self.textinput_7_3, self.textinput_7_4, self.textinput_7_5, self.textinput_7_6,
                              self.textinput_7_7, self.textinput_8_1, self.textinput_8_2, self.textinput_8_3,
                              self.textinput_8_4, self.textinput_8_5, self.textinput_8_6, self.textinput_8_7,
                              self.textinput_8_8, self.textinput_9_1, self.textinput_9_2, self.textinput_9_3,
                              self.textinput_9_4, self.textinput_9_5, self.textinput_9_6, self.textinput_9_7,
                              self.textinput_9_8, self.textinput_9_9, self.textinput_10_1, self.textinput_10_2,
                              self.textinput_10_3, self.textinput_10_4, self.textinput_10_5, self.textinput_10_6,
                              self.textinput_10_7, self.textinput_10_8, self.textinput_10_9, self.textinput_10_10,
                              self.textinput_11_1, self.textinput_11_2, self.textinput_11_3, self.textinput_11_4,
                              self.textinput_11_5, self.textinput_11_6, self.textinput_11_7, self.textinput_11_8,
                              self.textinput_11_9, self.textinput_11_10, self.textinput_11_11, self.textinput_12_1,
                              self.textinput_12_2, self.textinput_12_3, self.textinput_12_4, self.textinput_12_5,
                              self.textinput_12_6, self.textinput_12_7, self.textinput_12_8, self.textinput_12_9,
                              self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_5_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_6(self):
        self.ids.wheel_number.add_widget(self.textinput_6_1)
        self.ids.wheel_number.add_widget(self.textinput_6_2)
        self.ids.wheel_number.add_widget(self.textinput_6_3)
        self.ids.wheel_number.add_widget(self.textinput_6_4)
        self.ids.wheel_number.add_widget(self.textinput_6_5)
        self.ids.wheel_number.add_widget(self.textinput_6_6)
        wheel_6_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_4_1,
                              self.textinput_4_2, self.textinput_4_3, self.textinput_4_4, self.textinput_5_1,
                              self.textinput_5_2, self.textinput_5_3, self.textinput_5_4, self.textinput_5_5,
                              self.textinput_7_1, self.textinput_7_2,
                              self.textinput_7_3, self.textinput_7_4, self.textinput_7_5, self.textinput_7_6,
                              self.textinput_7_7, self.textinput_8_1, self.textinput_8_2, self.textinput_8_3,
                              self.textinput_8_4, self.textinput_8_5, self.textinput_8_6, self.textinput_8_7,
                              self.textinput_8_8, self.textinput_9_1, self.textinput_9_2, self.textinput_9_3,
                              self.textinput_9_4, self.textinput_9_5, self.textinput_9_6, self.textinput_9_7,
                              self.textinput_9_8, self.textinput_9_9, self.textinput_10_1, self.textinput_10_2,
                              self.textinput_10_3, self.textinput_10_4, self.textinput_10_5, self.textinput_10_6,
                              self.textinput_10_7, self.textinput_10_8, self.textinput_10_9, self.textinput_10_10,
                              self.textinput_11_1, self.textinput_11_2, self.textinput_11_3, self.textinput_11_4,
                              self.textinput_11_5, self.textinput_11_6, self.textinput_11_7, self.textinput_11_8,
                              self.textinput_11_9, self.textinput_11_10, self.textinput_11_11, self.textinput_12_1,
                              self.textinput_12_2, self.textinput_12_3, self.textinput_12_4, self.textinput_12_5,
                              self.textinput_12_6, self.textinput_12_7, self.textinput_12_8, self.textinput_12_9,
                              self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_6_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_7(self):
        self.ids.wheel_number.add_widget(self.textinput_7_1)
        self.ids.wheel_number.add_widget(self.textinput_7_2)
        self.ids.wheel_number.add_widget(self.textinput_7_3)
        self.ids.wheel_number.add_widget(self.textinput_7_4)
        self.ids.wheel_number.add_widget(self.textinput_7_5)
        self.ids.wheel_number.add_widget(self.textinput_7_6)
        self.ids.wheel_number.add_widget(self.textinput_7_7)
        wheel_7_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_4_1,
                              self.textinput_4_2, self.textinput_4_3, self.textinput_4_4, self.textinput_5_1,
                              self.textinput_5_2, self.textinput_5_3, self.textinput_5_4, self.textinput_5_5,
                              self.textinput_6_1, self.textinput_6_2, self.textinput_6_3, self.textinput_6_4,
                              self.textinput_6_5, self.textinput_6_6, self.textinput_8_1, self.textinput_8_2,
                              self.textinput_8_3,
                              self.textinput_8_4, self.textinput_8_5, self.textinput_8_6, self.textinput_8_7,
                              self.textinput_8_8, self.textinput_9_1, self.textinput_9_2, self.textinput_9_3,
                              self.textinput_9_4, self.textinput_9_5, self.textinput_9_6, self.textinput_9_7,
                              self.textinput_9_8, self.textinput_9_9, self.textinput_10_1, self.textinput_10_2,
                              self.textinput_10_3, self.textinput_10_4, self.textinput_10_5, self.textinput_10_6,
                              self.textinput_10_7, self.textinput_10_8, self.textinput_10_9, self.textinput_10_10,
                              self.textinput_11_1, self.textinput_11_2, self.textinput_11_3, self.textinput_11_4,
                              self.textinput_11_5, self.textinput_11_6, self.textinput_11_7, self.textinput_11_8,
                              self.textinput_11_9, self.textinput_11_10, self.textinput_11_11, self.textinput_12_1,
                              self.textinput_12_2, self.textinput_12_3, self.textinput_12_4, self.textinput_12_5,
                              self.textinput_12_6, self.textinput_12_7, self.textinput_12_8, self.textinput_12_9,
                              self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_7_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_8(self):
        self.ids.wheel_number.add_widget(self.textinput_8_1)
        self.ids.wheel_number.add_widget(self.textinput_8_2)
        self.ids.wheel_number.add_widget(self.textinput_8_3)
        self.ids.wheel_number.add_widget(self.textinput_8_4)
        self.ids.wheel_number.add_widget(self.textinput_8_5)
        self.ids.wheel_number.add_widget(self.textinput_8_6)
        self.ids.wheel_number.add_widget(self.textinput_8_7)
        self.ids.wheel_number.add_widget(self.textinput_8_8)
        wheel_8_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_4_1,
                              self.textinput_4_2, self.textinput_4_3, self.textinput_4_4, self.textinput_5_1,
                              self.textinput_5_2, self.textinput_5_3, self.textinput_5_4, self.textinput_5_5,
                              self.textinput_6_1, self.textinput_6_2, self.textinput_6_3, self.textinput_6_4,
                              self.textinput_6_5, self.textinput_6_6, self.textinput_7_1, self.textinput_7_2,
                              self.textinput_7_3, self.textinput_7_4, self.textinput_7_5, self.textinput_7_6,
                              self.textinput_7_7, self.textinput_9_1, self.textinput_9_2, self.textinput_9_3,
                              self.textinput_9_4, self.textinput_9_5, self.textinput_9_6, self.textinput_9_7,
                              self.textinput_9_8, self.textinput_9_9, self.textinput_10_1, self.textinput_10_2,
                              self.textinput_10_3, self.textinput_10_4, self.textinput_10_5, self.textinput_10_6,
                              self.textinput_10_7, self.textinput_10_8, self.textinput_10_9, self.textinput_10_10,
                              self.textinput_11_1, self.textinput_11_2, self.textinput_11_3, self.textinput_11_4,
                              self.textinput_11_5, self.textinput_11_6, self.textinput_11_7, self.textinput_11_8,
                              self.textinput_11_9, self.textinput_11_10, self.textinput_11_11, self.textinput_12_1,
                              self.textinput_12_2, self.textinput_12_3, self.textinput_12_4, self.textinput_12_5,
                              self.textinput_12_6, self.textinput_12_7, self.textinput_12_8, self.textinput_12_9,
                              self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_8_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_9(self):
        self.ids.wheel_number.add_widget(self.textinput_9_1)
        self.ids.wheel_number.add_widget(self.textinput_9_2)
        self.ids.wheel_number.add_widget(self.textinput_9_3)
        self.ids.wheel_number.add_widget(self.textinput_9_4)
        self.ids.wheel_number.add_widget(self.textinput_9_5)
        self.ids.wheel_number.add_widget(self.textinput_9_6)
        self.ids.wheel_number.add_widget(self.textinput_9_7)
        self.ids.wheel_number.add_widget(self.textinput_9_8)
        self.ids.wheel_number.add_widget(self.textinput_9_9)
        wheel_9_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_4_1,
                              self.textinput_4_2, self.textinput_4_3, self.textinput_4_4, self.textinput_5_1,
                              self.textinput_5_2, self.textinput_5_3, self.textinput_5_4, self.textinput_5_5,
                              self.textinput_6_1, self.textinput_6_2, self.textinput_6_3, self.textinput_6_4,
                              self.textinput_6_5, self.textinput_6_6, self.textinput_7_1, self.textinput_7_2,
                              self.textinput_7_3, self.textinput_7_4, self.textinput_7_5, self.textinput_7_6,
                              self.textinput_7_7, self.textinput_8_1, self.textinput_8_2, self.textinput_8_3,
                              self.textinput_8_4, self.textinput_8_5, self.textinput_8_6, self.textinput_8_7,
                              self.textinput_8_8, self.textinput_10_1, self.textinput_10_2,
                              self.textinput_10_3, self.textinput_10_4, self.textinput_10_5, self.textinput_10_6,
                              self.textinput_10_7, self.textinput_10_8, self.textinput_10_9, self.textinput_10_10,
                              self.textinput_11_1, self.textinput_11_2, self.textinput_11_3, self.textinput_11_4,
                              self.textinput_11_5, self.textinput_11_6, self.textinput_11_7, self.textinput_11_8,
                              self.textinput_11_9, self.textinput_11_10, self.textinput_11_11, self.textinput_12_1,
                              self.textinput_12_2, self.textinput_12_3, self.textinput_12_4, self.textinput_12_5,
                              self.textinput_12_6, self.textinput_12_7, self.textinput_12_8, self.textinput_12_9,
                              self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_9_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_10(self):
        self.ids.wheel_number.add_widget(self.textinput_10_1)
        self.ids.wheel_number.add_widget(self.textinput_10_2)
        self.ids.wheel_number.add_widget(self.textinput_10_3)
        self.ids.wheel_number.add_widget(self.textinput_10_4)
        self.ids.wheel_number.add_widget(self.textinput_10_5)
        self.ids.wheel_number.add_widget(self.textinput_10_6)
        self.ids.wheel_number.add_widget(self.textinput_10_7)
        self.ids.wheel_number.add_widget(self.textinput_10_8)
        self.ids.wheel_number.add_widget(self.textinput_10_9)
        self.ids.wheel_number.add_widget(self.textinput_10_10)
        wheel_10_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_4_1,
                               self.textinput_4_2, self.textinput_4_3, self.textinput_4_4, self.textinput_5_1,
                               self.textinput_5_2, self.textinput_5_3, self.textinput_5_4, self.textinput_5_5,
                               self.textinput_6_1, self.textinput_6_2, self.textinput_6_3, self.textinput_6_4,
                               self.textinput_6_5, self.textinput_6_6, self.textinput_7_1, self.textinput_7_2,
                               self.textinput_7_3, self.textinput_7_4, self.textinput_7_5, self.textinput_7_6,
                               self.textinput_7_7, self.textinput_8_1, self.textinput_8_2, self.textinput_8_3,
                               self.textinput_8_4, self.textinput_8_5, self.textinput_8_6, self.textinput_8_7,
                               self.textinput_8_8, self.textinput_9_1, self.textinput_9_2, self.textinput_9_3,
                               self.textinput_9_4, self.textinput_9_5, self.textinput_9_6, self.textinput_9_7,
                               self.textinput_9_8, self.textinput_9_9,
                               self.textinput_11_1, self.textinput_11_2, self.textinput_11_3, self.textinput_11_4,
                               self.textinput_11_5, self.textinput_11_6, self.textinput_11_7, self.textinput_11_8,
                               self.textinput_11_9, self.textinput_11_10, self.textinput_11_11, self.textinput_12_1,
                               self.textinput_12_2, self.textinput_12_3, self.textinput_12_4, self.textinput_12_5,
                               self.textinput_12_6, self.textinput_12_7, self.textinput_12_8, self.textinput_12_9,
                               self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_10_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_11(self):
        self.ids.wheel_number.add_widget(self.textinput_11_1)
        self.ids.wheel_number.add_widget(self.textinput_11_2)
        self.ids.wheel_number.add_widget(self.textinput_11_3)
        self.ids.wheel_number.add_widget(self.textinput_11_4)
        self.ids.wheel_number.add_widget(self.textinput_11_5)
        self.ids.wheel_number.add_widget(self.textinput_11_6)
        self.ids.wheel_number.add_widget(self.textinput_11_7)
        self.ids.wheel_number.add_widget(self.textinput_11_8)
        self.ids.wheel_number.add_widget(self.textinput_11_9)
        self.ids.wheel_number.add_widget(self.textinput_11_10)
        self.ids.wheel_number.add_widget(self.textinput_11_11)
        wheel_11_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_4_1,
                               self.textinput_4_2, self.textinput_4_3, self.textinput_4_4, self.textinput_5_1,
                               self.textinput_5_2, self.textinput_5_3, self.textinput_5_4, self.textinput_5_5,
                               self.textinput_6_1, self.textinput_6_2, self.textinput_6_3, self.textinput_6_4,
                               self.textinput_6_5, self.textinput_6_6, self.textinput_7_1, self.textinput_7_2,
                               self.textinput_7_3, self.textinput_7_4, self.textinput_7_5, self.textinput_7_6,
                               self.textinput_7_7, self.textinput_8_1, self.textinput_8_2, self.textinput_8_3,
                               self.textinput_8_4, self.textinput_8_5, self.textinput_8_6, self.textinput_8_7,
                               self.textinput_8_8, self.textinput_9_1, self.textinput_9_2, self.textinput_9_3,
                               self.textinput_9_4, self.textinput_9_5, self.textinput_9_6, self.textinput_9_7,
                               self.textinput_9_8, self.textinput_9_9, self.textinput_10_1, self.textinput_10_2,
                               self.textinput_10_3, self.textinput_10_4, self.textinput_10_5, self.textinput_10_6,
                               self.textinput_10_7, self.textinput_10_8, self.textinput_10_9, self.textinput_10_10,
                               self.textinput_12_1,
                               self.textinput_12_2, self.textinput_12_3, self.textinput_12_4, self.textinput_12_5,
                               self.textinput_12_6, self.textinput_12_7, self.textinput_12_8, self.textinput_12_9,
                               self.textinput_12_10, self.textinput_12_11, self.textinput_12_12]
        for i in wheel_11_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def add_textbox_for_12(self):
        self.ids.wheel_number.add_widget(self.textinput_12_1)
        self.ids.wheel_number.add_widget(self.textinput_12_2)
        self.ids.wheel_number.add_widget(self.textinput_12_3)
        self.ids.wheel_number.add_widget(self.textinput_12_4)
        self.ids.wheel_number.add_widget(self.textinput_12_5)
        self.ids.wheel_number.add_widget(self.textinput_12_6)
        self.ids.wheel_number.add_widget(self.textinput_12_7)
        self.ids.wheel_number.add_widget(self.textinput_12_8)
        self.ids.wheel_number.add_widget(self.textinput_12_9)
        self.ids.wheel_number.add_widget(self.textinput_12_10)
        self.ids.wheel_number.add_widget(self.textinput_12_11)
        self.ids.wheel_number.add_widget(self.textinput_12_12)
        wheel_12_non_widget = [self.textinput_3_1, self.textinput_3_2, self.textinput_3_3, self.textinput_4_1,
                               self.textinput_4_2, self.textinput_4_3, self.textinput_4_4, self.textinput_5_1,
                               self.textinput_5_2, self.textinput_5_3, self.textinput_5_4, self.textinput_5_5,
                               self.textinput_6_1, self.textinput_6_2, self.textinput_6_3, self.textinput_6_4,
                               self.textinput_6_5, self.textinput_6_6, self.textinput_7_1, self.textinput_7_2,
                               self.textinput_7_3, self.textinput_7_4, self.textinput_7_5, self.textinput_7_6,
                               self.textinput_7_7, self.textinput_8_1, self.textinput_8_2, self.textinput_8_3,
                               self.textinput_8_4, self.textinput_8_5, self.textinput_8_6, self.textinput_8_7,
                               self.textinput_8_8, self.textinput_9_1, self.textinput_9_2, self.textinput_9_3,
                               self.textinput_9_4, self.textinput_9_5, self.textinput_9_6, self.textinput_9_7,
                               self.textinput_9_8, self.textinput_9_9, self.textinput_10_1, self.textinput_10_2,
                               self.textinput_10_3, self.textinput_10_4, self.textinput_10_5, self.textinput_10_6,
                               self.textinput_10_7, self.textinput_10_8, self.textinput_10_9, self.textinput_10_10,
                               self.textinput_11_1, self.textinput_11_2, self.textinput_11_3, self.textinput_11_4,
                               self.textinput_11_5, self.textinput_11_6, self.textinput_11_7, self.textinput_11_8,
                               self.textinput_11_9, self.textinput_11_10, self.textinput_11_11]
        for i in wheel_12_non_widget:
            self.ids.wheel_number.remove_widget(i)
        return

    def clear_screen(self):
        if self.start_stop.text == "[size=60]Start[/size]":
            if int(self.ids.slot_number.text) == 3:
                self.textinput_3_1.text = ""
                self.textinput_3_2.text = ""
                self.textinput_3_3.text = ""
            elif int(self.ids.slot_number.text) == 4:
                self.textinput_4_1.text = ""
                self.textinput_4_2.text = ""
                self.textinput_4_3.text = ""
                self.textinput_4_4.text = ""
            elif int(self.ids.slot_number.text) == 5:
                self.textinput_5_1.text = ""
                self.textinput_5_2.text = ""
                self.textinput_5_3.text = ""
                self.textinput_5_4.text = ""
                self.textinput_5_5.text = ""
            elif int(self.ids.slot_number.text) == 6:
                self.textinput_6_1.text = ""
                self.textinput_6_2.text = ""
                self.textinput_6_3.text = ""
                self.textinput_6_4.text = ""
                self.textinput_6_5.text = ""
                self.textinput_6_6.text = ""
            elif int(self.ids.slot_number.text) == 7:
                self.textinput_7_1.text = ""
                self.textinput_7_2.text = ""
                self.textinput_7_3.text = ""
                self.textinput_7_4.text = ""
                self.textinput_7_5.text = ""
                self.textinput_7_6.text = ""
                self.textinput_7_7.text = ""
            elif int(self.ids.slot_number.text) == 8:
                self.textinput_8_1.text = ""
                self.textinput_8_2.text = ""
                self.textinput_8_3.text = ""
                self.textinput_8_4.text = ""
                self.textinput_8_5.text = ""
                self.textinput_8_6.text = ""
                self.textinput_8_7.text = ""
                self.textinput_8_8.text = ""
            elif int(self.ids.slot_number.text) == 9:
                self.textinput_9_1.text = ""
                self.textinput_9_2.text = ""
                self.textinput_9_3.text = ""
                self.textinput_9_4.text = ""
                self.textinput_9_5.text = ""
                self.textinput_9_6.text = ""
                self.textinput_9_7.text = ""
                self.textinput_9_8.text = ""
                self.textinput_9_9.text = ""
            elif int(self.ids.slot_number.text) == 10:
                self.textinput_10_1.text = ""
                self.textinput_10_2.text = ""
                self.textinput_10_3.text = ""
                self.textinput_10_4.text = ""
                self.textinput_10_5.text = ""
                self.textinput_10_6.text = ""
                self.textinput_10_7.text = ""
                self.textinput_10_8.text = ""
                self.textinput_10_9.text = ""
                self.textinput_10_10.text = ""
            elif int(self.ids.slot_number.text) == 11:
                self.textinput_11_1.text = ""
                self.textinput_11_2.text = ""
                self.textinput_11_3.text = ""
                self.textinput_11_4.text = ""
                self.textinput_11_5.text = ""
                self.textinput_11_6.text = ""
                self.textinput_11_7.text = ""
                self.textinput_11_8.text = ""
                self.textinput_11_9.text = ""
                self.textinput_11_10.text = ""
                self.textinput_11_11.text = ""
            elif int(self.ids.slot_number.text) == 12:
                self.textinput_12_1.text = ""
                self.textinput_12_2.text = ""
                self.textinput_12_3.text = ""
                self.textinput_12_4.text = ""
                self.textinput_12_5.text = ""
                self.textinput_12_6.text = ""
                self.textinput_12_7.text = ""
                self.textinput_12_8.text = ""
                self.textinput_12_9.text = ""
                self.textinput_12_10.text = ""
                self.textinput_12_11.text = ""
                self.textinput_12_12.text = ""
            return
        else:
            self.button_confirm.text = "Can't CLEAR while wheel is spinning"
            if self.theme == 0:
                self.animate_the_confirm_white_to_black_text()
            else:
                self.animate_the_confirm_black_to_white_text()

    def saving_wheel_1(self):
        self.ids.drop.dismiss()
        if self.theme == 0:
            self.button_confirm.text = self.ids.save_wheel_1.text
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            self.save_wheel_1_open()
        else:
            self.button_confirm.text = self.ids.save_wheel_1.text
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            self.save_wheel_1_open()
        pass

    def save_wheel_1_open(self):
        self.delete_1_point = 0
        if str(self.ids.save_wheel_1.text) != 'No item saved':
            # save_wheel_1 = open("save_wheel_1.txt", "r")
            # self.list_for_save_wheel_1.clear()
            # for line in save_wheel_1:
            #     self.list_for_save_wheel_1.append(line[:-1])
            # print(self.list_for_save_wheel_1)
            # save_wheel_1.close()
            if str(self.ids.save_wheel_1.text) == "3rd slot added":
                if int(self.ids.slot_number.text) == 3 and str(self.textinput_3_1.text) == "" and str(
                        self.textinput_3_2.text) == "" and str(self.textinput_3_3.text) == "":
                    self.textinput_3_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_3_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_3_3.text = self.list_for_save_wheel_1[2]
                    pass
                elif int(self.ids.slot_number.text) == 3 and str(self.textinput_3_1.text) != "" and str(
                        self.textinput_3_2.text) != "" and str(self.textinput_3_3.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel3
                    self.add_textbox_for_3()
                    self.ids.slot_number.text = "3"
                    self.textinput_3_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_3_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_3_3.text = self.list_for_save_wheel_1[2]
            elif str(self.ids.save_wheel_1.text) == "4th slot added":
                if int(self.ids.slot_number.text) == 4 and str(self.textinput_4_1.text) == "" and str(
                        self.textinput_4_2.text) == "" and str(self.textinput_4_3.text) == "" and str(
                        self.textinput_4_4.text) == "":
                    self.textinput_4_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_4_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_4_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_4_4.text = self.list_for_save_wheel_1[3]
                elif int(self.ids.slot_number.text) == 4 and str(self.textinput_4_1.text) != "" and str(
                        self.textinput_4_2.text) != "" and str(self.textinput_4_3.text) != "" and str(
                        self.textinput_4_4.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel4
                    self.add_textbox_for_4()
                    self.ids.slot_number.text = "4"
                    self.textinput_4_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_4_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_4_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_4_4.text = self.list_for_save_wheel_1[3]
            elif str(self.ids.save_wheel_1.text) == "5th slot added":
                if int(self.ids.slot_number.text) == 5 and str(self.textinput_5_1.text) == "" and str(
                        self.textinput_5_2.text) == "" and str(self.textinput_5_3.text) == "" and str(
                        self.textinput_5_4.text) == "" and str(self.textinput_5_5.text) == "":
                    self.textinput_5_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_5_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_5_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_5_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_5_5.text = self.list_for_save_wheel_1[4]
                elif int(self.ids.slot_number.text) == 5 and str(self.textinput_5_1.text) != "" and str(
                        self.textinput_5_2.text) != "" and str(self.textinput_5_3.text) != "" and str(
                        self.textinput_5_4.text) != "" and str(self.textinput_5_5.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel5
                    self.add_textbox_for_5()
                    self.ids.slot_number.text = "5"
                    self.textinput_5_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_5_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_5_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_5_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_5_5.text = self.list_for_save_wheel_1[4]
            elif str(self.ids.save_wheel_1.text) == "6th slot added":
                if int(self.ids.slot_number.text) == 6 and str(self.textinput_6_1.text) == "" and str(
                        self.textinput_6_2.text) == "" and str(self.textinput_6_3.text) == "" and str(
                        self.textinput_6_4.text) == "" and str(self.textinput_6_5.text) == "" and str(
                        self.textinput_6_6.text == ""):
                    self.textinput_6_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_6_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_6_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_6_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_6_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_6_6.text = self.list_for_save_wheel_1[5]
                elif int(self.ids.slot_number.text) == 6 and str(self.textinput_6_1.text) != "" and str(
                        self.textinput_6_2.text) != "" and str(self.textinput_6_3.text) != "" and str(
                        self.textinput_6_4.text) != "" and str(self.textinput_6_5.text) != "" and str(
                        self.textinput_6_6.text != ""):
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel6
                    self.add_textbox_for_6()
                    self.ids.slot_number.text = "6"
                    self.textinput_6_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_6_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_6_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_6_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_6_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_6_6.text = self.list_for_save_wheel_1[5]
            elif str(self.ids.save_wheel_1.text) == "7th slot added":
                if int(self.ids.slot_number.text) == 7 and str(self.textinput_7_1.text) == "" and str(
                        self.textinput_7_2.text) == "" and str(self.textinput_7_3.text) == "" and str(
                        self.textinput_7_4.text) == "" and str(self.textinput_7_5.text) == "" and str(
                        self.textinput_7_6.text) == "" and str(self.textinput_7_7.text) == "":
                    self.textinput_7_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_7_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_7_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_7_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_7_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_7_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_7_7.text = self.list_for_save_wheel_1[6]
                elif int(self.ids.slot_number.text) == 7 and str(self.textinput_7_1.text) != "" and str(
                        self.textinput_7_2.text) != "" and str(self.textinput_7_3.text) != "" and str(
                        self.textinput_7_4.text) != "" and str(self.textinput_7_5.text) != "" and str(
                        self.textinput_7_6.text) != "" and str(self.textinput_7_7.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel7
                    self.add_textbox_for_7()
                    self.ids.slot_number.text = "7"
                    self.textinput_7_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_7_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_7_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_7_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_7_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_7_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_7_7.text = self.list_for_save_wheel_1[6]
            elif str(self.ids.save_wheel_1.text) == "8th slot added":
                if int(self.ids.slot_number.text) == 8 and str(self.textinput_8_1.text) == "" and str(
                        self.textinput_8_2.text) == "" and str(self.textinput_8_3.text) == "" and str(
                        self.textinput_8_4.text) == "" and str(self.textinput_8_5.text) == "" and str(
                        self.textinput_8_6.text) == "" and str(self.textinput_8_7.text) == "" and str(
                        self.textinput_8_8.text) == "":
                    self.textinput_8_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_8_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_8_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_8_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_8_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_8_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_8_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_8_8.text = self.list_for_save_wheel_1[7]
                elif int(self.ids.slot_number.text) == 8 and str(self.textinput_8_1.text) != "" and str(
                        self.textinput_8_2.text) != "" and str(self.textinput_8_3.text) != "" and str(
                        self.textinput_8_4.text) != "" and str(self.textinput_8_5.text) != "" and str(
                        self.textinput_8_6.text) != "" and str(self.textinput_8_7.text) != "" and str(
                        self.textinput_8_8.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel8
                    self.add_textbox_for_8()
                    self.ids.slot_number.text = "8"
                    self.textinput_8_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_8_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_8_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_8_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_8_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_8_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_8_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_8_8.text = self.list_for_save_wheel_1[7]
            elif str(self.ids.save_wheel_1.text) == "9th slot added":
                if int(self.ids.slot_number.text) == 9 and str(self.textinput_9_1.text) == "" and str(
                        self.textinput_9_2.text) == "" and str(self.textinput_9_3.text) == "" and str(
                        self.textinput_9_4.text) == "" and str(self.textinput_9_5.text) == "" and str(
                        self.textinput_9_6.text) == "" and str(self.textinput_9_7.text) == "" and str(
                        self.textinput_9_8.text) == "" and str(self.textinput_9_9.text) == "":
                    self.textinput_9_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_9_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_9_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_9_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_9_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_9_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_9_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_9_8.text = self.list_for_save_wheel_1[7]
                    self.textinput_9_9.text = self.list_for_save_wheel_1[8]
                elif int(self.ids.slot_number.text) == 9 and str(self.textinput_9_1.text) != "" and str(
                        self.textinput_9_2.text) != "" and str(self.textinput_9_3.text) != "" and str(
                        self.textinput_9_4.text) != "" and str(self.textinput_9_5.text) != "" and str(
                        self.textinput_9_6.text) != "" and str(self.textinput_9_7.text) != "" and str(
                        self.textinput_9_8.text) != "" and str(self.textinput_9_9.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel9
                    self.add_textbox_for_9()
                    self.ids.slot_number.text = "9"
                    self.textinput_9_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_9_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_9_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_9_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_9_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_9_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_9_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_9_8.text = self.list_for_save_wheel_1[7]
                    self.textinput_9_9.text = self.list_for_save_wheel_1[8]
            elif str(self.ids.save_wheel_1.text) == "10th slot added":
                if int(self.ids.slot_number.text) == 10 and str(self.textinput_10_1.text) == "" and str(
                        self.textinput_10_2.text) == "" and str(self.textinput_10_3.text) == "" and str(
                        self.textinput_10_4.text) == "" and str(self.textinput_10_5.text) == "" and str(
                        self.textinput_10_6.text) == "" and str(self.textinput_10_7.text) == "" and str(
                        self.textinput_10_8.text) == "" and str(self.textinput_10_9.text) == "" and str(
                        self.textinput_10_10.text) == "":
                    self.textinput_10_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_10_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_10_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_10_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_10_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_10_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_10_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_10_8.text = self.list_for_save_wheel_1[7]
                    self.textinput_10_9.text = self.list_for_save_wheel_1[8]
                    self.textinput_10_10.text = self.list_for_save_wheel_1[9]
                elif int(self.ids.slot_number.text) == 10 and str(self.textinput_10_1.text) != "" and str(
                        self.textinput_10_2.text) != "" and str(self.textinput_10_3.text) != "" and str(
                        self.textinput_10_4.text) != "" and str(self.textinput_10_5.text) != "" and str(
                        self.textinput_10_6.text) != "" and str(self.textinput_10_7.text) != "" and str(
                        self.textinput_10_8.text) != "" and str(self.textinput_10_9.text) != "" and str(
                        self.textinput_10_10.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel10
                    self.add_textbox_for_10()
                    self.ids.slot_number.text = "10"
                    self.textinput_10_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_10_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_10_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_10_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_10_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_10_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_10_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_10_8.text = self.list_for_save_wheel_1[7]
                    self.textinput_10_9.text = self.list_for_save_wheel_1[8]
                    self.textinput_10_10.text = self.list_for_save_wheel_1[9]
            elif str(self.ids.save_wheel_1.text) == "11th slot added":
                if int(self.ids.slot_number.text) == 11 and str(self.textinput_11_1.text) == "" and str(
                        self.textinput_11_2.text) == "" and str(self.textinput_11_3.text) == "" and str(
                        self.textinput_11_4.text) == "" and str(self.textinput_11_5.text) == "" and str(
                        self.textinput_11_6.text) == "" and str(self.textinput_11_7.text) == "" and str(
                        self.textinput_11_8.text) == "" and str(self.textinput_11_9.text) == "" and str(
                        self.textinput_11_10.text) == "" and str(self.textinput_11_11.text) == "":
                    self.textinput_11_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_11_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_11_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_11_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_11_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_11_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_11_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_11_8.text = self.list_for_save_wheel_1[7]
                    self.textinput_11_9.text = self.list_for_save_wheel_1[8]
                    self.textinput_11_10.text = self.list_for_save_wheel_1[9]
                    self.textinput_11_11.text = self.list_for_save_wheel_1[10]
                elif int(self.ids.slot_number.text) == 11 and str(self.textinput_11_1.text) != "" and str(
                        self.textinput_11_2.text) != "" and str(self.textinput_11_3.text) != "" and str(
                        self.textinput_11_4.text) != "" and str(self.textinput_11_5.text) != "" and str(
                        self.textinput_11_6.text) != "" and str(self.textinput_11_7.text) != "" and str(
                        self.textinput_11_8.text) != "" and str(self.textinput_11_9.text) != "" and str(
                        self.textinput_11_10.text) != "" and str(self.textinput_11_11.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel11
                    self.add_textbox_for_11()
                    self.ids.slot_number.text = "11"
                    self.textinput_11_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_11_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_11_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_11_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_11_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_11_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_11_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_11_8.text = self.list_for_save_wheel_1[7]
                    self.textinput_11_9.text = self.list_for_save_wheel_1[8]
                    self.textinput_11_10.text = self.list_for_save_wheel_1[9]
                    self.textinput_11_11.text = self.list_for_save_wheel_1[10]
            elif str(self.ids.save_wheel_1.text) == "12th slot added":
                if int(self.ids.slot_number.text) == 12 and str(self.textinput_12_1.text) == "" and str(
                        self.textinput_12_2.text) == "" and str(self.textinput_12_3.text) == "" and str(
                        self.textinput_12_4.text) == "" and str(self.textinput_12_5.text) == "" and str(
                        self.textinput_12_6.text) == "" and str(self.textinput_12_7.text) == "" and str(
                        self.textinput_12_8.text) == "" and str(self.textinput_12_9.text) == "" and str(
                        self.textinput_12_10.text) == "" and str(self.textinput_12_11.text) == "" and str(
                        self.textinput_12_12.text) == "":
                    self.textinput_12_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_12_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_12_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_12_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_12_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_12_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_12_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_12_8.text = self.list_for_save_wheel_1[7]
                    self.textinput_12_9.text = self.list_for_save_wheel_1[8]
                    self.textinput_12_10.text = self.list_for_save_wheel_1[9]
                    self.textinput_12_11.text = self.list_for_save_wheel_1[10]
                    self.textinput_12_12.text = self.list_for_save_wheel_1[11]
                elif int(self.ids.slot_number.text) == 12 and str(self.textinput_12_1.text) != "" and str(
                        self.textinput_12_2.text) != "" and str(self.textinput_12_3.text) != "" and str(
                        self.textinput_12_4.text) != "" and str(self.textinput_12_5.text) != "" and str(
                        self.textinput_12_6.text) != "" and str(self.textinput_12_7.text) != "" and str(
                        self.textinput_12_8.text) != "" and str(self.textinput_12_9.text) != "" and str(
                        self.textinput_12_10.text) != "" and str(self.textinput_12_11.text) != "" and str(
                        self.textinput_12_12.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel12
                    self.add_textbox_for_12()
                    self.ids.slot_number.text = "12"
                    self.textinput_12_1.text = self.list_for_save_wheel_1[0]
                    self.textinput_12_2.text = self.list_for_save_wheel_1[1]
                    self.textinput_12_3.text = self.list_for_save_wheel_1[2]
                    self.textinput_12_4.text = self.list_for_save_wheel_1[3]
                    self.textinput_12_5.text = self.list_for_save_wheel_1[4]
                    self.textinput_12_6.text = self.list_for_save_wheel_1[5]
                    self.textinput_12_7.text = self.list_for_save_wheel_1[6]
                    self.textinput_12_8.text = self.list_for_save_wheel_1[7]
                    self.textinput_12_9.text = self.list_for_save_wheel_1[8]
                    self.textinput_12_10.text = self.list_for_save_wheel_1[9]
                    self.textinput_12_11.text = self.list_for_save_wheel_1[10]
                    self.textinput_12_12.text = self.list_for_save_wheel_1[11]

        else:
            self.button_confirm.text = "No file added"
            if self.theme == 0:
                self.animate_the_confirm_white_to_black_text()
            else:
                self.animate_the_confirm_black_to_white_text()

    def saving_wheel_2(self):
        self.ids.drop.dismiss()
        if self.theme == 0:
            self.button_confirm.text = self.ids.save_wheel_2.text
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            self.save_wheel_2_open()
        else:
            self.button_confirm.text = self.ids.save_wheel_2.text
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            self.save_wheel_2_open()
        pass

    def save_wheel_2_open(self):
        self.delete_2_point = 0
        if str(self.ids.save_wheel_2.text) != 'No item saved':
            # save_wheel_2 = open("save_wheel_2.txt", "r")
            # self.list_for_save_wheel_2.clear()
            # for line in save_wheel_2:
            #     self.list_for_save_wheel_2.append(line[:-1])
            # print(self.list_for_save_wheel_2)
            # save_wheel_2.close()
            if str(self.ids.save_wheel_2.text) == "3rd slot added":
                if int(self.ids.slot_number.text) == 3 and str(self.textinput_3_1.text) == "" and str(
                        self.textinput_3_2.text) == "" and str(self.textinput_3_3.text) == "":
                    self.textinput_3_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_3_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_3_3.text = self.list_for_save_wheel_2[2]
                    pass
                elif int(self.ids.slot_number.text) == 3 and str(self.textinput_3_1.text) != "" and str(
                        self.textinput_3_2.text) != "" and str(self.textinput_3_3.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel3
                    self.add_textbox_for_3()
                    self.ids.slot_number.text = "3"
                    self.textinput_3_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_3_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_3_3.text = self.list_for_save_wheel_2[2]
            elif str(self.ids.save_wheel_2.text) == "4th slot added":
                if int(self.ids.slot_number.text) == 4 and str(self.textinput_4_1.text) == "" and str(
                        self.textinput_4_2.text) == "" and str(self.textinput_4_3.text) == "" and str(
                        self.textinput_4_4.text) == "":
                    self.textinput_4_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_4_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_4_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_4_4.text = self.list_for_save_wheel_2[3]
                elif int(self.ids.slot_number.text) == 4 and str(self.textinput_4_1.text) != "" and str(
                        self.textinput_4_2.text) != "" and str(self.textinput_4_3.text) != "" and str(
                        self.textinput_4_4.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel4
                    self.add_textbox_for_4()
                    self.ids.slot_number.text = "4"
                    self.textinput_4_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_4_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_4_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_4_4.text = self.list_for_save_wheel_2[3]
            elif str(self.ids.save_wheel_2.text) == "5th slot added":
                if int(self.ids.slot_number.text) == 5 and str(self.textinput_5_1.text) == "" and str(
                        self.textinput_5_2.text) == "" and str(self.textinput_5_3.text) == "" and str(
                        self.textinput_5_4.text) == "" and str(self.textinput_5_5.text) == "":
                    self.textinput_5_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_5_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_5_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_5_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_5_5.text = self.list_for_save_wheel_2[4]
                elif int(self.ids.slot_number.text) == 5 and str(self.textinput_5_1.text) != "" and str(
                        self.textinput_5_2.text) != "" and str(self.textinput_5_3.text) != "" and str(
                        self.textinput_5_4.text) != "" and str(self.textinput_5_5.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel5
                    self.add_textbox_for_5()
                    self.ids.slot_number.text = "5"
                    self.textinput_5_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_5_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_5_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_5_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_5_5.text = self.list_for_save_wheel_2[4]
            elif str(self.ids.save_wheel_2.text) == "6th slot added":
                if int(self.ids.slot_number.text) == 6 and str(self.textinput_6_1.text) == "" and str(
                        self.textinput_6_2.text) == "" and str(self.textinput_6_3.text) == "" and str(
                        self.textinput_6_4.text) == "" and str(self.textinput_6_5.text) == "" and str(
                        self.textinput_6_6.text == ""):
                    self.textinput_6_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_6_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_6_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_6_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_6_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_6_6.text = self.list_for_save_wheel_2[5]
                elif int(self.ids.slot_number.text) == 6 and str(self.textinput_6_1.text) != "" and str(
                        self.textinput_6_2.text) != "" and str(self.textinput_6_3.text) != "" and str(
                        self.textinput_6_4.text) != "" and str(self.textinput_6_5.text) != "" and str(
                        self.textinput_6_6.text != ""):
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel6
                    self.add_textbox_for_6()
                    self.ids.slot_number.text = "6"
                    self.textinput_6_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_6_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_6_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_6_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_6_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_6_6.text = self.list_for_save_wheel_2[5]
            elif str(self.ids.save_wheel_2.text) == "7th slot added":
                if int(self.ids.slot_number.text) == 7 and str(self.textinput_7_1.text) == "" and str(
                        self.textinput_7_2.text) == "" and str(self.textinput_7_3.text) == "" and str(
                        self.textinput_7_4.text) == "" and str(self.textinput_7_5.text) == "" and str(
                        self.textinput_7_6.text) == "" and str(self.textinput_7_7.text) == "":
                    self.textinput_7_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_7_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_7_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_7_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_7_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_7_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_7_7.text = self.list_for_save_wheel_2[6]
                elif int(self.ids.slot_number.text) == 7 and str(self.textinput_7_1.text) != "" and str(
                        self.textinput_7_2.text) != "" and str(self.textinput_7_3.text) != "" and str(
                        self.textinput_7_4.text) != "" and str(self.textinput_7_5.text) != "" and str(
                        self.textinput_7_6.text) != "" and str(self.textinput_7_7.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel7
                    self.add_textbox_for_7()
                    self.ids.slot_number.text = "7"
                    self.textinput_7_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_7_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_7_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_7_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_7_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_7_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_7_7.text = self.list_for_save_wheel_2[6]
            elif str(self.ids.save_wheel_2.text) == "8th slot added":
                if int(self.ids.slot_number.text) == 8 and str(self.textinput_8_1.text) == "" and str(
                        self.textinput_8_2.text) == "" and str(self.textinput_8_3.text) == "" and str(
                        self.textinput_8_4.text) == "" and str(self.textinput_8_5.text) == "" and str(
                        self.textinput_8_6.text) == "" and str(self.textinput_8_7.text) == "" and str(
                        self.textinput_8_8.text) == "":
                    self.textinput_8_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_8_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_8_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_8_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_8_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_8_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_8_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_8_8.text = self.list_for_save_wheel_2[7]
                elif int(self.ids.slot_number.text) == 8 and str(self.textinput_8_1.text) != "" and str(
                        self.textinput_8_2.text) != "" and str(self.textinput_8_3.text) != "" and str(
                        self.textinput_8_4.text) != "" and str(self.textinput_8_5.text) != "" and str(
                        self.textinput_8_6.text) != "" and str(self.textinput_8_7.text) != "" and str(
                        self.textinput_8_8.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel8
                    self.add_textbox_for_8()
                    self.ids.slot_number.text = "8"
                    self.textinput_8_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_8_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_8_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_8_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_8_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_8_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_8_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_8_8.text = self.list_for_save_wheel_2[7]
            elif str(self.ids.save_wheel_2.text) == "9th slot added":
                if int(self.ids.slot_number.text) == 9 and str(self.textinput_9_1.text) == "" and str(
                        self.textinput_9_2.text) == "" and str(self.textinput_9_3.text) == "" and str(
                        self.textinput_9_4.text) == "" and str(self.textinput_9_5.text) == "" and str(
                        self.textinput_9_6.text) == "" and str(self.textinput_9_7.text) == "" and str(
                        self.textinput_9_8.text) == "" and str(self.textinput_9_9.text) == "":
                    self.textinput_9_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_9_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_9_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_9_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_9_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_9_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_9_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_9_8.text = self.list_for_save_wheel_2[7]
                    self.textinput_9_9.text = self.list_for_save_wheel_2[8]
                elif int(self.ids.slot_number.text) == 9 and str(self.textinput_9_1.text) != "" and str(
                        self.textinput_9_2.text) != "" and str(self.textinput_9_3.text) != "" and str(
                        self.textinput_9_4.text) != "" and str(self.textinput_9_5.text) != "" and str(
                        self.textinput_9_6.text) != "" and str(self.textinput_9_7.text) != "" and str(
                        self.textinput_9_8.text) != "" and str(self.textinput_9_9.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel9
                    self.add_textbox_for_9()
                    self.ids.slot_number.text = "9"
                    self.textinput_9_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_9_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_9_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_9_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_9_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_9_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_9_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_9_8.text = self.list_for_save_wheel_2[7]
                    self.textinput_9_9.text = self.list_for_save_wheel_2[8]
            elif str(self.ids.save_wheel_2.text) == "10th slot added":
                if int(self.ids.slot_number.text) == 10 and str(self.textinput_10_1.text) == "" and str(
                        self.textinput_10_2.text) == "" and str(self.textinput_10_3.text) == "" and str(
                        self.textinput_10_4.text) == "" and str(self.textinput_10_5.text) == "" and str(
                        self.textinput_10_6.text) == "" and str(self.textinput_10_7.text) == "" and str(
                        self.textinput_10_8.text) == "" and str(self.textinput_10_9.text) == "" and str(
                        self.textinput_10_10.text) == "":
                    self.textinput_10_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_10_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_10_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_10_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_10_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_10_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_10_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_10_8.text = self.list_for_save_wheel_2[7]
                    self.textinput_10_9.text = self.list_for_save_wheel_2[8]
                    self.textinput_10_10.text = self.list_for_save_wheel_2[9]
                elif int(self.ids.slot_number.text) == 10 and str(self.textinput_10_1.text) != "" and str(
                        self.textinput_10_2.text) != "" and str(self.textinput_10_3.text) != "" and str(
                        self.textinput_10_4.text) != "" and str(self.textinput_10_5.text) != "" and str(
                        self.textinput_10_6.text) != "" and str(self.textinput_10_7.text) != "" and str(
                        self.textinput_10_8.text) != "" and str(self.textinput_10_9.text) != "" and str(
                        self.textinput_10_10.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel10
                    self.add_textbox_for_10()
                    self.ids.slot_number.text = "10"
                    self.textinput_10_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_10_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_10_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_10_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_10_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_10_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_10_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_10_8.text = self.list_for_save_wheel_2[7]
                    self.textinput_10_9.text = self.list_for_save_wheel_2[8]
                    self.textinput_10_10.text = self.list_for_save_wheel_2[9]
            elif str(self.ids.save_wheel_2.text) == "11th slot added":
                if int(self.ids.slot_number.text) == 11 and str(self.textinput_11_1.text) == "" and str(
                        self.textinput_11_2.text) == "" and str(self.textinput_11_3.text) == "" and str(
                        self.textinput_11_4.text) == "" and str(self.textinput_11_5.text) == "" and str(
                        self.textinput_11_6.text) == "" and str(self.textinput_11_7.text) == "" and str(
                        self.textinput_11_8.text) == "" and str(self.textinput_11_9.text) == "" and str(
                        self.textinput_11_10.text) == "" and str(self.textinput_11_11.text) == "":
                    self.textinput_11_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_11_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_11_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_11_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_11_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_11_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_11_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_11_8.text = self.list_for_save_wheel_2[7]
                    self.textinput_11_9.text = self.list_for_save_wheel_2[8]
                    self.textinput_11_10.text = self.list_for_save_wheel_2[9]
                    self.textinput_11_11.text = self.list_for_save_wheel_2[10]
                elif int(self.ids.slot_number.text) == 11 and str(self.textinput_11_1.text) != "" and str(
                        self.textinput_11_2.text) != "" and str(self.textinput_11_3.text) != "" and str(
                        self.textinput_11_4.text) != "" and str(self.textinput_11_5.text) != "" and str(
                        self.textinput_11_6.text) != "" and str(self.textinput_11_7.text) != "" and str(
                        self.textinput_11_8.text) != "" and str(self.textinput_11_9.text) != "" and str(
                        self.textinput_11_10.text) != "" and str(self.textinput_11_11.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel11
                    self.add_textbox_for_11()
                    self.ids.slot_number.text = "11"
                    self.textinput_11_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_11_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_11_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_11_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_11_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_11_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_11_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_11_8.text = self.list_for_save_wheel_2[7]
                    self.textinput_11_9.text = self.list_for_save_wheel_2[8]
                    self.textinput_11_10.text = self.list_for_save_wheel_2[9]
                    self.textinput_11_11.text = self.list_for_save_wheel_2[10]
            elif str(self.ids.save_wheel_2.text) == "12th slot added":
                if int(self.ids.slot_number.text) == 12 and str(self.textinput_12_1.text) == "" and str(
                        self.textinput_12_2.text) == "" and str(self.textinput_12_3.text) == "" and str(
                        self.textinput_12_4.text) == "" and str(self.textinput_12_5.text) == "" and str(
                        self.textinput_12_6.text) == "" and str(self.textinput_12_7.text) == "" and str(
                        self.textinput_12_8.text) == "" and str(self.textinput_12_9.text) == "" and str(
                        self.textinput_12_10.text) == "" and str(self.textinput_12_11.text) == "" and str(
                        self.textinput_12_12.text) == "":
                    self.textinput_12_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_12_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_12_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_12_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_12_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_12_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_12_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_12_8.text = self.list_for_save_wheel_2[7]
                    self.textinput_12_9.text = self.list_for_save_wheel_2[8]
                    self.textinput_12_10.text = self.list_for_save_wheel_2[9]
                    self.textinput_12_11.text = self.list_for_save_wheel_2[10]
                    self.textinput_12_12.text = self.list_for_save_wheel_2[11]
                elif int(self.ids.slot_number.text) == 12 and str(self.textinput_12_1.text) != "" and str(
                        self.textinput_12_2.text) != "" and str(self.textinput_12_3.text) != "" and str(
                        self.textinput_12_4.text) != "" and str(self.textinput_12_5.text) != "" and str(
                        self.textinput_12_6.text) != "" and str(self.textinput_12_7.text) != "" and str(
                        self.textinput_12_8.text) != "" and str(self.textinput_12_9.text) != "" and str(
                        self.textinput_12_10.text) != "" and str(self.textinput_12_11.text) != "" and str(
                        self.textinput_12_12.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel12
                    self.add_textbox_for_12()
                    self.ids.slot_number.text = "12"
                    self.textinput_12_1.text = self.list_for_save_wheel_2[0]
                    self.textinput_12_2.text = self.list_for_save_wheel_2[1]
                    self.textinput_12_3.text = self.list_for_save_wheel_2[2]
                    self.textinput_12_4.text = self.list_for_save_wheel_2[3]
                    self.textinput_12_5.text = self.list_for_save_wheel_2[4]
                    self.textinput_12_6.text = self.list_for_save_wheel_2[5]
                    self.textinput_12_7.text = self.list_for_save_wheel_2[6]
                    self.textinput_12_8.text = self.list_for_save_wheel_2[7]
                    self.textinput_12_9.text = self.list_for_save_wheel_2[8]
                    self.textinput_12_10.text = self.list_for_save_wheel_2[9]
                    self.textinput_12_11.text = self.list_for_save_wheel_2[10]
                    self.textinput_12_12.text = self.list_for_save_wheel_2[11]
        else:
            self.button_confirm.text = "No file added"
            if self.theme == 0:
                self.animate_the_confirm_white_to_black_text()
            else:
                self.animate_the_confirm_black_to_white_text()

    def saving_wheel_3(self):
        self.ids.drop.dismiss()
        if self.theme == 0:
            self.button_confirm.text = self.ids.save_wheel_3.text
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            self.save_wheel_3_open()
        else:
            self.button_confirm.text = self.ids.save_wheel_3.text
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            self.save_wheel_3_open()
        pass

    def save_wheel_3_open(self):
        self.delete_3_point = 0
        if str(self.ids.save_wheel_3.text) != 'No item saved':
            if str(self.ids.save_wheel_3.text) == "3rd slot added":
                if int(self.ids.slot_number.text) == 3 and str(self.textinput_3_1.text) == "" and str(
                        self.textinput_3_2.text) == "" and str(self.textinput_3_3.text) == "":
                    self.textinput_3_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_3_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_3_3.text = self.list_for_save_wheel_3[2]
                    pass
                elif int(self.ids.slot_number.text) == 3 and str(self.textinput_3_1.text) != "" and str(
                        self.textinput_3_2.text) != "" and str(self.textinput_3_3.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel3
                    self.add_textbox_for_3()
                    self.ids.slot_number.text = "3"
                    self.textinput_3_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_3_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_3_3.text = self.list_for_save_wheel_3[2]
            elif str(self.ids.save_wheel_3.text) == "4th slot added":
                if int(self.ids.slot_number.text) == 4 and str(self.textinput_4_1.text) == "" and str(
                        self.textinput_4_2.text) == "" and str(self.textinput_4_3.text) == "" and str(
                        self.textinput_4_4.text) == "":
                    self.textinput_4_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_4_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_4_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_4_4.text = self.list_for_save_wheel_3[3]
                elif int(self.ids.slot_number.text) == 4 and str(self.textinput_4_1.text) != "" and str(
                        self.textinput_4_2.text) != "" and str(self.textinput_4_3.text) != "" and str(
                        self.textinput_4_4.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel4
                    self.add_textbox_for_4()
                    self.ids.slot_number.text = "4"
                    self.textinput_4_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_4_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_4_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_4_4.text = self.list_for_save_wheel_3[3]
            elif str(self.ids.save_wheel_3.text) == "5th slot added":
                if int(self.ids.slot_number.text) == 5 and str(self.textinput_5_1.text) == "" and str(
                        self.textinput_5_2.text) == "" and str(self.textinput_5_3.text) == "" and str(
                        self.textinput_5_4.text) == "" and str(self.textinput_5_5.text) == "":
                    self.textinput_5_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_5_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_5_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_5_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_5_5.text = self.list_for_save_wheel_3[4]
                elif int(self.ids.slot_number.text) == 5 and str(self.textinput_5_1.text) != "" and str(
                        self.textinput_5_2.text) != "" and str(self.textinput_5_3.text) != "" and str(
                        self.textinput_5_4.text) != "" and str(self.textinput_5_5.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel5
                    self.add_textbox_for_5()
                    self.ids.slot_number.text = "5"
                    self.textinput_5_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_5_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_5_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_5_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_5_5.text = self.list_for_save_wheel_3[4]
            elif str(self.ids.save_wheel_3.text) == "6th slot added":
                if int(self.ids.slot_number.text) == 6 and str(self.textinput_6_1.text) == "" and str(
                        self.textinput_6_2.text) == "" and str(self.textinput_6_3.text) == "" and str(
                        self.textinput_6_4.text) == "" and str(self.textinput_6_5.text) == "" and str(
                        self.textinput_6_6.text == ""):
                    self.textinput_6_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_6_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_6_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_6_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_6_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_6_6.text = self.list_for_save_wheel_3[5]
                elif int(self.ids.slot_number.text) == 6 and str(self.textinput_6_1.text) != "" and str(
                        self.textinput_6_2.text) != "" and str(self.textinput_6_3.text) != "" and str(
                        self.textinput_6_4.text) != "" and str(self.textinput_6_5.text) != "" and str(
                        self.textinput_6_6.text != ""):
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel6
                    self.add_textbox_for_6()
                    self.ids.slot_number.text = "6"
                    self.textinput_6_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_6_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_6_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_6_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_6_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_6_6.text = self.list_for_save_wheel_3[5]
            elif str(self.ids.save_wheel_3.text) == "7th slot added":
                if int(self.ids.slot_number.text) == 7 and str(self.textinput_7_1.text) == "" and str(
                        self.textinput_7_2.text) == "" and str(self.textinput_7_3.text) == "" and str(
                        self.textinput_7_4.text) == "" and str(self.textinput_7_5.text) == "" and str(
                        self.textinput_7_6.text) == "" and str(self.textinput_7_7.text) == "":
                    self.textinput_7_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_7_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_7_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_7_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_7_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_7_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_7_7.text = self.list_for_save_wheel_3[6]
                elif int(self.ids.slot_number.text) == 7 and str(self.textinput_7_1.text) != "" and str(
                        self.textinput_7_2.text) != "" and str(self.textinput_7_3.text) != "" and str(
                        self.textinput_7_4.text) != "" and str(self.textinput_7_5.text) != "" and str(
                        self.textinput_7_6.text) != "" and str(self.textinput_7_7.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel7
                    self.add_textbox_for_7()
                    self.ids.slot_number.text = "7"
                    self.textinput_7_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_7_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_7_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_7_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_7_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_7_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_7_7.text = self.list_for_save_wheel_3[6]
            elif str(self.ids.save_wheel_3.text) == "8th slot added":
                if int(self.ids.slot_number.text) == 8 and str(self.textinput_8_1.text) == "" and str(
                        self.textinput_8_2.text) == "" and str(self.textinput_8_3.text) == "" and str(
                        self.textinput_8_4.text) == "" and str(self.textinput_8_5.text) == "" and str(
                        self.textinput_8_6.text) == "" and str(self.textinput_8_7.text) == "" and str(
                        self.textinput_8_8.text) == "":
                    self.textinput_8_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_8_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_8_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_8_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_8_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_8_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_8_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_8_8.text = self.list_for_save_wheel_3[7]
                elif int(self.ids.slot_number.text) == 8 and str(self.textinput_8_1.text) != "" and str(
                        self.textinput_8_2.text) != "" and str(self.textinput_8_3.text) != "" and str(
                        self.textinput_8_4.text) != "" and str(self.textinput_8_5.text) != "" and str(
                        self.textinput_8_6.text) != "" and str(self.textinput_8_7.text) != "" and str(
                        self.textinput_8_8.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel8
                    self.add_textbox_for_8()
                    self.ids.slot_number.text = "8"
                    self.textinput_8_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_8_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_8_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_8_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_8_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_8_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_8_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_8_8.text = self.list_for_save_wheel_3[7]
            elif str(self.ids.save_wheel_3.text) == "9th slot added":
                if int(self.ids.slot_number.text) == 9 and str(self.textinput_9_1.text) == "" and str(
                        self.textinput_9_2.text) == "" and str(self.textinput_9_3.text) == "" and str(
                        self.textinput_9_4.text) == "" and str(self.textinput_9_5.text) == "" and str(
                        self.textinput_9_6.text) == "" and str(self.textinput_9_7.text) == "" and str(
                        self.textinput_9_8.text) == "" and str(self.textinput_9_9.text) == "":
                    self.textinput_9_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_9_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_9_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_9_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_9_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_9_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_9_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_9_8.text = self.list_for_save_wheel_3[7]
                    self.textinput_9_9.text = self.list_for_save_wheel_3[8]
                elif int(self.ids.slot_number.text) == 9 and str(self.textinput_9_1.text) != "" and str(
                        self.textinput_9_2.text) != "" and str(self.textinput_9_3.text) != "" and str(
                        self.textinput_9_4.text) != "" and str(self.textinput_9_5.text) != "" and str(
                        self.textinput_9_6.text) != "" and str(self.textinput_9_7.text) != "" and str(
                        self.textinput_9_8.text) != "" and str(self.textinput_9_9.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel9
                    self.add_textbox_for_9()
                    self.ids.slot_number.text = "9"
                    self.textinput_9_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_9_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_9_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_9_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_9_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_9_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_9_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_9_8.text = self.list_for_save_wheel_3[7]
                    self.textinput_9_9.text = self.list_for_save_wheel_3[8]
            elif str(self.ids.save_wheel_3.text) == "10th slot added":
                if int(self.ids.slot_number.text) == 10 and str(self.textinput_10_1.text) == "" and str(
                        self.textinput_10_2.text) == "" and str(self.textinput_10_3.text) == "" and str(
                        self.textinput_10_4.text) == "" and str(self.textinput_10_5.text) == "" and str(
                        self.textinput_10_6.text) == "" and str(self.textinput_10_7.text) == "" and str(
                        self.textinput_10_8.text) == "" and str(self.textinput_10_9.text) == "" and str(
                        self.textinput_10_10.text) == "":
                    self.textinput_10_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_10_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_10_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_10_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_10_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_10_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_10_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_10_8.text = self.list_for_save_wheel_3[7]
                    self.textinput_10_9.text = self.list_for_save_wheel_3[8]
                    self.textinput_10_10.text = self.list_for_save_wheel_3[9]
                elif int(self.ids.slot_number.text) == 10 and str(self.textinput_10_1.text) != "" and str(
                        self.textinput_10_2.text) != "" and str(self.textinput_10_3.text) != "" and str(
                        self.textinput_10_4.text) != "" and str(self.textinput_10_5.text) != "" and str(
                        self.textinput_10_6.text) != "" and str(self.textinput_10_7.text) != "" and str(
                        self.textinput_10_8.text) != "" and str(self.textinput_10_9.text) != "" and str(
                        self.textinput_10_10.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel10
                    self.add_textbox_for_10()
                    self.ids.slot_number.text = "10"
                    self.textinput_10_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_10_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_10_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_10_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_10_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_10_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_10_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_10_8.text = self.list_for_save_wheel_3[7]
                    self.textinput_10_9.text = self.list_for_save_wheel_3[8]
                    self.textinput_10_10.text = self.list_for_save_wheel_3[9]
            elif str(self.ids.save_wheel_3.text) == "11th slot added":
                if int(self.ids.slot_number.text) == 11 and str(self.textinput_11_1.text) == "" and str(
                        self.textinput_11_2.text) == "" and str(self.textinput_11_3.text) == "" and str(
                        self.textinput_11_4.text) == "" and str(self.textinput_11_5.text) == "" and str(
                        self.textinput_11_6.text) == "" and str(self.textinput_11_7.text) == "" and str(
                        self.textinput_11_8.text) == "" and str(self.textinput_11_9.text) == "" and str(
                        self.textinput_11_10.text) == "" and str(self.textinput_11_11.text) == "":
                    self.textinput_11_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_11_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_11_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_11_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_11_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_11_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_11_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_11_8.text = self.list_for_save_wheel_3[7]
                    self.textinput_11_9.text = self.list_for_save_wheel_3[8]
                    self.textinput_11_10.text = self.list_for_save_wheel_3[9]
                    self.textinput_11_11.text = self.list_for_save_wheel_3[10]
                elif int(self.ids.slot_number.text) == 11 and str(self.textinput_11_1.text) != "" and str(
                        self.textinput_11_2.text) != "" and str(self.textinput_11_3.text) != "" and str(
                        self.textinput_11_4.text) != "" and str(self.textinput_11_5.text) != "" and str(
                        self.textinput_11_6.text) != "" and str(self.textinput_11_7.text) != "" and str(
                        self.textinput_11_8.text) != "" and str(self.textinput_11_9.text) != "" and str(
                        self.textinput_11_10.text) != "" and str(self.textinput_11_11.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel11
                    self.add_textbox_for_11()
                    self.ids.slot_number.text = "11"
                    self.textinput_11_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_11_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_11_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_11_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_11_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_11_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_11_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_11_8.text = self.list_for_save_wheel_3[7]
                    self.textinput_11_9.text = self.list_for_save_wheel_3[8]
                    self.textinput_11_10.text = self.list_for_save_wheel_3[9]
                    self.textinput_11_11.text = self.list_for_save_wheel_3[10]
            elif str(self.ids.save_wheel_3.text) == "12th slot added":
                if int(self.ids.slot_number.text) == 12 and str(self.textinput_12_1.text) == "" and str(
                        self.textinput_12_2.text) == "" and str(self.textinput_12_3.text) == "" and str(
                        self.textinput_12_4.text) == "" and str(self.textinput_12_5.text) == "" and str(
                        self.textinput_12_6.text) == "" and str(self.textinput_12_7.text) == "" and str(
                        self.textinput_12_8.text) == "" and str(self.textinput_12_9.text) == "" and str(
                        self.textinput_12_10.text) == "" and str(self.textinput_12_11.text) == "" and str(
                        self.textinput_12_12.text) == "":
                    self.textinput_12_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_12_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_12_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_12_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_12_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_12_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_12_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_12_8.text = self.list_for_save_wheel_3[7]
                    self.textinput_12_9.text = self.list_for_save_wheel_3[8]
                    self.textinput_12_10.text = self.list_for_save_wheel_3[9]
                    self.textinput_12_11.text = self.list_for_save_wheel_3[10]
                    self.textinput_12_12.text = self.list_for_save_wheel_3[11]
                elif int(self.ids.slot_number.text) == 12 and str(self.textinput_12_1.text) != "" and str(
                        self.textinput_12_2.text) != "" and str(self.textinput_12_3.text) != "" and str(
                        self.textinput_12_4.text) != "" and str(self.textinput_12_5.text) != "" and str(
                        self.textinput_12_6.text) != "" and str(self.textinput_12_7.text) != "" and str(
                        self.textinput_12_8.text) != "" and str(self.textinput_12_9.text) != "" and str(
                        self.textinput_12_10.text) != "" and str(self.textinput_12_11.text) != "" and str(
                        self.textinput_12_12.text) != "":
                    pass
                else:
                    self.ids.wheel_number.source = self.wheel12
                    self.add_textbox_for_12()
                    self.ids.slot_number.text = "12"
                    self.textinput_12_1.text = self.list_for_save_wheel_3[0]
                    self.textinput_12_2.text = self.list_for_save_wheel_3[1]
                    self.textinput_12_3.text = self.list_for_save_wheel_3[2]
                    self.textinput_12_4.text = self.list_for_save_wheel_3[3]
                    self.textinput_12_5.text = self.list_for_save_wheel_3[4]
                    self.textinput_12_6.text = self.list_for_save_wheel_3[5]
                    self.textinput_12_7.text = self.list_for_save_wheel_3[6]
                    self.textinput_12_8.text = self.list_for_save_wheel_3[7]
                    self.textinput_12_9.text = self.list_for_save_wheel_3[8]
                    self.textinput_12_10.text = self.list_for_save_wheel_3[9]
                    self.textinput_12_11.text = self.list_for_save_wheel_3[10]
                    self.textinput_12_12.text = self.list_for_save_wheel_3[11]
        else:
            self.button_confirm.text = "No file added"
            if self.theme == 0:
                self.animate_the_confirm_white_to_black_text()
            else:
                self.animate_the_confirm_black_to_white_text()

    def delete_1(self):
        self.ids.drop.dismiss()
        self.delete_1_point = 1
        if self.theme == 0:
            self.button_confirm.text = "Successfully deleted"
            self.button_confirm.color = [1, 1, 1, 1]
            self.ids.save_wheel_1.text = "No item saved"
            self.list_for_detail[0]="No item saved"
            # self.list_for_save_wheel_1.clear()
            self.animate_the_confirm_white_to_black_text()

        else:
            self.button_confirm.text = "Successfully deleted"
            self.button_confirm.color = [0, 0, 0, 1]
            self.ids.save_wheel_1.text = "No item saved"
            # details = open("detail.txt", "r")
            # list_of_line = details.readlines()
            # list_of_line[0] = "No item saved"
            # details.close()
            self.list_for_detail[0] = "No item saved"
            # self.list_for_save_wheel_1.clear()
            self.animate_the_confirm_black_to_white_text()
        pass

    def delete_2(self):
        self.ids.drop.dismiss()
        self.delete_2_point = 1
        if self.theme == 0:
            self.button_confirm.text = "Successfully deleted"
            self.button_confirm.color = [1, 1, 1, 1]
            self.ids.save_wheel_2.text = "No item saved"
            self.list_for_detail[1] = "No item saved"
            # self.list_for_save_wheel_2.clear()
            self.animate_the_confirm_white_to_black_text()
        else:
            self.button_confirm.text = "Successfully deleted"
            self.button_confirm.color = [0, 0, 0, 1]
            self.ids.save_wheel_2.text = "No item saved"
            self.list_for_detail[1] = "No item saved"
            # self.list_for_save_wheel_2.clear()
            self.animate_the_confirm_black_to_white_text()
        pass

    def delete_3(self):
        self.ids.drop.dismiss()
        self.delete_3_point = 1
        if self.theme == 0:
            self.button_confirm.text = "Successfully deleted"
            self.button_confirm.color = [1, 1, 1, 1]
            self.ids.save_wheel_3.text = "No item saved"
            # details = open("detail.txt", "r")
            # list_of_line = details.readlines()
            # list_of_line[2] = "No item saved"
            # details.close()
            self.list_for_detail[0] = "No item saved"
            self.animate_the_confirm_white_to_black_text()
        else:
            self.button_confirm.text = "Successfully deleted"
            self.button_confirm.color = [0, 0, 0, 1]
            self.ids.save_wheel_3.text = "No item saved"
            # details = open("detail.txt", "r")
            # list_of_line = details.readlines()
            # list_of_line[2] = "No item saved"
            # details.close()
            self.list_for_detail[0] = "No item saved"
            self.animate_the_confirm_black_to_white_text()
        pass

    def save_wheel(self):
        self.ids.drop.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Successfully saved"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            self.save()
        else:
            self.button_confirm.text = "Successfully saved"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            self.save()
        pass

    def save(self):
        if str(self.ids.save_wheel_3.text) == 'No item saved':
            if str(self.ids.save_wheel_2.text) == 'No item saved':
                if str(self.ids.save_wheel_1.text) == 'No item saved':
                    if int(self.ids.slot_number.text) == 3:
                        if str(self.textinput_3_1.text) == "" or str(self.textinput_3_2.text) == "" or str(
                                self.textinput_3_3.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_3_1.text + "\n"
                            list_of_line[1] = self.textinput_3_2.text + "\n"
                            list_of_line[2] = self.textinput_3_3.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_3_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_3_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_3_3.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "rd slot added"
                    elif int(self.ids.slot_number.text) == 4:
                        if str(self.textinput_4_1.text) == "" or str(self.textinput_4_2.text) == "" or str(
                                self.textinput_4_3.text) == "" or str(self.textinput_4_4.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_4_1.text + "\n"
                            list_of_line[1] = self.textinput_4_2.text + "\n"
                            list_of_line[2] = self.textinput_4_3.text + "\n"
                            list_of_line[3] = self.textinput_4_4.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_4_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_4_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_4_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_4_4.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 5:
                        if str(self.textinput_5_1.text) == "" or str(self.textinput_5_2.text) == "" or str(
                                self.textinput_5_3.text) == "" or str(self.textinput_5_4.text) == "" or str(
                                self.textinput_5_5.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_5_1.text + "\n"
                            list_of_line[1] = self.textinput_5_2.text + "\n"
                            list_of_line[2] = self.textinput_5_3.text + "\n"
                            list_of_line[3] = self.textinput_5_4.text + "\n"
                            list_of_line[4] = self.textinput_5_5.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_5_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_5_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_5_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_5_4.text
                            self.list_for_save_wheel_1[4] = self.textinput_5_5.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 6:
                        if str(self.textinput_6_1.text) == "" or str(self.textinput_6_2.text) == "" or str(
                                self.textinput_6_3.text) == "" or str(self.textinput_6_4.text) == "" or str(
                                self.textinput_6_5.text) == "" or str(self.textinput_6_6.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_6_1.text + "\n"
                            list_of_line[1] = self.textinput_6_2.text + "\n"
                            list_of_line[2] = self.textinput_6_3.text + "\n"
                            list_of_line[3] = self.textinput_6_4.text + "\n"
                            list_of_line[4] = self.textinput_6_5.text + "\n"
                            list_of_line[5] = self.textinput_6_6.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_6_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_6_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_6_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_6_4.text
                            self.list_for_save_wheel_1[4] = self.textinput_6_5.text
                            self.list_for_save_wheel_1[5] = self.textinput_6_6.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 7:
                        if str(self.textinput_7_1.text) == "" or str(self.textinput_7_2.text) == "" or str(
                                self.textinput_7_3.text) == "" or str(self.textinput_7_4.text) == "" or str(
                                self.textinput_7_5.text) == "" or str(self.textinput_7_6.text) == "" or str(
                                self.textinput_7_7.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_7_1.text + "\n"
                            list_of_line[1] = self.textinput_7_2.text + "\n"
                            list_of_line[2] = self.textinput_7_3.text + "\n"
                            list_of_line[3] = self.textinput_7_4.text + "\n"
                            list_of_line[4] = self.textinput_7_5.text + "\n"
                            list_of_line[5] = self.textinput_7_6.text + "\n"
                            list_of_line[6] = self.textinput_7_7.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_7_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_7_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_7_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_7_4.text
                            self.list_for_save_wheel_1[4] = self.textinput_7_5.text
                            self.list_for_save_wheel_1[5] = self.textinput_7_6.text
                            self.list_for_save_wheel_1[6] = self.textinput_7_7.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 8:
                        if str(self.textinput_8_1.text) == "" or str(self.textinput_8_2.text) == "" or str(
                                self.textinput_8_3.text) == "" or str(self.textinput_8_4.text) == "" or str(
                                self.textinput_8_5.text) == "" or str(self.textinput_8_6.text) == "" or str(
                                self.textinput_8_7.text) == "" or str(self.textinput_8_8.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_8_1.text + "\n"
                            list_of_line[1] = self.textinput_8_2.text + "\n"
                            list_of_line[2] = self.textinput_8_3.text + "\n"
                            list_of_line[3] = self.textinput_8_4.text + "\n"
                            list_of_line[4] = self.textinput_8_5.text + "\n"
                            list_of_line[5] = self.textinput_8_6.text + "\n"
                            list_of_line[6] = self.textinput_8_7.text + "\n"
                            list_of_line[7] = self.textinput_8_8.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_8_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_8_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_8_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_8_4.text
                            self.list_for_save_wheel_1[4] = self.textinput_8_5.text
                            self.list_for_save_wheel_1[5] = self.textinput_8_6.text
                            self.list_for_save_wheel_1[6] = self.textinput_8_7.text
                            self.list_for_save_wheel_1[7] = self.textinput_8_8.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 9:
                        if str(self.textinput_9_1.text) == "" or str(self.textinput_9_2.text) == "" or str(
                                self.textinput_9_3.text) == "" or str(self.textinput_9_4.text) == "" or str(
                                self.textinput_9_5.text) == "" or str(self.textinput_9_6.text) == "" or str(
                                self.textinput_9_7.text) == "" or str(self.textinput_9_8.text) == "" or str(
                                self.textinput_9_9.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_9_1.text + "\n"
                            list_of_line[1] = self.textinput_9_2.text + "\n"
                            list_of_line[2] = self.textinput_9_3.text + "\n"
                            list_of_line[3] = self.textinput_9_4.text + "\n"
                            list_of_line[4] = self.textinput_9_5.text + "\n"
                            list_of_line[5] = self.textinput_9_6.text + "\n"
                            list_of_line[6] = self.textinput_9_7.text + "\n"
                            list_of_line[7] = self.textinput_9_8.text + "\n"
                            list_of_line[8] = self.textinput_9_9.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_9_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_9_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_9_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_9_4.text
                            self.list_for_save_wheel_1[4] = self.textinput_9_5.text
                            self.list_for_save_wheel_1[5] = self.textinput_9_6.text
                            self.list_for_save_wheel_1[6] = self.textinput_9_7.text
                            self.list_for_save_wheel_1[7] = self.textinput_9_8.text
                            self.list_for_save_wheel_1[8] = self.textinput_9_9.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 10:
                        if str(self.textinput_10_1.text) == "" or str(self.textinput_10_2.text) == "" or str(
                                self.textinput_10_3.text) == "" or str(self.textinput_10_4.text) == "" or str(
                                self.textinput_10_5.text) == "" or str(self.textinput_10_6.text) == "" or str(
                                self.textinput_10_7.text) == "" or str(self.textinput_10_8.text) == "" or str(
                                self.textinput_10_9.text) == "" or str(self.textinput_10_10.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_10_1.text + "\n"
                            list_of_line[1] = self.textinput_10_2.text + "\n"
                            list_of_line[2] = self.textinput_10_3.text + "\n"
                            list_of_line[3] = self.textinput_10_4.text + "\n"
                            list_of_line[4] = self.textinput_10_5.text + "\n"
                            list_of_line[5] = self.textinput_10_6.text + "\n"
                            list_of_line[6] = self.textinput_10_7.text + "\n"
                            list_of_line[7] = self.textinput_10_8.text + "\n"
                            list_of_line[8] = self.textinput_10_9.text + "\n"
                            list_of_line[9] = self.textinput_10_10.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_10_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_10_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_10_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_10_4.text
                            self.list_for_save_wheel_1[4] = self.textinput_10_5.text
                            self.list_for_save_wheel_1[5] = self.textinput_10_6.text
                            self.list_for_save_wheel_1[6] = self.textinput_10_7.text
                            self.list_for_save_wheel_1[7] = self.textinput_10_8.text
                            self.list_for_save_wheel_1[8] = self.textinput_10_9.text
                            self.list_for_save_wheel_1[9] = self.textinput_10_10.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 11:
                        if str(self.textinput_11_1.text) == "" or str(self.textinput_11_2.text) == "" or str(
                                self.textinput_11_3.text) == "" or str(self.textinput_11_4.text) == "" or str(
                                self.textinput_11_5.text) == "" or str(self.textinput_11_6.text) == "" or str(
                                self.textinput_11_7.text) == "" or str(self.textinput_11_8.text) == "" or str(
                                self.textinput_11_9.text) == "" or str(self.textinput_11_10.text) == "" or str(
                                self.textinput_11_11.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_11_1.text + "\n"
                            list_of_line[1] = self.textinput_11_2.text + "\n"
                            list_of_line[2] = self.textinput_11_3.text + "\n"
                            list_of_line[3] = self.textinput_11_4.text + "\n"
                            list_of_line[4] = self.textinput_11_5.text + "\n"
                            list_of_line[5] = self.textinput_11_6.text + "\n"
                            list_of_line[6] = self.textinput_11_7.text + "\n"
                            list_of_line[7] = self.textinput_11_8.text + "\n"
                            list_of_line[8] = self.textinput_11_9.text + "\n"
                            list_of_line[9] = self.textinput_11_10.text + "\n"
                            list_of_line[10] = self.textinput_11_11.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_11_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_11_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_11_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_11_4.text
                            self.list_for_save_wheel_1[4] = self.textinput_11_5.text
                            self.list_for_save_wheel_1[5] = self.textinput_11_6.text
                            self.list_for_save_wheel_1[6] = self.textinput_11_7.text
                            self.list_for_save_wheel_1[7] = self.textinput_11_8.text
                            self.list_for_save_wheel_1[8] = self.textinput_11_9.text
                            self.list_for_save_wheel_1[9] = self.textinput_11_10.text
                            self.list_for_save_wheel_1[10] = self.textinput_11_11.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 12:
                        if str(self.textinput_12_1.text) == "" or str(self.textinput_12_2.text) == "" or str(
                                self.textinput_12_3.text) == "" or str(self.textinput_12_4.text) == "" or str(
                                self.textinput_12_5.text) == "" or str(self.textinput_12_6.text) == "" or str(
                                self.textinput_12_7.text) == "" or str(self.textinput_12_8.text) == "" or str(
                                self.textinput_12_9.text) == "" or str(self.textinput_12_10.text) == "" or str(
                                self.textinput_12_11.text) == "" or str(self.textinput_12_12.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_1 = open("save_wheel_1.txt", "r")
                            list_of_line = save_wheel_1.readlines()
                            list_of_line[0] = self.textinput_12_1.text + "\n"
                            list_of_line[1] = self.textinput_12_2.text + "\n"
                            list_of_line[2] = self.textinput_12_3.text + "\n"
                            list_of_line[3] = self.textinput_12_4.text + "\n"
                            list_of_line[4] = self.textinput_12_5.text + "\n"
                            list_of_line[5] = self.textinput_12_6.text + "\n"
                            list_of_line[6] = self.textinput_12_7.text + "\n"
                            list_of_line[7] = self.textinput_12_8.text + "\n"
                            list_of_line[8] = self.textinput_12_9.text + "\n"
                            list_of_line[9] = self.textinput_12_10.text + "\n"
                            list_of_line[10] = self.textinput_12_11.text + "\n"
                            list_of_line[11] = self.textinput_12_12.text + "\n"
                            save_wheel_1 = open("save_wheel_1.txt", "w")
                            save_wheel_1.writelines(list_of_line)
                            save_wheel_1.close()
                            self.list_for_save_wheel_1[0] = self.textinput_12_1.text
                            self.list_for_save_wheel_1[1] = self.textinput_12_2.text
                            self.list_for_save_wheel_1[2] = self.textinput_12_3.text
                            self.list_for_save_wheel_1[3] = self.textinput_12_4.text
                            self.list_for_save_wheel_1[4] = self.textinput_12_5.text
                            self.list_for_save_wheel_1[5] = self.textinput_12_6.text
                            self.list_for_save_wheel_1[6] = self.textinput_12_7.text
                            self.list_for_save_wheel_1[7] = self.textinput_12_8.text
                            self.list_for_save_wheel_1[8] = self.textinput_12_9.text
                            self.list_for_save_wheel_1[9] = self.textinput_12_10.text
                            self.list_for_save_wheel_1[10] = self.textinput_12_11.text
                            self.list_for_save_wheel_1[11] = self.textinput_12_12.text
                            self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                else:
                    if int(self.ids.slot_number.text) == 3:
                        if str(self.textinput_3_1.text) == "" or str(self.textinput_3_2.text) == "" or str(
                                self.textinput_3_3.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_3_1.text + "\n"
                            list_of_line[1] = self.textinput_3_2.text + "\n"
                            list_of_line[2] = self.textinput_3_3.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_3_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_3_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_3_3.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "rd slot added"
                    elif int(self.ids.slot_number.text) == 4:
                        if str(self.textinput_4_1.text) == "" or str(self.textinput_4_2.text) == "" or str(
                                self.textinput_4_3.text) == "" or str(self.textinput_4_4.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_4_1.text + "\n"
                            list_of_line[1] = self.textinput_4_2.text + "\n"
                            list_of_line[2] = self.textinput_4_3.text + "\n"
                            list_of_line[3] = self.textinput_4_4.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_4_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_4_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_4_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_4_4.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 5:
                        if str(self.textinput_5_1.text) == "" or str(self.textinput_5_2.text) == "" or str(
                                self.textinput_5_3.text) == "" or str(self.textinput_5_4.text) == "" or str(
                                self.textinput_5_5.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_5_1.text + "\n"
                            list_of_line[1] = self.textinput_5_2.text + "\n"
                            list_of_line[2] = self.textinput_5_3.text + "\n"
                            list_of_line[3] = self.textinput_5_4.text + "\n"
                            list_of_line[4] = self.textinput_5_5.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_5_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_5_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_5_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_5_4.text
                            self.list_for_save_wheel_2[4] = self.textinput_5_5.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 6:
                        if str(self.textinput_6_1.text) == "" or str(self.textinput_6_2.text) == "" or str(
                                self.textinput_6_3.text) == "" or str(self.textinput_6_4.text) == "" or str(
                                self.textinput_6_5.text) == "" or str(self.textinput_6_6.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_6_1.text + "\n"
                            list_of_line[1] = self.textinput_6_2.text + "\n"
                            list_of_line[2] = self.textinput_6_3.text + "\n"
                            list_of_line[3] = self.textinput_6_4.text + "\n"
                            list_of_line[4] = self.textinput_6_5.text + "\n"
                            list_of_line[5] = self.textinput_6_6.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_6_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_6_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_6_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_6_4.text
                            self.list_for_save_wheel_2[4] = self.textinput_6_5.text
                            self.list_for_save_wheel_2[5] = self.textinput_6_6.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 7:
                        if str(self.textinput_7_1.text) == "" or str(self.textinput_7_2.text) == "" or str(
                                self.textinput_7_3.text) == "" or str(self.textinput_7_4.text) == "" or str(
                                self.textinput_7_5.text) == "" or str(self.textinput_7_6.text) == "" or str(
                                self.textinput_7_7.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_7_1.text + "\n"
                            list_of_line[1] = self.textinput_7_2.text + "\n"
                            list_of_line[2] = self.textinput_7_3.text + "\n"
                            list_of_line[3] = self.textinput_7_4.text + "\n"
                            list_of_line[4] = self.textinput_7_5.text + "\n"
                            list_of_line[5] = self.textinput_7_6.text + "\n"
                            list_of_line[6] = self.textinput_7_7.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_7_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_7_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_7_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_7_4.text
                            self.list_for_save_wheel_2[4] = self.textinput_7_5.text
                            self.list_for_save_wheel_2[5] = self.textinput_7_6.text
                            self.list_for_save_wheel_2[6] = self.textinput_7_7.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 8:
                        if str(self.textinput_8_1.text) == "" or str(self.textinput_8_2.text) == "" or str(
                                self.textinput_8_3.text) == "" or str(self.textinput_8_4.text) == "" or str(
                                self.textinput_8_5.text) == "" or str(self.textinput_8_6.text) == "" or str(
                                self.textinput_8_7.text) == "" or str(self.textinput_8_8.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_8_1.text + "\n"
                            list_of_line[1] = self.textinput_8_2.text + "\n"
                            list_of_line[2] = self.textinput_8_3.text + "\n"
                            list_of_line[3] = self.textinput_8_4.text + "\n"
                            list_of_line[4] = self.textinput_8_5.text + "\n"
                            list_of_line[5] = self.textinput_8_6.text + "\n"
                            list_of_line[6] = self.textinput_8_7.text + "\n"
                            list_of_line[7] = self.textinput_8_8.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_8_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_8_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_8_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_8_4.text
                            self.list_for_save_wheel_2[4] = self.textinput_8_5.text
                            self.list_for_save_wheel_2[5] = self.textinput_8_6.text
                            self.list_for_save_wheel_2[6] = self.textinput_8_7.text
                            self.list_for_save_wheel_2[7] = self.textinput_8_8.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 9:
                        if str(self.textinput_9_1.text) == "" or str(self.textinput_9_2.text) == "" or str(
                                self.textinput_9_3.text) == "" or str(self.textinput_9_4.text) == "" or str(
                                self.textinput_9_5.text) == "" or str(self.textinput_9_6.text) == "" or str(
                                self.textinput_9_7.text) == "" or str(self.textinput_9_8.text) == "" or str(
                                self.textinput_9_9.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_9_1.text + "\n"
                            list_of_line[1] = self.textinput_9_2.text + "\n"
                            list_of_line[2] = self.textinput_9_3.text + "\n"
                            list_of_line[3] = self.textinput_9_4.text + "\n"
                            list_of_line[4] = self.textinput_9_5.text + "\n"
                            list_of_line[5] = self.textinput_9_6.text + "\n"
                            list_of_line[6] = self.textinput_9_7.text + "\n"
                            list_of_line[7] = self.textinput_9_8.text + "\n"
                            list_of_line[8] = self.textinput_9_9.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_9_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_9_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_9_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_9_4.text
                            self.list_for_save_wheel_2[4] = self.textinput_9_5.text
                            self.list_for_save_wheel_2[5] = self.textinput_9_6.text
                            self.list_for_save_wheel_2[6] = self.textinput_9_7.text
                            self.list_for_save_wheel_2[7] = self.textinput_9_8.text
                            self.list_for_save_wheel_2[8] = self.textinput_9_9.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 10:
                        if str(self.textinput_10_1.text) == "" or str(self.textinput_10_2.text) == "" or str(
                                self.textinput_10_3.text) == "" or str(self.textinput_10_4.text) == "" or str(
                                self.textinput_10_5.text) == "" or str(self.textinput_10_6.text) == "" or str(
                                self.textinput_10_7.text) == "" or str(self.textinput_10_8.text) == "" or str(
                                self.textinput_10_9.text) == "" or str(self.textinput_10_10.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_10_1.text + "\n"
                            list_of_line[1] = self.textinput_10_2.text + "\n"
                            list_of_line[2] = self.textinput_10_3.text + "\n"
                            list_of_line[3] = self.textinput_10_4.text + "\n"
                            list_of_line[4] = self.textinput_10_5.text + "\n"
                            list_of_line[5] = self.textinput_10_6.text + "\n"
                            list_of_line[6] = self.textinput_10_7.text + "\n"
                            list_of_line[7] = self.textinput_10_8.text + "\n"
                            list_of_line[8] = self.textinput_10_9.text + "\n"
                            list_of_line[9] = self.textinput_10_10.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_10_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_10_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_10_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_10_4.text
                            self.list_for_save_wheel_2[4] = self.textinput_10_5.text
                            self.list_for_save_wheel_2[5] = self.textinput_10_6.text
                            self.list_for_save_wheel_2[6] = self.textinput_10_7.text
                            self.list_for_save_wheel_2[7] = self.textinput_10_8.text
                            self.list_for_save_wheel_2[8] = self.textinput_10_9.text
                            self.list_for_save_wheel_2[9] = self.textinput_10_10.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 11:
                        if str(self.textinput_11_1.text) == "" or str(self.textinput_11_2.text) == "" or str(
                                self.textinput_11_3.text) == "" or str(self.textinput_11_4.text) == "" or str(
                                self.textinput_11_5.text) == "" or str(self.textinput_11_6.text) == "" or str(
                                self.textinput_11_7.text) == "" or str(self.textinput_11_8.text) == "" or str(
                                self.textinput_11_9.text) == "" or str(self.textinput_11_10.text) == "" or str(
                                self.textinput_11_11.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_11_1.text + "\n"
                            list_of_line[1] = self.textinput_11_2.text + "\n"
                            list_of_line[2] = self.textinput_11_3.text + "\n"
                            list_of_line[3] = self.textinput_11_4.text + "\n"
                            list_of_line[4] = self.textinput_11_5.text + "\n"
                            list_of_line[5] = self.textinput_11_6.text + "\n"
                            list_of_line[6] = self.textinput_11_7.text + "\n"
                            list_of_line[7] = self.textinput_11_8.text + "\n"
                            list_of_line[8] = self.textinput_11_9.text + "\n"
                            list_of_line[9] = self.textinput_11_10.text + "\n"
                            list_of_line[10] = self.textinput_11_11.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_11_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_11_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_11_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_11_4.text
                            self.list_for_save_wheel_2[4] = self.textinput_11_5.text
                            self.list_for_save_wheel_2[5] = self.textinput_11_6.text
                            self.list_for_save_wheel_2[6] = self.textinput_11_7.text
                            self.list_for_save_wheel_2[7] = self.textinput_11_8.text
                            self.list_for_save_wheel_2[8] = self.textinput_11_9.text
                            self.list_for_save_wheel_2[9] = self.textinput_11_10.text
                            self.list_for_save_wheel_2[10] = self.textinput_11_11.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                    elif int(self.ids.slot_number.text) == 12:
                        if str(self.textinput_12_1.text) == "" or str(self.textinput_12_2.text) == "" or str(
                                self.textinput_12_3.text) == "" or str(self.textinput_12_4.text) == "" or str(
                                self.textinput_12_5.text) == "" or str(self.textinput_12_6.text) == "" or str(
                                self.textinput_12_7.text) == "" or str(self.textinput_12_8.text) == "" or str(
                                self.textinput_12_9.text) == "" or str(self.textinput_12_10.text) == "" or str(
                                self.textinput_12_11.text) == "" or str(self.textinput_12_12.text) == "":
                            self.button_confirm.text = "Please fill remaining slots"
                            if self.theme == 0:
                                self.animate_the_confirm_white_to_black_text()
                            else:
                                self.animate_the_confirm_black_to_white_text()
                            pass
                        else:
                            save_wheel_2 = open("save_wheel_2.txt", "r")
                            list_of_line = save_wheel_2.readlines()
                            list_of_line[0] = self.textinput_12_1.text + "\n"
                            list_of_line[1] = self.textinput_12_2.text + "\n"
                            list_of_line[2] = self.textinput_12_3.text + "\n"
                            list_of_line[3] = self.textinput_12_4.text + "\n"
                            list_of_line[4] = self.textinput_12_5.text + "\n"
                            list_of_line[5] = self.textinput_12_6.text + "\n"
                            list_of_line[6] = self.textinput_12_7.text + "\n"
                            list_of_line[7] = self.textinput_12_8.text + "\n"
                            list_of_line[8] = self.textinput_12_9.text + "\n"
                            list_of_line[9] = self.textinput_12_10.text + "\n"
                            list_of_line[10] = self.textinput_12_11.text + "\n"
                            list_of_line[11] = self.textinput_12_12.text + "\n"
                            save_wheel_2 = open("save_wheel_2.txt", "w")
                            save_wheel_2.writelines(list_of_line)
                            save_wheel_2.close()
                            self.list_for_save_wheel_2[0] = self.textinput_12_1.text
                            self.list_for_save_wheel_2[1] = self.textinput_12_2.text
                            self.list_for_save_wheel_2[2] = self.textinput_12_3.text
                            self.list_for_save_wheel_2[3] = self.textinput_12_4.text
                            self.list_for_save_wheel_2[4] = self.textinput_12_5.text
                            self.list_for_save_wheel_2[5] = self.textinput_12_6.text
                            self.list_for_save_wheel_2[6] = self.textinput_12_7.text
                            self.list_for_save_wheel_2[7] = self.textinput_12_8.text
                            self.list_for_save_wheel_2[8] = self.textinput_12_9.text
                            self.list_for_save_wheel_2[9] = self.textinput_12_10.text
                            self.list_for_save_wheel_2[10] = self.textinput_12_11.text
                            self.list_for_save_wheel_2[11] = self.textinput_12_12.text
                            self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
            else:
                if int(self.ids.slot_number.text) == 3:
                    if str(self.textinput_3_1.text) == "" or str(self.textinput_3_2.text) == "" or str(
                            self.textinput_3_3.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_3_1.text + "\n"
                        list_of_line[1] = self.textinput_3_2.text + "\n"
                        list_of_line[2] = self.textinput_3_3.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_3_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_3_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_3_3.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "rd slot added"
                elif int(self.ids.slot_number.text) == 4:
                    if str(self.textinput_4_1.text) == "" or str(self.textinput_4_2.text) == "" or str(
                            self.textinput_4_3.text) == "" or str(self.textinput_4_4.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_4_1.text + "\n"
                        list_of_line[1] = self.textinput_4_2.text + "\n"
                        list_of_line[2] = self.textinput_4_3.text + "\n"
                        list_of_line[3] = self.textinput_4_4.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_4_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_4_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_4_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_4_4.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 5:
                    if str(self.textinput_5_1.text) == "" or str(self.textinput_5_2.text) == "" or str(
                            self.textinput_5_3.text) == "" or str(self.textinput_5_4.text) == "" or str(
                            self.textinput_5_5.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_5_1.text + "\n"
                        list_of_line[1] = self.textinput_5_2.text + "\n"
                        list_of_line[2] = self.textinput_5_3.text + "\n"
                        list_of_line[3] = self.textinput_5_4.text + "\n"
                        list_of_line[4] = self.textinput_5_5.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_5_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_5_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_5_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_5_4.text
                        self.list_for_save_wheel_3[4] = self.textinput_5_5.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 6:
                    if str(self.textinput_6_1.text) == "" or str(self.textinput_6_2.text) == "" or str(
                            self.textinput_6_3.text) == "" or str(self.textinput_6_4.text) == "" or str(
                            self.textinput_6_5.text) == "" or str(self.textinput_6_6.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_6_1.text + "\n"
                        list_of_line[1] = self.textinput_6_2.text + "\n"
                        list_of_line[2] = self.textinput_6_3.text + "\n"
                        list_of_line[3] = self.textinput_6_4.text + "\n"
                        list_of_line[4] = self.textinput_6_5.text + "\n"
                        list_of_line[5] = self.textinput_6_6.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_6_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_6_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_6_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_6_4.text
                        self.list_for_save_wheel_3[4] = self.textinput_6_5.text
                        self.list_for_save_wheel_3[5] = self.textinput_6_6.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 7:
                    if str(self.textinput_7_1.text) == "" or str(self.textinput_7_2.text) == "" or str(
                            self.textinput_7_3.text) == "" or str(self.textinput_7_4.text) == "" or str(
                            self.textinput_7_5.text) == "" or str(self.textinput_7_6.text) == "" or str(
                            self.textinput_7_7.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_7_1.text + "\n"
                        list_of_line[1] = self.textinput_7_2.text + "\n"
                        list_of_line[2] = self.textinput_7_3.text + "\n"
                        list_of_line[3] = self.textinput_7_4.text + "\n"
                        list_of_line[4] = self.textinput_7_5.text + "\n"
                        list_of_line[5] = self.textinput_7_6.text + "\n"
                        list_of_line[6] = self.textinput_7_7.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_7_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_7_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_7_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_7_4.text
                        self.list_for_save_wheel_3[4] = self.textinput_7_5.text
                        self.list_for_save_wheel_3[5] = self.textinput_7_6.text
                        self.list_for_save_wheel_3[6] = self.textinput_7_7.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 8:
                    if str(self.textinput_8_1.text) == "" or str(self.textinput_8_2.text) == "" or str(
                            self.textinput_8_3.text) == "" or str(self.textinput_8_4.text) == "" or str(
                            self.textinput_8_5.text) == "" or str(self.textinput_8_6.text) == "" or str(
                            self.textinput_8_7.text) == "" or str(self.textinput_8_8.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_8_1.text + "\n"
                        list_of_line[1] = self.textinput_8_2.text + "\n"
                        list_of_line[2] = self.textinput_8_3.text + "\n"
                        list_of_line[3] = self.textinput_8_4.text + "\n"
                        list_of_line[4] = self.textinput_8_5.text + "\n"
                        list_of_line[5] = self.textinput_8_6.text + "\n"
                        list_of_line[6] = self.textinput_8_7.text + "\n"
                        list_of_line[7] = self.textinput_8_8.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_8_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_8_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_8_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_8_4.text
                        self.list_for_save_wheel_3[4] = self.textinput_8_5.text
                        self.list_for_save_wheel_3[5] = self.textinput_8_6.text
                        self.list_for_save_wheel_3[6] = self.textinput_8_7.text
                        self.list_for_save_wheel_3[7] = self.textinput_8_8.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 9:
                    if str(self.textinput_9_1.text) == "" or str(self.textinput_9_2.text) == "" or str(
                            self.textinput_9_3.text) == "" or str(self.textinput_9_4.text) == "" or str(
                            self.textinput_9_5.text) == "" or str(self.textinput_9_6.text) == "" or str(
                            self.textinput_9_7.text) == "" or str(self.textinput_9_8.text) == "" or str(
                            self.textinput_9_9.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_9_1.text + "\n"
                        list_of_line[1] = self.textinput_9_2.text + "\n"
                        list_of_line[2] = self.textinput_9_3.text + "\n"
                        list_of_line[3] = self.textinput_9_4.text + "\n"
                        list_of_line[4] = self.textinput_9_5.text + "\n"
                        list_of_line[5] = self.textinput_9_6.text + "\n"
                        list_of_line[6] = self.textinput_9_7.text + "\n"
                        list_of_line[7] = self.textinput_9_8.text + "\n"
                        list_of_line[8] = self.textinput_9_9.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_9_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_9_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_9_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_9_4.text
                        self.list_for_save_wheel_3[4] = self.textinput_9_5.text
                        self.list_for_save_wheel_3[5] = self.textinput_9_6.text
                        self.list_for_save_wheel_3[6] = self.textinput_9_7.text
                        self.list_for_save_wheel_3[7] = self.textinput_9_8.text
                        self.list_for_save_wheel_3[8] = self.textinput_9_9.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 10:
                    if str(self.textinput_10_1.text) == "" or str(self.textinput_10_2.text) == "" or str(
                            self.textinput_10_3.text) == "" or str(self.textinput_10_4.text) == "" or str(
                            self.textinput_10_5.text) == "" or str(self.textinput_10_6.text) == "" or str(
                            self.textinput_10_7.text) == "" or str(self.textinput_10_8.text) == "" or str(
                            self.textinput_10_9.text) == "" or str(self.textinput_10_10.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_10_1.text + "\n"
                        list_of_line[1] = self.textinput_10_2.text + "\n"
                        list_of_line[2] = self.textinput_10_3.text + "\n"
                        list_of_line[3] = self.textinput_10_4.text + "\n"
                        list_of_line[4] = self.textinput_10_5.text + "\n"
                        list_of_line[5] = self.textinput_10_6.text + "\n"
                        list_of_line[6] = self.textinput_10_7.text + "\n"
                        list_of_line[7] = self.textinput_10_8.text + "\n"
                        list_of_line[8] = self.textinput_10_9.text + "\n"
                        list_of_line[9] = self.textinput_10_10.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_10_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_10_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_10_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_10_4.text
                        self.list_for_save_wheel_3[4] = self.textinput_10_5.text
                        self.list_for_save_wheel_3[5] = self.textinput_10_6.text
                        self.list_for_save_wheel_3[6] = self.textinput_10_7.text
                        self.list_for_save_wheel_3[7] = self.textinput_10_8.text
                        self.list_for_save_wheel_3[8] = self.textinput_10_9.text
                        self.list_for_save_wheel_3[9] = self.textinput_10_10.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 11:
                    if str(self.textinput_11_1.text) == "" or str(self.textinput_11_2.text) == "" or str(
                            self.textinput_11_3.text) == "" or str(self.textinput_11_4.text) == "" or str(
                            self.textinput_11_5.text) == "" or str(self.textinput_11_6.text) == "" or str(
                            self.textinput_11_7.text) == "" or str(self.textinput_11_8.text) == "" or str(
                            self.textinput_11_9.text) == "" or str(self.textinput_11_10.text) == "" or str(
                            self.textinput_11_11.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_11_1.text + "\n"
                        list_of_line[1] = self.textinput_11_2.text + "\n"
                        list_of_line[2] = self.textinput_11_3.text + "\n"
                        list_of_line[3] = self.textinput_11_4.text + "\n"
                        list_of_line[4] = self.textinput_11_5.text + "\n"
                        list_of_line[5] = self.textinput_11_6.text + "\n"
                        list_of_line[6] = self.textinput_11_7.text + "\n"
                        list_of_line[7] = self.textinput_11_8.text + "\n"
                        list_of_line[8] = self.textinput_11_9.text + "\n"
                        list_of_line[9] = self.textinput_11_10.text + "\n"
                        list_of_line[10] = self.textinput_11_11.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_11_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_11_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_11_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_11_4.text
                        self.list_for_save_wheel_3[4] = self.textinput_11_5.text
                        self.list_for_save_wheel_3[5] = self.textinput_11_6.text
                        self.list_for_save_wheel_3[6] = self.textinput_11_7.text
                        self.list_for_save_wheel_3[7] = self.textinput_11_8.text
                        self.list_for_save_wheel_3[8] = self.textinput_11_9.text
                        self.list_for_save_wheel_3[9] = self.textinput_11_10.text
                        self.list_for_save_wheel_3[10] = self.textinput_11_11.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 12:
                    if str(self.textinput_12_1.text) == "" or str(self.textinput_12_2.text) == "" or str(
                            self.textinput_12_3.text) == "" or str(self.textinput_12_4.text) == "" or str(
                            self.textinput_12_5.text) == "" or str(self.textinput_12_6.text) == "" or str(
                            self.textinput_12_7.text) == "" or str(self.textinput_12_8.text) == "" or str(
                            self.textinput_12_9.text) == "" or str(self.textinput_12_10.text) == "" or str(
                            self.textinput_12_11.text) == "" or str(self.textinput_12_12.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_3 = open("save_wheel_3.txt", "r")
                        list_of_line = save_wheel_3.readlines()
                        list_of_line[0] = self.textinput_12_1.text + "\n"
                        list_of_line[1] = self.textinput_12_2.text + "\n"
                        list_of_line[2] = self.textinput_12_3.text + "\n"
                        list_of_line[3] = self.textinput_12_4.text + "\n"
                        list_of_line[4] = self.textinput_12_5.text + "\n"
                        list_of_line[5] = self.textinput_12_6.text + "\n"
                        list_of_line[6] = self.textinput_12_7.text + "\n"
                        list_of_line[7] = self.textinput_12_8.text + "\n"
                        list_of_line[8] = self.textinput_12_9.text + "\n"
                        list_of_line[9] = self.textinput_12_10.text + "\n"
                        list_of_line[10] = self.textinput_12_11.text + "\n"
                        list_of_line[11] = self.textinput_12_12.text + "\n"
                        save_wheel_3 = open("save_wheel_3.txt", "w")
                        save_wheel_3.writelines(list_of_line)
                        save_wheel_3.close()
                        self.list_for_save_wheel_3[0] = self.textinput_12_1.text
                        self.list_for_save_wheel_3[1] = self.textinput_12_2.text
                        self.list_for_save_wheel_3[2] = self.textinput_12_3.text
                        self.list_for_save_wheel_3[3] = self.textinput_12_4.text
                        self.list_for_save_wheel_3[4] = self.textinput_12_5.text
                        self.list_for_save_wheel_3[5] = self.textinput_12_6.text
                        self.list_for_save_wheel_3[6] = self.textinput_12_7.text
                        self.list_for_save_wheel_3[7] = self.textinput_12_8.text
                        self.list_for_save_wheel_3[8] = self.textinput_12_9.text
                        self.list_for_save_wheel_3[9] = self.textinput_12_10.text
                        self.list_for_save_wheel_3[10] = self.textinput_12_11.text
                        self.list_for_save_wheel_3[11] = self.textinput_12_12.text
                        self.ids.save_wheel_3.text = str(self.ids.slot_number.text) + "th slot added"

        elif str(self.ids.save_wheel_3.text) != 'No item saved' and str(
                self.ids.save_wheel_2.text) != 'No item saved' and str(self.ids.save_wheel_1.text) != 'No item saved':
            self.button_confirm.text = "No space left"
            if self.theme == 0:
                self.animate_the_confirm_white_to_black_text()
            else:
                self.animate_the_confirm_black_to_white_text()
        else:
            if str(self.ids.save_wheel_3.text) != 'No item saved' and str(
                    self.ids.save_wheel_2.text) != 'No item saved' and str(
                    self.ids.save_wheel_1.text) == 'No item saved':
                if int(self.ids.slot_number.text) == 3:
                    if str(self.textinput_3_1.text) == "" or str(self.textinput_3_2.text) == "" or str(
                            self.textinput_3_3.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_3_1.text + "\n"
                        list_of_line[1] = self.textinput_3_2.text + "\n"
                        list_of_line[2] = self.textinput_3_3.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "rd slot added"
                elif int(self.ids.slot_number.text) == 4:
                    if str(self.textinput_4_1.text) == "" or str(self.textinput_4_2.text) == "" or str(
                            self.textinput_4_3.text) == "" or str(self.textinput_4_4.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_4_1.text + "\n"
                        list_of_line[1] = self.textinput_4_2.text + "\n"
                        list_of_line[2] = self.textinput_4_3.text + "\n"
                        list_of_line[3] = self.textinput_4_4.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 5:
                    if str(self.textinput_5_1.text) == "" or str(self.textinput_5_2.text) == "" or str(
                            self.textinput_5_3.text) == "" or str(self.textinput_5_4.text) == "" or str(
                            self.textinput_5_5.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_5_1.text + "\n"
                        list_of_line[1] = self.textinput_5_2.text + "\n"
                        list_of_line[2] = self.textinput_5_3.text + "\n"
                        list_of_line[3] = self.textinput_5_4.text + "\n"
                        list_of_line[4] = self.textinput_5_5.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 6:
                    if str(self.textinput_6_1.text) == "" or str(self.textinput_6_2.text) == "" or str(
                            self.textinput_6_3.text) == "" or str(self.textinput_6_4.text) == "" or str(
                            self.textinput_6_5.text) == "" or str(self.textinput_6_6.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_6_1.text + "\n"
                        list_of_line[1] = self.textinput_6_2.text + "\n"
                        list_of_line[2] = self.textinput_6_3.text + "\n"
                        list_of_line[3] = self.textinput_6_4.text + "\n"
                        list_of_line[4] = self.textinput_6_5.text + "\n"
                        list_of_line[5] = self.textinput_6_6.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 7:
                    if str(self.textinput_7_1.text) == "" or str(self.textinput_7_2.text) == "" or str(
                            self.textinput_7_3.text) == "" or str(self.textinput_7_4.text) == "" or str(
                            self.textinput_7_5.text) == "" or str(self.textinput_7_6.text) == "" or str(
                            self.textinput_7_7.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_7_1.text + "\n"
                        list_of_line[1] = self.textinput_7_2.text + "\n"
                        list_of_line[2] = self.textinput_7_3.text + "\n"
                        list_of_line[3] = self.textinput_7_4.text + "\n"
                        list_of_line[4] = self.textinput_7_5.text + "\n"
                        list_of_line[5] = self.textinput_7_6.text + "\n"
                        list_of_line[6] = self.textinput_7_7.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 8:
                    if str(self.textinput_8_1.text) == "" or str(self.textinput_8_2.text) == "" or str(
                            self.textinput_8_3.text) == "" or str(self.textinput_8_4.text) == "" or str(
                            self.textinput_8_5.text) == "" or str(self.textinput_8_6.text) == "" or str(
                            self.textinput_8_7.text) == "" or str(self.textinput_8_8.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_8_1.text + "\n"
                        list_of_line[1] = self.textinput_8_2.text + "\n"
                        list_of_line[2] = self.textinput_8_3.text + "\n"
                        list_of_line[3] = self.textinput_8_4.text + "\n"
                        list_of_line[4] = self.textinput_8_5.text + "\n"
                        list_of_line[5] = self.textinput_8_6.text + "\n"
                        list_of_line[6] = self.textinput_8_7.text + "\n"
                        list_of_line[7] = self.textinput_8_8.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 9:
                    if str(self.textinput_9_1.text) == "" or str(self.textinput_9_2.text) == "" or str(
                            self.textinput_9_3.text) == "" or str(self.textinput_9_4.text) == "" or str(
                            self.textinput_9_5.text) == "" or str(self.textinput_9_6.text) == "" or str(
                            self.textinput_9_7.text) == "" or str(self.textinput_9_8.text) == "" or str(
                            self.textinput_9_9.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_9_1.text + "\n"
                        list_of_line[1] = self.textinput_9_2.text + "\n"
                        list_of_line[2] = self.textinput_9_3.text + "\n"
                        list_of_line[3] = self.textinput_9_4.text + "\n"
                        list_of_line[4] = self.textinput_9_5.text + "\n"
                        list_of_line[5] = self.textinput_9_6.text + "\n"
                        list_of_line[6] = self.textinput_9_7.text + "\n"
                        list_of_line[7] = self.textinput_9_8.text + "\n"
                        list_of_line[8] = self.textinput_9_9.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 10:
                    if str(self.textinput_10_1.text) == "" or str(self.textinput_10_2.text) == "" or str(
                            self.textinput_10_3.text) == "" or str(self.textinput_10_4.text) == "" or str(
                            self.textinput_10_5.text) == "" or str(self.textinput_10_6.text) == "" or str(
                            self.textinput_10_7.text) == "" or str(self.textinput_10_8.text) == "" or str(
                            self.textinput_10_9.text) == "" or str(self.textinput_10_10.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_10_1.text + "\n"
                        list_of_line[1] = self.textinput_10_2.text + "\n"
                        list_of_line[2] = self.textinput_10_3.text + "\n"
                        list_of_line[3] = self.textinput_10_4.text + "\n"
                        list_of_line[4] = self.textinput_10_5.text + "\n"
                        list_of_line[5] = self.textinput_10_6.text + "\n"
                        list_of_line[6] = self.textinput_10_7.text + "\n"
                        list_of_line[7] = self.textinput_10_8.text + "\n"
                        list_of_line[8] = self.textinput_10_9.text + "\n"
                        list_of_line[9] = self.textinput_10_10.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 11:
                    if str(self.textinput_11_1.text) == "" or str(self.textinput_11_2.text) == "" or str(
                            self.textinput_11_3.text) == "" or str(self.textinput_11_4.text) == "" or str(
                            self.textinput_11_5.text) == "" or str(self.textinput_11_6.text) == "" or str(
                            self.textinput_11_7.text) == "" or str(self.textinput_11_8.text) == "" or str(
                            self.textinput_11_9.text) == "" or str(self.textinput_11_10.text) == "" or str(
                            self.textinput_11_11.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_11_1.text + "\n"
                        list_of_line[1] = self.textinput_11_2.text + "\n"
                        list_of_line[2] = self.textinput_11_3.text + "\n"
                        list_of_line[3] = self.textinput_11_4.text + "\n"
                        list_of_line[4] = self.textinput_11_5.text + "\n"
                        list_of_line[5] = self.textinput_11_6.text + "\n"
                        list_of_line[6] = self.textinput_11_7.text + "\n"
                        list_of_line[7] = self.textinput_11_8.text + "\n"
                        list_of_line[8] = self.textinput_11_9.text + "\n"
                        list_of_line[9] = self.textinput_11_10.text + "\n"
                        list_of_line[10] = self.textinput_11_11.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 12:
                    if str(self.textinput_12_1.text) == "" or str(self.textinput_12_2.text) == "" or str(
                            self.textinput_12_3.text) == "" or str(self.textinput_12_4.text) == "" or str(
                            self.textinput_12_5.text) == "" or str(self.textinput_12_6.text) == "" or str(
                            self.textinput_12_7.text) == "" or str(self.textinput_12_8.text) == "" or str(
                            self.textinput_12_9.text) == "" or str(self.textinput_12_10.text) == "" or str(
                            self.textinput_12_11.text) == "" or str(self.textinput_12_12.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_12_1.text + "\n"
                        list_of_line[1] = self.textinput_12_2.text + "\n"
                        list_of_line[2] = self.textinput_12_3.text + "\n"
                        list_of_line[3] = self.textinput_12_4.text + "\n"
                        list_of_line[4] = self.textinput_12_5.text + "\n"
                        list_of_line[5] = self.textinput_12_6.text + "\n"
                        list_of_line[6] = self.textinput_12_7.text + "\n"
                        list_of_line[7] = self.textinput_12_8.text + "\n"
                        list_of_line[8] = self.textinput_12_9.text + "\n"
                        list_of_line[9] = self.textinput_12_10.text + "\n"
                        list_of_line[10] = self.textinput_12_11.text + "\n"
                        list_of_line[11] = self.textinput_12_12.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
            elif str(self.ids.save_wheel_3.text) != 'No item saved' and str(
                    self.ids.save_wheel_2.text) == 'No item saved' and str(
                    self.ids.save_wheel_1.text) != 'No item saved':
                if int(self.ids.slot_number.text) == 3:
                    if str(self.textinput_3_1.text) == "" or str(self.textinput_3_2.text) == "" or str(
                            self.textinput_3_3.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_3_1.text + "\n"
                        list_of_line[1] = self.textinput_3_2.text + "\n"
                        list_of_line[2] = self.textinput_3_3.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "rd slot added"
                elif int(self.ids.slot_number.text) == 4:
                    if str(self.textinput_4_1.text) == "" or str(self.textinput_4_2.text) == "" or str(
                            self.textinput_4_3.text) == "" or str(self.textinput_4_4.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_4_1.text + "\n"
                        list_of_line[1] = self.textinput_4_2.text + "\n"
                        list_of_line[2] = self.textinput_4_3.text + "\n"
                        list_of_line[3] = self.textinput_4_4.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 5:
                    if str(self.textinput_5_1.text) == "" or str(self.textinput_5_2.text) == "" or str(
                            self.textinput_5_3.text) == "" or str(self.textinput_5_4.text) == "" or str(
                            self.textinput_5_5.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_5_1.text + "\n"
                        list_of_line[1] = self.textinput_5_2.text + "\n"
                        list_of_line[2] = self.textinput_5_3.text + "\n"
                        list_of_line[3] = self.textinput_5_4.text + "\n"
                        list_of_line[4] = self.textinput_5_5.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 6:
                    if str(self.textinput_6_1.text) == "" or str(self.textinput_6_2.text) == "" or str(
                            self.textinput_6_3.text) == "" or str(self.textinput_6_4.text) == "" or str(
                            self.textinput_6_5.text) == "" or str(self.textinput_6_6.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_6_1.text + "\n"
                        list_of_line[1] = self.textinput_6_2.text + "\n"
                        list_of_line[2] = self.textinput_6_3.text + "\n"
                        list_of_line[3] = self.textinput_6_4.text + "\n"
                        list_of_line[4] = self.textinput_6_5.text + "\n"
                        list_of_line[5] = self.textinput_6_6.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 7:
                    if str(self.textinput_7_1.text) == "" or str(self.textinput_7_2.text) == "" or str(
                            self.textinput_7_3.text) == "" or str(self.textinput_7_4.text) == "" or str(
                            self.textinput_7_5.text) == "" or str(self.textinput_7_6.text) == "" or str(
                            self.textinput_7_7.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_7_1.text + "\n"
                        list_of_line[1] = self.textinput_7_2.text + "\n"
                        list_of_line[2] = self.textinput_7_3.text + "\n"
                        list_of_line[3] = self.textinput_7_4.text + "\n"
                        list_of_line[4] = self.textinput_7_5.text + "\n"
                        list_of_line[5] = self.textinput_7_6.text + "\n"
                        list_of_line[6] = self.textinput_7_7.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 8:
                    if str(self.textinput_8_1.text) == "" or str(self.textinput_8_2.text) == "" or str(
                            self.textinput_8_3.text) == "" or str(self.textinput_8_4.text) == "" or str(
                            self.textinput_8_5.text) == "" or str(self.textinput_8_6.text) == "" or str(
                            self.textinput_8_7.text) == "" or str(self.textinput_8_8.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_8_1.text + "\n"
                        list_of_line[1] = self.textinput_8_2.text + "\n"
                        list_of_line[2] = self.textinput_8_3.text + "\n"
                        list_of_line[3] = self.textinput_8_4.text + "\n"
                        list_of_line[4] = self.textinput_8_5.text + "\n"
                        list_of_line[5] = self.textinput_8_6.text + "\n"
                        list_of_line[6] = self.textinput_8_7.text + "\n"
                        list_of_line[7] = self.textinput_8_8.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 9:
                    if str(self.textinput_9_1.text) == "" or str(self.textinput_9_2.text) == "" or str(
                            self.textinput_9_3.text) == "" or str(self.textinput_9_4.text) == "" or str(
                            self.textinput_9_5.text) == "" or str(self.textinput_9_6.text) == "" or str(
                            self.textinput_9_7.text) == "" or str(self.textinput_9_8.text) == "" or str(
                            self.textinput_9_9.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_9_1.text + "\n"
                        list_of_line[1] = self.textinput_9_2.text + "\n"
                        list_of_line[2] = self.textinput_9_3.text + "\n"
                        list_of_line[3] = self.textinput_9_4.text + "\n"
                        list_of_line[4] = self.textinput_9_5.text + "\n"
                        list_of_line[5] = self.textinput_9_6.text + "\n"
                        list_of_line[6] = self.textinput_9_7.text + "\n"
                        list_of_line[7] = self.textinput_9_8.text + "\n"
                        list_of_line[8] = self.textinput_9_9.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 10:
                    if str(self.textinput_10_1.text) == "" or str(self.textinput_10_2.text) == "" or str(
                            self.textinput_10_3.text) == "" or str(self.textinput_10_4.text) == "" or str(
                            self.textinput_10_5.text) == "" or str(self.textinput_10_6.text) == "" or str(
                            self.textinput_10_7.text) == "" or str(self.textinput_10_8.text) == "" or str(
                            self.textinput_10_9.text) == "" or str(self.textinput_10_10.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_10_1.text + "\n"
                        list_of_line[1] = self.textinput_10_2.text + "\n"
                        list_of_line[2] = self.textinput_10_3.text + "\n"
                        list_of_line[3] = self.textinput_10_4.text + "\n"
                        list_of_line[4] = self.textinput_10_5.text + "\n"
                        list_of_line[5] = self.textinput_10_6.text + "\n"
                        list_of_line[6] = self.textinput_10_7.text + "\n"
                        list_of_line[7] = self.textinput_10_8.text + "\n"
                        list_of_line[8] = self.textinput_10_9.text + "\n"
                        list_of_line[9] = self.textinput_10_10.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 11:
                    if str(self.textinput_11_1.text) == "" or str(self.textinput_11_2.text) == "" or str(
                            self.textinput_11_3.text) == "" or str(self.textinput_11_4.text) == "" or str(
                            self.textinput_11_5.text) == "" or str(self.textinput_11_6.text) == "" or str(
                            self.textinput_11_7.text) == "" or str(self.textinput_11_8.text) == "" or str(
                            self.textinput_11_9.text) == "" or str(self.textinput_11_10.text) == "" or str(
                            self.textinput_11_11.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_11_1.text + "\n"
                        list_of_line[1] = self.textinput_11_2.text + "\n"
                        list_of_line[2] = self.textinput_11_3.text + "\n"
                        list_of_line[3] = self.textinput_11_4.text + "\n"
                        list_of_line[4] = self.textinput_11_5.text + "\n"
                        list_of_line[5] = self.textinput_11_6.text + "\n"
                        list_of_line[6] = self.textinput_11_7.text + "\n"
                        list_of_line[7] = self.textinput_11_8.text + "\n"
                        list_of_line[8] = self.textinput_11_9.text + "\n"
                        list_of_line[9] = self.textinput_11_10.text + "\n"
                        list_of_line[10] = self.textinput_11_11.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 12:
                    if str(self.textinput_12_1.text) == "" or str(self.textinput_12_2.text) == "" or str(
                            self.textinput_12_3.text) == "" or str(self.textinput_12_4.text) == "" or str(
                            self.textinput_12_5.text) == "" or str(self.textinput_12_6.text) == "" or str(
                            self.textinput_12_7.text) == "" or str(self.textinput_12_8.text) == "" or str(
                            self.textinput_12_9.text) == "" or str(self.textinput_12_10.text) == "" or str(
                            self.textinput_12_11.text) == "" or str(self.textinput_12_12.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_2 = open("save_wheel_2.txt", "r")
                        list_of_line = save_wheel_2.readlines()
                        list_of_line[0] = self.textinput_12_1.text + "\n"
                        list_of_line[1] = self.textinput_12_2.text + "\n"
                        list_of_line[2] = self.textinput_12_3.text + "\n"
                        list_of_line[3] = self.textinput_12_4.text + "\n"
                        list_of_line[4] = self.textinput_12_5.text + "\n"
                        list_of_line[5] = self.textinput_12_6.text + "\n"
                        list_of_line[6] = self.textinput_12_7.text + "\n"
                        list_of_line[7] = self.textinput_12_8.text + "\n"
                        list_of_line[8] = self.textinput_12_9.text + "\n"
                        list_of_line[9] = self.textinput_12_10.text + "\n"
                        list_of_line[10] = self.textinput_12_11.text + "\n"
                        list_of_line[11] = self.textinput_12_12.text + "\n"
                        save_wheel_2 = open("save_wheel_2.txt", "w")
                        save_wheel_2.writelines(list_of_line)
                        save_wheel_2.close()
                        self.ids.save_wheel_2.text = str(self.ids.slot_number.text) + "th slot added"
            elif str(self.ids.save_wheel_3.text) != 'No item saved' and str(
                    self.ids.save_wheel_2.text) == 'No item saved' and str(
                    self.ids.save_wheel_1.text) == 'No item saved':
                if int(self.ids.slot_number.text) == 3:
                    if str(self.textinput_3_1.text) == "" or str(self.textinput_3_2.text) == "" or str(
                            self.textinput_3_3.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_3_1.text + "\n"
                        list_of_line[1] = self.textinput_3_2.text + "\n"
                        list_of_line[2] = self.textinput_3_3.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "rd slot added"
                elif int(self.ids.slot_number.text) == 4:
                    if str(self.textinput_4_1.text) == "" or str(self.textinput_4_2.text) == "" or str(
                            self.textinput_4_3.text) == "" or str(self.textinput_4_4.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_4_1.text + "\n"
                        list_of_line[1] = self.textinput_4_2.text + "\n"
                        list_of_line[2] = self.textinput_4_3.text + "\n"
                        list_of_line[3] = self.textinput_4_4.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 5:
                    if str(self.textinput_5_1.text) == "" or str(self.textinput_5_2.text) == "" or str(
                            self.textinput_5_3.text) == "" or str(self.textinput_5_4.text) == "" or str(
                            self.textinput_5_5.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_5_1.text + "\n"
                        list_of_line[1] = self.textinput_5_2.text + "\n"
                        list_of_line[2] = self.textinput_5_3.text + "\n"
                        list_of_line[3] = self.textinput_5_4.text + "\n"
                        list_of_line[4] = self.textinput_5_5.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 6:
                    if str(self.textinput_6_1.text) == "" or str(self.textinput_6_2.text) == "" or str(
                            self.textinput_6_3.text) == "" or str(self.textinput_6_4.text) == "" or str(
                            self.textinput_6_5.text) == "" or str(self.textinput_6_6.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_6_1.text + "\n"
                        list_of_line[1] = self.textinput_6_2.text + "\n"
                        list_of_line[2] = self.textinput_6_3.text + "\n"
                        list_of_line[3] = self.textinput_6_4.text + "\n"
                        list_of_line[4] = self.textinput_6_5.text + "\n"
                        list_of_line[5] = self.textinput_6_6.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 7:
                    if str(self.textinput_7_1.text) == "" or str(self.textinput_7_2.text) == "" or str(
                            self.textinput_7_3.text) == "" or str(self.textinput_7_4.text) == "" or str(
                            self.textinput_7_5.text) == "" or str(self.textinput_7_6.text) == "" or str(
                            self.textinput_7_7.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_7_1.text + "\n"
                        list_of_line[1] = self.textinput_7_2.text + "\n"
                        list_of_line[2] = self.textinput_7_3.text + "\n"
                        list_of_line[3] = self.textinput_7_4.text + "\n"
                        list_of_line[4] = self.textinput_7_5.text + "\n"
                        list_of_line[5] = self.textinput_7_6.text + "\n"
                        list_of_line[6] = self.textinput_7_7.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 8:
                    if str(self.textinput_8_1.text) == "" or str(self.textinput_8_2.text) == "" or str(
                            self.textinput_8_3.text) == "" or str(self.textinput_8_4.text) == "" or str(
                            self.textinput_8_5.text) == "" or str(self.textinput_8_6.text) == "" or str(
                            self.textinput_8_7.text) == "" or str(self.textinput_8_8.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_8_1.text + "\n"
                        list_of_line[1] = self.textinput_8_2.text + "\n"
                        list_of_line[2] = self.textinput_8_3.text + "\n"
                        list_of_line[3] = self.textinput_8_4.text + "\n"
                        list_of_line[4] = self.textinput_8_5.text + "\n"
                        list_of_line[5] = self.textinput_8_6.text + "\n"
                        list_of_line[6] = self.textinput_8_7.text + "\n"
                        list_of_line[7] = self.textinput_8_8.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 9:
                    if str(self.textinput_9_1.text) == "" or str(self.textinput_9_2.text) == "" or str(
                            self.textinput_9_3.text) == "" or str(self.textinput_9_4.text) == "" or str(
                            self.textinput_9_5.text) == "" or str(self.textinput_9_6.text) == "" or str(
                            self.textinput_9_7.text) == "" or str(self.textinput_9_8.text) == "" or str(
                            self.textinput_9_9.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_9_1.text + "\n"
                        list_of_line[1] = self.textinput_9_2.text + "\n"
                        list_of_line[2] = self.textinput_9_3.text + "\n"
                        list_of_line[3] = self.textinput_9_4.text + "\n"
                        list_of_line[4] = self.textinput_9_5.text + "\n"
                        list_of_line[5] = self.textinput_9_6.text + "\n"
                        list_of_line[6] = self.textinput_9_7.text + "\n"
                        list_of_line[7] = self.textinput_9_8.text + "\n"
                        list_of_line[8] = self.textinput_9_9.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 10:
                    if str(self.textinput_10_1.text) == "" or str(self.textinput_10_2.text) == "" or str(
                            self.textinput_10_3.text) == "" or str(self.textinput_10_4.text) == "" or str(
                            self.textinput_10_5.text) == "" or str(self.textinput_10_6.text) == "" or str(
                            self.textinput_10_7.text) == "" or str(self.textinput_10_8.text) == "" or str(
                            self.textinput_10_9.text) == "" or str(self.textinput_10_10.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_10_1.text + "\n"
                        list_of_line[1] = self.textinput_10_2.text + "\n"
                        list_of_line[2] = self.textinput_10_3.text + "\n"
                        list_of_line[3] = self.textinput_10_4.text + "\n"
                        list_of_line[4] = self.textinput_10_5.text + "\n"
                        list_of_line[5] = self.textinput_10_6.text + "\n"
                        list_of_line[6] = self.textinput_10_7.text + "\n"
                        list_of_line[7] = self.textinput_10_8.text + "\n"
                        list_of_line[8] = self.textinput_10_9.text + "\n"
                        list_of_line[9] = self.textinput_10_10.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 11:
                    if str(self.textinput_11_1.text) == "" or str(self.textinput_11_2.text) == "" or str(
                            self.textinput_11_3.text) == "" or str(self.textinput_11_4.text) == "" or str(
                            self.textinput_11_5.text) == "" or str(self.textinput_11_6.text) == "" or str(
                            self.textinput_11_7.text) == "" or str(self.textinput_11_8.text) == "" or str(
                            self.textinput_11_9.text) == "" or str(self.textinput_11_10.text) == "" or str(
                            self.textinput_11_11.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_11_1.text + "\n"
                        list_of_line[1] = self.textinput_11_2.text + "\n"
                        list_of_line[2] = self.textinput_11_3.text + "\n"
                        list_of_line[3] = self.textinput_11_4.text + "\n"
                        list_of_line[4] = self.textinput_11_5.text + "\n"
                        list_of_line[5] = self.textinput_11_6.text + "\n"
                        list_of_line[6] = self.textinput_11_7.text + "\n"
                        list_of_line[7] = self.textinput_11_8.text + "\n"
                        list_of_line[8] = self.textinput_11_9.text + "\n"
                        list_of_line[9] = self.textinput_11_10.text + "\n"
                        list_of_line[10] = self.textinput_11_11.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
                elif int(self.ids.slot_number.text) == 12:
                    if str(self.textinput_12_1.text) == "" or str(self.textinput_12_2.text) == "" or str(
                            self.textinput_12_3.text) == "" or str(self.textinput_12_4.text) == "" or str(
                            self.textinput_12_5.text) == "" or str(self.textinput_12_6.text) == "" or str(
                            self.textinput_12_7.text) == "" or str(self.textinput_12_8.text) == "" or str(
                            self.textinput_12_9.text) == "" or str(self.textinput_12_10.text) == "" or str(
                            self.textinput_12_11.text) == "" or str(self.textinput_12_12.text) == "":
                        self.button_confirm.text = "Please fill remaining slots"
                        if self.theme == 0:
                            self.animate_the_confirm_white_to_black_text()
                        else:
                            self.animate_the_confirm_black_to_white_text()
                        pass
                    else:
                        save_wheel_1 = open("save_wheel_1.txt", "r")
                        list_of_line = save_wheel_1.readlines()
                        list_of_line[0] = self.textinput_12_1.text + "\n"
                        list_of_line[1] = self.textinput_12_2.text + "\n"
                        list_of_line[2] = self.textinput_12_3.text + "\n"
                        list_of_line[3] = self.textinput_12_4.text + "\n"
                        list_of_line[4] = self.textinput_12_5.text + "\n"
                        list_of_line[5] = self.textinput_12_6.text + "\n"
                        list_of_line[6] = self.textinput_12_7.text + "\n"
                        list_of_line[7] = self.textinput_12_8.text + "\n"
                        list_of_line[8] = self.textinput_12_9.text + "\n"
                        list_of_line[9] = self.textinput_12_10.text + "\n"
                        list_of_line[10] = self.textinput_12_11.text + "\n"
                        list_of_line[11] = self.textinput_12_12.text + "\n"
                        save_wheel_1 = open("save_wheel_1.txt", "w")
                        save_wheel_1.writelines(list_of_line)
                        save_wheel_1.close()
                        self.ids.save_wheel_1.text = str(self.ids.slot_number.text) + "th slot added"
            else:
                self.button_confirm.text = "Error"
                if self.theme == 0:
                    self.animate_the_confirm_white_to_black_text()
                else:
                    self.animate_the_confirm_black_to_white_text()

    def animate_the_confirm_white_to_black_text(self):
        anim = Animation(color=[0, 0, 0, 0], duration=6)
        anim.start(self.button_confirm)

    def animate_the_confirm_black_to_white_text(self):
        anim = Animation(color=[1, 1, 1, 0], duration=6)
        anim.start(self.button_confirm)

    def minute_0_off(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "No reminder is set"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
        else:
            self.button_confirm.text = "No reminder is set"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
        pass

    def notification_alarm_for_5(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="5 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo", app_icon=self.icon)# timeout=10 can also be given

    def notification_alarm_for_10(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="10 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo",app_icon=self.icon)

    def notification_alarm_for_15(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="15 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo",app_icon=self.icon)

    def notification_alarm_for_20(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="20 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo",app_icon=self.icon)

    def notification_alarm_for_30(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="30 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo",app_icon=self.icon)

    def notification_alarm_for_45(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="45 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo",app_icon=self.icon)

    def notification_alarm_for_60(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="60 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo",app_icon=self.icon)

    def notification_alarm_for_90(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="90 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo",app_icon=self.icon)

    def notification_alarm_for_120(self, _):
        plyer.notification.notify(title="Spinning",
                                  message="120 minutes are over.Please spin the wheel for other work",
                                  app_name="SpinToDo",app_icon=self.icon)

    def minute_5(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 5 minutes"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for_5, 300)
        else:
            self.button_confirm.text = "Notification will remind in 5 minutes"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for_5, 300)
        pass

    def minute_10(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 10 minutes"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for_10, 600)
        else:
            self.button_confirm.text = "Notification will remind in 10 minutes"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for_10, 600)
        pass

    def minute_15(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 15 minutes"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for_15, 900)
        else:
            self.button_confirm.text = "Notification will remind in 15 minutes"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for_15, 900)
        pass

    def minute_20(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 20 minutes"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for_20, 1200)
        else:
            self.button_confirm.text = "Notification will remind in 20 minutes"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for_20, 1200)
        pass

    def minute_30(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 30 minutes"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for30, 1800)
        else:
            self.button_confirm.text = "Notification will remind in 30 minutes"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for30, 1800)
        pass

    def minute_45(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 45 minutes"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for_45, 2700)
        else:
            self.button_confirm.text = "Notification will remind in 45 minutes"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for_45, 2700)
        pass

    def minute_60(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 1 hour"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for_60, 3600)
        else:
            self.button_confirm.text = "Notification will remind in 1 hour"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for_60, 3600)
        pass

    def minute_90(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 90 minutes"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for_90, 5400)
        else:
            self.button_confirm.text = "Notification will remind in 90 minutes"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for_90, 5400)
        pass

    def minute_120(self):
        self.ids.drop_reminder.dismiss()
        if self.theme == 0:
            self.button_confirm.text = "Notification will remind in 2 hours"
            self.button_confirm.color = [1, 1, 1, 1]
            self.animate_the_confirm_white_to_black_text()
            Clock.schedule_once(self.notification_alarm_for_120, 7200)
        else:
            self.button_confirm.text = "Notification will remind in 2 hours"
            self.button_confirm.color = [0, 0, 0, 1]
            self.animate_the_confirm_black_to_white_text()
            Clock.schedule_once(self.notification_alarm_for_120, 7200)
        pass


class ImageButton(ButtonBehavior, Image):
    pass


class drop(DropDown, ButtonBehavior):
    pass


class drop_reminder(DropDown, ButtonBehavior):
    pass


class SpinToDoApp(App):
    def build(self):
        Window.bind(on_keyboard=self.on_request_close)
        return HomePage()

    def on_request_close(self, window, keycode1, keycode2, text, modifiers):
        if keycode1 in [27, 1001]:
            self.textpopup(title='Exit', text='Are you sure?')
            self.last_details()
            return True
        return False

    def textpopup(self, title='', text=''):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text, bold=True))
        mybutton = Button(text='OK', size_hint=(1, 0.4), background_normal="middle_black_64.png")
        box.add_widget(mybutton)
        popup = Popup(title=title, content=box, size_hint=(None, None),
                      size=(Window.width - Window.width / 3, Window.height / 4))
        mybutton.bind(on_release=self.stop)
        popup.open()

    def last_details(self):
        details = open("detail.txt", "r")
        list_of_line = details.readlines()
        list_of_line[0] = str(self.root.ids.save_wheel_1.text) + "\n"
        list_of_line[1] = str(self.root.ids.save_wheel_2.text) + "\n"
        list_of_line[2] = str(self.root.ids.save_wheel_3.text) + "\n"
        details = open("detail.txt", "w")
        details.writelines(list_of_line)
        details.close()

if __name__ == "__main__":
    SpinToDoApp().run()
