import redis from 'redis'

const client = redis.createClient({
	host: 'localhost',
	port: 6379
});

client.on('error', (err) => {
	console.error("Redis client not connected to the server: ERROR_MESSAGE", err);
});

client.on('ready', () => {
	console.log("Redis client connected to the server");
});
