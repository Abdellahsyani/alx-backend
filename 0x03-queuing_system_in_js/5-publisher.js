import redis from 'redis'

const client = redis.createClient({
	host: 'localhost',
	port: 6379
});

client.on('error', (err) => {
	console.error("Redis client not connected to the server: ERROR MESSAGE", err);
});

client.on('ready', () => {
	console.log("Redis client connected to the server");
});

function publishMessage(message, time) {
	setTimeout(() => {
		console.log(`About to send ${message}`);
		client.publish('holberton school channel', message, (err, reply) => {
			if (err) {
				console.error("Error publishing the message", err);
			}
		});
	}, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
