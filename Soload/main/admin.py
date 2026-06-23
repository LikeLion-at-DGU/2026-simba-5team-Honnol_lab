from django.contrib import admin
from .models import Profile, Place, Tag, VisitTime, Purpose, Review, PlaceImage, ReviewImage

admin.site.register(Profile)
admin.site.register(Place)
admin.site.register(PlaceImage)
admin.site.register(Tag)
admin.site.register(VisitTime)
admin.site.register(Purpose)
admin.site.register(Review)
admin.site.register(ReviewImage)
# Register your models here.

