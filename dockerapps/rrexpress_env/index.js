const app = require("express")();
const appid = process.env.APPID;

app.get("/", (req,res) =>
res.send(`Port ${appid} for /.`))

app.get("/app1", (req,res) =>
res.send(`Port ${appid} for /app1.`))

app.get("/app2", (req,res) =>
res.send(`Port ${appid} for /app2.`))

app.get("/admin", (req,res) =>
res.send(`Port ${appid} for /admin.`))

app.listen(9000, ()=>console.log(`${appid} has a default listening port 9000`))
