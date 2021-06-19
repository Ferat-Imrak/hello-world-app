terraform {
  backend "gcs" {
    bucket  = "fuchicorp-ferat"
    prefix  = "dev/hello-world"
    project = "kubernetes-ferat"
  }
}
