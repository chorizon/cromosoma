#!/usr/bin/python3

from cromosoma.webmodel import WebModel
from cromosoma.coreforms import PasswordForm
from citoplasma.i18n import I18n

class UserModel(WebModel):
    
    def __init__(self, name_field_id="id"):
        
        super().__init__(name_field_id) 
        
        self.password_field='password'
    
    def create_forms(self, arr_fields={}):
        
        # Add password_repeat to forms from the model
        
        super().create_forms(arr_fields)
        
        if self.password_field in arr_fields:
            
            repeat_password=PasswordForm('repeat_password', '')
    
            repeat_password.required=1
            
            repeat_password.label=I18n.lang('common', 'repeat_password', 'Repeat Password')
            
            self.create_form_after('password', repeat_password)
        