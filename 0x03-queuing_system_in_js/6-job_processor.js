import { createQueue } from "kue";
const redisConnection = {
  redis: {
    port: 6379,
    host: "127.0.0.1", // Change this to your Redis server host if necessary
    auth: "", // Add authentication if required
  },
};

const queue = createQueue(redisConnection);

const sendNotification = function (phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};
queue.process("push_notification_code", (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
