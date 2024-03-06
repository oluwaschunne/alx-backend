import redis from "redis";
import { promisify } from "util";
const client = redis.createClient();
client
  .on("connect", (val) => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

const setNewSchool = function (schoolName, value) {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async function (schoolName) {
  const asyncGet = promisify(client.get).bind(client);
  const val = await asyncGet(schoolName);
  console.log(val);
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
