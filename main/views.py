from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import MoodEntryForm
from main.models import MoodEntry
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def show_main(request):
    mood_entries = MoodEntry.objects.all()
    context = {

        'nama' : "Farrell Zidane Raihandrawan",
        'npm' : "2306275600",
        'kelas' : "PBP B",

        'item_name1': 'Manchester United 98/99 UCL Final',
        'item_description1' : '''This is Ole Gunnar Solksjaer's Match Worn
                                jersey who scored the last minute game winner.''',
        'price1' : '150.000.000',
        'item_rating1' : '9/10',

        'item_name2': 'Blackburn Rovers 94/95 ',
        'item_description2' : '''This is Alan Shearer's Match Worn
                                jersey who led the team wins the Premier League.''',
        'price2' : '100.000.000',
        'item_rating2' : '9/10',

        'item_name3': 'France Home jersey WC 2006',
        'item_description3' : '''This is Zinedine Zidane's Match Worn
                                jersey when he did the iconic headbutt.''',
        'price3' : '150.000.000',
        'item_rating3' : '10/10',

        'mood_entries': mood_entries


    }

    return render(request, "main.html", context)


def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)

def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


