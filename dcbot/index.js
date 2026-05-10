// index.js'e eklenicek
const http = require("http");

http
  .createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("oksionthebeat");
  })
  .listen(3000);
  const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

client.on('ready', () => {
  console.log(`${client.user.tag} olarak giriş yapıldı!`);
});

client.on('messageCreate', (message) => {
  if (message.content === '!merhaba') {
    message.reply('Selam! Replit üzerinden JavaScript ile çalışıyorum.');
  }
});

// Buraya kendi bot token'ını yaz
client.login('MTQ4MjY2NTUzMDA5MDU4NjE5Mg.Gp0sxU.owJce2qNb7Os8hQD-4M18QP-74t_OxoXfoYNjE');