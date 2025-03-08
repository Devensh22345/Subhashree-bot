from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg 
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://envs.sh/iGX.mp4',
    'https://envs.sh/iG6.mp4',
    'https://envs.sh/iKh.mp4',
    'https://envs.sh/iK2.mp4',
    'https://envs.sh/iKF.mp4'
]

txt = ['hello']
txt1 = ['<b><blockquote> 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐭𝐨 𝐆𝐞𝐭 𝐕𝐢𝐫𝐚𝐥 𝐯𝐢𝐝𝐞𝐨 \n𝐉𝐮𝐬𝐭 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 👇👇 </blockquote>\n /START</b>']
txt2 = [
    '<b><blockquote> 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐭𝐨 𝐆𝐞𝐭 𝐕𝐢𝐫𝐚𝐥 𝐯𝐢𝐝𝐞𝐨 \n𝐉𝐮𝐬𝐭 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 👇👇 </blockquote>\n /START</b>'
]

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m: Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        print(f"Received join request from {kk.id} in {op.id}")

        # Image URL
        img = random.choice(gif)

        # Inline Keyboard
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💦 𝐆𝐄𝐓 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 𝐋𝐈𝐍𝐊🍑", url="https://t.me/video_call_robot?start=1")],
                [InlineKeyboardButton("𝐕𝐢𝐫𝐚𝐥 𝐯𝐢𝐝𝐞𝐨 𝐌𝐒𝐒", url="https://t.me/video_call_robot?start=1")],
            ]
        )

        text1 = random.choice(txt1)
        text2 = random.choice(txt2)

        await app.send_video(
            kk.id,
            img,
            caption="<blockquote></b>𝐈𝐧𝐬𝐭𝐚𝐧𝐭 𝐕𝐢𝐫𝐚𝐥 𝐌𝐨𝐝𝐞𝐥 𝐕𝐢𝐝𝐞𝐨 \n\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐓𝐨 𝐆𝐞𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤 👇👇</blockquote></b>",
            reply_markup=keyboard
        )
        await app.send_message(kk.id, text1)

        add_user(kk.id)

    except errors.PeerIdInvalid:
        print("User hasn't started the bot yet.")
    except Exception as err:
        print(f"Error: {err}")



@app.on_message(filters.command("start"))
async def start(_, m: Message):
    try:
        user = m.from_user
        log_msg = (
            f"📢 **New User Started Bot**\n\n"
            f"👤 Name: [{user.first_name}](tg://user?id={user.id})\n"
            f"🆔 User ID: `{user.id}`\n"
            f"🌍 Username: @{user.username if user.username else 'None'}"
        )
        await app.send_message(cfg.LOG_CHANNEL, log_msg)

        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐯𝐢𝐝𝐞𝐨", url="https://t.me/+QN3ive_lL1RjZGE1")],
                    [InlineKeyboardButton("𝐆𝐞𝐭 𝐌𝐨𝐫𝐞 𝐕𝐢𝐝𝐞𝐨𝐬", url="https://t.me/+QN3ive_lL1RjZGE1")]
                ]
            )

            add_user(user.id)
            await m.reply_video(
                random.choice(gif),
                caption=f"<b><blockquote>𝒀𝒐𝒖𝒓 𝑽𝒊𝒅𝒆𝒐 𝒊𝒔 𝑹𝒆𝒂𝒅𝒚. 𝑪𝒍𝒊𝒄𝒌 𝒉𝒆𝒓𝒆 𝑻𝒐 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅 👇👇👇</blockquote></b>",
                reply_markup=keyboard
            )

        elif m.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/+QN3ive_lL1RjZGE1")]]
            )
            add_group(m.chat.id)
            await m.reply_text(f"**🦊 Hello {user.first_name}!\nWrite me in private for more details**", reply_markup=keyboard)

        print(f"{user.first_name} started the bot!")

    except Exception as err:
        print(f"Error: {err}")




@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m: Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)


@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0

    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            await m.reply_to_message.copy(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now!")
app.run()
