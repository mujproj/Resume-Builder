from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .utils import *
from django.core.mail import EmailMessage
import smtplib
# from email.message import EmailMessage
import imghdr
from django.template.loader import get_template

# Create your views here.
def home(request):
    return render(request, 'form.html')

def resume(request):
    if request.method == "POST":

        a = request.POST["fname"]
        c = request.POST["lname"]
        d = request.POST["job-title"]
        e = request.POST["linkden"]
        f = request.POST["Email"]
        g = request.POST["phone"]
        h = request.POST["address"]
        i = request.POST["summary"]
        j = 0
        k = 0
        m = 0
        n = 0
        o = 0
        p = 0
        s = 0
        # j = request.POST["count 1"]
        # k = request.POST["count 2"]
        # l = request.POST["count 3"]
        # m = request.POST["board 1"]
        # n = request.POST["board 2"]
        # o = request.POST["board 3"]
        # p = request.POST["marks 1"]
        q = request.POST["skill1"]
        z = request.POST["skill2"]
        r = request.POST["job1"]
        s = request.POST["jobdescription"]

        # param = {'a': a, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'm': m, 'p': p, 'r': r, 's': s}

        b = request.FILES["image"]
        fs = FileSystemStorage()
        filename = fs.save(b.name, b)
        uploaded_file_url = fs.url(filename)
        template = get_template('index.html')
        context = {'a': a, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'm': m, 'p': p, 'q': q, 'r': r, 's': s, 'uploaded_file_url': uploaded_file_url}
        html = template.render(context)
        pdf = render_to_pdf('index.html', {'a': a, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'm': m, 'p': p, 'q': q, 'r': r, 's': s, 'uploaded_file_url': uploaded_file_url })
        # return render(request, 'index.html', {'a': a, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'm': m, 'p': p, 'q': q, 'r': r, 's': s, 'uploaded_file_url': uploaded_file_url })

        if pdf:
            print("HELLO")
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %(a)
            content = "inline; filename='%s'" %(filename)
            # download = request.GET.get("download", False)
            # print(download)
            # if download:
            #     content = "attachment; filename='%s'" %(filename)
            #     print("HERE")
            # response['Content-Disposition'] = content
            # download = request.get("downl")
            # print(download)
            # if download:
            #     content = "attachment; filename='%s'" %(filename)
            #     print("HHHH")
            response['Content-Disposition'] = content
            # return response

        # Starting email sending
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login('myline.dicksjohn@gmail.com', 'jayGUPTA#1998')
        subject = "HELLO YOUR RESUME IS READY"
        text_content = "HI I AM READY"
        from_email = "myline.dicksjohn@gmail.com"
        to = f
        message = EmailMessage(subject, text_content, from_email, [to])
        message.attach(pdf, a, 'file/pdf')
        message.send()
        # filename = 'pdf'
        # f = open(filename, 'rb')
        # fdata = f.read()
        # fname = pdf
        # file_type = imghdr.what(f.name)
        # msg.add_attachment(fdata, maintype='application', subtype='octet-stream', filename=fname)
        # s.send_message(msg)
        # s.quit()
        return HttpResponse(pdf, content_type='application/pdf')