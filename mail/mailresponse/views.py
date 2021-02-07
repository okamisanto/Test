from django.shortcuts import render
from django.core.mail import send_mail
from mail.settings import EMAIL_HOST_USER

# Create your views here.
def Home(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(
			'ถึง คุณ ' + message_name, #หัวเรื่อง
			'อยากได้งาน อยากได้งาน อยากได้งาน อยากได้งาน อยากได้งาน ', # ข้อความที่จะแสดง
			EMAIL_HOST_USER, # from email
			[message_email] # to email
			)

		return render(request,'conEmail.html',{'message_name':message_name})
	else:
		return render(request,'home.html')
