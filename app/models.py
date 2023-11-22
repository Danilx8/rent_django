from django.db import models
from simple_history.models import HistoricalRecords


class Bike(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    brand = models.ForeignKey(
        'Brand',
        models.CASCADE
    )
    type = models.ForeignKey(
        'BikeType',
        models.CASCADE
    )
    frame_size_inches = models.FloatField()
    cost_per_hour = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)

    history = HistoricalRecords

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Велосипед"
        verbose_name_plural = "Велосипеды"


class BikeType(models.Model):
    class MaterialChoice(models.TextChoices):
        ALUMINUM = "Алюминий",
        STEEL = "Сталь",
        CARBON = "Карбон",
        FIBER = "Волокно",
        TITANIUM = "Титан"

    class TireWidthChoice(models.TextChoices):
        NARROW = "Узкая",
        REGULAR = "Стандарт",
        WIDE = "Широкая"
    
    name = models.CharField(max_length=50)
    material = models.TextField(choices=MaterialChoice.choices)
    tire_width = models.TextField(choices=TireWidthChoice.choices)
    segment = models.ForeignKey(
        'Segment',
        models.DO_NOTHING
    )

    history = HistoricalRecords

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип велосипеда"
        verbose_name_plural = "Типы велосипедов"


class Car(models.Model):
    class DriversCategoriesChoice(models.TextChoices):
        A = "A",
        B = "B",
        C = "C",
        D = "D",
        E = "E"

    name = models.CharField(max_length=50)
    mileage_km = models.PositiveIntegerField()
    years_in_use = models.PositiveIntegerField()
    required_category = models.CharField(choices=DriversCategoriesChoice.choices,
                                         max_length=2)
    Brand = models.ForeignKey(
        'Brand',
        models.DO_NOTHING,
        null=True
    )
    horse_powers = models.PositiveIntegerField()
    zero_to_hundred_seconds = models.FloatField()
    trunk_capacity_liters = models.FloatField()
    seats_amount = models.PositiveIntegerField()
    type = models.ForeignKey(
        'CarType',
        models.DO_NOTHING
    )
    cost_per_hour = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)

    history = HistoricalRecords

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class CarType(models.Model):
    class BodyTypeChoice(models.TextChoices):
        THREE = "Трёхобъёмный",
        TWO = "Двухобъёмный",
        ONE = "Однообъёмный"

    class EngineTypeChoice(models.TextChoices):
        PETROL = "Бензиновый",
        DIESEL = "Дизельный",
        ELECTRIC = "Электрический"

    name = models.CharField(max_length=50)
    body_type = models.TextField(choices=BodyTypeChoice.choices)
    engine_type = models.TextField(choices=EngineTypeChoice.choices)
    segment = models.ForeignKey(
        'Segment',
        models.DO_NOTHING
    )

    history = HistoricalRecords

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип автомобиля"
        verbose_name_plural = "Типы автомобилей"


class Brand(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    history = HistoricalRecords

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Segment(models.Model):
    class UserTypeChoice(models.TextChoices):
        INDIVIDUAL = "Физлицо",
        BUSINESS = "Юрлицо"

    name = models.CharField(max_length=50)
    user_type = models.TextField(choices=UserTypeChoice.choices)

    history = HistoricalRecords

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сегмент рынка"
        verbose_name_plural = "Сегменты рынка"
