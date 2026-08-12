const express = require("express");
const app = express();
const os = require("os");

const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
  const hostname = os.hostname();

  console.log(`Request served by pod: ${hostname}`);

  res.json({
    message: "Hello from Node + Docker + Kubernetes 🚀",
    hostname
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
