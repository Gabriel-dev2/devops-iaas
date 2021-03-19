##### Provider Configurations ######
provider "aws" {
    region                  = local.region
    shared_credentials_file = "$HOME/.aws/credentials"
}
