from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Record, Item
from .filters import RecordFilter
from .forms import RecordForm, ItemForm, ShopForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render


class RecordList(ListView):
    model = Record
    ordering = '-date'
    template_name = 'finances.html'
    context_object_name = 'records'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RecordFilter(self.request.GET, queryset)
        print(self)
        return self.filterset.qs

    def get_context_data(self, ** kwargs):
        category = self.request.GET.get('category__icontains')
        context = super().get_context_data(**kwargs)

        result = 0
        items = {}

        for i in self.object_list:
            if i.is_income:
                result += i.sum
            else:
                if i.includes_items and category:
                    i_item = Item.objects.filter(record = i.id, category = int(category))

                    for j in i_item:
                        result -= j.cost
                        print(j.cost)

                else:
                    result -= i.sum

            if Item.objects.filter(record = i.id):

                items[i.id] = Item.objects.filter(record = i.id)
                #print(items)


        context['result'] = result
        context['items'] = items
        context['filterset'] = self.filterset

        return context


class RecordCreate(CreateView):
    form_class = RecordForm
    model = Record
    template_name = 'record_create.html'

class ItemCreate(CreateView):
    form_class = ItemForm
    model = Item
    template_name = 'record_create.html'

    def post(self, request, *args, **kwargs):
        item = Item(
            name = request.POST['name'],
            cost = request.POST['cost'],
            record = Record.objects.get(pk=int(request.GET.get('record'))),
            amount = request.POST['amount'],
            #category = request.POST['category'],
        )

        item.save()
        item.category.set(request.POST.getlist('category'))
        print(item.record)
        return redirect(f"/{item.record.id}/record_update/")


class RecordUpdate(UpdateView):
    form_class = RecordForm
    model = Record
    template_name = 'record_edit.html'

    def setup(self, request, *args, **kwargs):
        s = super().setup(request, *args, **kwargs)
        record_pk = int(request.get_full_path()[1:-15])
        items = Item.objects.filter(record=record_pk)

        if items:
            self.form_class = ShopForm

        return s


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        items = Item.objects.filter(record = context['object'].id)
        context['items'] = items
        print(context['object'].id)
        if items:
            self.form_class = ShopForm

        return context

class RecordDelete(DeleteView):
    model = Record
    template_name = 'default.html'
    success_url = '/'


class ItemDelete(DeleteView):
    model = Item
    template_name = 'default.html'
    #success_url = reverse_lazy('record_update')

    def form_valid(self, form):
        success_url = f'/{self.object.record_id}/record_update/'
        self.object.delete()
        return HttpResponseRedirect(success_url)

class ItemUpdate(UpdateView):
    form_class = ItemForm
    model = Item
    template_name = 'item_edit.html'

    def form_valid(self, form):
        success_url = f'/{self.object.record_id}/record_update/'
        self.object = form.save()
        return HttpResponseRedirect(success_url)