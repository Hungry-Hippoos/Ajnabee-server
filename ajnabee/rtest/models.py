from djutil.models import TimeStampedModel
from django.db.models import PositiveIntegerField, CharField, DateTimeField, TextField, BooleanField

class RtestModel(TimeStampedModel):
    user_id = PositiveIntegerField(blank=False, null=False)
    q1_opt = CharField(max_length=200,null=False,blank=False)
    q2_opt = CharField(max_length=200,null=False,blank=False)
    q3_opt = CharField(max_length=200,null=False,blank=False)
    q4_opt = CharField(max_length=200,null=False,blank=False)
    q5_opt = CharField(max_length=200,null=False,blank=False)
    q6_opt = CharField(max_length=200,null=False,blank=False)
    q7_opt = CharField(max_length=200,null=False,blank=False)
    q8_opt = CharField(max_length=200,null=False,blank=False)
    q9_opt = CharField(max_length=200,null=False,blank=False)
    q10_opt = CharField(max_length=200,null=False,blank=False)    


    def __str__(self):
        return "{}".format(self.id)

    def clean(self):
        '''
        find and clean existing entries for user
        '''

    def save(self, *args, **kwargs):
        self.clean()
        super(RtestModel, self).save(*args, **kwargs)
    
    # def __iter__(self):
        # return [ self.user_id, 
        #          self.q1_opt, 
        #          self.q1_opt, 
        #          self.q1_opt, 
        #          self.q1_opt, 
        #          self.q1_opt, 
        #          self.get_rel_to_head_display, 
        #          self.get_disability_display ] 

    # class Meta:
    #     verbose_name_plural = 'User Buffer'
    #     verbose_name = 'User Buffer'