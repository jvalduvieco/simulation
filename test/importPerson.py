import unittest
from io import StringIO
import csv

from Family import Family
from OpenFisca_simulator import Simulator
from data_import import person_from_row

one_row = u"""CODIGO_HOGAR,ID_PERS,GENERO,FECHA_NACIMIENTO,TFM,TFN,G_DISCAP,ENTRA,RENDA_MES,D_ALTA_MUNI,TREBALLA,D_SOC_DEMANDANT_OCUP
000008076,1,F,14/04/1966,,,36,SIMULADOR,"562,10 ",14/04/2000,SI,
"""
several_rows = u"""CODIGO_HOGAR,ID_PERS,GENERO,FECHA_NACIMIENTO,TFM,TFN,G_DISCAP,ENTRA,RENDA_MES,D_ALTA_MUNI,TREBALLA,D_SOC_DEMANDANT_OCUP
000008076,1,F,14/04/1966,,,36,SIMULADOR,"562,10 ",14/04/2002,SI,
000009073,2,M,09/04/1940,,VIGENT,,SIMULADOR,"704,08 ",14/04/1987,NO,
000009073,3,F,24/02/1996,,,,NO_RENDA_INF,"0,00 ",14/04/2003,NO,
000009073,4,F,24/10/1976,,,,NO_RENDA_INF,"0,00 ",14/04/2002,NO,2018/4
000010093,5,M,27/10/1958,VIGENT,,,NO_RENDA_INF,"0,00 ",14/04/2001,SI,
"""


class ImportAPersonTestCase(unittest.TestCase):
    def setUp(self):
        self.file = StringIO(one_row)

    def test_should_create_a_dict_from_a_row(self):
        reader = csv.DictReader(self.file, delimiter=',')
        person = list(reader)[0]
        self.assertEqual(person['CODIGO_HOGAR'], "000008076")

    def test_should_create_a_openfisca_person_from_a_row(self):
        reader = csv.DictReader(self.file, delimiter=',')
        person = list(reader)[0]
        json_person = person_from_row(person).to_openfisca_json('2017-1')
        self.assertRegexpMatches(json_person, '"ETERNITY": "1966-04-14"')


class RGCFamily(object):
    pass


def simulate_stream(stream):
    current_family = None
    simulator = Simulator()
    reader = csv.DictReader(stream, delimiter=',')
    result = {}
    for row in reader:
        person = person_from_row(row)

        if current_family is None:
            current_family = Family(person.familiy_id)

        if current_family.ID == person.familiy_id:
            current_family.add_person(person)
        else:
            result.update(zip([v.ID for v in current_family.persons], simulator.simulate('GG_270_mensual', '2017-1', current_family)))

            current_family = Family(person.familiy_id)
            current_family.add_person(person)
        result.update(zip([v.ID for v in current_family.persons], simulator.simulate('GG_270_mensual', '2017-1', current_family)))
    return result


class ImportAFamilyTestCase(unittest.TestCase):
    def setUp(self):
        self.file = StringIO(several_rows)

    def test_should_import_a_family(self):
        result = simulate_stream(self.file)
        assert str(result) == "{'1': 0.0, '3': 0.0, '2': 0.0, '5': 0.0, '4': 909.0}"


if __name__ == '__main__':
    unittest.main()
