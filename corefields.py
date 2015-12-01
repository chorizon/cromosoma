from cromosoma.webmodel import PhangoField
from cromosoma import coreforms

class IntegerField(PhangoField):
    
    def __init__(self, name, size=11, required=False):
        super(IntegerField, self).__init__(name, size, required)
    
    def check(self, value):
        
        self.error=None
        self.txt_error=''
        
        try:
        
            value=str(int(value))
        
            if value==0 and self.required==True:
                self.txt_error="The value is zero"
                self.error=True
        except:
            
            self.error=True

        return value
    
    def get_type_sql(self):

        return 'INT('+str(self.size)+') NOT NULL DEFAULT "0"'

class CharField(PhangoField):
    
    pass

class ForeignKeyField(IntegerField):
    
    def __init__(self, name, related_table, size=11, required=False, identifier_field='id', named_field="id", select_fields=[]):
    
        self.table_id=related_table.name_field_id
    
        self.table_name=related_table.name
    
        self.identifier_field=identifier_field
        
        self.named_field=named_field
        
        self.select_fields=select_fields
        
        super(ForeignKeyField, self).__init__(name, size, required)
    
        self.foreignkey=True

class BooleanField(IntegerField):
    
    def check(self, value):
        
        self.error=None
        self.txt_error=''
        
        value=str(int(value))
        
        if value<0 or value>1:
            txt_error="This value is boolean"
            self.error=True
            
        return value
    
    def get_type_sql(self):

        return 'BOOLEAN NOT NULL DEFAULT "0"'
    
    
