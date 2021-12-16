sudo yum update -y

# Amazon linux 2
sudo amazon-linux-extras install docker

# Amazon linux
# sudo yum install docker

# Use docker without sudo
# Have to logout and login after use this command
sudo usermod -a -G docker ec2-user
sudo restart
# Check docker command
# If you seen this error, Restart your instance
## Cannot connect to the Docker daemon. Is the docker daemon running on this host?
docker info
#sudo service docker start

# Install docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docekr-compose version

# Install git
sudo yum install git -y

# Clone repository
git clone https://github.com/4k1j/Coin-Data-Manager.git