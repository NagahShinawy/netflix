from django.contrib import admin

from .models import Video, VideoProxy, Vehicle, Airplane, MotorBike, Car, Honda, BMW


@admin.register(Video)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ("id", "video_id", "title", "slug")
    list_display_links = ("id", "video_id", "title")
    list_per_page = 5


admin.site.register(VideoProxy)


@admin.register(Vehicle)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "manufacturer")  # [Vehicle]


@admin.register(Airplane)
class AirplaneModelAdmin(admin.ModelAdmin):
    list_display = ("id", "vehicle_ptr_id", "model", "manufacturer")  # comes from parent class [Vehicle]
    list_display += ("is_cargo", "is_passenger")  # comes from child class [Airplane]


@admin.register(MotorBike)
class MotorBikeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "vehicle_ptr_id", "model", "manufacturer")  # comes from parent class [Vehicle]
    list_display += ("fuel",)  # comes from child class [MotorBike]


# @admin.register(Car)
# class CarModelAdmin(admin.ModelAdmin):
#     list_display = ("id", "vin", "model", "manufacturer", "year")  # comes from parent class [Car]


# @admin.register(Honda)
# class HondaModelAdmin(admin.ModelAdmin):
#     list_display = ("id", "manufacturer", "year")  # comes from parent class [Car]


admin.site.register(Car)
admin.site.register(Honda)
admin.site.register(BMW)