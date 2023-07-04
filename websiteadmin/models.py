from django.db import models
import uuid


class books(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    Bid=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100,null=True)
    subject=models.CharField(max_length=100,null=True)
    publisher=models.CharField(max_length=100,null=True)
    author=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    
class members (models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    memberid=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return self.name

    
class borrowbooks(models.Model):
    memberid=models.CharField(max_length=200)
    bookid=models.IntegerField()
    contact=models.IntegerField()
    borrowdate=models.DateField()
    returndate=models.DateField()
    

    def __str__(self):
        return self.book
    
class returnbook(models.Model):
    memberid=models.CharField(max_length=200)
    bookBorrow=models.CharField(max_length=100)
    bookid=models.CharField(max_length=10)
    returnDate=models.DateField()
    lateDate=models.IntegerField()
    fine=models.IntegerField()

    def __str__(self):
        return self.bookBorrow


    

    


