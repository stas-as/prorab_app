import asyncio
import logging
import sys 
from handlers import cmd_start, echo_handler
from loader import dp, bot


async def main() -> None:
    """Регистрация обработчиков команды /start и эха.
    Запуск процесса опроса для получения обновлений с помощью dp.start_polling(bot)."""
    dp.message.register(cmd_start)
    dp.message.register(echo_handler)
    await dp.start_pooling(bot)
    
#астройка журналирования на уровне INFO.
#Запуск основной функции main с использованием asyncio.run().
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

