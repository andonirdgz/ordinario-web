from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from .models import Artwork
from .forms import ArtworkForm, OrderForm
from . import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings


class ArtworksListView(ListView):
    model = Artwork


class ArtworkCreateView(CreateView):
    model = Artwork
    form_class = ArtworkForm
    success_url = reverse_lazy('artworks:artworks')


class ArtworkUpdateView(UpdateView):
    model = Artwork
    form_class = ArtworkForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('artworks:update', args=[self.object.id]) + '?ok'


class ArtworkDeleteView(DeleteView):
    model = Artwork
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy('artworks:artworks')


class ArtworkCreateOrder(CreateView):
    form_class = OrderForm
    template_name = "artworks/client_order.html"
    success_url = reverse_lazy('artworks:order_success')

    def form_valid(self, form):
        new_order = form.save(commit=False)
        new_order.save()

        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        total = form.cleaned_data.get('total')

        detail = self.request.session.get('order_detail')

        subject = 'Gracias por tu compra'
        message = f'Hola {name} gracias por tu compra.'
        message += '\n\nDetalle de su pedido:'

        for product in detail:
            message += f'\nProducto: {product["description"]}\t \nPrecio: {product["price"]}\t \nCantidad: {product["quantity"]}\n'

        message += f'\nTOTAL: {total} BTC \n\n Vuelva pronto :).'

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]

        send_mail(subject, message, email_from, recipient_list)

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ArtworkCreateOrder, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class OrderSuccess(TemplateView):
    template_name = "artworks/order_success.html"


def _createDictionary(order_data):
    dictionary = {}
    order_data = order_data[:-1]
    products = order_data.split('|')

    for product in products:
        detail = product.split("-")
        dictionary[detail[0]] = int(detail[1])

    return dictionary


def send_order(request):
    order = list()

    if request.method == 'POST':
        order_data = request.POST['order_data']
        products = _createDictionary(order_data)
        total = 0

        for barcode in products.keys():
            quantity = products[barcode]

            if quantity > 0:
                dict_product = {}
                artwork = Artwork.objects.get(pk=barcode)
                dict_product['id'] = artwork.id
                dict_product['description'] = artwork.title
                dict_product['quantity'] = quantity
                dict_product['price'] = artwork.price
                total += quantity * artwork.price
                order.append(dict_product)

        request.session['total_float'] = float(total)
        request.session['order_detail'] = order

    return render(request, 'artworks/order_detail.html', {'order': order, 'total': total})
