#!/usr/bin/env bash

# Exit immediately if any command fails
set -e

echo "=============================="
echo " Checking Node & npm versions "
echo "=============================="

# 1. Check Node version
if ! command -v node >/dev/null 2>&1; then
  echo "❌ Node.js is not installed"
  exit 1
fi
echo "✅ Node version: $(node -v)"

# 2. Check npm version
if ! command -v npm >/dev/null 2>&1; then
  echo "❌ npm is not installed"
  exit 1
fi
echo "✅ npm version: $(npm -v)"

echo
echo "=============================="
echo " Cloning React repo "
echo "=============================="

# 3. Clone the GitHub React repo
# 👉 Replace this URL with the actual repo if needed
REPO_URL="https://github.com/PritamChaudhari23/react-posts-app.git"

if [ -d "react-posts-app" ]; then
  echo "📁 Repo already exists. Skipping clone."
else
  git clone "$REPO_URL"
fi

# 4. cd into repo
cd react-posts-app

echo
echo "=============================="
echo " Installing dependencies "
echo "=============================="

# 5. npm install
npm install

echo
echo "=============================="
echo " Starting dev server "
echo "=============================="

# 6. npm run dev (Vite)
npm start &

# Give the dev server a moment to start
sleep 5

echo
echo "=============================="
echo " Opening browser "
echo "=============================="

# 7. Open browser on localhost:3000 (Git Bash / Windows)
explorer.exe "http://localhost:3000"

echo
echo "🚀 React app is running at http://localhost:3000"
