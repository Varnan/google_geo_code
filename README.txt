
Django Task 
Date : 08/10/2015
======================================================
======================================================

Write an endpoint to place an order. Model should emit a post save signal to calculate customers coordinates using Google geo code API.

Order table would have following fields:
		1. address line 1
		2. address line 2
		3. city
		4. contact_number
		5. Order time
		6. Amount
		7. Latitude
		8. Longitude


The Google Maps Geocoding API:

What is Geocoding?

Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739), which you can use to place markers on a map, or position the map.

Reverse geocoding is the process of converting geographic coordinates into a human-readable address. The Google Maps Geocoding API's reverse geocoding service also lets you find the address for a given place ID.

The Google Maps Geocoding API provides a direct way to access these services via an HTTP request.

For More Details :
	https://developers.google.com/maps/documentation/geocoding/intro?hl=en_US