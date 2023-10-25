terraform {
  backend "s3" {
    bucket         = "terraform-rds-1"
    region         = "ap-southeast-1"
    key            = "state/terraform.tfstate"
    dynamodb_table = "mycomponents_tf_lockid"
    encrypt        = true
  }
}