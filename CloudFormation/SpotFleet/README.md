# Spot Instance Fleet
Configure Spot Instance Fleet with cloudformation

# Usage
Files included: 

- initial.yml  - Basic yaml file to create spot instance fleet work with cloudformation
- SF_VPC.yml   - Create spot instance fleet within newly created VPC

# Key points

- instance created in new VPC won't get public ip
- need to define networkinterfaces in order to assign public ip to instance
- if define subnet and security group within networkinterfaces, cannot define the same outside
