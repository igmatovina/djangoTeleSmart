import factory  
import factory.django

Class CustomerFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = Customer

    description = factory.Faker('description')
    