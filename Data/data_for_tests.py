#-*- coding: utf-8 -*-
"""
data.py - модуль подзагрузки данных для предварительного просмотра показателей
"""
__all__ = [
        "data_ur_vip_zak_year",
        "data_ur_pov_zak_year",
        "data_ur_priv_new_cons_year",
        "data_ur_udovl_year",
        "data_ur_vip_zak_middle_year",
        "data_ur_pov_zak_middle_year",
        "data_ur_priv_new_cons_middle_year",
        "data_koef_nov_pri_razr_year",
        "data_koef_vned_konst_dok_year",
        "data_pok_kach_razr_kd_year",
        "data_pok_kach_razr_td_year",
        "data_koef_nov_pri_razr_middle_year",
        "data_koef_vned_konst_dok_middle_year",
        "data_pok_kach_razr_kd_middle_year",
        "data_pok_kach_razr_td_middle_year",
        "data_vip_graf_zak_year",
        "data_km_mastic_year",
        "data_km_pvh_year",
        "data_kp_mastic_year",
        "data_kp_pvh_year",
        "data_vip_graf_zak_middle_year",
        "data_km_mastic_middle_year",
        "data_km_pvh_middle_year",
        "data_kp_mastic_middle_year",
        "data_kp_pvh_middle_year",
        "data_kol_vip_prod_year",
        "data_ur_pr_obr_kach_mat_year",
        "data_ur_pr_obr_nep_mat_year",
        "data_ur_neispr_obor_year",
        "data_ur_nesoot_prod_year",
        "data_ur_teh_oth_year",
        "data_kol_vip_prod_middle_year",
        "data_ur_pr_obr_kach_mat_middle_year",
        "data_ur_pr_obr_nep_mat_middle_year",
        "data_ur_neispr_obor_middle_year",
        "data_ur_nesoot_prod_middle_year",
        "data_ur_teh_oth_middle_year",
        "data_kol_real_prod_year",
        "data_pret_i_rekl_year",
        "data_ur_postav_year",
        "data_kol_real_prod_middle_year",
        "data_pret_i_rekl_middle_year",
        "data_ur_postav_middle_year",
        "data_ur_prop_rab_dn_year",
        "data_ur_tek_kad_year",
        "data_ur_ukomp_kad_year",
        "data_ur_prop_rab_dnmiddle__year",
        "data_ur_tek_kad_middle_year",
        "data_ur_ukomp_kad_middle_year",
        "data_km_antiadgeziv_year",
        "data_kp_antiadgeziv_year",
        "data_km_bitkor_r_year",
        "data_kp_bitkor_r_year",
        "data_km_bitkor_u_year",
        "data_kp_bitkor_u_year",
        "data_km_korobki_year",
        "data_kp_korobki_year",
        "data_km_mbpr_year",
        "data_kp_mbpr_year",
        "data_km_mufty_year",
        "data_kp_mufty_year",
        "data_km_bsk_pvh_lip_year",
        "data_kp_bsk_pvh_lip_year",
        "data_km_selaron_pvh_year",
        "data_kp_selaron_pvh_year",
        "data_km_bsk_pvh_year",
        "data_kp_bsk_pvh_year",
        "data_km_pekom_year",
        "data_kp_pekom_year",
        "data_km_pakety_year",
        "data_kp_pakety_year",
        "data_km_polilen_year",
        "data_kp_polilen_year",
        "data_km_politerm_year",
        "data_kp_politerm_year",
        "data_km_sibtrubizol_pvh_lip_year",
        "data_kp_sibtrubizol_pvh_lip_year",
        "data_km_transkor_year",
        "data_kp_transkor_year",
        "data_km_shpuly_year",
        "data_kp_shpuly_year",
        "data_km_antiadgeziv_middle_year",
        "data_kp_antiadgeziv_middle_year",
        "data_km_bitkor_r_middle_year",
        "data_kp_bitkor_r_middle_year",
        "data_km_bitkor_u_middle_year",
        "data_kp_bitkor_u_middle_year",
        "data_km_korobki_middle_year",
        "data_kp_korobki_middle_year",
        "data_km_mbpr_middle_year",
        "data_kp_mbpr_middle_year",
        "data_km_mufty_middle_year",
        "data_kp_mufty_middle_year",
        "data_km_bsk_pvh_lip_middle_year",
        "data_kp_bsk_pvh_lip_middle_year",
        "data_km_selaron_pvh_middle_year",
        "data_kp_selaron_pvh_middle_year",
        "data_km_bsk_pvh_middle_year",
        "data_kp_bsk_pvh_middle_year",
        "data_km_pekom_middle_year",
        "data_kp_pekom_middle_year",
        "data_km_pakety_middle_year",
        "data_kp_pakety_middle_year",
        "data_km_polilen_middle_year",
        "data_kp_polilen_middle_year",
        "data_km_transkor_middle_year",
        "data_kp_transkor_middle_year",
        "data_km_shpuly_middle_year",
        "data_kp_shpuly_middle_year",
        #Строка редактирования
        "info_name", "lst_name",
            ]
info_name = {
        "data_ur_vip_zak_year":
         "Уровень выполнения заказов по годам",
        "data_ur_pov_zak_year":
         "Уровень повторных закупок по годам",
         "data_ur_priv_new_cons_year":
         "Уровень привлечения новых потребителей по годам",
        "data_ur_udovl_year":
         "Уровень удовлетворенности по годам",
        "data_ur_vip_zak_middle_year":
         "Уровень выполнения заказов по полугодиям",
        "data_ur_pov_zak_middle_year":
         "Уровень повторных закупок по полугодиям",
        "data_ur_priv_new_cons_middle_year":
         "Уровень привлечения новых потребителей по полугодиям",
        "data_koef_nov_pri_razr_year":
        "Кн по годам",
        "data_koef_vned_konst_dok_year":
        "Квн конструкторской документации по годам",
        "data_pok_kach_razr_kd_year":
        "Ккд по годам",
        "data_pok_kach_razr_td_year":
        "Ктд по годам",
        "data_koef_nov_pri_razr_middle_year":
        "Кн по полугодиям",
        "data_koef_vned_konst_dok_middle_year":
        "Квн конструкторской документации по полугодиям",
        "data_pok_kach_razr_kd_middle_year":
        "Ккд по полугодиям",
        "data_pok_kach_razr_td_middle_year":
        "Ктд по полугодиям",
        "data_vip_graf_zak_year":
        "Кз по годам",
        "data_km_mastic_year":
        "Км_Мастика по годам",
        "data_km_pvh_year":
        "Км_ПВХ по годам",
        "data_kp_mastic_year":
        "Кп_Мастика по годам",
        "data_kp_pvh_year":
        "Кп_ПВХ по годам",
        "data_vip_graf_zak_middle_year":
        "Кз по полугодиям",
        "data_km_mastic_middle_year":
        "Км_Мастика по полугодиям",
        "data_km_pvh_middle_year":
        "Км_ПВХ по полугодиям",
        "data_kp_mastic_middle_year":
        "Кп_Мастика по полугодиям",
        "data_kp_pvh_middle_year":
        "Кп_ПВХ по полугодиям",
        "data_kol_vip_prod_year":
        "Количество выпущенной продукции по годам",
        "data_ur_pr_obr_kach_mat_year":
        "Кпр кач по годам",
        "data_ur_pr_obr_nep_mat_year":
        "Кпр кол по годам",
        "data_ur_neispr_obor_year":
        "Уровень неисправности оборудования по годам",
        "data_ur_nesoot_prod_year":
        "Уровень несоответствующей продукции по годам",
        "data_ur_teh_oth_year":
        "Уровень техотходов по годам",
        "data_kol_vip_prod_middle_year":
        "Количество выпущеной продукции по полугодиям",
        "data_ur_pr_obr_kach_mat_middle_year":
        "Кпр кач по полугодиям",
        "data_ur_pr_obr_nep_mat_middle_year":
        "Кпр кол по полугодиям",
        "data_ur_neispr_obor_middle_year":
        "Уровень неисправности оборудования по полугодиям",
        "data_ur_nesoot_prod_middle_year":
        "Уровень несоответствующей продукции по полугодиям",
        "data_ur_teh_oth_middle_year":
        "Уровень техотходов по полугодиям",
        "data_kol_real_prod_year":
         "Количество реализованной продукции по годам",
        "data_pret_i_rekl_year":
         "Претензии и рекламации от потребителей по годам",
        "data_ur_postav_year":
         "Уровень поставок по годам",
        "data_kol_real_prod_middle_year":
         "Количество реализованной продукции по полугодиям",
        "data_pret_i_rekl_middle_year":
         "Претензии и рекламации от потребителей по полугодиям",
        "data_ur_postav_middle_year":
         "Уровень поставок по полугодиям",
        "data_ur_prop_rab_dn_year":
        "Уровень пропуска рабочих дней по годам",
        "data_ur_tek_kad_year":
        "Уровень текучести кадров по годам",
        "data_ur_ukomp_kad_year":
        "Уровень укомплектованности кадрами по годам",
        "data_ur_prop_rab_dnmiddle__year":
        "Уровень пропуска рабочих дней за полугодие",
        "data_ur_tek_kad_middle_year":
        "Уровень текучести кадров за полугодие",
        "data_ur_ukomp_kad_middle_year":
        "Уровень укомплектованности кадрами за полугодие",
        "data_km_antiadgeziv_year":
        "Км_Антиадгезив по годам",
        "data_kp_antiadgeziv_year":
        "Кп_Антиадгезив по годам",
        "data_km_bitkor_r_year":
        "Км_Биткор_Р по годам",
        "data_kp_bitkor_r_year":
        "Кп_Биткор_Р по годам",
        "data_km_bitkor_u_year":
        "Км_Биткор_Р(У) по годам",
        "data_kp_bitkor_u_year":
        "Кп_Биткор_Р(У) по годам",
        "data_km_korobki_year":
        "Км_Коробки по годам",
        "data_kp_korobki_year":
        "Кп_Коробки по годам",
        "data_km_mbpr_year":
        "Км_МБПР по годам",
        "data_kp_mbpr_year":
        "Кп_МБПР по годам",
        "data_km_mufty_year":
        "Км_Муфты по годам",
        "data_kp_mufty_year":
        "Кп_Муфты по годам",
        "data_km_bsk_pvh_lip_year":
        "Км_ОАО_БСК_липкая_ПВХ по годам",
        "data_kp_bsk_pvh_lip_year":
        "Кп_ОАО_БСК_липкая_ПВХ по годам",
        "data_km_selaron_pvh_year":
        "Км_ООО_Сэларон_ПВХ по годам",
        "data_kp_selaron_pvh_year":
        "Кп_ООО_Сэларон_ПВХ по годам",
        "data_km_bsk_pvh_year":
        "Км_ПВХ_ОАО_БСК по годам",
        "data_kp_bsk_pvh_year":
        "Кп_ПВХ_ОАО_БСК по годам",
        "data_km_pekom_year":
        "Км_ПЭКОМ по годам",
        "data_kp_pekom_year":
        "Кп_ПЭКОМ по годам",
        "data_km_pakety_year":
        "Км_Пакеты полиэтиленовые по годам",
        "data_kp_pakety_year":
        "Кп_Пакеты полиэтиленовые по годам",
        "data_km_polilen_year":
        "Км_Полилен по годам",
        "data_kp_polilen_year":
        "Кп_Полилен по годам",
        "data_km_politerm_year":
        "Км_Политерм по годам",
        "data_kp_politerm_year":
        "Кп_Политерм по годам",
        "data_km_sibtrubizol_pvh_lip_year":
        "Км_Сибтрубизол_липкая_ПВХ по годам",
        "data_kp_sibtrubizol_pvh_lip_year":
        "Кп_Сибтрубизол_липкая_ПВХ по годам",
        "data_km_transkor_year":
        "Км_Транскор по годам",
        "data_kp_transkor_year":
        "Кп_Транскор по годам",
        "data_km_shpuly_year":
        "Км_Шпули по годам",
        "data_kp_shpuly_year":
        "Кп_Шпули по годам",
        "data_km_antiadgeziv_middle_year":
        "Км_Антиадгезив по полугодиям",
        "data_kp_antiadgeziv_middle_year":
        "Кп_Антиадгезив по полугодиям",
        "data_km_bitkor_r_middle_year":
        "Км_Биткор_Р по полугодиям",
        "data_kp_bitkor_r_middle_year":
        "Кп_Биткор_Р по полугодиям",
        "data_km_bitkor_u_middle_year":
        "Км_Биткор_Р(У) по полугодиям",
        "data_kp_bitkor_u_middle_year":
        "Кп_Биткор_Р(У) по полугодиям",
        "data_km_korobki_middle_year":
        "Км_Коробки по полугодиям",
        "data_kp_korobki_middle_year":
        "Кп_Коробки по полугодиям",
        "data_km_mbpr_middle_year":
        "Км_МБПР по полугодиям",
        "data_kp_mbpr_middle_year":
        "Кп_МБПР по полугодиям",
        "data_km_mufty_middle_year":
        "Км_Муфты по полугодиям",
        "data_kp_mufty_middle_year":
        "Кп_Муфты по полугодиям",
        "data_km_bsk_pvh_lip_middle_year":
        "Км_ОАО_БСК_липкая_ПВХ по полугодиям",
        "data_kp_bsk_pvh_lip_middle_year":
        "Кп_ОАО_БСК_липкая_ПВХ по полугодиям",
        "data_km_selaron_pvh_middle_year":
        "Км_ООО_Сэларон_ПВХ по полугодиям",
        "data_kp_selaron_pvh_middle_year":
        "Кп_ООО_Сэларон_ПВХ по полугодиям",
        "data_km_bsk_pvh_middle_year":
        "Км_ПВХ_ОАО_БСК по полугодиям",
        "data_kp_bsk_pvh_middle_year":
        "Кп_ПВХ_ОАО_БСК по полугодиям",
        "data_km_pekom_middle_year":
        "Км_ПЭКОМ по полугодиям",
        "data_kp_pekom_middle_year":
        "Кп_ПЭКОМ по полугодиям",
        "data_km_pakety_middle_year":
        "Км_Пакеты полиэтиленовые по полугодиям",
        "data_kp_pakety_middle_year":
        "Кп_Пакеты полиэтиленовые по полугодиям",
        "data_km_polilen_middle_year":
        "Км_Полилен по полугодиям",
        "data_kp_polilen_middle_year":
        "Кп_Полилен по полугодиям",
        "data_km_transkor_middle_year":
        "Км_Транскор по полугодиям",
        "data_kp_transkor_middle_year":
        "Кп_Транскор по полугодиям",
        "data_km_shpuly_middle_year":
        "Км_Шпули по полугодиям",
        "data_kp_shpuly_middle_year":
        "Кп_Шпули по полугодиям",
            }
import pandas as pd
# ПРОЦЕСС Б(7.2) Связь с потребителем:
# Процесс Б(7.2) Связь с потребителем (годовые показатели)
data_ur_vip_zak_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.2) Связь с потребителем/Уровень выполнения заказов по годам.csv', index_col = 0)
data_ur_pov_zak_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.2) Связь с потребителем/Уровень повторных закупок по годам.csv', index_col = 0)
data_ur_priv_new_cons_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.2) Связь с потребителем/Уровень привлечения новых потребителей по годам.csv', index_col = 0)
data_ur_udovl_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.2) Связь с потребителем/Уровень удовлетворенности по годам.csv', index_col = 0)
# Процесс Б(7.2) Связь с потребителем (полугодовые показатели)
data_ur_vip_zak_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.2) Связь с потребителем/Уровень выполнения заказов по полугодиям.csv', index_col = 0)
data_ur_pov_zak_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.2) Связь с потребителем/Уровень повторных закупок по полугодиям.csv', index_col = 0)
data_ur_priv_new_cons_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.2) Связь с потребителем/Уровень привлечения новых потребителей по полугодиям.csv', index_col = 0)

# ПРОЦЕСС Б(7.3) Проектирование и разработка
# Процесс Б(7.3) Проектирование и разработка (годовые показатели)
data_koef_nov_pri_razr_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.3) Проектирование и разработка/Кн по годам.csv', index_col = 0)
data_koef_vned_konst_dok_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.3) Проектирование и разработка/Квн конструкторской документации по годам.csv', index_col = 0)
data_pok_kach_razr_kd_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.3) Проектирование и разработка/Ккд по годам.csv', index_col = 0)
data_pok_kach_razr_td_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.3) Проектирование и разработка/Ктд по годам.csv', index_col = 0)
# Процесс Б(7.3) Проектирование и разработка (полугодовые показатели)
data_koef_nov_pri_razr_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.3) Проектирование и разработка/Кн по полугодиям.csv', index_col = 0)
data_koef_vned_konst_dok_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.3) Проектирование и разработка/Квн конструкторской документации по полугодиям.csv', index_col = 0)
data_pok_kach_razr_kd_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.3) Проектирование и разработка/Ккд по полугодиям.csv', index_col = 0)
data_pok_kach_razr_td_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.3) Проектирование и разработка/Ктд по полугодиям.csv', index_col = 0)

# ПРОЦЕСС Б(7.4) Закупки
# Процесс Б(7.4) Закупки (годовые показатели)
data_vip_graf_zak_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.4) Закупки/Кз по годам.csv', index_col = 0)
data_km_mastic_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.4) Закупки/Км_Мастика по годам.csv', index_col = 0)
data_km_pvh_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.4) Закупки/Км_ПВХ по годам.csv', index_col = 0)
data_kp_mastic_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.4) Закупки/Кп_Мастика по годам.csv', index_col = 0)
data_kp_pvh_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.4) Закупки/Кп_ПВХ по годам.csv', index_col = 0)
# Процесс Б(7.4) Закупки (полугодовые показатели)
data_vip_graf_zak_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.4) Закупки/Кз по полугодиям.csv', index_col = 0)
data_km_mastic_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.4) Закупки/Км_Мастика по полугодиям.csv', index_col = 0)
data_km_pvh_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.4) Закупки/Км_ПВХ по полугодиям.csv', index_col = 0)
data_kp_mastic_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.4) Закупки/Кп_Мастика по полугодиям.csv', index_col = 0)
data_kp_pvh_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.4) Закупки/Кп_ПВХ по полугодиям.csv', index_col = 0)

# Процесс Б(7.5) Производство продукции
# Процесс Б(7.5) Производство продукции (годовые показатели)
data_kol_vip_prod_year =  pd.read_csv(r'Показатели csv годовые/Процесс Б(7.5) Производство продукции/Количество выпущенной продукции по годам.csv', index_col = 0)
data_ur_pr_obr_kach_mat_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.5) Производство продукции/Кпр кач по годам.csv', index_col = 0)
data_ur_pr_obr_nep_mat_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.5) Производство продукции/Кпр кол по годам.csv', index_col = 0)
data_ur_neispr_obor_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень неисправности оборудования по годам.csv', index_col = 0)
data_ur_nesoot_prod_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень несоответствующей продукции по годам.csv', index_col = 0)
data_ur_teh_oth_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.5) Производство продукции/Уровень техотходов по годам.csv', index_col = 0)
# Процесс Б(7.5) Производство продукции (полугодовые показатели)
data_kol_vip_prod_middle_year =  pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Количество выпущеной продукции по полугодиям.csv', index_col = 0)
data_ur_pr_obr_kach_mat_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Кпр кач по полугодиям.csv', index_col = 0)
data_ur_pr_obr_nep_mat_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Кпр кол по полугодиям.csv', index_col = 0)
data_ur_neispr_obor_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень неисправности оборудования по полугодиям.csv', index_col = 0)
data_ur_nesoot_prod_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень несоответствующей продукции по полугодиям.csv', index_col = 0)
data_ur_teh_oth_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.5) Производство продукции/Уровень техотходов по полугодиям.csv', index_col = 0)

# Процесс Б(7.7) Сбыт
# Процесс Б(7.7) Сбыт (годовые показатели)
data_kol_real_prod_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.7) Сбыт/Количество реализованной продукции по годам.csv', index_col = 0)
data_pret_i_rekl_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.7) Сбыт/Претензии и рекламации от потребителей по годам.csv', index_col = 0)
data_ur_postav_year = pd.read_csv(r'Показатели csv годовые/Процесс Б(7.7) Сбыт/Уровень поставок по годам.csv', index_col = 0)
# Процесс Б(7.7) Сбыт (полугодовые показатели)
data_kol_real_prod_middle_year =  pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.7) Сбыт/Количество реализованной продукции по полугодиям.csv', index_col = 0)
data_pret_i_rekl_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.7) Сбыт/Претензии и рекламации от потребителей по полугодиям.csv', index_col = 0)
data_ur_postav_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс Б(7.7) Сбыт/Уровень поставок по полугодиям.csv', index_col = 0)

# Процесс О(6.2) Человеческие ресурсы
# Процесс О(6.2) Человеческие ресурсы (годовые показатели)
data_ur_prop_rab_dn_year = pd.read_csv(r'Показатели csv годовые/Процесс О(6.2) Человеческие ресурсы/Уровень пропуска рабочих дней по годам.csv', index_col = 0)
data_ur_tek_kad_year = pd.read_csv(r'Показатели csv годовые/Процесс О(6.2) Человеческие ресурсы/Уровень текучести кадров по годам.csv', index_col = 0)
data_ur_ukomp_kad_year = pd.read_csv(r'Показатели csv годовые/Процесс О(6.2) Человеческие ресурсы/Уровень укомплектованности кадрами по годам.csv', index_col = 0)
# Процесс О(6.2) Человеческие ресурсы (полугодовые показатели)
data_ur_prop_rab_dnmiddle__year = pd.read_csv(r'Показатели csv полугодие/Процесс О(6.2) Человеческие ресурсы/Уровень пропуска рабочих дней за полугодие.csv', index_col = 0)
data_ur_tek_kad_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(6.2) Человеческие ресурсы/Уровень текучести кадров за полугодие.csv', index_col = 0)
data_ur_ukomp_kad_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(6.2) Человеческие ресурсы/Уровень укомплектованности кадрами за полугодие.csv', index_col = 0)

# Процесс О(8.2) Мониторинг и измерение продукции
# Процесс О(8.2) Мониторинг и измерение продукции (годовые показатели)
data_km_antiadgeziv_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Антиадгезив по годам.csv', index_col = 0)
data_kp_antiadgeziv_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Антиадгезив по годам.csv', index_col = 0)
data_km_bitkor_r_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Биткор_Р по годам.csv', index_col = 0)
data_kp_bitkor_r_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Биткор_Р по годам.csv', index_col = 0)
data_km_bitkor_u_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Биткор_Р(У) по годам.csv', index_col = 0)
data_kp_bitkor_u_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Биткор_Р(У) по годам.csv', index_col = 0)
data_km_korobki_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Коробки по годам.csv', index_col = 0)
data_kp_korobki_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Коробки по годам.csv', index_col = 0)
data_km_mbpr_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_МБПР по годам.csv', index_col = 0)
data_kp_mbpr_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_МБПР по годам.csv', index_col = 0)
data_km_mufty_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Муфты по годам.csv', index_col = 0)
data_kp_mufty_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Муфты по годам.csv', index_col = 0)
data_km_bsk_pvh_lip_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_ОАО_БСК_липкая_ПВХ по годам.csv', index_col = 0)
data_kp_bsk_pvh_lip_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ОАО_БСК_липкая_ПВХ по годам.csv', index_col = 0)
data_km_selaron_pvh_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_ООО_Сэларон_ПВХ по годам.csv', index_col = 0)
data_kp_selaron_pvh_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ООО_Сэларон_ПВХ по годам.csv', index_col = 0)
data_km_bsk_pvh_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_ПВХ_ОАО_БСК по годам.csv', index_col = 0)
data_kp_bsk_pvh_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ПВХ_ОАО_БСК по годам.csv', index_col = 0)
data_km_pekom_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_ПЭКОМ по годам.csv', index_col = 0)
data_kp_pekom_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ПЭКОМ по годам.csv', index_col = 0)
data_km_pakety_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Пакеты полиэтиленовые по годам.csv', index_col = 0)
data_kp_pakety_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Пакеты полиэтиленовые по годам.csv', index_col = 0)
data_km_polilen_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Полилен по годам.csv', index_col = 0)
data_kp_polilen_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Полилен по годам.csv', index_col = 0)
data_km_politerm_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Политерм по годам.csv', index_col = 0)
data_kp_politerm_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Политерм по годам.csv', index_col = 0)
data_km_sibtrubizol_pvh_lip_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Сибтрубизол_липкая_ПВХ по годам.csv', index_col = 0)
data_kp_sibtrubizol_pvh_lip_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Сибтрубизол_липкая_ПВХ по годам.csv', index_col = 0)
data_km_transkor_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Транскор по годам.csv', index_col = 0)
data_kp_transkor_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Транскор по годам.csv', index_col = 0)
data_km_shpuly_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Км_Шпули по годам.csv', index_col = 0)
data_kp_shpuly_year = pd.read_csv(r'Показатели csv годовые/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Шпули по годам.csv', index_col = 0)

# Процесс О(8.2) Мониторинг и измерение продукции (полугогодовые показатели)
data_km_antiadgeziv_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Антиадгезив по полугодиям.csv', index_col = 0)
data_kp_antiadgeziv_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Антиадгезив по полугодиям.csv', index_col = 0)
data_km_bitkor_r_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Биткор_Р по полугодиям.csv', index_col = 0)
data_kp_bitkor_r_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Биткор_Р по полугодиям.csv', index_col = 0)
data_km_bitkor_u_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Биткор_Р(У) по полугодиям.csv', index_col = 0)
data_kp_bitkor_u_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Биткор_Р(У) по полугодиям.csv', index_col = 0)
data_km_korobki_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Коробки по полугодиям.csv', index_col = 0)
data_kp_korobki_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Коробки по полугодиям.csv', index_col = 0)
data_km_mbpr_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_МБПР по полугодиям.csv', index_col = 0)
data_kp_mbpr_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_МБПР по полугодиям.csv', index_col = 0)
data_km_mufty_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Муфты по полугодиям.csv', index_col = 0)
data_kp_mufty_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Муфты по полугодиям.csv', index_col = 0)
data_km_bsk_pvh_lip_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_ОАО_БСК_липкая_ПВХ по полугодиям.csv', index_col = 0)
data_kp_bsk_pvh_lip_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ОАО_БСК_липкая_ПВХ по полугодиям.csv', index_col = 0)
data_km_selaron_pvh_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_ООО_Сэларон_ПВХ по полугодиям.csv', index_col = 0)
data_kp_selaron_pvh_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ООО_Сэларон_ПВХ по полугодиям.csv', index_col = 0)
data_km_bsk_pvh_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_ПВХ_ОАО_БСК по полугодиям.csv', index_col = 0)
data_kp_bsk_pvh_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ПВХ_ОАО_БСК по полугодиям.csv', index_col = 0)
data_km_pekom_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_ПЭКОМ по полугодиям.csv', index_col = 0)
data_kp_pekom_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_ПЭКОМ по полугодиям.csv', index_col = 0)
data_km_pakety_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Пакеты полиэтиленовые по полугодиям.csv', index_col = 0)
data_kp_pakety_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Пакеты полиэтиленовые по полугодиям.csv', index_col = 0)
data_km_polilen_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Полилен по полугодиям.csv', index_col = 0)
data_kp_polilen_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Полилен по полугодиям.csv', index_col = 0)
data_km_transkor_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Транскор по полугодиям.csv', index_col = 0)
data_kp_transkor_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Транскор по полугодиям.csv', index_col = 0)
data_km_shpuly_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Км_Шпули по полугодиям.csv', index_col = 0)
data_kp_shpuly_middle_year = pd.read_csv(r'Показатели csv полугодие/Процесс О(8.2) Мониторинг и измерение продукции/Кп_Шпули по полугодиям.csv', index_col = 0)
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
            ]
