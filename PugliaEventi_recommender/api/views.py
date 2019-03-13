from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from datetime import datetime, timedelta
import datedelta
import random

from .common import lightfm_manager, constant
from RuleBasedRecommender import Recommender
from PopularityRecommender import Recommender as PopRecommender
#from recommender_webapp.models import Comune, Distanza, Place, Mood, Companionship, Event
from .models import Place, Mood, Companionship, Valutazione, Utente, Comune, Event, Distanza, PrevisioniEventi, PrevisioniComuni, WeatherConditions, Sperimentazione, DummyPlace
from .serializers import UtenteSerializer, PlaceSerializer, EventSerializer, ValutazioneSerializer, SperimentazioneSerializer

from .common.data_loader import DataLoader

def addUserDb(username, location):
    utente = Utente.create(username,location)
    utente.save()
    return str(utente.id)

class getDatiSperimentazione(APIView):
    def get(self, request):
        sp = Sperimentazione.objects.all()
        serializer = SperimentazioneSerializer(instance=sp, many=True)
        return JsonResponse(serializer.data,safe=False, status=200)


class getComuni(APIView):
    def get(self, request, letters):
        input = letters;

        comuni = Distanza.objects.filter(cittaA__icontains=input)
        comuni_list = comuni.order_by().values_list('cittaA').distinct()[:15]
        comuni_nomi = []
        for c in comuni_list:
            comuni_nomi.append(c[0])

        return JsonResponse(comuni_nomi,safe=False, status=200)

class getEventi(APIView):
    def get(self, request, letters):
        input = letters;

        eventi = Event.objects.filter(title__icontains=input)
        eventi_list = comuni.order_by().values_list('title').distinct()[:15]
        eventi_nomi = []
        for c in eventi_list:
            eventi_nomi.append(c[0])

        return JsonResponse(eventi_nomi,safe=False, status=200)

class getLuoghi(APIView):
    def get(self, request, letters):
        input = letters;

        luoghi = Place.objects.filter(name__icontains=input)
        luoghi_list = luoghi.order_by().values_list('name').distinct()[:15]
        luoghi_nomi = []
        for c in luoghi_list:
            luoghi_nomi.append(c[0])

        return JsonResponse(luoghi_nomi,safe=False, status=200)


# Create your views here.
class getUserConfig(APIView):
    def post(self, request, *args, **kwargs):
        username = str(request.data.get('username'))
        users = Utente.objects.filter(username=username)
        active_user = users[0]
        return JsonResponse({"first_config_done": active_user.first_configuration },safe=False, status=200)


def checkNumValutazioni(valutazioni):
    n_angry_withFriends = 0
    n_angry_alone = 0
    n_joyful_withFriends = 0
    n_joyful_alone = 0
    n_sad_withFriends = 0
    n_sad_alone = 0

    for v in valutazioni:
        if v.mood == "angry":
            if v.companionship == "alone":
                n_angry_alone = n_angry_alone + 1
            else:
                n_angry_withFriends = n_angry_withFriends + 1
        elif v.mood == "joyful":
            if v.companionship == "alone":
                n_joyful_alone = n_joyful_alone + 1
            else:
                n_joyful_withFriends = n_joyful_withFriends + 1
        else:
            if v.companionship == "alone":
                n_sad_alone = n_sad_alone + 1
            else:
                n_sad_withFriends = n_sad_withFriends + 1

    return (n_angry_withFriends, n_angry_alone, n_joyful_withFriends, n_joyful_alone, n_sad_withFriends, n_sad_alone)


class getRatings (APIView):
    def post(self, request, *args, **kwargs):
        username = str(request.data.get('username'))

        users = Utente.objects.filter(username=username)
        active_user = users[0]
        user_id = active_user.id
        first_config_done = active_user.first_configuration

        valutazioni = Valutazione.objects.filter(user=active_user)
        (n_angry_withFriends, n_angry_alone, n_joyful_withFriends, n_joyful_alone, n_sad_withFriends, n_sad_alone) = checkNumValutazioni(valutazioni)

        serializer = ValutazioneSerializer(instance=valutazioni, many=True)
        output = {"first_config_done":first_config_done, "n_angry_withFriends":n_angry_withFriends,
        "n_angry_alone":n_angry_alone, "n_joyful_withFriends":n_joyful_withFriends, "n_joyful_alone":n_joyful_alone,
        "n_sad_withFriends":n_sad_withFriends, "n_sad_alone":n_sad_alone, "valutazioni":serializer.data}
        return JsonResponse(output,safe=False, status=200)




class addRating (APIView):
    def post(self, request, *args, **kwargs):
        username = str(request.data.get('username'))
        place_id = int(request.data.get('place-id'))
        mood = str(request.data.get('emotion'))
        companionship = str(request.data.get('companionship'))

        users = Utente.objects.filter(username=username)

        user_id = users[0].id
        user_context_id = str(user_id + 100) + str(Mood[mood].value) + str(Companionship[companionship].value)

        place = Place.objects.filter(placeId=place_id)
        valutazione = Valutazione.create(users[0],mood,companionship,place[0])
        valutazione.save()

        #aggiungi al modello solo se il modello per l'utente esiste già (ovvero se ha completato la prima configurazione in precedenza)
        #altrimenti analizza le valutazioni in db per verificare se l'utente ha terminato la configurazione
        #nel caso abbia valutazioni a sufficienza per completare la configurazione, allora crea li modello utente
        if  users[0].first_configuration:
            print("+++ adding rating to user model")
            lightfm_manager.add_rating(user_context_id, place_id, 3)
        else:
            valutazioni_utente = Valutazione.objects.filter(user=users[0])
            (n_angry_withFriends, n_angry_alone, n_joyful_withFriends, n_joyful_alone, n_sad_withFriends, n_sad_alone) = checkNumValutazioni(valutazioni_utente)

            if n_angry_withFriends >= constant.RATINGS_PER_CONTEXT_CONF and n_angry_alone >= constant.RATINGS_PER_CONTEXT_CONF and n_joyful_withFriends >= constant.RATINGS_PER_CONTEXT_CONF and \
                n_joyful_alone >= constant.RATINGS_PER_CONTEXT_CONF and n_sad_withFriends >= constant.RATINGS_PER_CONTEXT_CONF and  n_sad_alone >= constant.RATINGS_PER_CONTEXT_CONF:

                users[0].first_configuration = True
                user_zero = Utente.objects.get(username=username)
                user_zero.first_configuration = True
                user_zero.save()

                user_contexts = []
                user_contexts.append({'mood': Mood.joyful, 'companionship': Companionship.withFriends})
                user_contexts.append({'mood': Mood.joyful, 'companionship': Companionship.alone})
                user_contexts.append({'mood': Mood.angry, 'companionship': Companionship.withFriends})
                user_contexts.append({'mood': Mood.angry, 'companionship': Companionship.alone})
                user_contexts.append({'mood': Mood.sad, 'companionship': Companionship.withFriends})
                user_contexts.append({'mood': Mood.sad, 'companionship': Companionship.alone})

                print("+++ creating new user model")
                lightfm_manager.add_user(users[0].id, users[0].location, user_contexts, valutazioni_utente)


        return Response(status=201)

class getAllPlaces(APIView):
    def post(self, request, *args, **kwargs):
        username = str(request.data.get('username'))
        location = str(request.data.get('location'))
        place_name = str(request.data.get('luogo'))
        range = int(request.data.get('range'))
        only_with_events = int(request.data.get('only-with-events'))
        only_rated_places = int(request.data.get('only-rated-places'))

        users = Utente.objects.filter(username=username)
        user_id = users[0].id
        if location == '':
            location = users[0].location

        if place_name != "":
            filtered_places = Place.objects.filter(name__icontains=place_name)[:100]
        else:
            if only_rated_places == 1:
                eval_queryset = Valutazione.objects.filter(user=user_id)
                user_eval_places = []
                for e in eval_queryset:
                    user_eval_places.append(e.place.placeId)
                filtered_places = Place.objects.filter(placeId__in=user_eval_places)

            else:
                locations_in_range = []
                if location != '':
                    locations_in_range.append(location)
                    if range > 0:
                        locations_queryset = Distanza.objects.filter(cittaA=location,distanza__lte=range).order_by('distanza')
                        for loc in locations_queryset:
                            locations_in_range.append(loc.cittaB)
                    filtered_places = Place.objects.filter(location__in=locations_in_range).order_by('location', 'name')

                if only_with_events == 1:
                    date_today = datetime.today().date()
                    places_with_events = []
                    for p in filtered_places:
                        if(Event.objects.filter(place=p.name, date_to__gte=date_today).exists()):
                            places_with_events.append(p.placeId)
                    filtered_places = filtered_places.filter(placeId__in=places_with_events)

        serializer = PlaceSerializer(instance=filtered_places, many=True, context={'user_location':location, 'user_id':user_id})
        return JsonResponse(serializer.data,safe=False, status=200)




class getAllEvents(APIView):
    def post(self, request, *args, **kwargs):
        location = str(request.data.get('location'))
        range = int(request.data.get('range'))
        days = str(request.data.get('days'))
        weather_conditions = int(request.data.get('weather'))
        no_weather_data = int(request.data.get('no-weather-data'))
        start_date_raw = (request.data.get('start-date'))
        end_date_raw = (request.data.get('end-date'))

        start_date = datetime.strptime(start_date_raw, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_raw, '%Y-%m-%d').date()

        #offset = int(request.data.get('offset'))
        #date filter
        date_today = datetime.today().date()
        '''
        max_date = ''
         if days == '1d':
            max_start_date = date_today
        elif days == '7d':
            max_start_date = date_today + datedelta.datedelta(days=7)
        elif days == '1m':
            max_start_date = date_today + datedelta.datedelta(days=30)
        else:
            max_start_date = date_today + datedelta.datedelta(months=6)

        filtered_events = Event.objects.filter(date_to__gte=date_today, date_from__lte=max_start_date).order_by('date_to')
        '''
        filtered_events = Event.objects.filter(date_to__gte=start_date, date_from__lte=end_date).order_by('date_to')
        #location and range filter
        locations_in_range = []
        if location != '':
            locations_in_range.append(location)
            if range > 0:
                locations_queryset = Distanza.objects.filter(cittaA=location,distanza__lte=range).order_by('distanza')
                for loc in locations_queryset:
                    locations_in_range.append(loc.cittaB)

            filtered_events = filtered_events.filter(comune__in=locations_in_range)

        weather_filtered_events = []
        if weather_conditions > 0:
            max_weather = -1
            if weather_conditions == 1: max_weather = 4 #max pioggia
            if weather_conditions == 2: max_weather = 3 #max coperto
            if weather_conditions == 3: max_weather = 2 #max poco nuvoloso
            if weather_conditions == 4: max_weather = 1 #max sereno

            for ev in filtered_events:
                #prev = ev.previsioni_evento.all()
                previsioni_unfiltered = ev.previsioni_evento.all()
                prev = []
                for p in previsioni_unfiltered:
                    if p.idprevisione.data.date() >= start_date and p.idprevisione.data.date() <= end_date:
                        prev.append(p.idprevisione) #added
                if not prev and no_weather_data == 1: weather_filtered_events.append(ev) #aggiungi eventi senza previsioni meteo
                else:
                    for p in prev:
                        if p.get_condizioni().value <= max_weather: #rmved
                            weather_filtered_events.append(ev)
                            break
        else:
            weather_filtered_events = filtered_events



        serializer = EventSerializer(instance=weather_filtered_events, many=True, context={'user_location':location})
        return JsonResponse(serializer.data,safe=False, status=201)


class UserLogin(APIView):
    def post(self,request,*args,**kwargs):
        username = str(request.data.get('username'))
        schema = str(request.data.get('schema-sperimentazione'))

        utenti = Utente.objects.filter(username=username)

        if not utenti:
            #Uso Bari come valore predefinito dato che l'utente non si è registrato su feelathome
            utente = Utente.create(username,"Bari")
            utente.save()
        else:
            utente = utenti[0]

        sps = Sperimentazione.objects.filter(user_id=utente)
        if not sps:
            #creo 3 copie
            sp = Sperimentazione.create(utente,schema, datetime.now())
            sp.save()
            sp.id = None
            sp.save()
            sp.id = None
            sp.save()
        else:
            sps.update(schema=schema)

        all_sps_complete = Sperimentazione.objects.filter(user_id=utente, test_completato=False)
        if not all_sps_complete:
            test_completato = True
        else:
            test_completato = False

        #DataLoader.load_dummy_places()
        return Response(data={"user_location":str(utente.location), "sperimentazione_completata":str(test_completato)}, status=200)


class UserSignup(APIView):
    def post(self,request,*args,**kwargs):
        username = str(request.data.get('username'))
        location = str(request.data.get('location'))
        schema = str(request.data.get('schema-sperimentazione'))

        utente = Utente.create(username,location)
        utente.save()

        #creo 3 copie
        sp = Sperimentazione.create(utente,schema, datetime.now())
        sp.save()
        sp.id = None
        sp.save()
        sp.id = None
        sp.save()

        return Response(data={"user_id":utente.id})


class CreateMyrrorUserModel(APIView):
    def post(self,request,*args,**kwargs):
        username = str(request.data.get('username'))
        data = request.data["interessi"]

        users = Utente.objects.filter(username=username)
        user_id = users[0].id
        user_config_done = users[0].first_configuration

        if not user_config_done:
            for d in data:
                #print("INT: " +str(d["nome"]))
                tags = d["tags"]
                for t in tags:
                    #print(t)
                    if str(t["tag"]) != "Nessuno":
                        p_name = "Dummy Place " + str(t["tag"])
                        p = Place.objects.get(name=p_name)
                        dummyplace_id = p.placeId
                        mood = str(t["mood"])
                        companionship = str(t["companionship"])
                        #print(str(p) + " (" + mood + " " + companionship +")")

                        user_context_id = str(user_id + 100) + str(Mood[mood].value) + str(Companionship[companionship].value)

                        valutazione = Valutazione.create(users[0],mood,companionship,p)
                        valutazione.save()

            users[0].first_configuration = True
            user_zero = Utente.objects.get(username=username)
            user_zero.first_configuration = True
            user_zero.save()

            valutazioni_utente = Valutazione.objects.filter(user=users[0])

            user_contexts = []
            user_contexts.append({'mood': Mood.angry, 'companionship': Companionship.withFriends})
            user_contexts.append({'mood': Mood.angry, 'companionship': Companionship.alone})
            user_contexts.append({'mood': Mood.joyful, 'companionship': Companionship.withFriends})
            user_contexts.append({'mood': Mood.joyful, 'companionship': Companionship.alone})
            user_contexts.append({'mood': Mood.sad, 'companionship': Companionship.withFriends})
            user_contexts.append({'mood': Mood.sad, 'companionship': Companionship.alone})

            print("+++ creating new user model")
            lightfm_manager.add_user(users[0].id, users[0].location, user_contexts, valutazioni_utente)

        return Response(status=200)



class FindPlaceRecommendations(APIView):
    def post(self,request,*args,**kwargs):
        username = str(request.data.get('username'))
        location = str(request.data.get('location'))
        range = str(request.data.get('range'))
        mood = str(request.data.get('emotion'))
        companionship = str(request.data.get('companionship'))

        users = Utente.objects.filter(username=username)
        user_id = users[0].id

        if location == '':
            location = users[0].location
            range = 250

        user_context_id = str(user_id + 100) + str(Mood[mood].value) + str(Companionship[companionship].value)
        recs = lightfm_manager.find_recommendations(user_context_id,location,range,1)
        serializer = PlaceSerializer(instance=recs, many=True)
        #json = JSONRenderer().render(serializer.data)
        #print(json)
        #if serializer.is_valid():
            #serializer.save()
        return JsonResponse(serializer.data,safe=False, status=201)
        #return JsonResponse(serializer.errors, safe=False, status=400)

        #return JsonResponse({'foo':'bar'})
        #return Response(data={"recs":recs})
        #return Response(data={"foo":str(recs)})


class RuleBasedRecommender(APIView):
    parser_classes = (JSONParser,)
    def post(self,request,*args,**kwargs):
        data = request.data["data"]
        location_filter = data["location"]
        range = data["range"]
        weather = data["weather"]
        no_weather_data = data["no-weather-data"]

        recommended_events = Recommender.find_recommendations(data, location_filter, range, weather, no_weather_data)

        serializer = EventSerializer(instance=recommended_events, many=True, context={'user_location':location_filter})
        return JsonResponse(serializer.data,safe=False, status=201)


class FindEventRecommendations(APIView):
    def post(self,request,*args,**kwargs):
        username = str(request.data.get('username'))

        location_filter = str(request.data.get('location'))
        range = str(request.data.get('range'))
        mood = str(request.data.get('emotion'))
        companionship = str(request.data.get('companionship'))
        weather_conditions = int(request.data.get('weather'))
        no_weather_data = int(request.data.get('no-weather-data'))

        users = Utente.objects.filter(username=username)
        user_id = users[0].id


        if location_filter == '':
            location = users[0].location
            range = 250
        else:
            location = location_filter

        user_context_id = str(user_id + 100) + str(Mood[mood].value) + str(Companionship[companionship].value)
        #recs = lightfm_manager.find_recommendations(user_context_id,location,60,1)
        recommended_events = lightfm_manager.find_events_recommendations(user_context_id,location,range, weather_conditions, no_weather_data)
        #for r in recommended_events:
        #    prev = r.previsionieventi_set.all()
        #    for p in prev:
        #        print(str(p.idprevisione))


        serializer = EventSerializer(instance=recommended_events, many=True, context={'user_location':location_filter})
        return JsonResponse(serializer.data,safe=False, status=201)

class FindEventRecommendationsAllRecommenders(APIView):
    def post(self,request,*args,**kwargs):
        username = str(request.data.get('username'))

        location_filter = str(request.data.get('location'))
        range = str(request.data.get('range'))
        mood = str(request.data.get('emotion'))
        companionship = str(request.data.get('companionship'))
        weather_conditions = int(request.data.get('weather'))
        no_weather_data = int(request.data.get('noweatherdata'))

        data = request.data

        users = Utente.objects.filter(username=username)
        user_id = users[0].id


        if location_filter == '':
            location = users[0].location
            range = 300
        else:
            location = location_filter

        user_context_id = str(user_id + 100) + str(Mood[mood].value) + str(Companionship[companionship].value)

        recsRules = Recommender.find_recommendations(data, location_filter, range, weather_conditions, no_weather_data)
        recsLightFM = lightfm_manager.find_events_recommendations(user_context_id,location,range, weather_conditions, no_weather_data)
        recsPopular = PopRecommender.find_recommendations()

        serializerRules = EventSerializer(instance=recsRules, many=True, context={'user_location':location_filter})
        serializerLightFM = EventSerializer(instance=recsLightFM, many=True, context={'user_location':location_filter})
        serializerPopular = EventSerializer(instance=recsPopular, many=True, context={'user_location':location_filter})

        lists="RLP" #Rulebased, Lightfm, Popularity
        shuffled_lists = ''.join(random.sample(lists,len(lists)))

        i = 1
        resp = {}
        for c in shuffled_lists:
            if c == 'R':
                resp["Lista"+str(i)] = serializerRules.data
            elif c == 'L':
                resp["Lista"+str(i)] = serializerLightFM.data
            else:
                resp["Lista"+str(i)] = serializerPopular.data
            i = i + 1

        #print(shuffled_lists)
        sps = Sperimentazione.objects.filter(user=users[0], test_completato=False)

        if not sps:
            return JsonResponse({},safe=False, status=201)

        sp = sps[0]
        resp["testcode"] = sp.id
        sp.ordine_lista_a = shuffled_lists[:1]
        sp.ordine_lista_b = shuffled_lists[1:2]
        sp.ordine_lista_c = shuffled_lists[2:3]
        sp.save()

        return JsonResponse(resp,safe=False, status=201)



class AddUserModel(APIView):
    def post(self,request,*args,**kwargs):
        mood_configuration = {}
        companionship_configuration = {}
        rated_places = []
        user_contexts = []
        username = str(request.data.get('username'))
        utente = Utente.objects.filter(username=username)
        place = "boh"

        '''place = Place.objects.filter(placeId=78)
        valutazione = Valutazione.create(utente[0],"joyful","alone",place[0])
        valutazione.save()'''

        '''place = Place.objects.filter(placeId=80)
        valutazione = Valutazione.create(utente[0],"joyful","alone",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=81)
        valutazione = Valutazione.create(utente[0],"joyful","alone",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=82)
        valutazione = Valutazione.create(utente[0],"joyful","alone",place[0])
        valutazione.save()

        place = Place.objects.filter(placeId=83)
        valutazione = Valutazione.create(utente[0],"joyful","withFriends",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=84)
        valutazione = Valutazione.create(utente[0],"joyful","withFriends",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=85)
        valutazione = Valutazione.create(utente[0],"joyful","withFriends",place[0])
        valutazione.save()

        place = Place.objects.filter(placeId=86)
        valutazione = Valutazione.create(utente[0],"angry","alone",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=87)
        valutazione = Valutazione.create(utente[0],"angry","alone",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=88)
        valutazione = Valutazione.create(utente[0],"angry","alone",place[0])
        valutazione.save()

        place = Place.objects.filter(placeId=89)
        valutazione = Valutazione.create(utente[0],"angry","withFriends",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=90)
        valutazione = Valutazione.create(utente[0],"angry","withFriends",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=91)
        valutazione = Valutazione.create(utente[0],"angry","withFriends",place[0])
        valutazione.save()

        place = Place.objects.filter(placeId=92)
        valutazione = Valutazione.create(utente[0],"sad","alone",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=93)
        valutazione = Valutazione.create(utente[0],"sad","alone",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=94)
        valutazione = Valutazione.create(utente[0],"sad","alone",place[0])
        valutazione.save()

        place = Place.objects.filter(placeId=95)
        valutazione = Valutazione.create(utente[0],"sad","withFriends",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=96)
        valutazione = Valutazione.create(utente[0],"sad","withFriends",place[0])
        valutazione.save()
        place = Place.objects.filter(placeId=97)
        valutazione = Valutazione.create(utente[0],"sad","withFriends",place[0])
        valutazione.save()'''


        user_ratings = Valutazione.objects.filter(user=utente[0].id)
        user_contexts.append({'mood': Mood.joyful, 'companionship': Companionship.withFriends})
        user_contexts.append({'mood': Mood.joyful, 'companionship': Companionship.alone})
        user_contexts.append({'mood': Mood.angry, 'companionship': Companionship.withFriends})
        user_contexts.append({'mood': Mood.angry, 'companionship': Companionship.alone})
        user_contexts.append({'mood': Mood.sad, 'companionship': Companionship.withFriends})
        user_contexts.append({'mood': Mood.sad, 'companionship': Companionship.alone})

        lightfm_manager.add_user(utente[0].id,utente[0].location, user_contexts, user_ratings)

        return Response(data={"id":str(utente[0].id), "place":str(place)})


class SendSperimentazione(APIView):
    def post(self,request,*args,**kwargs):
        username = str(request.data.get('username'))

        user = Utente.objects.get(username=username)
        sp = Sperimentazione.objects.get(user=user)


        lista_interesse = str(request.data.get('listaInteressante'))
        lista_personalita = str(request.data.get('listaPersonalita'))


        if lista_interesse == "A":
            sp.lista_preferita_interesse = sp.ordine_lista_a
        elif lista_interesse == "B":
            sp.lista_preferita_interesse = sp.ordine_lista_b
        else:
            sp.lista_preferita_interesse = sp.ordine_lista_c


        if lista_personalita == "A":
            sp.lista_preferita_personalita = sp.ordine_lista_a
        elif lista_personalita == "B":
            sp.lista_preferita_personalita = sp.ordine_lista_b
        else:
            sp.lista_preferita_personalita = sp.ordine_lista_c


        sp.note= str(request.data.get('comment'))

        ordine_A = sp.ordine_lista_a
        ordine_B = sp.ordine_lista_b
        ordine_C = sp.ordine_lista_c

        if ordine_A == "L":
            sp.l1 = bool(request.data.get('A1'))
            sp.l2 = bool(request.data.get('A2'))
            sp.l3 = bool(request.data.get('A3'))
            sp.l4 = bool(request.data.get('A4'))
            sp.l5 = bool(request.data.get('A5'))
        elif ordine_A == "R":
            sp.r1 = bool(request.data.get('A1'))
            sp.r2 = bool(request.data.get('A2'))
            sp.r3 = bool(request.data.get('A3'))
            sp.r4 = bool(request.data.get('A4'))
            sp.r5 = bool(request.data.get('A5'))
        else:
            sp.p1 = bool(request.data.get('A1'))
            sp.p2 = bool(request.data.get('A2'))
            sp.p3 = bool(request.data.get('A3'))
            sp.p4 = bool(request.data.get('A4'))
            sp.p5 = bool(request.data.get('A5'))

        if ordine_B == "L":
            sp.l1 = bool(request.data.get('B1'))
            sp.l2 = bool(request.data.get('B2'))
            sp.l3 = bool(request.data.get('B3'))
            sp.l4 = bool(request.data.get('B4'))
            sp.l5 = bool(request.data.get('B5'))
        elif ordine_B == "R":
            sp.r1 = bool(request.data.get('B1'))
            sp.r2 = bool(request.data.get('B2'))
            sp.r3 = bool(request.data.get('B3'))
            sp.r4 = bool(request.data.get('B4'))
            sp.r5 = bool(request.data.get('B5'))
        else:
            sp.p1 = bool(request.data.get('B1'))
            sp.p2 = bool(request.data.get('B2'))
            sp.p3 = bool(request.data.get('B3'))
            sp.p4 = bool(request.data.get('B4'))
            sp.p5 = bool(request.data.get('B5'))

        if ordine_C == "L":
            sp.l1 = bool(request.data.get('C1'))
            sp.l2 = bool(request.data.get('C2'))
            sp.l3 = bool(request.data.get('C3'))
            sp.l4 = bool(request.data.get('C4'))
            sp.l5 = bool(request.data.get('C5'))
        elif ordine_C == "R":
            sp.r1 = bool(request.data.get('C1'))
            sp.r2 = bool(request.data.get('C2'))
            sp.r3 = bool(request.data.get('C3'))
            sp.r4 = bool(request.data.get('C4'))
            sp.r5 = bool(request.data.get('C5'))
        else:
            sp.p1 = bool(request.data.get('C1'))
            sp.p2 = bool(request.data.get('C2'))
            sp.p3 = bool(request.data.get('C3'))
            sp.p4 = bool(request.data.get('C4'))
            sp.p5 = bool(request.data.get('C5'))


        sp.data_fine = datetime.now()
        sp.test_completato = True

        sp.save()
        return Response(status=200)





    '''queryset = Utente.objects.all()
    serializer_class = UtenteSerializer

    def perform_create(self, serializer):
        serializer.save()'''

'''class AddUser(APIView):
    def post(self,request,*args,**kwargs):
        mood_configuration = {}
        companionship_configuration = {}
        rated_places = []
        user_contexts = []

        email = str(request.data.get('email'))
        password = str(request.data.get('password'))
        location = str(request.data.get('location'))

        User.email = email
        User.set_password(password)
        User.save()

        location_found = Comune.objects.filter(nome__iexact=location)
        User.profile.location = location_found.first().nome
        User.save()

        user_ratings = Rating.objects.filter(user=int(request.data.get('userId')))
        user_contexts.append({'mood': Mood.joyful, 'companionship': Companionship.withFriends})
        user_contexts.append({'mood': Mood.joyful, 'companionship': Companionship.alone})
        user_contexts.append({'mood': Mood.angry, 'companionship': Companionship.withFriends})
        user_contexts.append({'mood': Mood.angry, 'companionship': Companionship.alone})
        user_contexts.append({'mood': Mood.sad, 'companionship': Companionship.withFriends})
        user_contexts.append({'mood': Mood.sad, 'companionship': Companionship.alone})

        lightfm_manager.add_user(int(request.data.get('userId')),str(request.data.get('location')), user_contexts, user_ratings)
        return Response(data={"result":"user " +  str(request.data.get('userId')) + " added"})'''
