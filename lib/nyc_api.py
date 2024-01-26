import requests
import json

class GetPrograms:

    def get_programs(self):
      # API URL for giphy search
        URL = "https://api.giphy.com/v1/gifs/search?q=dolphin&api_key=WfxQyIQju5PMND31ITPmcFptrTC6hyhY"

      # Make a GET request to the Giphy API
        response = requests.get(URL)
        return response.json() # Return the JSON content of the response

    def get_all_urls(self):
        url_list = [] # List to store GIF URLs
        data = self.get_programs().get("data", [])  # Get the 'Data' list from the API response

        for item in data:
            images = item.get("images", {}) # Get the image dictionary from each item
            original_url = images.get("original", {}).get("url")

            url_list.append(original_url)

        return url_list

# programs = GetPrograms().get_programs()
# print(programs)

all_urls = GetPrograms().get_all_urls()
for a_ulr in all_urls:
  print(all_urls)
