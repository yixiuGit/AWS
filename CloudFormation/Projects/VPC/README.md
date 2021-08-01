# Task List

- create a new VPC with cidr block 10.0.0.0/21
- create a new security group allow all traffic on port 80, 8000, 22
- create a new network ACL, not in use for this project
- create 4 subnets, 2 are public facing, 2 are private
- create 1 internet gateway associated with 2 public subnet
- create 2 elastic IPs
- create 2 NAT gateways and associated with 2 elastic IPs and 2 private subnets
- create 1 public route table, 1 public route, associate 2 public subnets with the route and route table and internet gateway
- create 2 private route tables, 2 private routes, associate 2 private subnets with each route/route table and individual NAT gateway
- create 1 EC2 launch template
- create 2 ASG, one for public, one for private
- create 2 target group, one for public, one for private
- create 2 application load balancer, one for public, one for private
- launch 4 EC2 instances, one for each subnet
- the load balancers do health check for each EC2

# Tricks

### EC2 launch template
- always use SecurityGroupIds instead of SecurityGroups
- when enable hibration, have to enable encryption as well
- Amazon linux 2 ebs devicename is /dev/xvba
- Amazon ubuntu devicename is /dev/sda
### EC2 instance profile
- when you create role to allow ec2 access s3 and assign the role to instance profile then associate the instance profile to EC2
  when try to install package on the EC2 using yum, it trys to install package from S3 which will fail the process
