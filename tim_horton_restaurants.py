import requests
import json
import pandas as pd
import logging

API_URL = "https://use1-prod-th.rbictg.com/graphql"

# Configuration
USER_LAT = 43.666354
USER_LNG = -79.383539
SEARCH_RADIUS = 15000
FIRST_N_BRANCHES = 5

HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.timhortons.com',
    'Referer': 'https://www.timhortons.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

PAYLOAD = json.dumps([
    {
        "operationName": "GetRestaurants",
        "variables": {
            "input": {
                "filter": "NEARBY",
                "coordinates": {
                    "userLat": USER_LAT,
                    "userLng": USER_LNG,
                    "searchRadius": SEARCH_RADIUS
                },
                "first": FIRST_N_BRANCHES,
                "status": "OPEN"
            }
        },
        "query": "query GetRestaurants($input: RestaurantsInput) {\n  restaurants(input: $input) {\n    pageInfo {\n      hasNextPage\n      endCursor\n      __typename\n    }\n    totalCount\n    nodes {\n      ...RestaurantNodeFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment RestaurantNodeFragment on RestaurantNode {\n  _id\n  storeId\n  isAvailable\n  posVendor\n  chaseMerchantId\n  curbsideHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  deliveryHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  diningRoomHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  distanceInMiles\n  drinkStationType\n  driveThruHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  driveThruLaneType\n  email\n  environment\n  franchiseGroupId\n  franchiseGroupName\n  frontCounterClosed\n  hasBreakfast\n  hasBurgersForBreakfast\n  hasCatering\n  hasCurbside\n  hasDelivery\n  hasDineIn\n  hasDriveThru\n  hasTableService\n  hasMobileOrdering\n  hasLateNightMenu\n  hasParking\n  hasPlayground\n  hasTakeOut\n  hasWifi\n  hasLoyalty\n  id\n  isDarkKitchen\n  isFavorite\n  isHalal\n  isRecent\n  latitude\n  longitude\n  mobileOrderingStatus\n  name\n  number\n  parkingType\n  phoneNumber\n  physicalAddress {\n    address1\n    address2\n    city\n    country\n    postalCode\n    stateProvince\n    stateProvinceShort\n    __typename\n  }\n  playgroundType\n  pos {\n    vendor\n    __typename\n  }\n  posRestaurantId\n  restaurantImage {\n    asset {\n      _id\n      metadata {\n        lqip\n        palette {\n          dominant {\n            background\n            foreground\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    crop {\n      top\n      bottom\n      left\n      right\n      __typename\n    }\n    hotspot {\n      height\n      width\n      x\n      y\n      __typename\n    }\n    __typename\n  }\n  restaurantPosData {\n    _id\n    __typename\n  }\n  status\n  vatNumber\n  __typename\n}\n\nfragment OperatingHoursFragment on OperatingHours {\n  friClose\n  friOpen\n  monClose\n  monOpen\n  satClose\n  satOpen\n  sunClose\n  sunOpen\n  thrClose\n  thrOpen\n  tueClose\n  tueOpen\n  wedClose\n  wedOpen\n  __typename\n}\n"
    }
])

logging.basicConfig(filename='error.log', level=logging.ERROR)

def fetch_and_save_data():
    try:
        response = requests.post(API_URL, headers=HEADERS, data=PAYLOAD)

        if response.status_code == 200:
            json_responses = response.json()

            restaurant_data = []

            for json_response in json_responses:
                restaurants = json_response.get("data", {}).get("restaurants", {}).get("nodes", [])
                for restaurant in restaurants:
                    restaurant_info = {
                        "Name": restaurant.get("name", ""),
                        "City": restaurant.get("physicalAddress", {}).get("city", ""),
                        "State": restaurant.get("physicalAddress", {}).get("stateProvince", ""),
                        "PostalCode": restaurant.get("physicalAddress", {}).get("postalCode", ""),
                        "PhoneNumber": restaurant.get("phoneNumber", ""),
                        "Latitude": restaurant.get("latitude", ""),
                        "Longitude": restaurant.get("longitude", ""),
                    }
                    restaurant_data.append(restaurant_info)

            df = pd.DataFrame(restaurant_data)

            df.to_csv("tim_hortons_restaurants.csv", index=False)
            print("Data saved successfully.")
        else:
            print("Failed to retrieve data. Status code:", response.status_code)
            logging.error(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        print("An error occurred:", str(e))
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    fetch_and_save_data()
