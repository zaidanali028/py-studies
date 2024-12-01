from config.constants import MY_IP, MY_SSH_KEY_NAME, AWS_REGION
from services.vpc_service import create_vpc, create_subnet
from services.ec2_service import create_security_group, create_ec2_instance, associate_elastic_ip
from services.s3_service import create_s3_bucket
from utils.outputs import print_resource_outputs
import boto3

def main():
    """
    Main entry point for provisioning AWS infrastructure using Boto3.
    Steps include creating a VPC, subnets, security groups, EC2 instances, 
    associating Elastic IPs, and creating an S3 bucket.
    """
    # Initialize Boto3 session with the desired AWS region
    boto3.setup_default_session(region_name=AWS_REGION)

    try:
        # Step 1: Creating VPC and Subnets
        vpc_id = create_vpc()
        public_subnet_id = create_subnet(vpc_id, "10.0.1.0/24", "us-east-1a", "PUBLIC")
        private_subnet_id = create_subnet(vpc_id, "10.0.2.0/24", "us-east-1a", "PRIVATE")

        # Step 2: Creating Security Groups
        bastion_sg_id = create_security_group(
            vpc_id, "BastionSG", "Security group for Bastion", {
                "ingress": [{"protocol": "tcp", "port": 22, "cidr": f"{MY_IP}/32"}]
            }
        )

        frontend_sg_id = create_security_group(
            vpc_id, "FrontendSG", "Security group for Frontend", {
                "ingress": [
                    {"protocol": "tcp", "port": 22, "cidr": f"{MY_IP}/32"},
                    {"protocol": "tcp", "port": 80, "cidr": "0.0.0.0/0"}
                ]
            }
        )

        backend_sg_id = create_security_group(
            vpc_id, "BackendSG", "Security group for Backend", {
                "ingress": [
                    {"protocol": "tcp", "port": 8080, "cidr": "10.0.1.0/24"}
                ]
            }
        )

        # Step 3: Create EC2 Instances
        bastion_instance_id = create_ec2_instance(
            public_subnet_id, bastion_sg_id, "t2.micro", MY_SSH_KEY_NAME, "ami-12345678"
        )
        associate_elastic_ip(bastion_instance_id)

        frontend_instance_id = create_ec2_instance(
            public_subnet_id, frontend_sg_id, "t2.micro", MY_SSH_KEY_NAME, "ami-12345678"
        )
        associate_elastic_ip(frontend_instance_id)

        backend_instance_id = create_ec2_instance(
            private_subnet_id, backend_sg_id, "t2.micro", MY_SSH_KEY_NAME, "ami-12345678"
        )

        # Step 4: Create S3 Bucket
        s3_bucket_name = create_s3_bucket("my-unique-bucket-name")

        # Step 5: Outputs
        print_resource_outputs({
            "VPCID": vpc_id,
            "PublicSubnetID": public_subnet_id,
            "PrivateSubnetID": private_subnet_id,
            "BastionInstanceID": bastion_instance_id,
            "FrontendInstanceID": frontend_instance_id,
            "BackendInstanceID": backend_instance_id,
            "S3BucketName": s3_bucket_name
        })

    except Exception as e:
        # Gracefully handle errors and print the message
        print(f"An error occurred: {e}")


# running the main function to provision AWS infrastructure
main()
