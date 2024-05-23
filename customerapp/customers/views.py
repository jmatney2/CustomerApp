"""Views for the Customers app"""

import json

from typing import Any

from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView


from .models import Customer
from .forms import CustomerForm


class IndexView(TemplateView):
    """Main landing page for customers app"""

    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Retrieve all customers as context"""
        return {"customers": Customer.objects.all()}


class AddCustomerView(TemplateView):
    """View for adding and deleting customers"""

    template_name = "add_customer.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Load a form for the webpage"""
        return {"form": CustomerForm}

    def post(self, request: HttpRequest):
        """Handle loading new customers"""
        context = self.get_context_data()
        form = CustomerForm(request.POST)

        if form.is_valid():
            new_customer = Customer(**form.cleaned_data)
            new_customer.save()

            # Return a success message
            context["success"] = (
                f"Added customer {new_customer.first_name} "
                f"{new_customer.last_name} successfully!"
            )
        else:
            # Retain information from invalid form
            context["form"] = CustomerForm(form.data)

        # Use response to reload user's window
        return self.render_to_response(context)

    def delete(self, request: HttpRequest):
        """Delete customers"""
        # JSON works better than query dict in this instance
        data = json.loads(request.body)
        customer_id = data["customer_id"]

        # Delete customer and return the result
        result = Customer.objects.filter(id=customer_id).delete()
        return HttpResponse(result)
