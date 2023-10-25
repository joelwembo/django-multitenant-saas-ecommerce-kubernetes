variable "aws_region" {
  type    = string
  default = "ap-southeast-1"
}
variable "cidr_block" {
  default = "10.0.0.0/16"
}
variable "subnet" {
  default = "10.0.0.0/24"
}
variable "instance_type" {
  type    = string
  default = "t2.micro"
}
variable "aws_availability_zone" {
  type    = string
  default = "ap-southeast-1b"
}

variable "access_key" {
  default = "****"
}
variable "secret_key" {
  default = "*****"
}

variable "bucket" {
  default = "bucket"
}