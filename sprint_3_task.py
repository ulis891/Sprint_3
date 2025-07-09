import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def get_name_items(self):
         return self.__name_items
    
    @property
    def get_number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise ValueError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1
    
    def delete_item_from_check(self, name):
        if name in self.__name_items:
            self.__name_items.remove(name)
            self.__number_items -= 1
        else:
            raise NameError('Позиция отсутствует в чеке')
    
    def check_amount(self):
        total = [self.__item_price[name] for name in self.__name_items]
        if self.__number_items > 10:
            return sum(total) * 0.9
        return sum(total)

    def _twenty_percent_tax_calculation(self):
        twenty_percent_tax = [name for name in self.__name_items if self.__tax_rate[name] == 20]
        total = [self.__item_price[name] for name in twenty_percent_tax]
        total_sum = sum(map(lambda x: x * 0.2, total))
        if self.__number_items > 10:
            return total_sum * 0.9
        return total_sum


    def _ten_percent_tax_calculation(self):
        ten_percent_tax = [name for name in self.__name_items if self.__tax_rate[name] == 10]
        total = [self.__item_price[name] for name in ten_percent_tax]
        total_sum = sum(map(lambda x: x * 0.1, total))
        if self.__number_items > 10:
            return total_sum * 0.9
        return total_sum


    def total_tax(self):
        return self._twenty_percent_tax_calculation() + self._ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'

    @staticmethod
    def get_date_and_time():
        now = datetime.datetime.now()
        date = [['часы', lambda x: x.hour], ['минуты',lambda x: x.minute],['день',lambda x: x.day],['месяц',lambda x: x.month], ['год',lambda x: x.year]]
        date_and_time = [f'{dt[0]}: {dt[1](now)}' for dt in date ]
        return date_and_time




tt = OnlineSalesRegisterCollector()
tt.add_item_to_cheque('чипсы')
tt.add_item_to_cheque('чипсы')
tt.add_item_to_cheque('кола')
tt.add_item_to_cheque('чипсы')
tt.add_item_to_cheque('чипсы')
tt.add_item_to_cheque('кола')
tt.add_item_to_cheque('чипсы')
tt.add_item_to_cheque('чипсы')
tt.add_item_to_cheque('кола')
tt.add_item_to_cheque('чипсы')
tt.add_item_to_cheque('чипсы')
tt.add_item_to_cheque('кола')
tt.delete_item_from_check('кола')
tt.add_item_to_cheque('молоко')
print(tt.get_name_items)
print(tt.get_number_items)
print(tt.check_amount())
print(tt._ten_percent_tax_calculation())
print(tt._twenty_percent_tax_calculation())
print(tt.total_tax())
print(OnlineSalesRegisterCollector.get_telephone_number(9856548758))
print(OnlineSalesRegisterCollector.get_date_and_time())