import json
import unittest

from numpy.testing import assert_array_equal
from openfisca_barcelona import BarcelonaTaxBenefitSystem
from openfisca_core.simulations import Simulation


class ImportAPersonTestCase(unittest.TestCase):
    def setUp(self):
        self._tax_benefit_system = BarcelonaTaxBenefitSystem()
        self._data = """
        {
            "families":{
                "1":{
                    "sustentadors_i_custodia": ["adult1"],
                    "tipus_familia_monoparental": {"2017-1":"nop"}
                },
                "2":{
                    "sustentadors_i_custodia": ["adult2"],
                    "tipus_familia_monoparental": {"2017-1":"nop"}
                },
                "3":{
                    "sustentadors_i_custodia": ["adult3", "adult4"],
                    "tipus_familia_monoparental": {"2017-1":"nop"}
                }
            },
            "unitats_de_convivencia": {
                "1":{
                    "persones_que_conviuen": ["adult1"]
                },
                "2":{
                    "persones_que_conviuen": ["adult2"]
                },
                "3":{
                    "persones_que_conviuen": ["adult3", "adult4"]
                }       
            },
            "families_fins_a_segon_grau":{
                "1":{
                    "familiars": ["adult1"]
                },
                "2":{
                    "familiars": ["adult2"]
                },
                "3":{
                    "familiars": ["adult3", "adult4"]
                }
            },
            "persones": {
                "adult1": {
                    "data_naixement": {"ETERNITY": "1961-01-15"},
                    "ingressos_bruts_ultims_sis_mesos": {"2017-1": 1500 },
                    "es_orfe_dels_dos_progenitors": {"2017-1": false },
                    "es_victima_de_violencia_masclista": {"2017-1": false },
                    "es_divorciada_de_familia_reagrupada": {"2017-1": false },
                    "porta_dos_anys_o_mes_empadronat_a_catalunya": {"2017-1": true },
                    "situacio_laboral": {"2017-1":"aturat"},
                    "beneficiari_de_prestacio_residencial": {"2017-1": false },
                    "ingressat_en_centre_penitenciari": {"2017-1": false },
                    "en_els_ultims_12_mesos_ha_fet_baixa_voluntaria_de_la_feina": {"2017-1": false },
                    "inscrit_com_a_demandant_docupacio": {"2017-1": true }
                },
                "adult2": {
                    "data_naixement": {"ETERNITY": "1961-01-15"},
                    "ingressos_bruts_ultims_sis_mesos": {"2017-1": 15000 },
                    "es_orfe_dels_dos_progenitors": {"2017-1": false },
                    "es_victima_de_violencia_masclista": {"2017-1": false },
                    "es_divorciada_de_familia_reagrupada": {"2017-1": false },
                    "porta_dos_anys_o_mes_empadronat_a_catalunya": {"2017-1": true },
                    "situacio_laboral": {"2017-1":"aturat"},
                    "beneficiari_de_prestacio_residencial": {"2017-1": false },
                    "ingressat_en_centre_penitenciari": {"2017-1": false },
                    "en_els_ultims_12_mesos_ha_fet_baixa_voluntaria_de_la_feina": {"2017-1": false },
                    "inscrit_com_a_demandant_docupacio": {"2017-1": true }
                },
                "adult3": {
                    "data_naixement": {"ETERNITY": "1961-01-15"},
                    "ingressos_bruts_ultims_sis_mesos": {"2017-1": 1500 },
                    "es_orfe_dels_dos_progenitors": {"2017-1": false },
                    "es_victima_de_violencia_masclista": {"2017-1": false },
                    "es_divorciada_de_familia_reagrupada": {"2017-1": false },
                    "porta_dos_anys_o_mes_empadronat_a_catalunya": {"2017-1": true },
                    "situacio_laboral": {"2017-1":"aturat"},
                    "beneficiari_de_prestacio_residencial": {"2017-1": false },
                    "ingressat_en_centre_penitenciari": {"2017-1": false },
                    "en_els_ultims_12_mesos_ha_fet_baixa_voluntaria_de_la_feina": {"2017-1": false },
                    "inscrit_com_a_demandant_docupacio": {"2017-1": true }
                },
                 "adult4": {
                    "data_naixement": {"ETERNITY": "1961-01-15"},
                    "ingressos_bruts_ultims_sis_mesos": {"2017-1": 1500 },
                    "es_orfe_dels_dos_progenitors": {"2017-1": false },
                    "es_victima_de_violencia_masclista": {"2017-1": false },
                    "es_divorciada_de_familia_reagrupada": {"2017-1": false },
                    "porta_dos_anys_o_mes_empadronat_a_catalunya": {"2017-1": true },
                    "situacio_laboral": {"2017-1":"aturat"},
                    "beneficiari_de_prestacio_residencial": {"2017-1": false },
                    "ingressat_en_centre_penitenciari": {"2017-1": false },
                    "en_els_ultims_12_mesos_ha_fet_baixa_voluntaria_de_la_feina": {"2017-1": false },
                    "inscrit_com_a_demandant_docupacio": {"2017-1": true }
                }
            }
        }
        """

    def test_should_create_a_dict_from_a_row(self):
        simulation = Simulation(tax_benefit_system=self._tax_benefit_system, simulation_json=json.loads(self._data))
        result = simulation.calculate('GG_270_mensual', period='2017-1')
        assert_array_equal(result, [314, -0, 586, 586])
