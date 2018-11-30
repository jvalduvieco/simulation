from datetime import datetime, date

from Person import Person


def to_float(a_number):
    return float(a_number.replace('.', '').replace(',', '.'))


def to_bool(a_bool):
    assert a_bool == "true" or a_bool == "false", "Not a boolean: " + a_bool
    return a_bool == "true"


def vigent_to_true(a_string):
    return a_string == 'VIGENT'


def si_to_true(a_string):
    return a_string == 'SI'


def not_empty_to_true(a_string):
    return a_string != ""


def to_str_american_date(a_date):
    return '{0.year:4d}-{0.month:02d}-{0.day:02d}'.format(a_date)


def to_date(a_str_date):
    return datetime.strptime(a_str_date, '%d/%m/%Y')


def to_int(a_str_int):
    return int(a_str_int) if a_str_int != "" else 0


def age(date_born_american_str):
    date_born = datetime.strptime(date_born_american_str, '%Y-%m-%d')
    today = date.today()
    return today.year - date_born.year - ((today.month, today.day) < (date_born.month, date_born.day))


def person_from_row(a_csv_row):
    data_naixement = to_date(a_csv_row['FECHA_NACIMIENTO'])
    anys_empadronament_barcelona = age(to_str_american_date(to_date(a_csv_row['D_ALTA_MUNI'])))
    renda_mes = to_float(a_csv_row['RENDA_MES'])
    return Person(ID=a_csv_row['ID_PERS'],
                  familiy_id=a_csv_row['CODIGO_HOGAR'],
                  data_naixement=to_str_american_date(data_naixement),
                  ingressos_bruts_ultims_sis_mesos=renda_mes * 6,
                  es_orfe_dels_dos_progenitors=False,
                  es_victima_de_violencia_masclista=False,
                  es_divorciada_de_familia_reagrupada=False,
                  porta_dos_anys_o_mes_empadronat_a_catalunya=anys_empadronament_barcelona >= 2,
                  situacio_laboral='treball_compte_daltri_jornada_complerta' if si_to_true(
                      a_csv_row['TREBALLA']) else 'aturat',
                  beneficiari_de_prestacio_residencial=False,
                  ingressat_en_centre_penitenciari=False,
                  en_els_ultims_12_mesos_ha_fet_baixa_voluntaria_de_la_feina=False,
                  inscrit_com_a_demandant_docupacio=not_empty_to_true(a_csv_row['D_SOC_DEMANDANT_OCUP']),
                  familia_nombrosa=vigent_to_true(a_csv_row['TFN']),
                  familia_monoparental=vigent_to_true(a_csv_row['TFM']),
                  grau_discapacitat=to_int(a_csv_row['G_DISCAP']),
                  municipi_empadronament='barcelona'
                  )
