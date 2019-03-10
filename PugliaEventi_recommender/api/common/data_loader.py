from . import constant
from api.models import Place, Place

class DataLoader:
    data_in_memory = {'places_dict': {}, 'places_list': [], 'place_feature': {}}

    def __init__(self):
        self.__load_data_from_db()

    def __load_data_from_db(self):
        for place in Place.objects.all():
            if "Dummy Place" not in place.name:
                self.data_in_memory['places_dict'][place.placeId] = place
                self.data_in_memory['places_list'].append(place)

                if place.freeEntry:
                    self.data_in_memory['place_feature'][constant.FREE_ENTRY] = place
                if place.teatro:
                    self.data_in_memory['place_feature'][constant.TEATRO] = place
                if place.spiaggia:
                    self.data_in_memory['place_feature'][constant.SPIAGGIA] = place
                if place.museo:
                    self.data_in_memory['place_feature'][constant.MUSEO] = place
                if place.romantico:
                    self.data_in_memory['place_feature'][constant.ROMANTICO] = place
                if place.benessere:
                    self.data_in_memory['place_feature'][constant.BENESSERE] = place
                if place.mangiare:
                    self.data_in_memory['place_feature'][constant.MANGIARE] = place
                if place.bere:
                    self.data_in_memory['place_feature'][constant.BERE] = place
                if place.dormire:
                    self.data_in_memory['place_feature'][constant.DORMIRE] = place
                if place.goloso:
                    self.data_in_memory['place_feature'][constant.GOLOSO] = place
                if place.libri:
                    self.data_in_memory['place_feature'][constant.LIBRI] = place
                if place.informale:
                    self.data_in_memory['place_feature'][constant.INFORMALE] = place
                if place.raffinato:
                    self.data_in_memory['place_feature'][constant.RAFFINATO] = place
                if place.avventura:
                    self.data_in_memory['place_feature'][constant.AVVENTURA] = place
                if place.cinema:
                    self.data_in_memory['place_feature'][constant.CINEMA] = place
                if place.arte:
                    self.data_in_memory['place_feature'][constant.ARTE] = place
                if place.cultura:
                    self.data_in_memory['place_feature'][constant.CULTURA] = place
                if place.folklore:
                    self.data_in_memory['place_feature'][constant.FOLKLORE] = place
                if place.cittadinanza:
                    self.data_in_memory['place_feature'][constant.CITTADINANZA] = place
                if place.vita_notturna:
                    self.data_in_memory['place_feature'][constant.VITA_NOTTURNA] = place
                if place.concerti:
                    self.data_in_memory['place_feature'][constant.CONCERTI] = place
                if place.jazz:
                    self.data_in_memory['place_feature'][constant.JAZZ] = place
                if place.musica_classica:
                    self.data_in_memory['place_feature'][constant.MUSICA_CLASSICA] = place
                if place.geek:
                    self.data_in_memory['place_feature'][constant.GEEK] = place
                if place.bambini:
                    self.data_in_memory['place_feature'][constant.BAMBINI] = place
            #else:
            #    print("Skipping loading of " + str(place.name))
            #print(str(self.data_in_memory))
            #break

    def load_dummy_places():
        p = []
        p.append(Place.create("Dummy Place Free_entry"))
        p[-1].freeEntry = 1
        p.append(Place.create("Dummy Place Teatro"))
        p[-1].teatro = 1
        p.append(Place.create("Dummy Place Spiaggia"))
        p[-1].spiaggia = 1
        p.append( Place.create("Dummy Place Museo"))
        p[-1].museo = 1
        p.append(Place.create("Dummy Place Romantico"))
        p[-1].romantico = 1
        p.append(Place.create("Dummy Place Benessere"))
        p[-1].benessere = 1
        p.append(Place.create("Dummy Place Mangiare"))
        p[-1].mangiare= 1
        p.append(Place.create("Dummy Place Bere"))
        p[-1].bere = 1
        p.append(Place.create("Dummy Place Dormire"))
        p[-1].dormire = 1
        p.append(Place.create("Dummy Place Goloso"))
        p[-1].goloso = 1
        p.append(Place.create("Dummy Place Libri"))
        p[-1].libri = 1
        p.append(Place.create("Dummy Place Informale"))
        p[-1].informale = 1
        p.append(Place.create("Dummy Place Raffinato"))
        p[-1].raffinato = 1
        p.append(Place.create("Dummy Place Avventura"))
        p[-1].avventura = 1
        p.append(Place.create("Dummy Place Cinema"))
        p[-1].cinema = 1
        p.append(Place.create("Dummy Place Arte"))
        p[-1].arte = 1
        p.append(Place.create("Dummy Place Cultura"))
        p[-1].cultura = 1
        p.append(Place.create("Dummy Place Folklore"))
        p[-1].folklore = 1
        p.append(Place.create("Dummy Place Cittadinanza"))
        p[-1].cittadinanza = 1
        p.append(Place.create("Dummy Place Vita_notturna"))
        p[-1].vita_notturna = 1
        p.append(Place.create("Dummy Place Concerti"))
        p[-1].concerti = 1
        p.append(Place.create("Dummy Place Jazz"))
        p[-1].jazz = 1
        p.append(Place.create("Dummy Place Musica_classica"))
        p[-1].musica_classica = 1
        p.append(Place.create("Dummy Place Geek"))
        p[-1].geek = 1
        p.append(Place.create("Dummy Place Bambini"))
        p[-1].bambini = 1

        p.append(Place.create("Dummy Place Empty"))

        for x in p:
            x.save()
