import requests
def get_bot_response(user_input):
    country_name = user_input.strip()

    # Check if the input is a country name
        # Make a request to the REST API to get country details
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    if response.status_code == 200:
        country_details = response.json()
            # Extract relevant information from the response
        country_info = {
                "Name": country_details[0]["name"]["official"],
                "Capital": country_details[0]["capital"][0],
                "Continent": country_details[0]["region"],
            }
        return f"Here are some details about {country_name}:\n\n{country_info}"
    else:
        return "Sorry, I couldn't retrieve the details for that country."
print(get_bot_response("Kenya"))