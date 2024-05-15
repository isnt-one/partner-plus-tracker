import asyncio
from logger import setup_logger
from partner_plus import partner_plus_tracker

GOAL_CHECK_TIMEOUT = 600 # delay in seconds

log = setup_logger('core-app')

async def interval_task(interval, func):
    while True:
        asyncio.create_task(func)
        await asyncio.sleep(interval)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    coro = interval_task(GOAL_CHECK_TIMEOUT, partner_plus_tracker())

    try:
        loop.run_until_complete(coro)
    except (KeyboardInterrupt, Exception):
        pass
    finally:
        coro.close()
        tasks = asyncio.all_tasks(loop)
        expensive_tasks = {task for task in tasks if task._coro.__name__ != coro.__name__}
        loop.run_until_complete(asyncio.gather(*expensive_tasks))
        log.info('exiting app')

if __name__ == '__main__':
    main()