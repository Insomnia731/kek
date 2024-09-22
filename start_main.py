import sys
import subprocess
import time
import random
import asyncio
import aiohttp

async def get_ip_info():
    try:
        async with session.get("https://ipinfo.io") as response:
            print(f"Response status: {response.status}")
            content_type = response.headers.get('Content-Type')
            print(f"Content-Type: {content_type}")

            if response.status == 200 and 'application/json' in content_type:
                data = await response.json()
                ip = data.get('ip')
                city = data.get('city')
                country = data.get('country')
                print(f"IP: {ip}")
                print(f"Location: {city}, {country}")
            else:
                error_text = await response.text()
                print(f"Error: {response.status}, {error_text}")
    except Exception as e:
        print(f"Error: {e}")

def run_main(arg=None):
    if arg is not None:
        subprocess.run([sys.executable, 'hello.py'] + arg)
    else:
        subprocess.run([sys.executable, 'hello.py'])

if __name__ == "__main__":
    asyncio.run(get_ip_info())
    time.sleep(random.randint(0, 5))  # 2 минуты
    run_main(["-a", "2"])  # Запускает main.py -a 2
