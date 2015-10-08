from django.db import models



# Order Details
class Orders(models.Model):
    address1 = models.CharField(max_length=50,verbose_name="Address 1",null=True,blank=True)
    address2 = models.CharField(max_length=50,verbose_name="Address 2",null=True,blank=True)
    city = models.CharField(max_length=50,verbose_name="City",null=True,blank=True)
    mobile = models.CharField(max_length=50,verbose_name="Mobile",null=True,blank=True)
    order_time = models.DateTimeField(auto_now_add=True,verbose_name="Order Time")
    amount = models.FloatField(verbose_name="Amount",null=True,blank=True)
    latitude = models.FloatField(verbose_name="Latitude",null=True,blank=True)
    longitude = models.FloatField(verbose_name="Longitude",null=True,blank=True)


    def __unicode__(self):
        return str(self.id)+ "-"+self.mobile

    class Meta:
        verbose_name = ("Orders")
        verbose_name_plural = ("Orders")

