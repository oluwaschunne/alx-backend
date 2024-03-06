import redis from "redis";
const client = redis.createClient();
client
  .on("connect", (val) => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

const dict = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const key of Object.keys(dict)) {
  client.hset("HolbertonSchools", key, dict[key], redis.print);
}
client.hgetall("HolbertonSchools", (err, val) => {
  console.log(val);
});
