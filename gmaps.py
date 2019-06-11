import googlemaps

gm = googlemaps.Client(key='AIzaSyAiVw3AgMxnP6KHhwcR54VgQo8eS6w1ekM')

dist =  gm.distance_matrix('kolkata','Bardhaman')['rows'][0]['elements'][0]


print dist
