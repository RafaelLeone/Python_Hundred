import json
import os


new_data = {
    "website2": {
        "email": "email",
        "password": "password",
    }
}

# Get the absolute path to the directory containing the script.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.json")

try:
    with open(file_path, 'r') as data_file:
        # Read old data.
        data = json.load(data_file)
except FileNotFoundError:
    with open(file_path, 'w') as data_file:
        json.dump(new_data, data_file, indent=4)
else:
    # Update old data with new data.
    data.update(new_data)

    with open(file_path, 'w') as data_file:
        # Save updated data.
        json.dump(data, data_file, indent=4)
finally:
    print("Done")
