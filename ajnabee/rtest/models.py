from djutil.models import TimeStampedModel
from django.db.models import PositiveIntegerField, CharField, DateTimeField, TextField, BooleanField

class RtestModel(TimeStampedModel):
    user_id = CharField(blank=False, null=False)
    q1_opt = CharField(null=False,blank=False)
    q2_opt = CharField(null=False,blank=False)
    q3_opt = CharField(null=False,blank=False)
    q4_opt = CharField(null=False,blank=False)
    q5_opt = CharField(null=False,blank=False)
    q6_opt = CharField(null=False,blank=False)
    q7_opt = CharField(null=False,blank=False)
    q8_opt = CharField(null=False,blank=False)
    q9_opt = CharField(null=False,blank=False)
    q10_opt = CharField(null=False,blank=False)    


    def __str__(self):
        return "{}".format(self.id)

    def clean(self):
        '''
        find and clean existing entries for user
        '''

    def save(self, *args, **kwargs):
        self.clean()
        super(UserBuffer, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'User Buffer'
        verbose_name = 'User Buffer'