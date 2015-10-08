
from django.shortcuts import render_to_response,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Context, loader
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Orders
# Create your views here.



import requests

API_KEY = 'AIzaSyBtSJ8xdvKEHPgxXVSW5F_e3ySwQ_n7T9I'


#Order Form
@csrf_exempt
def home(request):
	print "Inside Orders Page #######"

	rg = request.POST.get

	status = False

	if request.POST:

		addr1 = rg('addr1')
		addr2 = rg('addr2')
		city = rg('city')
		mobile = rg('mobile')
		amount = rg('amount')
		lat = rg('lat')
		longi = rg('long')

		print "Order Details #####", addr1,addr2,city,mobile,amount,lat,longi

		if addr1 and addr2 and city and mobile and amount:

			order = Orders()
			order.address1 = addr1
			order.address2 = addr2
			order.city = city
			order.mobile = mobile
			order.amount = amount

			if lat and longi:
				order.latitude = lat
				order.longitude = longi
				order.save()
				status = "success"
			else:
				address = ','.join(addr1.split(',') + addr2.split(',') + city.split(','))
				api_key = API_KEY
				api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
				api_response_dict = api_response.json()

				if api_response_dict['status'] == 'OK':
					latitude = api_response_dict['results'][0]['geometry']['location']['lat']
					longitude = api_response_dict['results'][0]['geometry']['location']['lng']
					
					print 'Latitude:', latitude
					print 'Longitude:', longitude

					order.latitude = latitude
					order.longitude = longitude
					order.save()
					status = "success"
					return HttpResponseRedirect(reverse('details', kwargs={'order_id': order.id}))

		else:
			print "Error"
			status = "error"


	variables = RequestContext(request, {'status':status,})
	return render_to_response('home.html', variables)

def details(request,order_id):

	if order_id:
		order = Orders.objects.get(id=order_id)

	variables = RequestContext(request, {'order':order,})
	return render_to_response('details.html', variables)

