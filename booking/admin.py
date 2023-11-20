from django.contrib import admin
from .models import Author, Post, UserProfile
# from .models import ExtraFeatures, Booking

# Register your models here.
# admin.register(ExtraFeatures)
# admin.register(Booking)

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(UserProfile)



