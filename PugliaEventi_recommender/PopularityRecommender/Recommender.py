from operator import itemgetter
from django.db.models import Q
from datetime import datetime
from django.db.models import Max

import datedelta


from api.common import constant
from api.models import Place, Distanza, Event




N_OF_RECOMMENDATIONS = 5

def find_recommendations():
    date_today = datetime.today().date()
    max_date = date_today + datedelta.datedelta(days=30)
    filtered_events = Event.objects.filter(date_to__gte=date_today, date_from__lte=max_date).order_by('-popularity')
    evs = filtered_events[:5]
    for ev in evs:
        print(str(ev) + "pop: " + str(ev.popularity))
    return evs
