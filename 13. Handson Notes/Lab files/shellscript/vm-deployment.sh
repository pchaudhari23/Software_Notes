#!/usr/bin/env bash

set -e

# =====================
# CONFIG
# =====================
REPO_URL="https://github.com/your-org/react-posts-app.git"
APP_DIR="react-posts-app"
BUILD_DIR="dist"              # or "build" for CRA

REMOTE_USER="deploy"
REMOTE_IP="192.168.1.50"
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
echo " Deploying to on-prem VM "
echo "=============================="

ssh "$REMOTE_USER@$REMOTE_IP" << EOF
  sudo mkdir -p $REMOTE_DIR
  sudo chown -R $REMOTE_USER:$REMOTE_USER $REMOTE_DIR
EOF

rsync -avz --delete \
  "$BUILD_DIR/" \
  "$REMOTE_USER@$REMOTE_IP:$REMOTE_DIR"

ssh "$REMOTE_USER@$REMOTE_IP" << EOF
  sudo systemctl reload nginx || true
EOF

echo "✅ On-prem deployment complete"
