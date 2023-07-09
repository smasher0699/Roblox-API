import asyncio
from roblox import Client
client = Client()

async def main(id):
    return await client.get_group(id)
    
obj = asyncio.get_event_loop().run_until_complete(main(13492190))


group = {
    ["Name"] == obj.name,
    ["Members"] == obj.get_members(),
}
print(group["Name"])