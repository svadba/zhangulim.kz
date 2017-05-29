from .models import Flavor
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.views.generic import ListView
import telebot
from django.http import HttpResponseRedirect
from datetime import datetime

# IndexView выводит все букет с формой
class IndexView(ListView):
    template_name = 'flavors/flavores_list.html'
    context_object_name = 'flavors'
    model = Flavor
    paginate_by = 9
    form = ContactForm

    def get_queryset(self):
        flavors = Flavor.objects.all()
        return flavors


# Букет по отдельности
def flavor_detail1(request, flavor_id):
    flavor = get_object_or_404(Flavor, pk=flavor_id)
    return render(request, 'flavors/detail_flavor.html', {'flavor': flavor})


# функция flavor_detail отправляет команду в телеграмм бота для вывода сообщения в группе
def flavor_detail(request):
    bot = telebot.TeleBot('341119502:AAEwGwsn0h-koif-WL4HkEjmaUUNE0SGUkM')
    form = ContactForm(request.POST or None)
    chat_id = '-204203716'
    context = {}
    if request.method == "POST":
        # if form.is_valid():
        context['Имя'] = request.POST.get('name', 'name not faund')
        context['Tel'] = request.POST.get('phone', 'phone not faund')
        context['Букет'] = request.POST.get('flavor', 'flavor not faund')
        # context['Адрес'] = request.POST.get('adress', 'name not faund')
        context['Дата заявки'] = datetime.now().strftime('%d/%m/%Y --%H:%M:%S')
        text = str(context).replace(',', '\n')
        text = text.replace('{', '')
        text = text.replace('}', '')
        text = text.replace("'", ' ')
        return HttpResponseRedirect('/thanks/', bot.send_message(chat_id, text))
    return render(request, 'flavors/flavores_list.html', {'form': form, "found": request.GET.get("found", False)})


def thanks(request):
    return render(request, 'flavors/flavor_detail.html')