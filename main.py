Creating a comprehensive Python program for a project like Smart-Waste-Tracker involves several components, including IoT integration for real-time data collection, data storage and processing, machine learning for route optimization, and APIs for communication with the IoT devices and possibly a user interface. Below is a simplified version of this project, focusing on structure and key components. Due to complexity, especially in ML route optimization, this version will provide a framework with placeholders where specific implementations would be needed:

```python
# Import necessary libraries
import json
import requests
import random
from datetime import datetime, timedelta

# Simulated data and configurations
DUSTBIN_IDS = [1, 2, 3, 4, 5]
CAPACITY_THRESHOLD = 0.8  # Threshold for determining when a bin needs collection
API_ENDPOINT = "http://example.com/iot_endpoint"  # Placeholder IoT endpoint
ROUTE_OPTIMIZER_API = "http://example.com/route_optimizer"  # Placeholder for route optimization API

# Utility function to simulate waste level readings from IoT devices
def get_waste_level_from_iot(dustbin_id):
    try:
        # Simulate data from IoT device (replace with real IoT API call in production)
        response = requests.get(f"{API_ENDPOINT}/dustbin/{dustbin_id}")
        if response.status_code == 200:
            return response.json().get('waste_level', random.uniform(0, 1))
        else:
            raise Exception("Failed to get data from IoT device.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to IoT API: {e}")
        return random.uniform(0, 1)  # Fallback to random data for development/testing

# Function to check which bins need collection
def check_bins_needing_collection():
    bins_needing_collection = {}
    for dustbin_id in DUSTBIN_IDS:
        level = get_waste_level_from_iot(dustbin_id)
        print(f"Dustbin {dustbin_id} waste level: {level:.2f}")
        if level >= CAPACITY_THRESHOLD:
            bins_needing_collection[dustbin_id] = level
    return bins_needing_collection

# Example route optimization request
def get_optimized_route(bins):
    try:
        if not bins:
            print("No bins need collection at the moment.")
            return

        payload = {
            "bins": list(bins.keys()),
            "current_location": "municipal_garage_location"
        }

        # Make the API call to get optimized route
        response = requests.post(ROUTE_OPTIMIZER_API, json=payload)

        if response.status_code == 200:
            optimized_route = response.json().get('route', [])
            print(f"Optimized route: {optimized_route}")
            return optimized_route
        else:
            raise Exception("Route optimization failed.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to route optimizer API: {e}")
        return []

# Main function to simulate the waste tracker process
def smart_waste_tracker():
    # Check which bins need collection
    bins_needing_collection = check_bins_needing_collection()

    # Get optimized route for the collection
    get_optimized_route(bins_needing_collection)

# Entry point for the program
if __name__ == "__main__":
    # Simulate running the smart waste tracker every hour
    while True:
        try:
            print(f"Running Smart Waste Tracker at {datetime.now()}")
            smart_waste_tracker()

            # Sleep for an hour until the next execution
            print("Waiting for the next run...\n")
            time.sleep(3600)  # Wait for 1 hour
        except KeyboardInterrupt:
            print("Exiting the program.")
            break
        except Exception as e:
            print(f"An error occurred: {e}.")
```

### Key Components Explained:

1. **IoT Data Simulation**: 
   - `get_waste_level_from_iot()` simulates gathering waste level data from IoT devices. In a real scenario, this function would retrieve data from actual IoT sensors monitoring bin levels.
   
2. **Threshold Checking**: 
   - `check_bins_needing_collection()` determines which bins need collection based on predefined capacity thresholds.

3. **Route Optimization**: 
   - `get_optimized_route()` simulates interaction with a backend service that provides optimized routing. In practice, this would use pathfinding algorithms or a third-party service.

4. **Main Loop**:
   - A loop simulates hourly checks. This can be adapted to use real-time scheduling mechanisms for efficiency.
  
5. **Error Handling**: 
   - Simple error handling is integrated via try-except blocks to catch and inform about failed operations such as network requests.

In practice, you'd need to replace simulated APIs with actual endpoints and possibly store data in a database like PostgreSQL or MongoDB, depending on the needs of your application. Additionally, the route optimization would involve more advanced computations, potentially utilizing algorithms like Dijkstra's, A*, or calling external APIs like Google Maps Distance Matrix API.