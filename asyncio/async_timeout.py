import asyncio

async def main():
    cmd = "ping -c 5 google.com".split()
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE)
    try:
        await asyncio.wait_for(proc.wait(), timeout=4.0)
    except asyncio.TimeoutError:
        proc.kill()
        print('timeout!')
    finally:
        async for data in proc.stdout:
            line = data.decode("utf-8").strip("\n")
            print(line)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()