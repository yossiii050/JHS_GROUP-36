from django.test import TestCase


from jobs.models import Upload

class UploadTest(TestCase):
    def setUp(self):
        Upload.objects.create(title="test1",body="JHSJHSJHSJHSJHSJHSHS")
        Upload.objects.create(title="test2",body="abcdefghi")
        Upload.objects.create(title="test3",body="asdfghjkl;poijhgfdsfghj")

    def values(self):
        Upload.objects.create(hybrid=True,time="part time")
        Upload.objects.create(hybrid=False,time="full time")
        Upload.objects.create(hybrid=True,time="shifts")


# Create your tests here.
