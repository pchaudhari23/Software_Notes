#!/usr/bin/env bash

set -e

# =====================
# CONFIG
# =====================
REPO_URL="https://github.com/your-org/react-posts-app.git"
APP_DIR="react-posts-app"
BUILD_DIR="dist"                  # or "build"

EC2_USER="ec2-user"                # ubuntu for Ubuntu AMI
EC2_HOST="ec2-54-123-45-67.compute.amazonaws.com"
SSH_KEY="$HOME/.ssh/my-ec2-key.pem"

REMOTE_DIR="/var/www/react-posts-app"

echo "=============================="
echo " Checking Node & npm versions "
echo "=============================="

node -v
npm -v

echo
echo "=============================="
echo " Cloning repository "
echo "=============================="

if [ -d "$APP_DIR" ]; then
  echo "📁 Repo already exists, skipping clone"
else
  git clone "$REPO_URL"
fi

cd "$APP_DIR"

echo
echo "=============================="
echo " Installing dependencies "
echo "=============================="

npm install

echo
echo "=============================="
echo " Building React app "
echo "=============================="

npm run build

if [ ! -d "$BUILD_DIR" ]; then
  echo "❌ Build directory not found"
  exit 1
fi

echo
echo "=============================="
echo " Deploying to AWS EC2 "
echo "=============================="

ssh -i "$SSH_KEY" "$EC2_USER@$EC2_HOST" << EOF
  sudo mkdir -p $REMOTE_DIR
  sudo chown -R $EC2_USER:$EC2_USER $REMOTE_DIR
EOF

rsync -avz --delete \
  -e "ssh -i $SSH_KEY" \
  "$BUILD_DIR/" \
  "$EC2_USER@$EC2_HOST:$REMOTE_DIR"

ssh -i "$SSH_KEY" "$EC2_USER@$EC2_HOST" << EOF
  sudo systemctl reload nginx || true
EOF

echo "✅ EC2 deployment complete"
