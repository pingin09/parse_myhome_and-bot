class Data:
    def __init__(self, forms):
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
                             'Чугурети': 687618311}}
        self.type_s = {'Продажа': 1, 'Аренда': 3, 'Аренда посуточно': 7}
        self.type_s_towr = {'Квартира': 1, 'Дома и дачи': 2, 'Коммерческая площадь': 3}
        self.forms = forms

    def formats(self):
        lastForm = {'Keyword': self.city[self.forms['town']][0],
                    'cities': self.city[self.forms['town']][1],
                    'regions': self.regions[self.forms['town']][self.forms['district']],
                    'fullregions': self.regions[self.forms['town']][self.forms['district']],
                    'AdType': 3,
                    'PrTypeID%5B%5D': self.type_s_towr[self.forms['type_of_house']],
                    'SortID': 1,
                    'FCurrencyID': 1,
                    'RoomNums%5B%5D': int(self.forms['flat_quolity']),
                    'FPriceFrom': int(self.forms['min_prise']),
                    'FPriceTo': int(self.forms['max_prise'])}
        if self.forms['handle_owner'] == 'Да':
            lastForm['OwnerTypeID'] = 1

            # if add bot check $ or lari
            # if forms['Макс - мин цена, валюта'][2] == 'Доллар':
            #     lastForm['FCurrencyID'] = 1
            # elif forms['Макс - мин цена, валюта'][2] == 'Лари':
            #     lastForm['FCurrencyID'] = 3

        return lastForm