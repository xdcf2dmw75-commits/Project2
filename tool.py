import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type, format_number, PhoneNumberFormat
import requests
import socket

def phone_info():
    num = input("Введите номер (+...): ")

    try:
        parsed = phonenumbers.parse(num)
        zones = timezone.time_zones_for_number(parsed)

        t = number_type(parsed)
        if t == phonenumbers.PhoneNumberType.MOBILE:
            t = "Мобильный"
        elif t == phonenumbers.PhoneNumberType.FIXED_LINE:
            t = "Стационарный"
        else:
            t = "Неизвестно"

        print("\n========== ИНФО НОМЕРА ==========")
        print("Номер:", num)
        print("Регион:", geocoder.description_for_number(parsed, "ru"))
        print("Оператор:", carrier.name_for_number(parsed, "ru"))
        print("Тип:", t)
        print("Часовой пояс:", zones[0])
        print("Валидный:", phonenumbers.is_valid_number(parsed))
        print("Формат международный:", format_number(parsed, PhoneNumberFormat.INTERNATIONAL))
        print("Формат национальный:", format_number(parsed, PhoneNumberFormat.NATIONAL))
        print("================================")

    except:
        print("Ошибка номера")

    input("\nНажми Enter...")


def ip_info():
    ip = input("Введите IP: ")

    try:
        r = requests.get("http://ip-api.com/json/" + ip)
        data = r.json()

        print("\n========== ИНФО IP ==========")
        print("IP:", ip)
        print("Страна:", data.get("country"))
        print("Регион:", data.get("regionName"))
        print("Город:", data.get("city"))
        print("Провайдер:", data.get("isp"))
        print("Организация:", data.get("org"))
        print("Часовой пояс:", data.get("timezone"))
        print("Координаты:", data.get("lat"), data.get("lon"))
        print("Статус:", data.get("status"))
        print("================================")

    except:
        print("Ошибка IP")

    input("\nНажми Enter...")


def email_info():
    email = input("Введите email: ")

    try:
        username = email.split("@")[0]
        domain = email.split("@")[1]

        print("\n========== ИНФО EMAIL ==========")
        print("Email:", email)
        print("Имя пользователя:", username)
        print("Домен:", domain)

        if "gmail.com" in domain:
            print("Сервис: Gmail")
        elif "yandex" in domain:
            print("Сервис: Яндекс")
        elif "mail.ru" in domain:
            print("Сервис: Mail.ru")
        else:
            print("Сервис: неизвестный")

        print("================================")

    except:
        print("Ошибка email")

    input("\nНажми Enter...")


def site_info():
    site = input("Введите сайт: ")

    try:
        ip = socket.gethostbyname(site)

        print("\n========== ИНФО САЙТА ==========")
        print("Домен:", site)
        print("IP:", ip)

        try:
            socket.create_connection((site, 80), timeout=3)
            print("Порт 80: открыт")
        except:
            print("Порт 80: закрыт")

        print("================================")

    except:
        print("Ошибка сайта")

    input("\nНажми Enter...")


while True:

    print("""
================================
        ANGEL KOROL TOOL
================================
1 - Инфо по номеру
2 - Инфо по IP
3 - Инфо по email
4 - Инфо по сайту
5 - Выход
================================
""")

    choice = input("Выбери: ")

    if choice == "1":
        phone_info()

    elif choice == "2":
        ip_info()

    elif choice == "3":
        email_info()

    elif choice == "4":
        site_info()

    elif choice == "5":
        break
