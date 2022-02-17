import config


async def log(guild, message):
    print(message)
    channel = guild.get_channel(config.CHANNEL_LOG) or await guild.fetch_channel(config.CHANNEL_LOG)
    if channel:
        await channel.send(message)
    else:
        print("log: Could not find the log channel")