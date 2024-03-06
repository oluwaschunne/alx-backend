import redis from "redis";
const client = redis.createClient();
client
  .on("connect", (val) => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });
client.subscribe("holberton school channel");

client.on("message", (channe, message) => {
  console.log(message);
  if (message === "KILL_SERVER") {
    client.unsubscribe("holberton school channel");
    client.quit();
  }
});
