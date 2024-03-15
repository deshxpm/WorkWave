import re
import datetime
from django.conf import settings
from django.template.loader import get_template

def get_context(request=None , **kwargs):
    # try:
    type_msg = 'None'
    text = None
    if request.session.get("_message", None) is not None:
        msg = request.session.pop("_message")
        if msg.get("type") == "success" or msg.get("type") == "SUCCESS" or str(msg.get("type")) == "25":
            type_msg = "toastrsuccess"
        else:
            type_msg = "toastrerror"
        text = msg.get("text")        
    kwargs.update({
            'title': '',
            type_msg : text ,
            'today':datetime.date.today(),
        })
    # except:
    #     pass
    return kwargs

def is_mobile(input):
    if len(input) == 10:
        return str(input).isnumeric()
    return False
