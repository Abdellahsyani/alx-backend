import redis from 'redis'
import { promisify } from 'util'


const client = redis.createClient({
	host: 'localhost',
	port: 6379
});

const Cityscore = promisify(client.hgetall).bind(client)

client.on('error', (err) => {
	console.error("Redis client not connected to the server:", err);
});

client.on('ready', async () => {
	console.log("Redis client connected to the server");

	try {
		await client.hset('HolbertonSchools','Portland', 50,'Seattle', 80,'New York', 20,
			'Bogota', 20,
			'Cali', 40,
			'Paris', 2
		);
		const city = await Cityscore('HolbertonSchools');
		console.log(city);
	} catch (err) {
		console.error("Error setting the city scores:", err);
	} finally {
        client.quit(); // Close the connection to the Redis server
    }
});
