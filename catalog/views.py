from django.shortcuts import render
from .models import User, Expense
# Create your views here.


from django.views import generic


class ExpenseListView(generic.ListView):
    model = Expense
    context_object_name = 'expenses_list'   # your own name for the list as a template variable
    #queryset = Expense.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'expenses/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context