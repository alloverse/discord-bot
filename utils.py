import config


async def output(guild, message):
    print(message)
    channel = guild.get_channel(config.CHANNEL_OUTPUT) or await guild.fetch_channel(config.CHANNEL_OUTPUT)
    if channel:
        await channel.send(message)
    else:
        await log("output: Could not find the output channel")

async def log(guild, message):
    print(message)
    channel = guild.get_channel(config.CHANNEL_LOG) or await guild.fetch_channel(config.CHANNEL_LOG)
    if channel:
        await channel.send(message)
    else:
        print("log: Could not find the log channel")