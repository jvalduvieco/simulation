import json


class Person(object):
    def __init__(self, ID, familiy_id, data_naixement, ingressos_bruts_ultims_sis_mesos, es_orfe_dels_dos_progenitors,
                 es_victima_de_violencia_masclista, es_divorciada_de_familia_reagrupada,
                 porta_dos_anys_o_mes_empadronat_a_catalunya, situacio_laboral, beneficiari_de_prestacio_residencial,
                 ingressat_en_centre_penitenciari, en_els_ultims_12_mesos_ha_fet_baixa_voluntaria_de_la_feina,
                 inscrit_com_a_demandant_docupacio, familia_nombrosa, familia_monoparental, grau_discapacitat,
                 municipi_empadronament):
        self.ID = ID
        self.familiy_id = familiy_id
        self.inscrit_com_a_demandant_docupacio = inscrit_com_a_demandant_docupacio
        self.en_els_ultims_12_mesos_ha_fet_baixa_voluntaria_de_la_feina = en_els_ultims_12_mesos_ha_fet_baixa_voluntaria_de_la_feina
        self.ingressat_en_centre_penitenciari = ingressat_en_centre_penitenciari
        self.beneficiari_de_prestacio_residencial = beneficiari_de_prestacio_residencial
        self.situacio_laboral = situacio_laboral
        self.porta_dos_anys_o_mes_empadronat_a_catalunya = porta_dos_anys_o_mes_empadronat_a_catalunya
        self.es_divorciada_de_familia_reagrupada = es_divorciada_de_familia_reagrupada
        self.es_victima_de_violencia_masclista = es_victima_de_violencia_masclista
        self.es_orfe_dels_dos_progenitors = es_orfe_dels_dos_progenitors
        self.ingressos_bruts_ultims_sis_mesos = ingressos_bruts_ultims_sis_mesos
        self.data_naixement = data_naixement
        self.familia_nombrosa = familia_nombrosa
        self.familia_monoparental = familia_monoparental
        self.grau_discapacitat = grau_discapacitat
        self.municipi_empadronament = municipi_empadronament

    def to_openfisca_dict(self, period):
        eternity_keys = ['data_naixement']
        excluded_keys = ['ID', 'familia_monoparental', 'familia_nombrosa', 'familiy_id']

        return {k: {period if k not in eternity_keys else 'ETERNITY': v} for k, v in self.__dict__.items() if
                k not in excluded_keys}

    def to_openfisca_json(self, period):
        return json.dumps(self.to_openfisca_dict(period),
                          sort_keys=True, indent=4)
