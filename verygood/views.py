from django.shortcuts import render
import sqlite3
from blog import models as bm
# Create your views here.

content_list = [
    'Какой девиз у солдат дивизии имени Майкла Джексона? <br> "Ни шагу вперед!"',
    'Шел мужик по улице, никого не трогал, и вдруг попал под каток. Переехал его каток и выплюнул сзади такую тряпочку цветастую. А в это время бабуся по той улице шла — видит тряпочка. Кинула ее в авоську, пришла домой и в качестве коврика перед дверью постелила. Три года все кто к бабусе приходили вытирали об коврик грязные ноги, в результате чего коврик немного запылился. Бабулька постирала его и повесила на балкончике. Вот тут-то мужик простудился и умер.',
    '- Рабинович, а вы еврей по папе или по маме? <br>- По ситуации.',
    '- как вас зовут?<br>- scp-055<br>- как вас зовут? <br><br>ребята давайте запомним',
    '-Вам привет от трёх лиц.<br>-От кого?<br>-От Бога.'
]






def index(request):
    html = ""
    if request.method == 'POST':
        query = request.POST['query']
        answer = "chuvak, ty dumal chto-to zdes' budet?"
        html = f'<mark>{answer}</mark>'

    context = {
        'response':html,
        'jumoreski':bm.generate_content()
    }
    return render(request, "index_main.html", context)