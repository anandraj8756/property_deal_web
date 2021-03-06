from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact

# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id =request.POST['listing_id']
        listing =request.POST['listing']
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']
        user_id =request.POST['user_id']
        realtor_email =request.POST['realtor_email']


        #Check If user has made inquery Already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquery for this listing')
                return redirect('/listings/'+listing_id) 

        contact = Contact(listing=listing, name=name, phone=phone,
        email=email, message=message, listing_id=listing_id, user_id=user_id)

        contact.save()

        #Send Email
#        send_mail (
#            'Property Listing Inquery',
#            'There has been inquery for'+ listing + '.Sign into the admin pannel for more Info',
#            'ashagaya95@gmail.com',
#            [realtor_email, '500061157@stu.upes.ac.in'],
#            fail_silently= False
#
#        )

        messages.success(request, 'Your request has been submited, a reatlor will get back to you soon')
        return redirect('/listings/'+listing_id)
