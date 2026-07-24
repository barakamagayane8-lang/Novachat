from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class NovaChat(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"

        layout = MDBoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        titre = MDLabel(
            text="🌟 NovaChat",
            halign="center",
            font_style="H3"
        )

        self.message = MDTextField(
            hint_text="Écrire un message..."
        )

        bouton = MDRaisedButton(
            text="Envoyer",
            pos_hint={"center_x": 0.5}
        )

        bouton.bind(
            on_press=self.envoyer
        )

        self.reponse = MDLabel(
            text="Bienvenue dans NovaChat",
            halign="center"
        )

        layout.add_widget(titre)
        layout.add_widget(self.reponse)
        layout.add_widget(self.message)
        layout.add_widget(bouton)

        return layout

    def envoyer(self, instance):
        if self.message.text:
            self.reponse.text = "Moi : " + self.message.text
            self.message.text = ""


NovaChat().run()