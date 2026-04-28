from django import template
from math import trunc

register = template.Library()

@register.filter
def liked_filter(likes):
    if likes>1000000:
        temp_likes = (trunc(likes/100000))/10
        likes = f"{temp_likes}M"
    elif likes>10000:
        temp_likes = trunc(likes/1000)
        likes = f"{temp_likes}K"
    return likes