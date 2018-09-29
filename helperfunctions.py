from dateutil.parser import *
def is_date(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False

def parse_datetime(string):
    return parse(string)