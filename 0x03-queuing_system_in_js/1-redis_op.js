import redis from 'redis'

const client = redis.createClient({
        host: 'localhost',
        port: 6379
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, redis.print);
}

client.on('error', (err) => {
        console.error("Redis client not connected to the server: ERROR_MESSAGE", err);
});

client.on('ready', () => {
        console.log("Redis client connected to the server");
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
