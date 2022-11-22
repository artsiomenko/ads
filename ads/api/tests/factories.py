from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
import factory
import itertools
import random
from main.models import Ad, Rubric


def random_email():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
    all_combos = [''.join(combo) for combo in list(itertools.combinations(letters, 7))]
    return random.sample(all_combos, 1)[0] + '@gmail.com'


class RubricFactory(DjangoModelFactory):
    class Meta:
        model = Rubric

    name = 'Real estate'


class RubricFactory2(DjangoModelFactory):
    class Meta:
        model = Rubric

    name = 'Transport'


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'Angelika'
    email = random_email()
    password = 'SavoskoSasha21'
    first_name = 'Anzhalika'
    last_name = 'Artsiomenka'


class UserFactory2(DjangoModelFactory):
    class Meta:
        model = User

    username = 'User2'
    email = random_email()
    password = 'User2'
    first_name = 'User2'
    last_name = 'User2'


class AdFactory(DjangoModelFactory):
    class Meta:
        model = Ad

    id = 10
    title = 'House_title'
    content = 'House_content'
    price = 50000000
    author = factory.SubFactory(UserFactory)
    rubric = factory.SubFactory(RubricFactory)


class AdFactory2(DjangoModelFactory):
    class Meta:
        model = Ad

    id = 20
    title = 'Car_title'
    content = 'Car_content'
    price = 5
    author = factory.SubFactory(UserFactory2)
    rubric = factory.SubFactory(RubricFactory2)


