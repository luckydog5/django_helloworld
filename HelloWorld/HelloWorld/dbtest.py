"""
database operation,test1 is a object defined by models.py
"""    
from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
    test1=Test(name='runoob')
    test1.save()
    test2=Test(name='Lucky')
    test2.save()
    test3=Test(name='lucy')
    test3.save()
    response=""
    response1=""
    list=Test.objects.all()
    response2=Test.objects.filter(id=1) # filter can be seen as WHERE
    response3=Test.objects.get(id=1) # get single object
    Test.objects.order_by('name')[0:2]
    Test.objects.order_by("id")
    Test.objects.filter(name="runoob").order_by("id")
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
    #return HttpResponse("<p>It works!</p>")

