import re
def search_money(your_str):
    return re.finditer(r'((\d+)(\s?)(\$|₽|€))|((\$|₽|€)(\s?)(\d+))', your_str)
