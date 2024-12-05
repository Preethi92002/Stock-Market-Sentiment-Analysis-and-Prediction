from telethon.sync import TelegramClient

# Replace these with your API ID and Hash
api_id = '27236094'  # Replace with your actual API ID
api_hash = 'ebd2c4c3308e3c46d4172f43a9ebbceb'  # Replace with your actual API Hash
phone = '+918688747633'  # Replace with your phone number

# Connect to Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def scrape_telegram(channel_name, limit=100):
    await client.start()
    user = await client.get_me()  # Correctly await this
    print(f"Connected as {user.first_name}")  # Access first_name after getting user

    # Get messages from the specified channel
    messages = []
    async for message in client.iter_messages(channel_name, limit=limit):
        if message.text:  # Ensure the message contains text
            messages.append(message.text)

    # Save messages to a text file
    with open('data/telegram_data.txt', 'w', encoding='utf-8') as f:
        for msg in messages:
            f.write(msg + '\n')

    print(f"Scraped {len(messages)} messages from {channel_name}")


# Replace with the correct Telegram channel username
with client:
    client.loop.run_until_complete(scrape_telegram('@StockMarketNews_Live1'))
