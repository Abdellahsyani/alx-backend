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

client.subscribe("holberton school channel");
client.on('message', (channel, message) => {
	console.log(`Received message: ${message} on channel: ${channel}`);

	if (message === "KILL_SERVER") {
		client.unsubscribe();
		client.quit();
		console.log("Redis client unsubscribe and diseconnected from the channel");
	}
});
