from cromosoma.webmodel import PhangoField
from cromosoma import coreforms

class IntegerField(PhangoField):
    
    def __init__(self, name, size=11, required=False):
        super(IntegerField, self).__init__(name, size, required)
    
    def check(self, value):
        
        error=None
        
        value=str(int(value))
        
        if value==0:
            txt_error="The value is zero"
            error=True
            
        return value
    
    def get_type_sql(self):

        return 'INT('+str(self.size)+') NOT NULL DEFAULT "0"'

class CharField(PhangoField):
    
    pass

class PasswordField(PhangoField):
    
    def __init__(self, name, size=255, required=False):
        self.protected=True
        super(PasswordField, self).__init__(name, size, required)    
    

class ForeignKeyField(IntegerField):
    
    def __init__(self, name, related_table, size=11, required=False, identifier_field='id', named_field="id", select_fields=[]):
    
        self.table_id=related_table.name_field_id
    
        self.table_name=related_table.name
    
        self.identifier_field=identifier_field
        
        self.named_field=named_field
        
        self.select_fields=select_fields
        
        super(ForeignKeyField, self).__init__(name, size, required)
    
        self.foreignkey=True
        
