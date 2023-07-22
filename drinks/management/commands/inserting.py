from django.core.management.base import BaseCommand
from drinks.models import Article,Categories  # Replace 'myapp' with your app name
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Inserts 100 fake records into the Article model'

    def handle(self, *args, **options):
        fake = Faker()
        categories = Categories.objects.all()  # Replace 'Categories' with your actual model for categories

        for _ in range(100):
            article = Article(
                model=fake.word(),
                brand=fake.company(),
                description=fake.paragraph(nb_sentences=5, variable_nb_sentences=True),
                price=str(random.randint(10, 1000)),  # Assuming the price is a string
                url=fake.url(),
                category=random.choice(categories),
            )
            article.save()

        self.stdout.write(self.style.SUCCESS('Successfully inserted 100 fake records into the Article model.'))

    