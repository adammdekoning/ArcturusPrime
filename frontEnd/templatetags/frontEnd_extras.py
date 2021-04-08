import datetime
from django import template

register = template.Library()

def format_time(time):
    try:
        formatted_time = time.strftime('%M:%S.%f')
        return formatted_time[:-5]
    except:
        return '-'

register.filter('format_time', format_time)
