# Discord Bot intergration with Eureka (Euri)

**Euri** is an open-source, Eureka-powered Discord bot that allows you to intergrate [Eureka-AI](https://eureka-ai.co.uk) anywhere. Mention "Euri" in any message and she will respond with intelligent replied from Eureka's API

## Features

- **Message detection** - Just mention "Euri" in any message to trigger a response
- **Powered by Eureka-AI** - Uses Eureka-AI to generate respones
- **Typing effect** - Shows the typing effect within the discord app
- **Command support** - Quick linkes to documentation, contact email and our offical website.
- Build with [nextcord](https://pypi.org/project/nextcord/)

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Eureka-API/DiscordBot
cd DiscordBot
```

2. **Install dependencies**'

```bash
pip install -r requirements.txt
```

3. **Create `.env` file**

```env
DISCORD_TOKEN=your_discord_bot_token
EUREKA_API_KEY=your_eureka_api_key
```

4. **Run the bot**

```bash
python bot.py
```

## Example commands

- `Hey euri, how are you` - Triggers a reply from Eureka-AI
- `!ping` - Replies with `Pong!`
- `!support` - Shows an embed with support links

## Configuration

You can customise:

- Command prefix (currently `"!"`)
- Trigger keyword (`"euri" by default)
- Add your own custom commands or interactions within `bot.py`

## License

This project is under [MIT License](https://github.com/Eureka-API/DiscordBot/LICENSE)

## Powered by

[Eureka-AI](https://eureka-ai.co.uk) - Empowering developers with AI.
