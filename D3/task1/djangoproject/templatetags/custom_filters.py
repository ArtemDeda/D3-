from django import template

register = template.Library()


@register.filter(is_safe=True)
def censor(value):
    unwanted_words = ['пиздец', 'pizdec', 'задолбало']
    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))

    return value
