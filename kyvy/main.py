from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

import back

class Body(BoxLayout):

    def __init__(self, **kwargs):
        super(Body, self).__init__(**kwargs)


    def clear_form(self):
        self.ids.txtname.text=''
        self.ids.txtaddress.text=''
        self.ids.txtphno.text=''
        self.ids.txtnodays.text=''
        self.ids.txttype.text=''
        
    def add_record(self):
        back.insert(self.ids.txtname.text,\
                    self.ids.txtaddress.text,\
                    self.ids.txtphno.text,\
                    self.ids.txtnodays.text,\
                    self.ids.txttype.text,\
                    '')
        self.ids.lbl.text = 'Total cash: %s'%str(self.calculation(int(self.ids.txtnodays.text),\
                                           self.ids.txttype.text))

    def calculation(self,no_of_days,room_type):
        if room_type=="normal" or room_type=="NORMAL":
            total=int(no_of_days)*1500
            return total
        elif room_type=="KING" or room_type=="king":
            total=int(no_of_days)*1800
            return total
        elif room_type=="delux" or room_type=="DELUX":
            total=int(no_of_days)*2000
            return total

    def move_next(self):
        pass

    def move_previous(self):
        pass

    def delete_record(self):
        pass


    def view_all(self):
        pass
    
        
        

class MainApp(App):

    def build(self):
        return Body()

if __name__=='__main__':
    MainApp().run()
