from django.shortcuts import render,redirect
from .models import db
from .models import assign
# Create your views here.
#function created to call other pages(switching to other pages) for that we use urls.py
'''
def asd(request):
	print("arul")
	return render(request,'py.html')
'''

def zxc(request):
	if request.method=="POST":
		obj=db()
		obj.Mname=request.POST['name']
		obj.Mphno=request.POST['phno']
		obj.Mprof=request.POST['desig']
		obj.Mpassword=request.POST['pswd']
		obj.Memail=request.POST['emailid']
		obj.save()
		return render(request,'formpage.html')
	return render(request,'py.html')	

def loginform(request):
	try:
		if request.session['user_session']!="logout":
			return redirect("/dashboard")
		else:
			raise Exception()
	except:
		return render(request,'formpage.html')
	return render(request,'formpage.html')

def dashBoard(request):
	try:
		if request.session['user_session']!="logout":
			if request.method=="POST":
				ob=assign()
				ob.Topic=request.POST["topic"]
				ob.Assignment=request.POST["assign"]
				ob.save()
				return render(request,'dashBoard.html',{'session':request.session['user_session']})

			obj=assign.objects.all()
			obj2=db.objects.filter(id=request.session['Id'])
			print(obj)
			return render(request,'dashBoard.html',{'session':request.session['user_session'],'teach':obj,'acc':obj2})
		else:
			raise Exception()

		return render(request,'dashBoard.html',{'session':request.session['user_session']})
	except:
		if request.method=="POST":
			try:
				obj=db.objects.get(Mphno__exact=request.POST['phno'],Mpassword__exact=request.POST['pswd'])
				request.session['user_session']=obj.Mname
				request.session['Id']=obj.id
				return render(request,'dashBoard.html')
			except:
				return render(request,'formpage.html')
		return render(request,'formpage.html')




def data(request):
	obj=db.objects.filter(id=request.session['Id'])
	return render(request,'data.html',{'user':obj})


def logout(request):
	try:
		del request.session['user_session']
		request.session['user_session']="logout"
	except KeyError:
		pass
	return redirect("/home")

def Home(request):
	try:
		if request.session['user_session']!="logout":
			return render(request,'home.html',{'session':request.session['user_session']})
		else:
			raise Exception()
	except:
		return render(request,'home.html')
	return render(request,'home.html')

def updateData(request):
	if request.method=="POST":
		ob=db.objects.get(id=request.session['Id'])
		if request.POST['name']==ob.Mname:
			pass
		else:
			ob.Mname=request.POST['name']

		if request.POST['email']==ob.Memail:
			pass
		else:
			ob.Memail=request.POST['email']

		if request.POST['PhNo']==ob.Mphno:
			pass
		else:
			ob.Mphno=request.POST['PhNo']
		ob.save()

	return redirect("./data")


