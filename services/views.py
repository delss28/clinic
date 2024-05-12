from django.shortcuts import render

# Create your views here.
def services(reguest):
    context = {
        'services': [
        {'name': 'ЛОР'},
        {'name':'Хирургия'},
        {'name':'Гинекология'},
        {'name':'Аллергология-иммунология'},
        {'name':'Стоматология'},
        {'name':'Офтальмология'},
        {'name':'Инфекционист'},
        {'name':'Гастроэнторология'},
        {'name':'УЗИ диагностика'},
        {'name':'Кардиология'},
        {'name':'Эндокринология'},
        {'name':'Физиотерапия'},
        {'name':'Психиатрия'},
        {'name':'Генетик'},
        {'name':'Дерматология'},
        {'name':'Неврология'},
        {'name':'Эндоскопия'},
        {'name':'Травматология-ортопедия'},
        ],
    }
    return render(reguest,'services/services.html',context)

def service(reguest):
    return render(reguest,'services/service.html')
