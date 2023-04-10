import requests

# Set the base URL for the API
base_url = 'https://www.ncei.noaa.gov/access/services/data/v1'

# Set the dataset ID and location ID for Nashville, TN
dataset_id = 'daily-summaries'
location_id = 'CITY:US470016'

# Set the start and end dates for the data
start_date = '2020-01-01'
end_date = '2020-12-31'

# Set the parameters for the API request
params = {
    'dataset': dataset_id,
    'startDate': start_date,
    'endDate': end_date,
    'stations': location_id,
    'dataTypes': 'PRCP',  # precipitation data
    'format': 'json',
    'includeAttributes': 'false',
    'includeStationName': 'false',
    'includeStationLocation': 'false'
}

# Make the API request and get the response data as JSON
response = requests.get(base_url, params=params)
data = response.json()

# Check if the data list contains any elements
if len(data) > 0 and 'data' in data[0]:
    # Extract the daily precipitation data from the response
    precip_data = [day['value'] for day in data[0]['data']]

    # Print the precipitation data for the first 10 days of the year
    print(precip_data[:10])
else:
    print('No precipitation data available for the specified location and dates.')
