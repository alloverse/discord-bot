import config

def button_id(view: str, id: int) -> str:
    return f"{config.BOT_NAME}:{view}:{id}"
