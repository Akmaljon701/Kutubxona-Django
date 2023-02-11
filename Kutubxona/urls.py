
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bosh_sahifa),

    path('mualliflar/', hamma_mualliflar),
    path('kitoblar/', hamma_kitoblar),
    path('recordlar/', hamma_recordlar),
    path('adminlar/', hamma_adminlar),
    path('talabalar/', hamma_talabalar),

    path('muallif/<int:son>/', bitta_muallif),
    path('kitob/<int:son>/', bitta_kitob),
    path('record/<int:son>/', bitta_record),
    path('talaba/<int:son>/', bitta_talaba),
    path('one_admin/<int:son>/', bitta_admin),


    path('muallif_ochrish/<int:son>/', muallif_ochrish),
    path('kitob_ochrish/<int:son>/', kitob_ochirish),
    path('record_ochrish/<int:son>/', record_ochrish),
    path('talaba_ochrish/<int:son>/', talaba_ochrish),
    path('admin_ochrish/<int:son>/', admin_ochrish),


]
