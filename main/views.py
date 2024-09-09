from django.shortcuts import render

# Create your views here.
def show_main(request):
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


    }

    return render(request, "main.html", context)