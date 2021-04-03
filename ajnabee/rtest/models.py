from djutil.models import TimeStampedModel
from django.db.models import PositiveIntegerField, CharField, DateTimeField, TextField, BooleanField
import numpy as np

# RtestModel.objects.create(user_id = 3,q1_opt="3",q2_opt="2",q3_opt="3",q4_opt="6",q5_opt="1",q6_opt="2",q7_opt="4",q8_opt="4",q9_opt="4",q10_opt="3")

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

    def get_opt(self):
       return np.array([self.user_id,self.q1_opt , self.q2_opt , self.q3_opt , self.q4_opt , self.q5_opt,
         self.q1_opt, self.q2_opt, self.q3_opt, self.q4_opt, self.q5_opt ])

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