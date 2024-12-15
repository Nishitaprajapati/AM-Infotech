import datetime

import pypdf
from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import User, Area, Product, Cart, Compliant, Complaints, connectus, Cartfinal, Feedback,Inquery,Order,Category,Offer,order_details
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages



# Create your views here.
def index(request):
    subid = 1
    subid2 = 2
    subid3 = 3
    subid4 = 4
    subid5 = 5
    subid6 = 6
    subid7 = 7
    subid8 = 8
    subid9 = 9
    subid10 = 10



    user = Product.objects.filter(sub_category_id=subid)
    user2 = Product.objects.filter(sub_category_id=subid2)
    user3 = Product.objects.filter(sub_category_id=subid3)
    user4 = Product.objects.filter(sub_category_id=subid4)
    user5 = Product.objects.filter(sub_category_id=subid5)
    user6 = Product.objects.filter(sub_category_id=subid6)
    user7 = Product.objects.filter(sub_category_id=subid7)
    user8 = Product.objects.filter(sub_category_id=subid8)
    user9 = Product.objects.filter(sub_category_id=subid9)
    user10 = Product.objects.filter(sub_category_id=subid10)

    context = {
        'data1': user,
        'data2': user2,
        'data3': user3,
        'data4': user4,
        'data5': user5,
        'data6': user6,
        'data7': user7,
        'data8': user8,
        'data9': user9,
        'data10': user10,


    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def chekout(request):
    if request.session.get('log_id') is not None:
        id2 = request.session['log_id']
        print(id2)
        fetchcartdata = Cart.objects.filter(user_id=id2, product_status=1)
        print(fetchcartdata)
        carttotal = Cart.objects.filter(user_id=id2, product_status=1).aggregate(Sum('totalprice'))
        print(carttotal)
        fetchpid = Cart.objects.filter(user_id=id2, product_status=1).values('product_id')
        print(fetchpid)
        print(fetchcartdata)
        fetchproductdata = Product.objects.filter(id__in=fetchpid)
        print(fetchproductdata)

        userdetails = User.objects.get(id=id2)
        context = {
            'cart': fetchcartdata,
            'product': fetchproductdata,
            'user': userdetails,
            'carttotal': carttotal
        }
        return render(request, 'checkout.html', context)
    else:
        return redirect(loginform)



def placeorder(request,id):
    id2 = request.session['log_id']
    amount = float(id)
    if request.method=='POST':
        addre=request.POST.get("address1")
    orderquery = Order(Pay_amount=amount,Payment_status='offline',cgst=1.0,sgst=1.0,is_order_cancel='no',user_id=User(id=id2),address=addre)
    orderquery.save()
    lastid = Order.objects.latest('id').pk
    fetchcartdata = Cart.objects.filter(user_id=id2, product_status=1)
    for ob in fetchcartdata:
         ob.product_status = 0
         ob.orderid = lastid
         ob.save()
    oj=Cart.objects.filter(orderid=lastid)
    for item in oj:
        orderdetails1 = order_details(product_id=item.product_id,order_id=Order(id=lastid),price=item.totalprice,quantity=item.quantity,user_id=User(id=id2))
        orderdetails1.save()
    context={
        'tamount':amount,
        'lastid':lastid
    }
    return render(request,'payment.html',context)

def cancelorder(request,id):
    query = Order.objects.get(id=id)
    query.delete()
    return redirect(orders)




def orderdetails(request,id):

    id2 = request.session['log_id']
    fetchcartdata=Cart.objects.filter(orderid=id)
    carttotal=Cart.objects.filter(orderid=id).aggregate(Sum('totalprice'))
    fatchpid=Cart.objects.filter(orderid=id).values('product_id')
    fetchproductdata=Product.objects.filter(id__in=fatchpid)
    userdetails=User.objects.get(id=id2)
    o=Order.objects.filter(id=id)
    print(fetchcartdata)
    print(carttotal)
    print(fetchproductdata)
    print(userdetails)
    context={
        'cart':fetchcartdata,
        'product':fetchproductdata,
        'user':userdetails,
        'carttotal':carttotal,
        'orderid':id,
        'orderdata':o

    }
    return render(request,'orderdetails.html',context)
def contact(request):
    return render(request, 'contact.html')


def faqs(request):
    return render(request, 'faqs.html')


def help(request):
    return render(request, 'help.html')


def payment(request):
    return render(request, 'payment.html')


def privacy(request):
    return render(request, 'privacy.html')


def product(request):
    subid11 = 11
    user11 = Product.objects.filter(sub_category_id=subid11)

    context = {
        'data11': user11
    }
    return render(request, 'product.html', context)


def product2(request):
    return render(request, 'product2.html')

def single(request):
    return redirect(singleproduct)


def singlee(request):
    return render(request, 'single2.html')


def miband(request):
    return render(request, 'miband.html')


def termas(request):
    return render(request, 'terms.html')


def mi4tv(request):
    return render(request, 'mi4tv.html')


def logout(request):
    try:
        del request.session['log_user']
        del request.session['log_name']
        del request.session['log_id']
    except:
        pass

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("Email")
        contact = request.POST.get("contact")
        address = request.POST.get("area")
        zender = request.POST.get("ze")
        password = request.POST.get("Password")
        confirmpassword = request.POST.get("ConfirmPassword")

        try:
            user = User.objects.get(Email_id=email)
        except:
            user = None



        if user is not None:

            return render(request, 'index.html')
        else:
            error = ""
            if len(password) < 8:
                error = "not"
                x = 0
        if len(contact) == 10:
            for i in contact:
                if '9' >= i >= '0':
                    if contact[0] == " 6 " or contact[0] == "7" or contact[0] == "8" or contact[0] == "9":
                        pass
                    else:
                        error = "not"
                        break
        else:
            error = "not"
            messages.error(request,"password is not valid")

        if not error:
            query = User(First_name=fname, Last_name=lname, Email_id=email, Contact_number=contact, Password=password,
                         Address=address,cpassword=confirmpassword, Gender=zender, area=Area(id=1))
            query.save()
            return render(request, 'contact.html')
        else:
            return render(request, 'index.html')
    return render(request, 'index.html')


def login(request):
    return render(request, 'index.html')


def logincheck(request):
    if request.method == "POST":
        email = request.POST.get("uemail")
        password = request.POST.get("upass")

        if len(password) < 8:
            error = "not"
            return render(request, 'index.html')
        else:
            try:
                user = User.objects.get(Email_id=email, Password=password)
                request.session['log_user'] = user.Email_id
                request.session['log_id'] = user.id
                request.session['log_name'] = user.First_name
                request.session.save()
            except:
                user = None

        if user is not None:
            return render(request, 'contact.html')
        else:

            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def product3(request):
    subid12 = 12

    user12 = Product.objects.filter(sub_category_id=subid12)

    context = {
        'data12': user12
    }
    return render(request, 'product3.html', context)


def tabandwatch(request):
    subid13 = 13

    user13 = Product.objects.filter(sub_category_id=subid13)

    context = {
        'data13': user13
    }
    return render(request, 'tabandwatch.html', context)


def pro(request):
    subid14 = 14

    user14 = Product.objects.filter(sub_category_id=subid14)

    context = {
        'data14': user14
    }

    return render(request, 'lep.html', context)


def tv(reqest):
    subid15 = 15
    subid16 = 16
    user15 = Product.objects.filter(sub_category_id=subid15)
    user16 = Product.objects.filter(sub_category_id=subid16)

    context = {
        'data15': user15,
        'data16': user16
    }
    return render(reqest, 'tv.html', context)


def lg32inch(request):
    return render(request, 'lg32inch.html')


def complaint(request):
    return render(request, "complaints.html")


def com(request):
    if request.method == 'POST':
        com_details = request.POST.get("com")
        user1=request.POST.get("user")
        query = Complaints(compliant_details=com_details,user_id=User(user1))
        query.save()

    return render(request, "complaints.html")


def connect(request):
    if request.method == 'POST':
        name = request.POST.get("uname")
        email = request.POST.get("uemail")
        subject = request.POST.get("usubject")
        details = request.POST.get("details")

        query = connectus(name=name, email=email, subject_here=subject, details=details)
        query.save()

    return render(request, 'contact.html')


def ac(request):
    subid17 = 17
    subid18 = 18
    subid19 = 19
    subid22 = 22

    user17 = Product.objects.filter(sub_category_id=subid17)
    user18 = Product.objects.filter(sub_category_id=subid18)
    user19 = Product.objects.filter(sub_category_id=subid19)
    user22 = Product.objects.filter(sub_category_id=subid22)

    context = {
        'data17': user17,
        'data18': user18,
        'data19': user19,
        'data22': user22
    }

    return render(request, 'ac.html', context)


def destroycart(request,id):
    query = Cart.objects.get(id=id)
    query.delete()
    return redirect(chekout)


def registerrr(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("Email")
        contact = request.POST.get("contact")
        address = request.POST.get("area")

        password = request.POST.get("Password")
        confirmpassword = request.POST.get("ConfirmPassword")
        userimg=request.POST.get("pimage")
        question=request.POST.get("que-names")
        answer=request.POST.get("ans")

        try:
            user = User.objects.get(Email_id=email)
            messages.error(request,'Please Enter different Emailid!')
        except:
            user = None

        if user is not None:

            return render(request, 'register.html')
        else:
            error = ""
            if len(password) < 8:
                error = "not"
                x = 0
        if len(contact)==10:
            for i in contact:
                if '9' >= i >= '0':
                    if contact[0] == " 6 " or contact[0] == "7" or contact[0] == "8" or contact[0] == "9" or contact[0] == "1":
                        pass
                    else:
                        error = "not"

                        break
        else:
            messages.error(request, "Contact Number is not correct")
            error = "not"

        if not error:
            if  password==confirmpassword:
                query = User(First_name=fname, Last_name=lname, Email_id=email, Contact_number=contact,
                             Password=password, Address=address, cpassword=confirmpassword, area=Area(id=1),
                             image2=userimg, Security_Que=question, Security_Answer=answer)
                query.save()
                messages.success(request, "SUCCESSFULLY REGISTER")
                return render(request, 'login.html')
            else:
                messages.error(request,"password is not same")
        else:
            messages.error(request,'MAKE CORRECT DETAILS')
            return render(request, 'register.html')
    return render(request, 'register.html')


def finallogin(request):
    return render(request, 'login.html')


def loginform(request):
    if request.method == "POST":
        email = request.POST.get("uemail")
        password = request.POST.get("upass")

        if len(password) < 8:
            error = "not"
            messages.error(request, " PLEASE ENTER A CORRECT PASSWORD  ")
            return render(request, 'login.html')
        else:
            try:
                user = User.objects.get(Email_id=email, Password=password)
                request.session['log_user'] = user.Email_id
                request.session['log_id'] = user.id
                request.session['log_name'] = user.First_name
                request.session['log_name'] = user.First_name
                request.session['log_name'] = user.First_name
            except:
                user = None

        if user is not None:
            return redirect(index)
        else:
            messages.error(request, " MAKE A CORRECT DETAILS.......")
            return render(request, 'login.html')

    return render(request, 'login.html')


def singleproduct(request,id):
    query = Product.objects.get(id=id)
    feed1=Feedback.objects.all()
    id2=Offer.objects.get(product_id=id)
    offer1=Offer.objects.get(id=id2)



    context = {
        'singleproduct': query,
        'feed_data':feed1,
        'offerdata':offer1
    }


    return render(request, "single.html", context)


def addtocart(request, id):
   if request.session.get('log_id')is not None:
       id2 = request.session['log_id']
       price = request.POST.get("price")
       quantity = request.POST.get("quant[1]")
       pid = request.POST.get("proid")
       print(pid)
       price = int(price)
       quantity = int(quantity)
       totalpricee = price * quantity

       try:
           checkquery = Cart.objects.get(product_id=pid, product_status=1, user_id=id2)
       except:
           checkquery = None

       print(checkquery)
       if checkquery is not None:
           checkquery.quantity = checkquery.quantity + quantity
           checkquery.totalprice = checkquery.totalprice + totalpricee
           checkquery.save()
       else:
           cartquery = Cart(product_id=Product(id=id), quantity=quantity, product_status=1, user_id=User(id=id2),
                            orderid=0, totalprice=totalpricee)
           cartquery.save()
       return redirect(index)
   else:
       return redirect(loginform)

def profile(request):
    if request.session.get('log_id') is not None:
        id = request.session['log_id']
        print(id)
        user2 = User.objects.filter(id=id)
        context = {
            'data1': user2
        }
        return render(request, 'profile.html', context)
    else:
        return redirect(loginform)






def update(request,id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("contact")
        error = ""
        getuser = User.objects.get(id=id)
        getuser.First_name = name
        getuser.Email_id = email
        getuser.Contact_number = phone
        getuser.save()
        messages.success(request, 'UPDATE SUCCEFULLY ')
        return redirect('login')
    else:
        return render(request,'login.html')



     #  if len(phone) == 10:
      #      for i in phone:
      #          if '9' >= i >= '0':
       #             if phone[0] == " 6 " or phone[0] == "7" or phone[0] == "8" or phone[0] == "9":
        #                pass
         #           else:
          #              error = "not"
           #             messages.error(request, "contact number is not valid")
            #            break
             #   else:
              #      error = "not"
               #     messages.error(request, "phone number is not valid")
                #    break

            #else:
             #   error = "not"
              #  messages.error(request, "phone number contains only digit")

            #if not error:








def feedbackview(request):
    if request.session.get('log_id') is not None:
        if request.method == 'POST':
            fdata = request.POST.get("fdata")
            pid = request.POST.get("pro_id")
            uid = request.POST.get("user_id")
        fquery = Feedback(feedback=fdata, product_id=Product(id=pid), user_id=User(id=uid))
        fquery.save()
        feed1 = Feedback.objects.filter(product_id=pid,)
        context = {
            'feed_data': feed1
        }
        return redirect('singleproduct', pid)
    else:
        return redirect(loginform)


def inquery(request):
    if request.method == 'POST':
        inq_details= request.POST.get("inq")
        id2 = request.POST.get("user_id")
        query = Inquery(inquery_description=inq_details,user_id=User(id=id2))
        query.save()

    id3 = request.session['log_id']
    responce=Inquery.objects.filter(user_id=id3)

    context={
        'data1':responce
    }

    return render(request,'inquiry.html',context)

def orders(request):
    id = request.session['log_id']
    orderdata=Order.objects.filter(user_id=id)


    context={
        'o1':orderdata
    }
    return render(request,'order.html',context)

def re(request):
    return  render(request,'re.html')

def reportstock(request):
    return render(request,'report.html')

def reportcategory(request):
    return render(request,'reportcategory.html')

def reportinquery(request):
    return  render(request,'reportinquery.html')

def reportfeedback(request):
    return render(request,'reportfeedback.html')

def reportorder(request):
    return render(request,'orderreport.html')

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template


from xhtml2pdf import pisa

def stockreport(request,id):
  if id==1:
     template = get_template('report.html')
     product = Product.objects.all()
     context = {
         'productdata': product
     }
     html = template.render(context)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
          return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None

  if id==2:
      template = get_template('reportcategory.html')
      cate = Category.objects.all()
      context = {
         'category': cate
      }
      html = template.render(context)
      result = BytesIO()
      pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
      if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
      return None

  if id==3:
      template = get_template('reportinquery.html')
      cate = Inquery.objects.all()
      context = {
          'inquery': cate
      }
      html = template.render(context)
      result = BytesIO()
      pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
      if not pdf.err:
          return HttpResponse(result.getvalue(), content_type='application/pdf')
      return None
  if id == 4:
      template = get_template('reportfeedback.html')
      feedback = Feedback.objects.all()
      context = {
          'feedbackdata': feedback
      }
      html = template.render(context)
      result = BytesIO()
      pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
      if not pdf.err:
          return HttpResponse(result.getvalue(), content_type='application/pdf')
      return None
  if id == 5:
      template = get_template('orderreport.html')
      feedback = Order.objects.all()
      context = {
          'orderdata': feedback
      }
      html = template.render(context)
      result = BytesIO()
      pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
      if not pdf.err:
          return HttpResponse(result.getvalue(), content_type='application/pdf')
      return None

  return render(request,'r.html')


def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST['email']
       # try:
           # if request.session.get('log_id') is not None:
              #  user = User.objects.get(Email_id=username)
              #  request.session['log_user'] = user.Email_id
             #   request.session['log_id'] = user.id
              #  request.session.save()
          #  else:
             #   username=username
            # print(user.dp)
      #  except  .DoesNotExist:
           # user = None
        #if user exist then only below condition will run otherwise it will give error as described in else condition.
        if request.session.get('log_id') is None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'priyanksalot91@gmail.com',
                [username],
                fail_silently=False,
            )
            # NOTE: must include below details in settings.py
            # detail tutorial - https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
            # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            # EMAIL_HOST = 'smtp.gmail.com'
            # EMAIL_USE_TLS = True
            # EMAIL_PORT = 587
            # EMAIL_HOST_USER = 'mail from which email will be sent'
            # EMAIL_HOST_PASSWORD = 'pjobvjckluqrtpkl'   #turn on 2 step verification and then generate app password which will be 16 digit code and past it here

            #############################################

            #now update the password in model
            cuser = User.objects.get(Email_id=username)
            cuser.Password = password
            cuser.cpassword=password
            cuser.save(update_fields=['Password'])
            cuser.save(update_fields=['cpassword'])

            print('Mail sent')
            messages.info(request, 'mail is sent')
            return render(request, 'login.html')

        else:
            messages.info(request, 'This account does not exist')
    return render(request,'login.html')

def forgot(request):
    return render(request,'forgot.html')
def changep(request):
    if request.method == "POST":
        email = request.POST.get("Email")
        oldpass = request.POST.get("oldpassword")
        newpass = request.POST.get("newpassword")
        user1 = User.objects.get(Email_id=email)
        user1.Email_id = email
        user1.Password = newpass
        user1.save()
        messages.success(request, "Password changed Successfully")
        return redirect(loginform)

    else:
        pass
    return render(request,'changepass.html')

def invoice(request,id):

    template = get_template('invoice.html')
    id2 = request.session['log_id']
    fetchcartdata = Cart.objects.filter(orderid=id)
    carttotal = Cart.objects.filter(orderid=id).aggregate(Sum('totalprice'))
    fatchpid = Cart.objects.filter(orderid=id).values('product_id')
    fetchproductdata = Product.objects.filter(id__in=fatchpid)
    userdetails = User.objects.get(id=id2)
    order=Order.objects.get(id=id)
    print(fetchcartdata)
    print(carttotal)
    print(fetchproductdata)
    print(userdetails)


    context = {
        'cart': fetchcartdata,
        'product': fetchproductdata,
        'user': userdetails,
        'carttotal': carttotal,
        'orderid': id,
        'order':order
    }
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

#def sendreport(request,id):

 #   template = get_template('invoice.html')
  #  id2 = request.session['log_id']
   # fetchcartdata = Cart.objects.filter(orderid=id)
    #carttotal = Cart.objects.filter(orderid=id).aggregate(Sum('totalprice'))
    #fatchpid = Cart.objects.filter(orderid=id).values('product_id')
    #fetchproductdata = Product.objects.filter(id__in=fatchpid)
    #userdetails = User.objects.get(id=id2)
    #order = Order.objects.get(id=id)
    #print(fetchcartdata)
    #print(carttotal)
    #print(fetchproductdata)
    #print(userdetails)

    #context = {
     #   'cart': fetchcartdata,
      #  'product': fetchproductdata,
       # 'user': userdetails,
        #'carttotal': carttotal,
        #'orderid': id,
        #'order': order
    #}
    #html = template.render(context)
    #result = BytesIO()
    #pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    #k= HttpResponse(result.getvalue(), content_type='application/pdf')




    ############ code for sending mail ########################
    #username =request.POST.get("email")
    #from django.core.mail import send_mail

    #send_mail(
     #   'Your New Password',
      #  msg,
       # 'priyanksalot91@gmail.com',
        #'priyanksalot91@gmail.com',
        #fail_silently=False,
    #)
    #return render(request,'order.html')