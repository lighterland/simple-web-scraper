import requests
from bs4 import BeautifulSoup

# Set the URL of the web page you want to scrape
url = "http://www.example.com"

# Fetch the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.text, "html.parser")

  # Find all of the div elements on the page
  divs = soup.find_all("div")

  # Check if any div elements were found
  if divs:
    # Save the data to a file or database
    with open("data.txt", "w") as f:
      for div in divs:
        f.write(div.text + "\n")
  else:
    # No div elements were found, handle the error
    print("No div elements were found.")
else:
  # Request was not successful, handle the error
  print(f"Request failed with status code {response.status_code}.")
