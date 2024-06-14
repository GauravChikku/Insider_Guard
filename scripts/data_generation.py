import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize faker
fake = Faker()

# Define parameters
num_logs = 1000  # Number of logs to generate

# Function to generate user activity logs
def generate_activity_logs(num_logs, dataset):
    logs = []
    for _ in range(num_logs):
        app_info = dataset.sample().iloc[0]
        app_name = app_info['App_Name']
        category = app_info['Category']
        app_type = app_info['Type']
        
        user_id = fake.uuid4()
        activity_type = random.choice(['install', 'uninstall', 'open', 'update', 'crash'])
        timestamp = fake.date_time_this_year()
        
        details = {
            'install': f"User {user_id} installed {app_name} from category {category}.",
            'uninstall': f"User {user_id} uninstalled {app_name} from category {category}.",
            'open': f"User {user_id} opened {app_name} from category {category}.",
            'update': f"User {user_id} updated {app_name} from category {category}.",
            'crash': f"App {app_name} from category {category} crashed on user {user_id}'s device."
        }
        
        logs.append({
            'user_id': user_id,
            'app_name': app_name,
            'category': category,
            'app_type': app_type,
            'activity_type': activity_type,
            'timestamp': timestamp,
            'details': details[activity_type]
        })
    return pd.DataFrame(logs)

# Sample data to demonstrate the function until the actual file is available
sample_data = {
    'App_Name': ['App1', 'App2', 'App3', 'App4', 'App5'],
    'Category': ['Category1', 'Category2', 'Category3', 'Category4', 'Category5'],
    'Type': ['Malware', 'Benign', 'Malware', 'Benign', 'Malware']
}
dataset = pd.DataFrame(sample_data)

# Generate the logs
activity_logs = generate_activity_logs(num_logs, dataset)

# Save to CSV
activity_logs.to_csv('android_app_activity_logs.csv', index=False)

# Print a sample of the logs to verify
print(activity_logs.head(10))
