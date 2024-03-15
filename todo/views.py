from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        created_by = request.user
        ticket = Ticket.objects.create(title=title, description=description, created_by=created_by)
        ticket.send_status_notification()
        messages.success(request, 'Ticket created successfully!')
        return redirect('ticket_list')
    return render(request, 'ticket_create.html')

@login_required
def ticket_update(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        status = request.POST['status']
        ticket.status = status
        ticket.save()
        ticket.send_status_notification()
        messages.success(request, 'Ticket status updated successfully!')
        return redirect('ticket_list')
    return render(request, 'ticket_update.html', {'ticket': ticket})
