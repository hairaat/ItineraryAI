import requests

class ItineraryAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    def get_hotels(self, location, date):
        params = {
            'location': location,
            'radius': 5000,  # Search radius in meters
            'type': 'lodging',  # Type is set to lodging for hotels
            'key': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        hotels = response.json().get('results', [])
        return hotels

    def get_eateries(self, location, date):
        params = {
            'location': location,
            'radius': 5000,  # Search radius in meters
            'type': 'restaurant',  # Type is set to restaurant for eateries
            'key': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        eateries = response.json().get('results', [])
        return eateries

if __name__ == "__main__":
    api_key = "YOUR_GOOGLE_PLACES_API_KEY"
    itinerary_ai = ItineraryAI(api_key)
    location = input("Enter location: ")
    date = input("Enter date: ")

    hotels = itinerary_ai.get_hotels(location, date)
    eateries = itinerary_ai.get_eateries(location, date)

    print("Plausible Hotels:")
    for hotel in hotels:
        print(hotel['name'])

    print("\nPlausible Eateries:")
    for eatery in eateries:
        print(eatery['name'])
