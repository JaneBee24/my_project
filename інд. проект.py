def all_commands(command):
    keywords = {
        'Комунальні': public_utilities,
        'Сміття': garbage_function,
        'Загальні витрати': general_expenses
    }

    if command in keywords:
        keywords[command]()
    else:
        print('Данного ключового слова не знайдено, спробуйте ще')

def public_utilities():
    print('Розрахунок комунальних витрат на місяць: ')
    while True:
        water = int(input('Введіть витрати на воду: '))
        electricity = int(input('Введіть витрати на електроенергію:'))
        gas = int(input('Введіть витрати на газ: '))
        if water > 0 and electricity > 0 and gas > 0:
            utilities = water + electricity + gas
            print('Це ваш розрахунок комунальних витрат на місяць', utilities)
            break
        else:
            print('Виникла помилка. Будь ласка, введіть значення більше 0')


def garbage_function():
    print('Розрахунок вивезення сміття на місяць')
    while True:
        sq_meter = int(input('Введіть площу свого будинку у кв.м: '))
        if sq_meter > 0:
            garbage_result = (sq_meter * 372.35) / 12
            print('Це ваш розрахунок вивезення сміття на місяць: ',(round(garbage_result)))
            break
        else:
            print('Виникла помилка. Будь ласка, введіть значення більше 0')
        
            
def general_expenses():
    print('Розрахунок загальних витрат на утримання будинку')
    while True:
        monthly_utilities = int(input('Введіть ваші витрати на комунальні послуги/інтернет: '))
        monthly_insurance = int(input('Введіть ваші витрати на страхування: '))
        monthly_rent = int(input('Введіть ваші витрати на оренду/кредит на житло: '))
        monthly_service = int(input('Введіть ваші витрати на технічне обслуговування: '))
        monthly_other = int(input('Введіть ваші інші витрати: '))
        if monthly_utilities >= 0 and monthly_insurance >= 0 and monthly_rent >= 0 and monthly_service >= 0 and monthly_other >= 0:
            all_spending = monthly_utilities + monthly_insurance + monthly_rent + monthly_service +monthly_other 
            print('Це ваші сумарні витрати на обслуговування будинку в місяць', all_spending )
            break
        else:
            print('Виникла помилка. Будь ласка, введіть 0 або більше значення')

if __name__ == "__main__":
    user_input = input('Це програма розрахунку витрат на утримання будинку. Введіть те, що ви хочете розрахувати по ключовим словам: '
                       '«Комунальні» - розрахунок комунальних витрат на місяць, '
                       '«Сміття» - розрахунок вивезення сміття на місяць, '
                       '«Загальні витрати» - розрахунок загальних витрат на утримання будинку: ')

    all_commands(user_input)
