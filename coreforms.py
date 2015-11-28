#!/usr/bin/python3

from collections import OrderedDict

#Forms para python3

class BaseForm:
    
    def __init__(self, name, value):
        
        self.label=name
        self.name=name
        self.default_value=value
        self.css=''
        self.type='text'
        self.field=None
        self.required=False
        self.txt_error=''
        
    def form(self):
        
        return '<input type="'+self.type+'" class="'+self.css+'" name="'+self.name+'" value="'+self.setform(self.default_value)+'">'
    
    #Method for escape value for html input. DON'T CHANGE IF YOU DON'T KNOWN WHAT ARE YOU DOING
    
    def setform(self, value):
        
        value=str(value)
        
        return value.replace('"', '&quot;')

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

"""
class SelectForm(BaseForm):
	
	def form(self):
		
		the_form='<select name="">\n'
		
		for k,v in arr_select.items():
			pass
		
		the_form+='</select>\n'
		
		pass
    
    def __init__(self, name, value):
		
		self.arr_select=OrderedDict()
		
        super(SelectForm, self).__init__(name, value)
"""