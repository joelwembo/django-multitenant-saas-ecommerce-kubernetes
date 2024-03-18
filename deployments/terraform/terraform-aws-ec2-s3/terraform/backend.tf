terraform {
  backend "s3" {
    bucket         = "django-app-8"
    region         = "ap-southeast-1"
    key            = "state/terraform.tfstate"
    dynamodb_table = "data_onents_tf_lockid"
    encrypt        = true
  }
}


