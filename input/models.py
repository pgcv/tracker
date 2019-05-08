from django.db import models

class UserInfo(models.Model):
	company_name = models.CharField(max_length=50)
	username = models.CharField(max_length=30)
	email = models.CharField(max_length=100)
	phone = models.IntegerField()
	password = models.CharField(max_length=50)
	image = models.ImageField(upload_to='profile_image', blank=True, default='unknown.jpg' )

	class Meta:
		db_table="tracker"

    

class File(models.Model):
    name= models.CharField(max_length=500)
    processed=models.IntegerField(default=0)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")


    def __str__(self):
        return self.name + ": " + str(self.filepath)

class OutFile(models.Model):
    name= models.CharField(max_length=500)
    processed=models.IntegerField(default=0)
    filepath= models.FileField(upload_to='outfiles/', null=True, verbose_name="")


    def __str__(self):
        return self.name + ": " + str(self.filepath)        


