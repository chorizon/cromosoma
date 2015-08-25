#!/usr/bin/python3

#Forms para python3

class BaseForm:
    
    def __init__(name, value):
        
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
