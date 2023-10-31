from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact, PhoneNumber

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(name=form.cleaned_data['name'])
            contact.save()
            numbers = form.cleaned_data['numbers'].split(',')
            for number in numbers:
                PhoneNumber.objects.create(contact=contact, number=number.strip())
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(request, 'phone_book_app/add_contact.html', {'form': form})


def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'phone_book_app/list.html', {'contacts': contacts})

def contact_details(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'phone_book_app/details.html', {'contact': contact})
