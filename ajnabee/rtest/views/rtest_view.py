import logging
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ajnabee.rtest.services.rtest_test_recommendations import recommend
from ajnabee.rtest.services.rtest_service import get_all_user_data,get_user_data
from ajnabee.rtest.serializers.rtest_ser import RtestSerializer
import numpy as np

class RtestView(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)



    def get(self, request,pk):
        '''
        :params : pk
        '''
        user_data = get_user_data(pk)
        user_data_recommend = user_data.get_opt()
        print("User Data",user_data.get_opt())
        all_user_data = get_all_user_data()
        print("All data ",all_user_data)
        nrows = len(all_user_data)
        print("Number of rows ",nrows)
        X = np.zeros([nrows,11])
        for i,users in enumerate(all_user_data):
            print("User ",users.get_opt())
            X[i,:] = users.get_opt()
        print(X)
        self.user_ids = recommend(X,X,user_data_recommend,2)
        print("Recommend ",self.user_ids)
        recommended_user_objects = []
        for user in all_user_data:
            if user.user_id in self.user_ids:
                if user.user_id != user_data.user_id:
                    recommended_user_objects.append(user)
        serializer_data = RtestSerializer(instance=recommended_user_objects,many = True).data
        return Response({'data':serializer_data})
        

class RtestAllView(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request):
        '''
        GET all users data
        '''
        all_user_data = get_all_user_data()
        # print(all_user_data)
        serializer_data = RtestSerializer(instance=all_user_data,many=True).data
        return Response({'data':serializer_data})
        