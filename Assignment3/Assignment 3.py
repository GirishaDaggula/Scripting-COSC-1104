'''
Author: Girisha Daggula
Student ID: 100974333
'''
import time
from google.cloud import monitoring_v3
from google.cloud import compute_v1
from google.protobuf.timestamp_pb2 import Timestamp
import datetime
import google.auth


PROJECT_ID = "daggula"
ZONE = "northamerica-northeast1-a"
INSTANCE_GROUP_NAME = "web-app-group"
THRESHOLD = 70  # CPU utilization threshold to scale up
SCALE_UP = 1    # Number of instances to add
SCALE_DOWN = 1  # Number of instances to remove

# Google Cloud authentication
def get_credentials():
    credentials, project = google.auth.default()
    return credentials, project

# Function to get CPU utilization from Google Cloud Monitoring
def get_cpu_utilization(project_id, zone, instance_group_name):
    # Initializing the Monitoring API client
    monitoring_client = monitoring_v3.MetricServiceClient()
    
    # Define the time window for data (last 60 minutes)
    end_time = time.time()
    start_time = end_time - 3600  # Last hour

    # Create the timestamp objects (timezone-aware)
    start_timestamp = Timestamp()
    start_datetime = datetime.datetime.utcfromtimestamp(start_time).replace(tzinfo=datetime.timezone.utc)
    start_timestamp.FromDatetime(start_datetime)
    
    end_timestamp = Timestamp()
    end_datetime = datetime.datetime.utcfromtimestamp(end_time).replace(tzinfo=datetime.timezone.utc)
    end_timestamp.FromDatetime(end_datetime)

    # Defines the metric filter to monitor CPU utilization
    metric = "compute.googleapis.com/instance/disk/write_bytes_count"
    
    # Creating the request
    request = monitoring_v3.ListTimeSeriesRequest(
        name=f"projects/{project_id}",
        filter=f'metric.type="{metric}"',
        interval=monitoring_v3.TimeInterval(
            start_time=start_timestamp, end_time=end_timestamp
        ),
        aggregation=monitoring_v3.Aggregation(
            alignment_period=google.protobuf.duration_pb2.Duration(seconds=60),
            per_series_aligner=monitoring_v3.Aggregation.Aligner.ALIGN_RATE
        ),
    )

    # Get the time series data
    time_series = monitoring_client.list_time_series(request=request)
    
    # Extract the average CPU utilization value (in percentage)
    cpu_usage = 0
    count = 0
    for series in time_series:
        for point in series.points:
            cpu_usage += point.value.double_value
            count += 1
    if count > 0:
        cpu_usage /= count
    return cpu_usage

# Function to scale the instance group
def scale_instance_group(project_id, zone, instance_group_name, scale_by):
    # Initialize the Compute Engine API client
    compute_client = compute_v1.InstanceGroupManagersClient()

    # Get the current instance group
    instance_group_manager = compute_client.get(
        project=project_id,
        zone=zone,
        instance_group_manager=instance_group_name
    )
    
    # Calculate the new target size
    current_size = instance_group_manager.target_size
    new_size = current_size + scale_by

    # Update the instance group size
    operation = compute_client.resize(
        project=project_id,
        zone=zone,
        instance_group_manager=instance_group_name,
        size=new_size
    )

    # Wait for the operation to complete
    print(f"Scaling the instance group to {new_size} instances.")
    operation.result()  
    print(f"Successfully scaled the instance group to {new_size} instances.")

# Main function to monitor and scale based on CPU usage
def monitor_and_scale():
    try:
        while True:
            # Fetch the current CPU utilization
            cpu_usage = get_cpu_utilization(PROJECT_ID, ZONE, INSTANCE_GROUP_NAME)
            print(f"Current CPU utilization: {cpu_usage}%")

            if cpu_usage > THRESHOLD:
                # Scale up the instance group if CPU usage exceeds the threshold
                print("CPU usage exceeds threshold. Scaling up...")
                scale_instance_group(PROJECT_ID, ZONE, INSTANCE_GROUP_NAME, SCALE_UP)
            elif cpu_usage < (THRESHOLD - 20):  # Scale down if usage is 20% lower than the threshold
                print("CPU usage is low. Scaling down...")
                scale_instance_group(PROJECT_ID, ZONE, INSTANCE_GROUP_NAME, -SCALE_DOWN)
            else:
                print("CPU usage is normal. No scaling required.")
            
            # Sleep for 60 seconds before checking again
            time.sleep(60)
    
    except Exception as e:
        print(f"Error occurred during scaling: {str(e)}")

# Execute the monitoring and scaling process
if __name__ == "__main__":
    monitor_and_scale()
