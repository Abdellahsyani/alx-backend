import redis from 'redis'
import { promisify } from 'util'

const client = redis.createClient({
        host: 'localhost',
        port: 6379
});

function setNewSchool(schoolName, value) {
        client.set(schoolName, value, redis.print);
}

const displaySchoolValue = promisify(client.get).bind(client);

async function getAsync(schoolName) {
	try {
		const value = await displaySchoolValue(schoolName);
		console.log(value);
	} catch (err) {
		console.error("Error to get the value", err);
	}
}

client.on('error', (err) => {
        console.error("Redis client not connected to the server: ERROR_MESSAGE", err);
});

client.on('ready', () => {
        console.log("Redis client connected to the server");
});

getAsync('Holberton');

setNewSchool('HolbertonSanFrancisco', '100');
getAsync('HolbertonSanFrancisco');
