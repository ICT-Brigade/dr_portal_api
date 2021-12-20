from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django_filters import FilterSet,CharFilter
from catalog.models import Post
from main.settings import STATIC_URL


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context

class PostFilter(FilterSet):
    description = CharFilter(field_name='description', lookup_expr='icontains')
    campaign_type = CharFilter(field_name='campaign_type__value', lookup_expr='icontains')
    beneficiary_location = CharFilter(field_name='beneficiary_location', lookup_expr='icontains')
    class Meta:
        model = Post
        fields = ['description', 'campaign_type__value', 'beneficiary_location']


# Create your views here.


class PostListView(FilteredListView):
    filterset_class = PostFilter
    model = Post
    context_object_name = 'posts_list'
    paginate_by = 6
    template_name = '../templates/catalog_list.html'
    context = {
        'static_url': STATIC_URL
    }
