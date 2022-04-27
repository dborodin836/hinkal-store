from random import choice, randint

from backend.goods.models import Dish
from backend.user.models import Customer, Vendor
from backend.contact.models import Contact

CUSTOMERS_NAME_SAMPLES = (
    'Joe',
    'Jack',
    'Arnold',
    'Alexander',
    'Vladick',
    'Beth',
    'Marta',
    'Bein',
    'Will',
    'Jared',
    'Vladimir',
    'Tony',
    'Julia',
    'Ann',
    'Dan',
    'Dane',
    'Emma',
    'Emanuel',
    'Marcello',
    'Mark',
    'Oliver',
)

CUSTOMERS_SURNAME_SAMPLES = (
    'Putin',
    'Beep-Boop',
    'Smith',
    'Leto',
    'Stark',
    'Zinich',
    'Bilik',
    'Schwarzenegger',
    'Macron',
    'Lutz',
    'Pelme',
    'Okken',
    'Kreken',
    'Cramer',
    'Tolkien',
    'Williams',
    'Allen',
    'Mayer',
    'Muller',
    'Scott',
)

COMPANY_NAME_SAMPLES = (
    'Mann Co.',
    'MegaHard',
    'Gunix',
    'Stream',
    'Picassa',
)


def _get_username(full_name: str) -> str:
    plain_name = ''.join(full_name.split())
    return plain_name[randint(6, len(plain_name))] + '_' + str(randint(1000, 9999))


# Creating customers
def create_customers(amount: int = 30,
                     customer_names=None, customer_surnames=None, static_password=None) -> None:

    names = customer_names or CUSTOMERS_NAME_SAMPLES
    surnames = customer_surnames or CUSTOMERS_SURNAME_SAMPLES
    password = static_password or 'customerpass'

    for _ in range(amount):
        name = choice(names)
        last_name = choice(surnames)
        full_name = name + ' ' + last_name
        username = _get_username(full_name)
        try:
            Customer.objects.create(username=username, password=password, first_name=name, last_name=last_name)
            print(f'User "{username}" created successfully!')
        except Exception as e:
            print(e)


def populate_db_f() -> None:
    create_customers()


if __name__ == '__main__':
    populate_db_f()

