#-*- coding: utf-8 -*-
"""
# version 0.2a
# author: andrew.bezzubov - 02/02/2020 year
===============================================================

# The indicators of process
+--------------------------------------+-----------------------------------+
|              Переменная              |             Показатель            |
+--------------------------------------+-----------------------------------+
|         data_ur_vip_zak_year         | Уровень выполнения заказов по ... |
|         data_ur_pov_zak_year         | Уровень повторных закупок по г... |
|      data_ur_priv_new_cons_year      | Уровень привлечения новых потр... |
|          data_ur_udovl_year          | Уровень удовлетворенности по г... |
|     data_ur_vip_zak_middle_year      | Уровень выполнения заказов по ... |
|     data_ur_pov_zak_middle_year      | Уровень повторных закупок по п... |
|  data_ur_priv_new_cons_middle_year   | Уровень привлечения новых потр... |
|     data_koef_nov_pri_razr_year      |           Кн по годам...          |
|    data_koef_vned_konst_dok_year     | Квн конструкторской документац... |
|      data_pok_kach_razr_kd_year      |          Ккд по годам...          |
|      data_pok_kach_razr_td_year      |          Ктд по годам...          |
|  data_koef_nov_pri_razr_middle_year  |        Кн по полугодиям...        |
| data_koef_vned_konst_dok_middle_year | Квн конструкторской документац... |
|  data_pok_kach_razr_kd_middle_year   |        Ккд по полугодиям...       |
|  data_pok_kach_razr_td_middle_year   |        Ктд по полугодиям...       |
|        data_vip_graf_zak_year        |           Кз по годам...          |
|         data_km_mastic_year          |       Км_Мастика по годам...      |
|           data_km_pvh_year           |         Км_ПВХ по годам...        |
|         data_kp_mastic_year          |       Кп_Мастика по годам...      |
|           data_kp_pvh_year           |         Кп_ПВХ по годам...        |
|    data_vip_graf_zak_middle_year     |        Кз по полугодиям...        |
|      data_km_mastic_middle_year      |    Км_Мастика по полугодиям...    |
|       data_km_pvh_middle_year        |      Км_ПВХ по полугодиям...      |
|      data_kp_mastic_middle_year      |    Кп_Мастика по полугодиям...    |
|       data_kp_pvh_middle_year        |      Кп_ПВХ по полугодиям...      |
|        data_kol_vip_prod_year        | Количество выпущенной продукци... |
|     data_ur_pr_obr_kach_mat_year     |        Кпр кач по годам...        |
|     data_ur_pr_obr_nep_mat_year      |        Кпр кол по годам...        |
|       data_ur_neispr_obor_year       | Уровень неисправности оборудов... |
|       data_ur_nesoot_prod_year       | Уровень несоответствующей прод... |
|         data_ur_teh_oth_year         |   Уровень техотходов по годам...  |
|    data_kol_vip_prod_middle_year     | Количество выпущеной продукции... |
| data_ur_pr_obr_kach_mat_middle_year  |      Кпр кач по полугодиям...     |
|  data_ur_pr_obr_nep_mat_middle_year  |      Кпр кол по полугодиям...     |
|   data_ur_neispr_obor_middle_year    | Уровень неисправности оборудов... |
|   data_ur_nesoot_prod_middle_year    | Уровень несоответствующей прод... |
|     data_ur_teh_oth_middle_year      | Уровень техотходов по полугоди... |
|       data_kol_real_prod_year        | Количество реализованной проду... |
|        data_pret_i_rekl_year         | Претензии и рекламации от потр... |
|         data_ur_postav_year          |    Уровень поставок по годам...   |
|    data_kol_real_prod_middle_year    | Количество реализованной проду... |
|     data_pret_i_rekl_middle_year     | Претензии и рекламации от потр... |
|      data_ur_postav_middle_year      | Уровень поставок по полугодиям... |
|       data_ur_prop_rab_dn_year       | Уровень пропуска рабочих дней ... |
|         data_ur_tek_kad_year         | Уровень текучести кадров по го... |
|        data_ur_ukomp_kad_year        | Уровень укомплектованности кад... |
|   data_ur_prop_rab_dnmiddle__year    | Уровень пропуска рабочих дней ... |
|     data_ur_tek_kad_middle_year      | Уровень текучести кадров за по... |
|    data_ur_ukomp_kad_middle_year     | Уровень укомплектованности кад... |
|       data_km_antiadgeziv_year       |     Км_Антиадгезив по годам...    |
|       data_kp_antiadgeziv_year       |     Кп_Антиадгезив по годам...    |
|        data_km_bitkor_r_year         |      Км_Биткор_Р по годам...      |
|        data_kp_bitkor_r_year         |      Кп_Биткор_Р по годам...      |
|        data_km_bitkor_u_year         |     Км_Биткор_Р(У) по годам...    |
|        data_kp_bitkor_u_year         |     Кп_Биткор_Р(У) по годам...    |
|         data_km_korobki_year         |       Км_Коробки по годам...      |
|         data_kp_korobki_year         |       Кп_Коробки по годам...      |
|          data_km_mbpr_year           |        Км_МБПР по годам...        |
|          data_kp_mbpr_year           |        Кп_МБПР по годам...        |
|          data_km_mufty_year          |        Км_Муфты по годам...       |
|          data_kp_mufty_year          |        Кп_Муфты по годам...       |
|       data_km_bsk_pvh_lip_year       | Км_ОАО_БСК_липкая_ПВХ по годам... |
|       data_kp_bsk_pvh_lip_year       | Кп_ОАО_БСК_липкая_ПВХ по годам... |
|       data_km_selaron_pvh_year       |   Км_ООО_Сэларон_ПВХ по годам...  |
|       data_kp_selaron_pvh_year       |   Кп_ООО_Сэларон_ПВХ по годам...  |
|         data_km_bsk_pvh_year         |     Км_ПВХ_ОАО_БСК по годам...    |
|         data_kp_bsk_pvh_year         |     Кп_ПВХ_ОАО_БСК по годам...    |
|          data_km_pekom_year          |        Км_ПЭКОМ по годам...       |
|          data_kp_pekom_year          |        Кп_ПЭКОМ по годам...       |
|         data_km_pakety_year          | Км_Пакеты полиэтиленовые по го... |
|         data_kp_pakety_year          | Кп_Пакеты полиэтиленовые по го... |
|         data_km_polilen_year         |       Км_Полилен по годам...      |
|         data_kp_polilen_year         |       Кп_Полилен по годам...      |
|        data_km_politerm_year         |      Км_Политерм по годам...      |
|        data_kp_politerm_year         |      Кп_Политерм по годам...      |
|   data_km_sibtrubizol_pvh_lip_year   | Км_Сибтрубизол_липкая_ПВХ по г... |
|   data_kp_sibtrubizol_pvh_lip_year   | Кп_Сибтрубизол_липкая_ПВХ по г... |
|        data_km_transkor_year         |      Км_Транскор по годам...      |
|        data_kp_transkor_year         |      Кп_Транскор по годам...      |
|         data_km_shpuly_year          |        Км_Шпули по годам...       |
|         data_kp_shpuly_year          |        Кп_Шпули по годам...       |
|   data_km_antiadgeziv_middle_year    |  Км_Антиадгезив по полугодиям...  |
|   data_kp_antiadgeziv_middle_year    |  Кп_Антиадгезив по полугодиям...  |
|     data_km_bitkor_r_middle_year     |    Км_Биткор_Р по полугодиям...   |
|     data_kp_bitkor_r_middle_year     |    Кп_Биткор_Р по полугодиям...   |
|     data_km_bitkor_u_middle_year     |  Км_Биткор_Р(У) по полугодиям...  |
|     data_kp_bitkor_u_middle_year     |  Кп_Биткор_Р(У) по полугодиям...  |
|     data_km_korobki_middle_year      |    Км_Коробки по полугодиям...    |
|     data_kp_korobki_middle_year      |    Кп_Коробки по полугодиям...    |
|       data_km_mbpr_middle_year       |      Км_МБПР по полугодиям...     |
|       data_kp_mbpr_middle_year       |      Кп_МБПР по полугодиям...     |
|      data_km_mufty_middle_year       |     Км_Муфты по полугодиям...     |
|      data_kp_mufty_middle_year       |     Кп_Муфты по полугодиям...     |
|   data_km_bsk_pvh_lip_middle_year    | Км_ОАО_БСК_липкая_ПВХ по полуг... |
|   data_kp_bsk_pvh_lip_middle_year    | Кп_ОАО_БСК_липкая_ПВХ по полуг... |
|   data_km_selaron_pvh_middle_year    | Км_ООО_Сэларон_ПВХ по полугоди... |
|   data_kp_selaron_pvh_middle_year    | Кп_ООО_Сэларон_ПВХ по полугоди... |
|     data_km_bsk_pvh_middle_year      |  Км_ПВХ_ОАО_БСК по полугодиям...  |
|     data_kp_bsk_pvh_middle_year      |  Кп_ПВХ_ОАО_БСК по полугодиям...  |
|      data_km_pekom_middle_year       |     Км_ПЭКОМ по полугодиям...     |
|      data_kp_pekom_middle_year       |     Кп_ПЭКОМ по полугодиям...     |
|      data_km_pakety_middle_year      | Км_Пакеты полиэтиленовые по по... |
|      data_kp_pakety_middle_year      | Кп_Пакеты полиэтиленовые по по... |
|     data_km_polilen_middle_year      |    Км_Полилен по полугодиям...    |
|     data_kp_polilen_middle_year      |    Кп_Полилен по полугодиям...    |
|     data_km_transkor_middle_year     |    Км_Транскор по полугодиям...   |
|     data_kp_transkor_middle_year     |    Кп_Транскор по полугодиям...   |
|      data_km_shpuly_middle_year      |     Км_Шпули по полугодиям...     |
|      data_kp_shpuly_middle_year      |     Кп_Шпули по полугодиям...     |
|      data_kol_vip_mufty_year         |   Количество выпущенных муфт...   |
|      data_kol_vip_kompl_year         |Количество выпущенных комплектов...|
|      data_kol_narezki_year           |   Количество нарезки пб ленты...  |
|      data_kol_rezki_pvh_lip_year     |   Количество резки ПВХ липкой...  |
|       data_ur_rash_mater_year        | Уровень расхода материалов Крм... |
|        data_ur_otkl_prod_year        |Уровень отклонений продукции Котк..|
|      data_ur_prost_kach_year         | Уровень простоя обор. Кпр кач...  |
|      data_ur_prost_nepost_year       | Уровень простоя обор. Кпр кол...  |
|  data_kol_vip_mufty_middle_year      |   Количество выпущенных муфт...   |
|  data_kol_vip_kompl_middle_year      |Количество выпущенных комплектов...|
|  data_kol_narezki_middle_year        |   Количество нарезки пб ленты...  |
|  data_kol_rezki_pvh_lip_middle_year  |   Количество резки ПВХ липкой...  |
|  data_ur_rash_mater_middle_year      | Уровень расхода материалов Крм... |
|  data_ur_otkl_prod_middle_year       |Уровень отклонений продукции Котк..|
|  data_ur_prost_kach_middle_year      | Уровень простоя обор. Кпр кач...  |
|  data_ur_prost_nepost_middle_year    | Уровень простоя обор. Кпр кол...  |
|  data_test                           | Тестовые данные ...               |
+--------------------------------------+-----------------------------------+
# The indicators of adhaesio
+---------------+---------------------------+--------------------------------+
| Идентификатор |     Наименования лент     | Наименование листов/переменных |
+---------------+---------------------------+--------------------------------+
|      001      |          ПИРМА-З          |            П_З / pz            |
|      002      |          ПИРМА-Л          |            П_Л / pl            |
|      003      |        ЛИТКОР-З_газ       |      ЛИТ_З_газ / lz_gaz        |
|      004      |     ЛИТКОР-З_тр_нефть     | ЛИТ_З_тр_нефть / lz_tr_neft    |
|      005      |        ЛИТКОР-Л_газ       |      ЛИТ_Л_газ / ll_gaz        |
|      006      |     ЛИТКОР-Л_тр_нефть     | ЛИТ_Л_тр_нефть / ll_tr_neft    |
|      007      | ЛИТКОР-НН толщина 1.9 мм. |     ЛИТ_НН_1_9 / lnn_1_9       |
|      008      | ЛИТКОР-НН толщина 2.0 мм. |     ЛИТ_НН_2_0 / lnn_2_0       |
|      009      | ЛИТКОР-НН толщина 1.7 мм. |     ЛИТ_НН_1_7 / lnn_1_7       |
|      010      |    БПИ толщина 1.7 мм.    |     БПИ_1_7 / bpi_1_7          |
|      011      |     БПИ толщина 2.0 мм    |     БПИ_2_0 / bpi_2_0          |
|      012      |ЛИТКОР-НН толщина 1.0 мм.  |     ЛИТ_НН_1_0 / lnn_1_0       |
+---------------+---------------------------+--------------------------------+
"""
# Импорт основных модулей
#--------------------------------------------------------
import pandas as pd
import numpy as np
import os
import sys
# Корневая дирректория для импорта
#--------------------------------------------------------
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# ПРОЦЕСС Б(7.2) Связь с потребителем:
# Процесс Б(7.2) Связь с потребителем (годовые показатели)
data_ur_vip_zak_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.2) Связь с потребителем/Уровень выполнения заказов по годам.csv', index_col = 0)
data_ur_pov_zak_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.2) Связь с потребителем/Уровень повторных закупок по годам.csv', index_col = 0)
data_ur_priv_new_cons_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.2) Связь с потребителем/Уровень привлечения новых потребителей по годам.csv', index_col = 0)
data_ur_udovl_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.2) Связь с потребителем/Уровень удовлетворенности по годам.csv', index_col = 0)
# Процесс Б(7.2) Связь с потребителем (полугодовые показатели)
data_ur_vip_zak_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.2) Связь с потребителем/Уровень выполнения заказов по полугодиям.csv', index_col = 0)
data_ur_pov_zak_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.2) Связь с потребителем/Уровень повторных закупок по полугодиям.csv', index_col = 0)
data_ur_priv_new_cons_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.2) Связь с потребителем/Уровень привлечения новых потребителей по полугодиям.csv', index_col = 0)

# ПРОЦЕСС Б(7.3) Проектирование и разработка
# Процесс Б(7.3) Проектирование и разработка (годовые показатели)
data_koef_nov_pri_razr_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.3) Проектирование и разработка/Кн по годам.csv', index_col = 0)
data_koef_vned_konst_dok_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.3) Проектирование и разработка/Квн конструкторской документации по годам.csv', index_col = 0)
data_pok_kach_razr_kd_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.3) Проектирование и разработка/Ккд по годам.csv', index_col = 0)
data_pok_kach_razr_td_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.3) Проектирование и разработка/Ктд по годам.csv', index_col = 0)
# Процесс Б(7.3) Проектирование и разработка (полугодовые показатели)
data_koef_nov_pri_razr_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.3) Проектирование и разработка/Кн по полугодиям.csv', index_col = 0)
data_koef_vned_konst_dok_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.3) Проектирование и разработка/Квн конструкторской документации по полугодиям.csv', index_col = 0)
data_pok_kach_razr_kd_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.3) Проектирование и разработка/Ккд по полугодиям.csv', index_col = 0)
data_pok_kach_razr_td_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.3) Проектирование и разработка/Ктд по полугодиям.csv', index_col = 0)

# ПРОЦЕСС Б(7.4) Закупки
# Процесс Б(7.4) Закупки (годовые показатели)
data_vip_graf_zak_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.4) Закупки/Кз по годам.csv', index_col = 0)
data_km_mastic_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.4) Закупки/Км_Мастика по годам.csv', index_col = 0)
data_km_pvh_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.4) Закупки/Км_ПВХ по годам.csv', index_col = 0)
data_kp_mastic_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.4) Закупки/Кп_Мастика по годам.csv', index_col = 0)
data_kp_pvh_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.4) Закупки/Кп_ПВХ по годам.csv', index_col = 0)
# Процесс Б(7.4) Закупки (полугодовые показатели)
data_vip_graf_zak_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.4) Закупки/Кз по полугодиям.csv', index_col = 0)
data_km_mastic_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.4) Закупки/Км_Мастика по полугодиям.csv', index_col = 0)
data_km_pvh_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.4) Закупки/Км_ПВХ по полугодиям.csv', index_col = 0)
data_kp_mastic_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.4) Закупки/Кп_Мастика по полугодиям.csv', index_col = 0)
data_kp_pvh_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.4) Закупки/Кп_ПВХ по полугодиям.csv', index_col = 0)

# Процесс Б(7.5) Производство продукции
# Процесс Б(7.5) Производство продукции (годовые показатели)
data_kol_vip_prod_year =  pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Количество выпущенной продукции по годам.csv', index_col = 0)
data_ur_pr_obr_kach_mat_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Кпр кач по годам.csv', index_col = 0)
data_ur_pr_obr_nep_mat_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Кпр кол по годам.csv', index_col = 0)
data_ur_neispr_obor_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень неисправности оборудования по годам.csv', index_col = 0)
data_ur_nesoot_prod_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень несоответствующей продукции по годам.csv', index_col = 0)
data_ur_teh_oth_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень техотходов по годам.csv', index_col = 0)
data_kol_vip_mufty_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Количество выпущенных муфт по годам.csv', index_col = 0)
data_kol_vip_kompl_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Количество комплектов ЛИТКОР КМ по годам.csv', index_col = 0)
data_kol_narezki_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Количество нарезки пб ленты по годам.csv', index_col = 0)
data_kol_rezki_pvh_lip_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Количество резки ПВХ липкой по годам.csv', index_col = 0)
data_ur_rash_mater_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень расхода материалов по годам.csv', index_col = 0)
data_ur_otkl_prod_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень отклонений продукции по годам.csv', index_col = 0)
data_ur_prost_kach_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень простоя из-за непост мат по годам.csv', index_col = 0)
data_ur_prost_nepost_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень простоя из-за несоот кач по годам.csv', index_col = 0)


# Процесс Б(7.5) Производство продукции (полугодовые показатели)
data_kol_vip_prod_middle_year =  pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Количество выпущеной продукции по полугодиям.csv', index_col = 0)
data_ur_pr_obr_kach_mat_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Кпр кач по полугодиям.csv', index_col = 0)
data_ur_pr_obr_nep_mat_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Кпр кол по полугодиям.csv', index_col = 0)
data_ur_neispr_obor_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень неисправности оборудования по полугодиям.csv', index_col = 0)
data_ur_nesoot_prod_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень несоответствующей продукции по полугодиям.csv', index_col = 0)
data_ur_teh_oth_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень техотходов по полугодиям.csv', index_col = 0)
data_kol_vip_mufty_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Количество выпущенных муфт по полугодиям.csv', index_col = 0)
data_kol_vip_kompl_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Количество комплектов ЛИТКОР КМ по полугодиям.csv', index_col = 0)
data_kol_narezki_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Количество нарезки пб ленты по полугодиям.csv', index_col = 0)
data_kol_rezki_pvh_lip_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Количество резки ПВХ липкой по полугодиям.csv', index_col = 0)
data_ur_rash_mater_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень расхода материалов по полугодиям.csv', index_col = 0)
data_ur_otkl_prod_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень отклонений продукции по полугодиям.csv', index_col = 0)
data_ur_prost_kach_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень простоя из-за непост мат по полугодиям.csv', index_col = 0)
data_ur_prost_nepost_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень простоя из-за несоот кач по полугодиям.csv', index_col = 0)

# Процесс Б(7.7) Сбыт
# Процесс Б(7.7) Сбыт (годовые показатели)
data_kol_real_prod_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.7) Сбыт/Количество реализованной продукции по годам.csv', index_col = 0)
data_pret_i_rekl_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.7) Сбыт/Претензии и рекламации от потребителей по годам.csv', index_col = 0)
data_ur_postav_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс Б(7.7) Сбыт/Уровень поставок по годам.csv', index_col = 0)
# Процесс Б(7.7) Сбыт (полугодовые показатели)
data_kol_real_prod_middle_year =  pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.7) Сбыт/Количество реализованной продукции по полугодиям.csv', index_col = 0)
data_pret_i_rekl_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.7) Сбыт/Претензии и рекламации от потребителей по полугодиям.csv', index_col = 0)
data_ur_postav_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс Б(7.7) Сбыт/Уровень поставок по полугодиям.csv', index_col = 0)

# Процесс О(6.2) Человеческие ресурсы
# Процесс О(6.2) Человеческие ресурсы (годовые показатели)
data_ur_prop_rab_dn_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(6.2) Человеческие ресурсы/Уровень пропуска рабочих дней по годам.csv', index_col = 0)
data_ur_tek_kad_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(6.2) Человеческие ресурсы/Уровень текучести кадров по годам.csv', index_col = 0)
data_ur_ukomp_kad_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(6.2) Человеческие ресурсы/Уровень укомплектованности кадрами по годам.csv', index_col = 0)
# Процесс О(6.2) Человеческие ресурсы (полугодовые показатели)
data_ur_prop_rab_dnmiddle__year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(6.2) Человеческие ресурсы/Уровень пропуска рабочих дней за полугодие.csv', index_col = 0)
data_ur_tek_kad_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(6.2) Человеческие ресурсы/Уровень текучести кадров за полугодие.csv', index_col = 0)
data_ur_ukomp_kad_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(6.2) Человеческие ресурсы/Уровень укомплектованности кадрами за полугодие.csv', index_col = 0)

# Процесс О(8.2) Мониторинг и измерение продукции
# Процесс О(8.2) Мониторинг и измерение продукции (годовые показатели)
data_km_antiadgeziv_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Антиадгезив по годам.csv', index_col = 0)
data_kp_antiadgeziv_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Антиадгезив по годам.csv', index_col = 0)
data_km_bitkor_r_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Биткор_Р по годам.csv', index_col = 0)
data_kp_bitkor_r_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Биткор_Р по годам.csv', index_col = 0)
data_km_bitkor_u_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Биткор_Р(У) по годам.csv', index_col = 0)
data_kp_bitkor_u_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Биткор_Р(У) по годам.csv', index_col = 0)
data_km_korobki_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Коробки по годам.csv', index_col = 0)
data_kp_korobki_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Коробки по годам.csv', index_col = 0)
data_km_mbpr_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_МБПР по годам.csv', index_col = 0)
data_kp_mbpr_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_МБПР по годам.csv', index_col = 0)
data_km_mufty_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Муфты по годам.csv', index_col = 0)
data_kp_mufty_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Муфты по годам.csv', index_col = 0)
data_km_bsk_pvh_lip_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_ОАО_БСК_липкая_ПВХ по годам.csv', index_col = 0)
data_kp_bsk_pvh_lip_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ОАО_БСК_липкая_ПВХ по годам.csv', index_col = 0)
data_km_selaron_pvh_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_ООО_Сэларон_ПВХ по годам.csv', index_col = 0)
data_kp_selaron_pvh_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ООО_Сэларон_ПВХ по годам.csv', index_col = 0)
data_km_bsk_pvh_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_ПВХ_ОАО_БСК по годам.csv', index_col = 0)
data_kp_bsk_pvh_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ПВХ_ОАО_БСК по годам.csv', index_col = 0)
data_km_pekom_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_ПЭКОМ по годам.csv', index_col = 0)
data_kp_pekom_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ПЭКОМ по годам.csv', index_col = 0)
data_km_pakety_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Пакеты полиэтиленовые по годам.csv', index_col = 0)
data_kp_pakety_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Пакеты полиэтиленовые по годам.csv', index_col = 0)
data_km_polilen_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Полилен по годам.csv', index_col = 0)
data_kp_polilen_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Полилен по годам.csv', index_col = 0)
data_km_politerm_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Политерм по годам.csv', index_col = 0)
data_kp_politerm_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Политерм по годам.csv', index_col = 0)
data_km_sibtrubizol_pvh_lip_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Сибтрубизол_липкая_ПВХ по годам.csv', index_col = 0)
data_kp_sibtrubizol_pvh_lip_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Сибтрубизол_липкая_ПВХ по годам.csv', index_col = 0)
data_km_transkor_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Транскор по годам.csv', index_col = 0)
data_kp_transkor_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Транскор по годам.csv', index_col = 0)
data_km_shpuly_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Шпули по годам.csv', index_col = 0)
data_kp_shpuly_year = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Шпули по годам.csv', index_col = 0)

# Процесс О(8.2) Мониторинг и измерение продукции (полугогодовые показатели)
data_km_antiadgeziv_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Антиадгезив по полугодиям.csv', index_col = 0)
data_kp_antiadgeziv_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Антиадгезив по полугодиям.csv', index_col = 0)
data_km_bitkor_r_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Биткор_Р по полугодиям.csv', index_col = 0)
data_kp_bitkor_r_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Биткор_Р по полугодиям.csv', index_col = 0)
data_km_bitkor_u_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Биткор_Р(У) по полугодиям.csv', index_col = 0)
data_kp_bitkor_u_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Биткор_Р(У) по полугодиям.csv', index_col = 0)
data_km_korobki_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Коробки по полугодиям.csv', index_col = 0)
data_kp_korobki_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Коробки по полугодиям.csv', index_col = 0)
data_km_mbpr_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_МБПР по полугодиям.csv', index_col = 0)
data_kp_mbpr_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_МБПР по полугодиям.csv', index_col = 0)
data_km_mufty_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Муфты по полугодиям.csv', index_col = 0)
data_kp_mufty_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Муфты по полугодиям.csv', index_col = 0)
data_km_bsk_pvh_lip_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_ОАО_БСК_липкая_ПВХ по полугодиям.csv', index_col = 0)
data_kp_bsk_pvh_lip_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ОАО_БСК_липкая_ПВХ по полугодиям.csv', index_col = 0)
data_km_selaron_pvh_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_ООО_Сэларон_ПВХ по полугодиям.csv', index_col = 0)
data_kp_selaron_pvh_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ООО_Сэларон_ПВХ по полугодиям.csv', index_col = 0)
data_km_bsk_pvh_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_ПВХ_ОАО_БСК по полугодиям.csv', index_col = 0)
data_kp_bsk_pvh_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ПВХ_ОАО_БСК по полугодиям.csv', index_col = 0)
data_km_pekom_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_ПЭКОМ по полугодиям.csv', index_col = 0)
data_kp_pekom_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ПЭКОМ по полугодиям.csv', index_col = 0)
data_km_pakety_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Пакеты полиэтиленовые по полугодиям.csv', index_col = 0)
data_kp_pakety_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Пакеты полиэтиленовые по полугодиям.csv', index_col = 0)
data_km_polilen_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Полилен по полугодиям.csv', index_col = 0)
data_kp_polilen_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Полилен по полугодиям.csv', index_col = 0)
data_km_transkor_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Транскор по полугодиям.csv', index_col = 0)
data_kp_transkor_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Транскор по полугодиям.csv', index_col = 0)
data_km_shpuly_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Шпули по полугодиям.csv', index_col = 0)
data_kp_shpuly_middle_year = pd.read_csv(parentdir+r'/Data/Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Шпули по полугодиям.csv', index_col = 0)

#Тестовые данные

data_test = pd.read_csv(parentdir+r'/Data/Показатели csv годовые/Test_indicators/test_empty.csv', index_col = 0)

# ПОКАЗАТЕЛИ АДГЕЗИИ
pz = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='П_З'
    )
pl = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='П_Л'
    )
lz_gaz = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_З_газ'
    )
lz_tr_neft = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_З_тр_нефть'
    )
ll_gaz = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_Л_газ'
    )
ll_tr_neft = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_Л_тр_нефть'
    )
lnn_1_9 = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_НН_1_9'
    )
lnn_2_0 = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_НН_2_0'
    )
lnn_1_7 = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_НН_1_7'
    )
bpi_1_7 = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='БПИ_1_7'
    )
bpi_2_0 = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='БПИ_2_0'
    )
lnn_1_0 = pd.read_excel(
    parentdir+r'/Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_НН_1_0'
    )
lst_name = [
        data_ur_vip_zak_year,
        data_ur_pov_zak_year,
        data_ur_priv_new_cons_year,
        data_ur_udovl_year,
        data_ur_vip_zak_middle_year,
        data_ur_pov_zak_middle_year,
        data_ur_priv_new_cons_middle_year,
        data_koef_nov_pri_razr_year,
        data_koef_vned_konst_dok_year,
        data_pok_kach_razr_kd_year,
        data_pok_kach_razr_td_year,
        data_koef_nov_pri_razr_middle_year,
        data_koef_vned_konst_dok_middle_year,
        data_pok_kach_razr_kd_middle_year,
        data_pok_kach_razr_td_middle_year,
        data_vip_graf_zak_year,
        data_km_mastic_year,
        data_km_pvh_year,
        data_kp_mastic_year,
        data_kp_pvh_year,
        data_vip_graf_zak_middle_year,
        data_km_mastic_middle_year,
        data_km_pvh_middle_year,
        data_kp_mastic_middle_year,
        data_kp_pvh_middle_year,
        data_kol_vip_prod_year,
        data_ur_pr_obr_kach_mat_year,
        data_ur_pr_obr_nep_mat_year,
        data_ur_neispr_obor_year,
        data_ur_nesoot_prod_year,
        data_ur_teh_oth_year,
        data_kol_vip_prod_middle_year,
        data_ur_pr_obr_kach_mat_middle_year,
        data_ur_pr_obr_nep_mat_middle_year,
        data_ur_neispr_obor_middle_year,
        data_ur_nesoot_prod_middle_year,
        data_ur_teh_oth_middle_year,
        data_kol_real_prod_year,
        data_pret_i_rekl_year,
        data_ur_postav_year,
        data_kol_real_prod_middle_year,
        data_pret_i_rekl_middle_year,
        data_ur_postav_middle_year,
        data_ur_prop_rab_dn_year,
        data_ur_tek_kad_year,
        data_ur_ukomp_kad_year,
        data_ur_prop_rab_dnmiddle__year,
        data_ur_tek_kad_middle_year,
        data_ur_ukomp_kad_middle_year,
        data_km_antiadgeziv_year,
        data_kp_antiadgeziv_year,
        data_km_bitkor_r_year,
        data_kp_bitkor_r_year,
        data_km_bitkor_u_year,
        data_kp_bitkor_u_year,
        data_km_korobki_year,
        data_kp_korobki_year,
        data_km_mbpr_year,
        data_kp_mbpr_year,
        data_km_mufty_year,
        data_kp_mufty_year,
        data_km_bsk_pvh_lip_year,
        data_kp_bsk_pvh_lip_year,
        data_km_selaron_pvh_year,
        data_kp_selaron_pvh_year,
        data_km_bsk_pvh_year,
        data_kp_bsk_pvh_year,
        data_km_pekom_year,
        data_kp_pekom_year,
        data_km_pakety_year,
        data_kp_pakety_year,
        data_km_polilen_year,
        data_kp_polilen_year,
        data_km_politerm_year,
        data_kp_politerm_year,
        data_km_sibtrubizol_pvh_lip_year,
        data_kp_sibtrubizol_pvh_lip_year,
        data_km_transkor_year,
        data_kp_transkor_year,
        data_km_shpuly_year,
        data_kp_shpuly_year,
        data_kol_vip_mufty_year,
        data_kol_vip_kompl_year,
        data_kol_narezki_year,
        data_kol_rezki_pvh_lip_year,
        data_ur_rash_mater_year,
        data_ur_otkl_prod_year,
        data_ur_prost_kach_year,
        data_ur_prost_nepost_year,
        data_km_antiadgeziv_middle_year,
        data_kp_antiadgeziv_middle_year,
        data_km_bitkor_r_middle_year,
        data_kp_bitkor_r_middle_year,
        data_km_bitkor_u_middle_year,
        data_kp_bitkor_u_middle_year,
        data_km_korobki_middle_year,
        data_kp_korobki_middle_year,
        data_km_mbpr_middle_year,
        data_kp_mbpr_middle_year,
        data_km_mufty_middle_year,
        data_kp_mufty_middle_year,
        data_km_bsk_pvh_lip_middle_year,
        data_kp_bsk_pvh_lip_middle_year,
        data_km_selaron_pvh_middle_year,
        data_kp_selaron_pvh_middle_year,
        data_km_bsk_pvh_middle_year,
        data_kp_bsk_pvh_middle_year,
        data_km_pekom_middle_year,
        data_kp_pekom_middle_year,
        data_km_pakety_middle_year,
        data_kp_pakety_middle_year,
        data_km_polilen_middle_year,
        data_kp_polilen_middle_year,
        data_km_transkor_middle_year,
        data_kp_transkor_middle_year,
        data_km_shpuly_middle_year,
        data_kp_shpuly_middle_year,
        data_kol_vip_mufty_middle_year,
        data_kol_vip_kompl_middle_year,
        data_kol_narezki_middle_year,
        data_kol_rezki_pvh_lip_middle_year,
        data_ur_rash_mater_middle_year,
        data_ur_otkl_prod_middle_year,
        data_ur_prost_kach_middle_year,
        data_ur_prost_nepost_middle_year,
        data_test,
            ]
# The indicators of adhaesio
lst_adhaesio = [
            pz,
            pl,
            lz_gaz,
            lz_tr_neft,
            ll_gaz,
            ll_tr_neft,
            lnn_1_9,
            lnn_2_0,
            lnn_1_7,
            bpi_1_7,
            bpi_2_0,
            lnn_1_0,
            #data_test,
            ]


