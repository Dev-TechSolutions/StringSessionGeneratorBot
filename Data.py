from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to generate Pyrogram and Telethon String Session. Use the below buttons to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("โ Start Generating Session โ", callback_data="Generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="Home")]
    ]

    generate_button = [
        [InlineKeyboardButton("๐ฅ Start Generating Session ๐ฅ", callback_data="generate")]
    ]

    support_button = [
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("๐ฅ Start Generating Session ๐ฅ", callback_data="generate")],
        [InlineKeyboardButton("๐จโ๐ป Repo ๐จโ๐ป", url="https://github.com/Dev-TechSolutions/StringSessionGenerator")],
        [
            InlineKeyboardButton("How to Use โ", callback_data="help"),
            InlineKeyboardButton(" About", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
ยป Click the below button or use /generate command to start generating session!
ยป Click the required button; [Pyrogram/Telethon]
ยป Enter the required variables when asked.
"""

    # About Message
    ABOUT = """
๐จโ๐ป **About Me** 

A Telegram Bot to Generate Pyrogram and Telethon String Session...

[Pyrogram](docs.pyrogram.org)
[Telethon](docs.telethon.org)

Language : [Python](www.python.org)
"""