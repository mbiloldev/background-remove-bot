import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from rembg import remove
from PIL import Image
import io

BOT_TOKEN = "YOUR_BOT_TOKEN"
= await bot.get_file(photo.file_id)
    file_bytes = await bot.download_file(file.file_path)
    
    input_image = Image.open(file_bytes)
    output_image = remove(input_image)
    

    await message.answer_document(
        types.BufferedInputFile(output_bytes.read(), filename="result.png")
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
