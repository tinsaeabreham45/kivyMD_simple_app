from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem, MDList
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from kivymd.uix.textfield import MDTextField

Window.size = (400, 500)
nav_helper = '''
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Learn English'
                        left_action_items:[["menu",lambda x: nav_drawer.set_state('toggle')]]
                        elevation:2
                    Widget:
'''


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.main_screen = Screen()
        self.given_sentence = MDTextField(hint_text='write a sentence here',
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                          size_hint_x=None,
                                          width=300
                                          )
        self.action_btn = MDRectangleFlatButton(text='Show Answer', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                                on_release=self.sent_analyzer)
        self.main_screen.add_widget(self.given_sentence)
        self.main_screen.add_widget(self.action_btn)
        self.my_nav = Builder.load_string(nav_helper)

        self.main_screen.add_widget(self.my_nav)

        return self.main_screen

    def sent_analyzer(self, obj):
        sentence = self.given_sentence.text
        token_sentence = word_tokenize(sentence)
        pos_tag_sent = pos_tag(token_sentence)
        self.scroll_list = ScrollView(pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.list_view = MDList()
        self.scroll_list.add_widget(self.list_view)
        close_btn=MDRectangleFlatButton(text='close',on_release=self.delete_view)
        Noun_list = [word for (word, pos) in pos_tag_sent if pos.startswith('NN')]
        for words in Noun_list:
            items = TwoLineListItem(text='noun ' + words)
            self.list_view.add_widget(items)
        self.main_screen.add_widget(close_btn)

        self.main_screen.add_widget(self.scroll_list)
    def delete_view(self,obj):
        del self.scroll_list




MyApp().run()
