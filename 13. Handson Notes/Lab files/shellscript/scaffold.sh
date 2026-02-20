#!/usr/bin/env bash

set -e

# =====================
# CONFIG
# =====================
PROJECT_NAME="vite-react-app"

echo "=============================="
echo " Scaffolding Vite React App"
echo "=============================="

# 1. Create Vite project (React + JavaScript)
CI=true npm create vite@latest "$PROJECT_NAME" --yes -- --template react --no-rolldown --no-interactive


# 2. Enter project
cd "$PROJECT_NAME"

echo
echo "=============================="
echo " Cleaning default files"
echo "=============================="

# 3. Delete public folder
rm -rf public

# 4. Delete assets folder
rm -rf src/assets

echo
echo "=============================="
echo " Updating source files"
echo "=============================="

# 5. Update App.jsx
cat > src/App.jsx << 'EOF'
function App() {
  return (
    <p>Hello world from Vite!!!</p>
  )
}

export default App
EOF

# 6. Update App.css
cat > src/App.css << 'EOF'
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}
EOF

# 7. Update main.css
cat > src/main.css << 'EOF'
body {
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 320px;
  min-height: 100vh;
}
EOF

echo
echo "=============================="
echo " Installing dependencies"
echo "=============================="

# 8. Install dependencies
npm install

echo
echo "=============================="
echo " Starting dev server"
echo "=============================="

# 9. Run dev server
npm run dev &
sleep 2
explorer.exe "http://localhost:5173"
wait
