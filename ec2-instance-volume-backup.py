import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="ap-southeast-2")


def create_ec2_instance_volume_snapshot():
    volumes= ec2_client.describe_volumes(
        Filters=[
            {
                "Name":"tag:Name",
                "Values":['production']
            }
        ]
    )

    for volume in volumes['Volumes']:
        new_volume_snapshot = ec2_client.create_snapshot(VolumeId=volume['VolumeId'])
        print(new_volume_snapshot)

schedule.every(20).seconds.do(create_ec2_instance_volume_snapshot)

while True:
    schedule.run_pending()
