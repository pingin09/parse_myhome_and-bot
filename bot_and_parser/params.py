class data:
    def __init__(self):
        self.city = {'Тбилиси':
                    ['Тбилиси', 1996871],
                'Батуми':
                    ['Батуми', 874215],
                'Кутаиси':
                    ['Кутаиси', 8742174],
                'Рустави':
                    ['Рустави', 5997314]
                }
        self.regions = {'Тбилиси':
                       {'Глдани': 687578743,
                        'Дидубе': 687611312,
                        'Ваке': 687611312,
                        'Исани': 688350922,
                        'Крцанисский': 689701920,
                        'Мтанцминда': 689678147,
                        'Надзаладеви': 688137211,
                        'Сабуртало': 687602533,
                        'Самгори': 688330506,
                        'Чугурети': 687618311
                        }
                   }
        self.type_s = {'Продажа': 1, 'Аренда': 3, 'Аренда посуточно': 7}
        self.type_s_towr = {'Квартиры': 1, 'Дома и дачи': 2, 'Коммерческая площадь': 3}
        self.OwnerTypeID = {'Собственник' : 1, 'Нет': None}
    def formats(self, city_inp, regions_inp, type_s_inp, types_towr_inp,owner_inp, sort=3):
        cityID_last = self.city[city_inp][1]
        cityNAME_last = self.city[city_inp][0]
        region_last = self.regions[city_inp][regions_inp]
        owner_inp = self.OwnerTypeID[owner_inp]
        type_s_last = self.type_s[type_s_inp]
        type_towr_last = self.type_s_towr[types_towr_inp]
        return data.lastForm(self, [cityID_last, cityNAME_last, region_last, owner_inp, type_s_last, type_towr_last, sort])

    def lastForm(self, prelast):
        last_form = {
            'Keyword': prelast[1],
            'cities': prelast[0],
            'AdTypeID': prelast[4],
            'PrTypeID%5B%5D': prelast[5],
            'regions': prelast[2],
            'fullregions': prelast[2],
            'OwnerTypeID': prelast[3]
                     }
        return last_form

x = data()
y = x.formats(input('Введите город поиска'),input('Введите регион поиска'), input('Введите тип объявлений'),
                input('Введите тип собственности'), input('Собственник'))


