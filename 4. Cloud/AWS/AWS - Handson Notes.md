1. Create an EC2 instance and SSH into it. Create Security group rules to allow custom TCP port.
2. Install necessary dependencies
3. Take clone of repo, enter the repo and install deps and create build
4. Create a directory and copy the build to it
5. Create nginx config file and add the configuration

Deploying a react app on EC2
Deploying a node app on EC2

SSH into EC2:

1. Navigate to the folder where the ssh key is stored using windows powershell
2. ssh -i "SSH_Key_filename.pem" ec2-user@public_ip_of_ec2

   Amazon linux:sudo yum update -y => sudo yum install -y ...
   Ubuntu:sudo apt update => sudo apt-get install -y ....

3. sudo yum install -y nodejs git
4. git clone `<repo url>`
5. cd repo and npm install

install - nodejs, npm, git, nginx

- add all tcp inbound rule in SG to allow different ports
- a seperate directory is required to store the build.
- then nginx will serve contents of the build folder to browser

---

configuring nginx:

1. sudo yum install -y nginx
2. sudo systemctl start nginx
3. sudo systemctl enable nginx
4. check the public ip/dns - nginx welcome page should appear
5. Create a directory to store your production build: sudo mkdir -p /var/www/html/your-app
6. Copy your build files from the dist directory to Nginx's default web root: sudo cp -r /path/to/your/project/dist/_ /var/www/html/your-app/
   /home/ec2-user/jenkins-react/dist/_
7. Configure Nginx to serve your app. Open the Nginx configuration file and update it: sudo nano /etc/nginx/nginx.conf
8. Test nginx config: sudo nginx -t
9. Restart nginx: sudo systemctl restart nginx

home path - /home/ec2-user
nginx conf path - /etc/nginx/nginx.conf
build folder path - /var/www/html/

nginx config file:

user nginx;
worker_processes auto;
pid /var/run/nginx.pid;

events {
worker_connections 1024;
}

http {
include mime.types;
default_type application/octet-stream;

    # Your other configurations here, such as log formats

    server {
        listen 80;
        server_name 18.234.113.200;
        root /var/www/html/react-deployment/;
        index index.html;

    location / {
            try_files $uri /index.html;
        }
    }

}

---

To get path - use pwd or find file_name
