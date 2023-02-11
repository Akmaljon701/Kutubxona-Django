from django.db import models

class Muallif(models.Model):
    JINS = [
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol")
    ]

    ism = models.CharField(max_length=30)
    tugilgan_yil = models.DateField()
    trik = models.BooleanField()
    kitob_soni = models.PositiveSmallIntegerField()
    jinsi = models.CharField(max_length=10, choices=JINS,)

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=30, choices=[
        ("Badiiy", "Badiiy"),
        ("Ilmiy", "Ilmiy"),
        ("Hujjatli", "Hujjatli")
    ])
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    kurs = models.PositiveSmallIntegerField()
    bitruvchi = models.BooleanField()

    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=30)
    ish_vaqti = models.CharField(max_length=30, choices=(
        ("7:00-12:00", "7:00-12:00"),
        ("13:00-18:00", "13:00-18:00"),
    ))

    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qaytargan_sana = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.talaba} - {self.kitob}"
