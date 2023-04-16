import boto3
import schedule
from operator import itemgetter


# Get all ec2 instance in the sydney region within this account
ec2_client = boto3.client('ec2', region_name="ap-southeast-2")

# Get all ec2 instance in the sydney region within this account
ec2_resource = boto3.resource('ec2', region_name="ap-southeast-2")

# Get current instance with tag = "Name" and value="production"
# Assume there are only one ec2 instance is in production 
my_instance = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'production',
            ]
        },
    ]
)

my_instance_id = my_instance['Reservations'][0]['Instances'][0]['InstanceId']
my_instance_availability_zone = my_instance['Reservations'][0]['Instances'][0]['Placement']['AvailabilityZone']

# Get the volumes of the current instance, assume that there are only one volume attached to the instance
volumes = ec2_client.describe_volumes(
     Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [my_instance_id]
        }
    ]
)

my_instance_volume_id = volumes ['Volumes'][0]['VolumeId']

#Get all snapshots of the volume
snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [my_instance_volume_id]
        }
    ]
)

# Get the latest snapshot 
latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]

new_volume = ec2_client.create_volume(
    AvailabilityZone = my_instance_availability_zone,
    SnapshotId=latest_snapshot['SnapshotId'],
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags':[
                {
                    'Key':"Name",
                    'Value':"production"
                }
            ]
        
        }
    ]
)


while True:
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    if vol.state == 'available':
        response =ec2_resource.Instance(my_instance_id).attach_volume(
            VolumeId=new_volume['VolumeId'],
            Device='/dev/xvdb'
        )
        break