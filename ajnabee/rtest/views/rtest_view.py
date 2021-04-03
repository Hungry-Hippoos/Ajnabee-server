import logging
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ajnabee.rtest.services.rtest_service import get_all_user_data,get_user_data
from ajnabee.rtest.serializers.rtest_ser import RtestSerializer

class RtestView(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request,pk):
        '''
        :params : pk
        '''
        user_data = get_user_data(pk)
        all_user_data = get_all_user_data()
        serializer_data = RtestSerializer(instance=user_data).data
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
        serializer_data = RtestSerializer(instance=user_data,many=True).data
        return Response({'data':serializer_data})
        