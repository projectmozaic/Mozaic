#!/bin/bash
# define variables
key_id="AKIAJJP733QM2AGEE2YA"
access_key="rhuCQ/n63u3H35A1EtEvV1oqp8bSkHu/Bn3UFPrI"
region_name="us-west-2"
key_name="1-key"
echo $key_id
# aws ec2 describe-security-groups --group-names my-sg > /dev/null
output="$(aws ec2 describe-security-groups --group-names my1-sg)"
echo ${output:0:1}
if [ "${output:0:1}" != "{" ]; then
	output="$(aws ec2 create-security-group --group-name my1-sg --description "security group for development environment in EC2")"
fi
output="$(aws ec2 describe-security-groups --group-names my1-sg)"
# echo $output
group_id="$(echo $output | grep -Po '(?<="GroupId": ")[^"]*')"
echo $group_id
aws ec2 create-key-pair --key-name $key_name --query 'KeyMaterial' --output text > $key_name.pem
chmod 400 $key_name.pem
sleep 5s
instance_Id="$(aws ec2 run-instances --image-id ami-29ebb519 --security-group-ids $group_id --count 1 --instance-type t2.micro --key-name $key_name --query 'Instances[0].InstanceId')"
echo $instance_Id
sleep 10s
# get_ip_command="aws ec2 describe-instances --instance-ids ${instance_Id:1:-1} --query 'Reservations[0].Instances[0].PublicIpAddress'"
# ip_address="$($get_ip_command)"
# echo $ip_address
aws ec2 describe-instances --instance-ids ${instance_Id:1:-1} --query 'Reservations[0].Instances[0].PublicIpAddress'
# Would need to save the ip address
# aws ec2 create-security-group --group-name my-sg --description "security group for development environment in EC2"