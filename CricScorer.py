from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.config import Config

# Set resizable to False before application starts
Config.set('graphics', 'resizable', False)


Builder.load_file('score.kv')

# Python code
class Lay(Widget):
    def over_plus(self, value):
        self.overs = self.ids.balls.text
        self.result = value+int(self.overs)
        if self.result == 6:
            self.ids.ov.text= str(int(self.ids.ov.text)+1)
            self.ids.balls.text=str(0)
        else:
            self.ids.balls.text = str(self.result)

    #def over_sub(self, value):
        #self.overs = self.ids.balls.text
        #self.result = int(self.overs)-value
        #if self.ids.balls.text == 0:
            #self.ids.ov.text= str(int(self.ids.ov.text)-1)
            #self.overs=str(5)
        #else:
            #self.ids.balls.text = str(self.result)

    def inc_score(self, value):
        result=int(self.ids.score.text)+value
        self.ids.score.text=str(result)
        self.over_plus(1)

    def wide(self, value):
        self.result=int(self.ids.score.text)+value
        self.ids.score.text=str(self.result)

    def out(self, value):
        self.result=int(self.ids.wick.text)+value
        self.ids.wick.text=str(self.result)
        if self.ids.wick.text==str(10):
            self.ids.no_0.disabled = True
            self.ids.no_1.disabled = True
            self.ids.no_2.disabled = True
            self.ids.no_4.disabled = True
            self.ids.no_6.disabled = True
            self.ids.wide.disabled = True
            self.ids.out.disabled = True
            self.ids.nb.disabled = True
            self.ids.b.disabled = False
            self.ids.plus.disabled = True
            self.ids.minus.disabled = True

    def enable(self):
        self.ids.no_0.disabled = False
        self.ids.no_1.disabled = False
        self.ids.no_2.disabled = False
        self.ids.no_4.disabled = False
        self.ids.no_6.disabled = False
        self.ids.wide.disabled = False
        self.ids.out.disabled = False
        self.ids.nb.disabled = False
        self.ids.b.disabled = False
        self.ids.plus.disabled = False
        self.ids.minus.disabled = False

        self.ids.ov.text=str(0)
        self.ids.balls.text=str(0)
        self.ids.score.text=str(0)
        self.ids.wick.text=str(0)

class CricScorerApp(App):
    def build(self):
        Window.size=(360,640)
        Window.resize=False,False
        return Lay()

if __name__ == '__main__':
    CricScorerApp().run()
