#Bloque que contiene los settings del terraform incluyendo los providers
terraform {
  #Listado de providers que necesitará nuestro terraform
  required_providers {
    #Nombre arbitrario del provider
    aws = {
      #Source (nombre oficial) del provider
      source = "hashicorp/aws"
      #Version (opcional) del source
      version = "~> 4.16"
    }
  }

  #Versión del terraform (opcional)
  required_version = ">= 1.2.0"
}
#Configuración del provider declarado arriba
provider "aws" {
  region = "us-west-2"
}
#Definición de los componentes tanto fisicos como virtuales.
resource "aws_instance" "app_server" { #Tipo de recurso y nombre del recurso para crear un ID, aws_instance.app_server.
  ami           = "ami-08d70e59c07c61a3a"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
