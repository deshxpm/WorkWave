from django.shortcuts import render
from .models import PayrollTransaction

def payroll_transaction_list(request):
    payroll_transactions = PayrollTransaction.objects.all()
    return render(request, 'payroll_transaction_list.html', {'payroll_transactions': payroll_transactions})
