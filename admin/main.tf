variable "token" {
  type     = string
  nullable = false
}

provider "github" {
  token = var.token # or `GITHUB_TOKEN`
  owner = "conda"
}

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
  required_version = "~> 1.3.7"
}
