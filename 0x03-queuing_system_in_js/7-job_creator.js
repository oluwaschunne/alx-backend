#!/usr/bin/yarn dev
import { createQueue } from "kue";

const jobs = [
  {
    phoneNumber: "4153518780",
    message: "This is the code 1234 to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153518743",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4153538781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153118782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4153718781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4159518782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4158718781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153818782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4154318781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4151218782",
    message: "This is the code 4321 to verify your account",
  },
];
const redisConnection = {
  redis: {
    port: 6379,
    host: "127.0.0.1", // Change this to your Redis server host if necessary
    auth: "", // Add authentication if required
  },
};

const queue = createQueue({
  name: "push_notification_code_2",
});

for (const job of jobs) {
  const new_job = queue.create("push_notification_code_2", job);
  new_job
    .on("enqueue", () => {
      console.log(`Notification job created: ${new_job.id}`);
    })
    .on("complete", (result) => {
      console.log(`Notification job ${new_job.id} completed`);
    })
    .on("failed", (err) => {
      console.log(`Notification job ${new_job.id} failed: ${err}`);
    })
    .on("progress", (progress, data) => {
      console.log(`Notification job ${new_job.id} ${progress}% complete`);
    });

  new_job.save();
}
