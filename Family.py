import json

from data_adapters import age


class Family(object):
    def __init__(self, family_identifier):
        self.persons = []
        self.sustentadors_i_custodia = []
        self.menors = []
        self.altres_adults = []
        self.monoparental = False
        self.nombrosa = False
        self.ID = family_identifier

    def add_person(self, person):
        if age(person.data_naixement) < 17:
            self.menors.append(person.ID)
        elif self.sustentadors_i_custodia.__len__() < 2:
            self.sustentadors_i_custodia.append(person.ID)
        else:
            self.altres_adults.append(person.ID)
        if person.familia_monoparental:
            self.monoparental = True
        if person.familia_nombrosa:
            self.nombrosa = True
        self.persons.append(person)

    def __str__(self):
        return str(self.__dict__)

    def to_openfisca_dict(self, period):
        return {
            "families": {
                self.ID: {
                    "sustentadors_i_custodia": [v for v in self.sustentadors_i_custodia],
                    "menors": [v for v in self.menors],
                    "altres_familiars": [v for v in self.altres_adults],
                    "tipus_familia_monoparental": {"2017-1": "general" if self.monoparental else "nop"}
                },
            },
            "unitats_de_convivencia": {
                self.ID + "uc": {
                    "persones_que_conviuen": [v.ID for v in self.persons]
                }
            },
            "families_fins_a_segon_grau": {
                self.ID + "2g": {
                    "familiars": [v.ID for v in self.persons]
                }
            },
            "persones": {v.ID: v.to_openfisca_dict(period) for v in self.persons}
        }

    def to_openfisca_json(self, period):
        return json.dumps(self.to_openfisca_dict(period),
                          sort_keys=True, indent=4)
