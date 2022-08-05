from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def distance():
    (latitude_1,longitude_1,city_name_1) = get_cities('first')
    (latitude_2,longitude_2,city_name_2) = get_cities('second')
    city_one = (latitude_1,longitude_1)
    city_two = (latitude_2,longitude_2)

    #distance = ((longitude_2-longitude_1)**2 + (latitude_2-latitude_1)**2)**(0.5)
    #distance_str = str(distance)[0:6]
    print(f'The KM distance between {city_name_1} and {city_name_2} is: ', geodesic(city_one,city_two).km)

def get_cities(number):
    
    geolocator = Nominatim(user_agent='MyApp')
    city = input(f'Write the name of the {number} city: ')
    location = geolocator.geocode(city)
    return(location.latitude,location.longitude,city)

if __name__ == '__main__':
    distance()