provider "aws" {
  region = var.region
}

resource "aws_instance" "flask_server" {
  ami                    = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type          = "t2.micro"
  associate_public_ip_address = true

  tags = {
    Name = "FlaskAppServer"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo amazon-linux-extras install docker -y
              sudo service docker start
              sudo usermod -a -G docker ec2-user
              docker run -d -p 80:5000 axel/flask-app
              EOF
}

