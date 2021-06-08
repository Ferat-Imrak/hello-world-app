terraform {
  backend "gcs" {
    bucket  = "fuchicorp-ferat"
    prefix  = "qa/hello-world"
    project = "kubernetes-ferat"
  }
}
