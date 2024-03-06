#!/usr/bin/yarn dev
import { createQueue } from "kue";
const redisConnection = {
  redis: {
    port: 6379,
    host: "127.0.0.1", // Change this to your Redis server host if necessary
    auth: "", // Add authentication if required
  },
};

// Create a queue with Redis connection options
const queue = createQueue(redisConnection, { name: "push_notification_code" });

const job = queue.create("push_notification_code", {
  phoneNumber: "08104899622",
  message: "Account registered",
});

job
  .on("enqueue", () => {
    console.log("Notification job created:", job.id);
  })
  .on("complete", () => {
    console.log("Notification job completed");
  })
  .on("failed attempt", () => {
    console.log("Notification job failed");
  });
job.save();
