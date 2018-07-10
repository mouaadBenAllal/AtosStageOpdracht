# Django
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView
from airbnbatos.forms import DocumentForm
from airbnbatos.models import Document, CsvExport
import csv

# Third party packages
from chartit import PivotDataPool, PivotChart


def index(request):
    """ View function for home page of site. """

    # Render the HTML template base.html
    return render(request, 'base.html')


class DocumentsList(ListView):
    """ Class based view for list of csv documents. """

    model = Document
    template_name = "fileupload/filelist.html"


def model_form_upload(request):
    """ View function for upload csv document. """

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        # returns template formupload.html with form
            return redirect('documents_list')
    else:
        form = DocumentForm()

    # returns template formupload.html with form.
    return render(request, 'fileupload/formupload.html', {
        'uploaddocform': form,

    })


def export_csv(request):
    """ View function for exporting csv into database. """

    file_exported = request.POST.get('document', None)

    with open('../run/media/' + file_exported, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            room_id = row['room_id']
            host_id = row['host_id']
            room_type = row['room_type']
            borough = row['borough']
            neighborhood = row['neighborhood']
            reviews = row['reviews']
            overall_satisfaction = row['overall_satisfaction']
            accommodates = row['accommodates']
            bedrooms = row['bedrooms']
            price = row['price']
            minstay = row['minstay']
            latitude = row['latitude']
            longitude = row['longitude']
            last_modified = row['last_modified']

            CsvExport(
                room_id=room_id,
                host_id=host_id,
                room_type=room_type,
                borough=borough,
                neighborhood=neighborhood,
                reviews=reviews,
                overall_satisfaction=overall_satisfaction,
                accommodates=accommodates,
                bedrooms=bedrooms,
                price=price,
                minstay=minstay,
                latitude=latitude,
                longitude=longitude,
                last_modified=last_modified,
            ).save()

    data = {
        'message': "Csv data is exported to the database!",
    }

    # returns json data to client side
    return JsonResponse(data)


def total_reviews_per_room(request):
    """ View function for displaying pivot chart on page. """

    room_pivot_data = PivotDataPool(
        series=[{
            'options': {
                'source': CsvExport.objects.only("room_type", "reviews"),
                'categories': ['room_type'],
                'legend_by': 'room_type',
                'top_n_per_cat': 100,
            },
            'terms': {
                'total_reviews': Sum('reviews'),
            }
        }]
    )

    room_pivot_chart = PivotChart(
        datasource=room_pivot_data,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['total_reviews']
        }],
        chart_options={
            'title': {
                'text': 'Total reviews per room type'
            },
            'xAxis': {
                'title': {
                    'text': 'Type of room'
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Reviews'
                }
            }
        }
    )

    # Renders the HTML template total_reviewsroom.html and pivotchart.
    return render_to_response('charts/total_reviewsroom.html', {'roompivotchart': room_pivot_chart})
