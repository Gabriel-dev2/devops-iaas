/* CONFIGURACAO DO BACKEND PARA O TERRAFORM https://www.terraform.io/docs/backends/types/s3.html */
terraform {
    backend "s3" {
        bucket = ""
        key    = ""
        region = "us-east-1"
    }
}

data "aws_caller_identity" "current" {}