from django.shortcuts import render,redirect
from django.http import HttpResponse
from. models import books,borrowbooks,returnbook,members
from django.db.models import Max
from .form import UpdateMembersForm
from .form import UpdateBooks

def home(request):
    return render(request,'home.html')

def addbook(request):
    if request.method=="POST":
        bookidCount=books.objects.count()
        Bid='SSBID'+str(bookidCount+1)
        name=request.POST["bookname"]
        title=request.POST["title"]
        subject=request.POST['subject']
        publisher=request.POST['publisher']
        author=request.POST['author']
       
        # form=addbookform(request.POST or None)
        if name or title or subject or publisher or author != "":
            print("valid form")
            newBook=books(Bid=Bid,name=name,title=title,subject=subject,publisher=publisher,author=author)
            newBook.save()

        

    return render(request,'Addbook.html',locals())

def addmember(request):
    if request.method=="POST":
        idcount=members.objects.count()
        memberid='SSBSMEMID'+str(idcount+1) 
        name=request.POST["fname"]
        contact=request.POST["contact"]
        mail=request.POST["email"]
       

        newMember=members(memberid=memberid,name=name,contact=contact,email=mail)
        newMember.save()


    return render(request,'Addmember.html',locals())

def borrwdetails(request):
    if request.method=="POST":
        userID=request.POST["Uid"]
        bookID=request.POST["Bid"]
        contact=request.POST["contact"]
        borDate=request.POST["borDate"]
        rdate=request.POST["Rdate"]
       
        newborrowbooks=borrowbooks(memberid=userID,bookid=bookID,contact=contact,borrowdate=borDate,returndate=rdate)
        newborrowbooks.save()
    return render(request,'BorrwDetails.html')

def returnbooks(request):
    if request.method=="POST":
        memID=request.POST["mid"]
        Bid=request.POST["Bid"]
        retDate=request.POST["retDate"]
        lateDate=request.POST["lateDate"]
        fine=request.POST['fine']

        newReturnBooks=returnbook(memberid=memID,bookid=Bid,returnDate=retDate,lateDate=lateDate,fine=fine)
        newReturnBooks.save()

        borrwdata=borrowbooks.objects.all()
        retdata=returnbook.objects.all()

        for Rdata in retdata:
            for Bdata in borrwdata:
                if Rdata.memberid == Bdata.memberid:
                    retbook=borrowbooks.objects.filter(memberid=Rdata.memberid).delete()
    return render(request,'Return.html')

def reportdata(request):
    datareport=borrowbooks.objects.all()
    allbooks=books.objects.count()
    allmembers=members.objects.count()
    allbookborrow=borrowbooks.objects.count()
    return render(request,'Reports.html',{'database':datareport,'allbooks':allbooks,'allmembers':allmembers,'allbookborrow':allbookborrow})

    # return render(request,'Reports.html')


def ViewAllbooks(request):

    allbooks=books.objects.all()
    return render(request,'Allbooks.html',{'allbooks':allbooks})
    


def ViewAllmembers(request):     
    allmembers=members.objects.all()
    return render(request,'Allmembers.html',{'allmembers':allmembers})
        
def Memberlist(request):
    Memberlist=members.objects.all()
    
    return render(request,'Memberlist.html',{'Memberlist':Memberlist})

def ViewAllbookborrws(request):
    allbookborrws=borrowbooks.objects.all()
    return render(request,'Allbookborrws.html',{'allbookborrows':allbookborrws})

def updateMembers(request, pid):
    member = members.objects.get(id=pid)
    form = UpdateMembersForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect('ViewAllmembers') 
    return render(request, 'Updatemember.html', {'form': form})



def deleteMember(request,pid):
    member=members.objects.get(id=pid)
    member.delete()
    return redirect ('ViewAllmembers')

def updatebooks(request,pid):
    book=books.objects.get(id=pid)
    form=UpdateBooks(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('ViewAllbooks')
    return render(request,'UpdateBooks.html',{'form':form})

def deletebooks(request,pid):
    book=books.objects.get(id=pid)
    book.delete()
    return redirect('ViewAllbooks')
    

    


