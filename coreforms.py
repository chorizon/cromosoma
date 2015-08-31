#!/usr/bin/python3

#Forms para python3

class BaseForm:
    
    def __init__(self, name, value):
        
        self.label=name
        self.name=name
        self.default_value=value
        self.css=''
        self.type='text'
        self.required=False
        
    def form(self):
        
        return '<input type="'+self.type+'" class="'+self.css+'" name="'+self.name+'" value="'+self.setform(self.default_value)+'">'
    
    #Method for escape value for html input
    
    def setform(self, value):
        
        return value.replace('"', '\"')

class TextForm(BaseForm):
    
    def __init__(self, name, value):
        super(TextForm, self).__init__(name, value)

class PasswordForm(BaseForm):
    
    def __init__(self, name, value):
        super(PasswordForm, self).__init__(name, value)
        self.type='password'

class HiddenForm(BaseForm):
    
    def __init__(self, name, value):
        super(HiddenForm, self).__init__(name, value)
        self.type='hidden'
       