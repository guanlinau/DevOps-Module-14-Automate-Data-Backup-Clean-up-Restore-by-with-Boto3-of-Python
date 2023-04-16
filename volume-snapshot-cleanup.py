import boto3
import schedule
from operator import itemgetter


# Get all ec2 instance in the sydney region within this account
ec2_client = boto3.client('ec2', region_name="ap-southeast-2")

# Define a function to invoke the cleanup task automatically in a specified time
def scheduled_cleanup_snapshots():

    # Filter all the volumes with tag in production environment within this region
    volumes= ec2_client.describe_volumes(
            Filters=[
                {
                    "Name":"tag:Name",
                    "Values":['production']
                }
            ]
        )

    # Iterate the volumes

    for volume in volumes['Volumes']:
        snaps = ec2_client.describe_snapshots(
            Filters=[
                {
                    'Name': 'volume-id',
                    'Values': [
                        volume['VolumeId'],
                    ]
                },
            ],
            OwnerIds=['self']
        )
        # Sort the snapshots by snapsort created_time via operator module and sorted function
        snapshots_sorted = sorted(snaps['Snapshots'], key=itemgetter('StartTime'), reverse=True)
        # Delete all the rest of snapshots except the two latest ones.
        for snapshot_sorted in snapshots_sorted[2:]:
            ec2_client.delete_snapshot(SnapshotId=snapshot_sorted['SnapshotId'])

schedule.every().wednesday.at("9:00").do(scheduled_cleanup_snapshots)

while True:
    schedule.run_pending()
