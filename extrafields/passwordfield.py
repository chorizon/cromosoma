from cromosoma.corefields import PhangoField
from cromosoma.coreforms import PasswordForm
from passlib.hash import bcrypt

class PasswordField(PhangoField):
    
    def __init__(self, name, size=255, required=False):
        
        super(PasswordField, self).__init__(name, size, required)    
        self.protected=True
        self.name_form=PasswordForm
        self.default_value=''
    
    def check(self, value):
        
        self.txt_error=''
        self.error=False
        print(value)
        value.strip()
        
        if value=='':
            
            self.txt_error="The value is empty"
            self.error=True
            
        else:
            value = bcrypt.encrypt(value)
            
        
        return value
    
    @staticmethod
    def verify( password, h):
        
        return bcrypt.verify(password, h)