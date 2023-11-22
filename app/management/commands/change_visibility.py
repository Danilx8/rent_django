from django.core.management import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from app.models import Bike, Car


class Command(BaseCommand):
    help = "Changes listed vehicles' visibility to False (0) or True(any). Value comes first, next - vehicles."

    def add_arguments(self, parser):
        parser.add_argument('value',
                            metavar='visibility option to apply to vehicles',
                            type=int,
                            help='pick a value: 0 - False, any other number - True')
        parser.add_argument('vehicles',
                            type=int,
                            nargs='+',
                            help="list vehicles' ids to apply the visibility options")
        parser.add_argument('-b',
                            '--bikes',
                            action='store_true',
                            default=False,
                            help="specifies vehicles' ids to be bikes' ones"
                            )
        parser.add_argument('-c',
                            '--cars',
                            action='store_true',
                            default=False,
                            help="specifies vehicles' ids to be cars' ones"
                            )

    def handle(self, *args, **options):
        if options['bikes'] == options['cars']:
            raise CommandError('you chose flags wrong')

        availability = bool(options['value'])
        with transaction.atomic():
            if options['bikes']:
                for bike_id in options['vehicles']:
                    try:
                        bike = Bike.objects.get(pk=bike_id)
                        bike.is_available = availability
                        bike.save()
                    except ObjectDoesNotExist:
                        raise CommandError('bike with id: {0} does not exist'.format(bike_id))
            else:
                for car_id in options['vehicles']:
                    try:
                        car = Car.objects.get(pk=car_id)
                        car.is_available = availability
                        car.save()
                    except ObjectDoesNotExist:
                        raise CommandError('car with id {0} does not exist'.format(car_id))
