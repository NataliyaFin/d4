from django import template
 
register = template.Library() # регестрируем наши фильтры

@register.filter(name='censor')
def censor(value, arg):
    censorList = ['жопа', 'срака', 'сраный', 'бля', 'говно', 'сука', ]
    vEdit = value
    result = ''

    for word in censorList:
        vTemp = vEdit.lower().replace(word, arg * len(word))
        vEdit = vTemp

    for i in range(0, len(value)):
        if (value[i] != vEdit[i]):
            result += vEdit[i].upper()
        else:
            result += vEdit[i]

    return result