# Tim Hortons Store Locator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description
The Tim Hortons Store Locator is a Python-based project that allows you to explore and retrieve information about Tim Hortons restaurant locations. Tim Hortons is a popular Canadian-based fast-food restaurant chain known for its coffee, donuts, and other menu items. This project utilizes the Tim Hortons GraphQL API to fetch data about Tim Hortons locations, including their geographical coordinates, and stores this data in a CSV file which then can be used for further analysis or visualization.

## Features
- Fetch Tim Hortons location data using GraphQL.
- Extract important information such as restaurant names, addresses, phone numbers, and geographical coordinates.
- Store the extracted data in a CSV file for easy access and analysis.
- Customizable configuration for location coordinates and search radius.
- Error handling and logging for robustness.

## Requirements
- Python 3.x
- Requests library
- Pandas library

## Usage
1. Clone this repository: `git clone https://github.com/zararashraf/TimHortonsStoreLocator.git`
2. Install the required libraries: `pip install requests pandas`
3. Run the script: `python main.py`

## Code Repository
You can find the source code for this project on [GitHub](https://github.com/zararashraf/TimHortonsStoreLocator/blob/main/tim_hortons_restaurants.py).


## Screenshots
![screenshot](https://github.com/zararashraf/TimHortonsStoreLocator/assets/36181292/c2ca1e87-6f8d-4824-bbe4-3b2e1be3ff11)


## Credits
- Data Source: U.S. Department of Health & Human Services - CDC
- Python Requests: https://docs.python-requests.org/en/latest/
- Python Pandas: [https://pandas.pydata.org/en/latest/](https://pandas.pydata.org/getting_started.html)

## License
This project is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). You are free to use, modify, and distribute the code as long as you provide appropriate attribution.
