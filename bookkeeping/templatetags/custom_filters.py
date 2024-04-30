from django import template


register = template.Library()


@register.filter()
def find_items(items, register_id):

    if register_id in items:
        return items[register_id]


@register.filter()
def multi(cost, amount):

    return cost * amount


@register.filter()
def itemsresult(items):
    result = 0
    for i in items:
        result += i.cost * i.amount

    return result
