# Packer can be run from any machine with access to AWS Credentials
# Packer doesn't need to be run on a machine in the AWS environment

# For more information please see:
# https://www.packer.io/intro/getting-started/setup.html
# https://www.packer.io/intro/getting-started/build-image.html

# packer validate template.json
# packer build template.json

# an initial source-ami must be created before you can run packer
# the source-ami can be easily created through the aws console

# Note after a build, it takes ~5 minutes for the ami to appear in the 
# EC2 management console

# using the cli to describe-images will likely return faster
# aws ec2 describe-images ec2 describe-images --owners your_aws_id

