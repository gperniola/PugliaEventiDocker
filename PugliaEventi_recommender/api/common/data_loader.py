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
            #else:
            #    print("Skipping loading of " + str(place.name))
            #print(str(self.data_in_memory))
            #break

    def load_dummy_places():
        p = []
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
        p.append(Place.create("Dummy Place Empty"))

        for x in p:
            x.save()
