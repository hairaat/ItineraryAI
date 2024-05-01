# ItineraryAI
This Python code defines a class called ItineraryAI, which serves as an interface for interacting with the Google Places API to retrieve information about hotels and eateries near a specified location. Here's a breakdown of what the code does:

Class ItineraryAI:
It has two methods:
get_hotels: Retrieves a list of hotels near a specified location.
get_eateries: Retrieves a list of eateries (restaurants) near a specified location.
Both methods take two parameters: location (the location to search around) and date (presumably the date of the itinerary, although it's not used in the methods).
The class is initialized with an API key for accessing the Google Places API.
Method get_hotels:
Constructs parameters for the Google Places API nearby search request, specifying the location, search radius, type of place (lodging for hotels), and the API key.
Sends a GET request to the Google Places API with the constructed parameters.
Parses the JSON response and extracts the list of hotels.
Method get_eateries:
Similar to get_hotels but tailored for eateries (restaurants).
Main Block:
If the script is executed directly (not imported), it prompts the user to input a location and date.
It then uses the ItineraryAI class to fetch a list of hotels and eateries near the specified location and prints them out.
This code essentially acts as a simple tool for suggesting hotels and eateries for a given location and date, leveraging the Google Places API
