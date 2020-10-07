from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.DateField(blank=True)
    specialite = models.CharField(max_length=100,blank=True)
    language = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return ' {}'.format(self.user.first_name)




class Stimul_slov(models.Model):
    stimulus = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return "%s" % ( self.stimulus)

class Otvet(models.Model):  
  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, db_column="user")
    answer = models.CharField(max_length=200, blank=True)
    stimul = models.ForeignKey(Stimul_slov, on_delete=models.CASCADE)
    def __str__(self):
        return  "%s: %s ----> %s " % (self.user, self.stimul, self.answer, )




class Answer(models.Model):
    ans = models.CharField(max_length=200, blank=True)
    stimul = models.ForeignKey(Stimul_slov, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    