#!/usr/bin/python3

#Forms para python3

class BaseForm:
    
    def __init__(name, value):
        
        self.label=name
        self.name=name
        self.default_value=value
        self.css=''
        self.type='text'
        self.required=False
        
    def form():
        
        return '<input type="'+self.type+'" class="'+self.css+'" name="'+self.setform(self.default_value)+'">'
    
    #Method for escape value for html input
    
    def setform(value):
        
        return value.replace('"', '\"')

class TextForm(BaseForm):
    
    def __init__(name, value):
        super(TextForm, self).__init__(name, value)

class PasswordForm(BaseForm):
    
    def __init__(name, value):
        self.type='password'
        super(PasswordForm, self).__init__(name, value)

class HiddenForm(BaseForm):
    
    def __init__(name, value):
        self.type='hidden'
        super(PasswordForm, self).__init__(name, value)
       