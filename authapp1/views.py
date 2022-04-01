from django.shortcuts import render
from authapp1.models import finance
import json

# Create your views here

def uploadfiledata(request):
    filedata = request.POST.get('uploadTextValue')
    fd = '''{"fd":'''
    fd.join(filedata)
    fd.join('''}''')

    filedata_obj = json.loads(filedata)
    for eachelement in filedata_obj:
        try:
            obj = finance.objects.get(Id=eachelement["id"], UserId=eachelement["userId"])
            print('data already existed with given user Id')
            obj.save()
            abc= finance.objects.all()

            return render(request,'show.html',{'abc':abc})
        except finance.DoesNotExist:
         rec = finance.objects.create(Id=eachelement["id"], UserId=eachelement["userId"], title=eachelement["title"],
                                   body=eachelement["body"])
         print('Data Table Inserted')
         rec.save()

    recs = finance.objects.all()
    return render(request,'show.html',{"recs":recs})