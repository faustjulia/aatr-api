import requests


# Hiking shoes = 55
# Sunscreen = 60
# Beach towel = 60
# Sun glasses = 59
# Water bottle = 60

# TODO: Exercise 1: A proper request following all the previous instructions
# 1. Add variable type to the 'response'
# 2. Instead of using separate 'url' variable,
#    move 'https://amazon-products1.p.rapidapi.com/search' in .get(url=...)
# 3. Instead of using separate 'headers' variable,
#    move {... headers_content ...} in .get(headers=...)
# 4. Instead of using separate 'querystring' variable,
#    move {... querystring_content ...} in .get(params=...)
# 5. Choose one either single or double quotes,
#    and stick with them - replace all of them with one type.

# TODO: Exercise 2: Create a 'ProductRequest' class
# 1. Create a new 'ProductRequest' class blueprint
# 2. Create a new method called 'def _request(self) -> requests.Response:'
# 3. Move the content of 'Exercise 1' to the new '_request' method (return the response)


# TODO: Exercise 3: Move parts that don't change to the __init__
# 1. Create a new 'self.url' variable in '__init__' method (and use it in code)
# 2. Create a new 'self.headers' variable in '__init__' method (and use it in code)


class ProductRequest:

    def __init__(
        self,
        headers={
            'x-rapidapi-host': 'amazon-products1.p.rapidapi.com',
            'x-rapidapi-key': '053e00a14fmsh0a56e00fbabbe95p1438bajsn8d4c446bdd86'
        },

    ):
        self.headers = headers

    def _request(self) -> requests.Response:
        response: requests.models.Response = requests.get(

            url='https://amazon-products1.p.rapidapi.com/search',

            headers=self.headers,
            params={
                'country': 'US',
                'query': 'Water bottle',
                'page': '1'
            }
        )

        print(response)

        # data = response.json()
        # print(data)
        # 
        # print(response.json()['results'][0].get('title'))
        # print(response.json()['results'][0].get('image'))
        # print(response.json()['results'][0].get('full_link'))
        # print(response.json()['results'][0].get('prices'))

        return response
