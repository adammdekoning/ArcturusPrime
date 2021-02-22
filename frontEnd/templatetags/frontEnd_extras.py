import datetime
from django import template

register = template.Library()

def format_time(time):
    formatted_time = time.strftime('%M:%S.%f')
    return formatted_time[:-5]

register.filter('format_time', format_time)
