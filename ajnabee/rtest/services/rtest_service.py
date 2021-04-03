from ajnabee.rtest.models import RtestModel

def get_all_user_data():
    all_user_data = RtestModel.objects.all()
    return all_user_data

def get_user_data(pk):
    all_user_data = RtestModel.objects.get(user_id=pk)
    return all_user_data