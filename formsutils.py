#!/usr/bin/python3

from cromosoma import corefields
from bottle import request, FormsDict

def pass_values_to_form(post, arr_form, yes_error=True):
    
    for key, value in arr_form.items():
        post[key]=post.get(key, '')
        arr_form[key].default_value=post[key]
        
        if arr_form[key].field==None:
           arr_form[key].field=corefields.CharField(key, 255, required=False) 
        
        # Recheck value if no set error field
        if arr_form[key].field.error == None:
            arr_form[key].field.check(post[key])
        
        if arr_form[key].required==True and arr_form[key].field.error==True and yes_error==True:
           arr_form[key].txt_error=arr_form[key].field.txt_error

        # Reset error on field. 

        arr_form[key].field.error=None

    return arr_form

def show_form(post, arr_form, t, yes_error=True):
    
    pass_values_to_form(post, arr_form, yes_error)
    
    return t.load_template('forms/modelform.phtml', forms=arr_form)

# Need this for obtain utf8 valid values

def obtain_get():
    
    return request.query.decode()

def obtain_post():
    
    return request.forms.decode()
    
    
    