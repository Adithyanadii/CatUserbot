import asyncio

from telethon import events

from userbot.utils import admin_cmd, register

# ================= CONSTANT =================


A = (
    "`▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `\n"
    "`████▌▄▌▄▐▐▌█████ `\n"
    "`████▌▄▌▄▐▐▌▀████ `\n"
    "`▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `\n"
)

B = (
    "`╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `\n"
    "`╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `\n"
    "`╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `\n"
    "`╱┗━━━┛╰━━━╯┗━━━┛╱ `\n"
)


D = (
    "`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
    "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
    "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `"
)

E = (
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n >🌹 *`"
    "`\n                    `"
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n🌹<\ *`"
)

F = (
    "`\n█████████`"
    "`\n█▄█████▄█`"
    "`\n█▼▼▼▼▼`"
    "`\n█  Hello Man`"
    "`\n█▲▲▲▲▲`"
    "`\n█████████`"
    "`\n ██   ██`"
)


@borg.on(admin_cmd(pattern="ml (.*)"))
async def kakashi(jisan):
    message = jisan.pattern_match.group(1)
    await jisan.edit(
        "`\n█████████`"
        "`\n█▄█████▄█`"
        "`\n█▼▼▼▼▼`"
        f"`\n█  {message}`"
        "`\n█▲▲▲▲▲`"
        "`\n█████████`"
        "`\n ██   ██`"
    )


@borg.on(admin_cmd(pattern=r"paw$"))
async def kakashi(jisan):
    await jisan.edit("`(=ↀωↀ=)`")


@borg.on(admin_cmd(pattern=r"tf$"))
async def kakashi(jisan):
    await jisan.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")


@borg.on(admin_cmd(pattern=r"gay$"))
async def kakashi(jisan):
    await jisan.edit(
        "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
        "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
        "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈U GAY`"
        "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈"
    )


@borg.on(admin_cmd(pattern=r"bot$"))
async def kakashi(jisan):
    await jisan.edit(
        "` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
        "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `"
    )


@borg.on(admin_cmd(pattern=r"hai$"))
async def kakashi(jisan):
    await jisan.edit(
        "\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HELLO!┊😀`"
        "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HELLO!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
        "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`"
    )


@borg.on(admin_cmd(pattern=r"nou$"))
async def kakashi(jisan):
    await jisan.edit(
        "`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
        "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
        "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
        "`\n┗━━┻━┛`"
    )


@borg.on(admin_cmd(pattern=r"sayhi$"))
async def kakashi(jisan):
    await jisan.edit(
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛🔷🔷🔷🔷️🔷🔷🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷💛💛️💛💛💛🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷️🔷💛"
        "\n💛🔷💛💛💛💛️💛🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
    )


@borg.on(admin_cmd(pattern=r"fail$"))
async def kakashi(fail):
    await fail.edit(A)


@borg.on(admin_cmd(pattern=r"lol$"))
async def kakashi(lol):
    await lol.edit(B)


@borg.on(admin_cmd(pattern=r"lool$"))
async def kakashi(loal):
    await loal.edit(D)


@borg.on(admin_cmd(pattern=r"nih$"))
async def kakashi(shit):
    await shit.edit(E)


@borg.on(admin_cmd(pattern=r"hallo$"))
async def kakashi(hello):
    await hello.edit(E)
