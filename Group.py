import asyncio
from roblox import Client
client = Client()

async def main(id):
    return await client.get_group(id)
    
obj = asyncio.get_event_loop().run_until_complete(main(13492190))


group = {
    "Name": obj.name,
    "Members": obj.get_members(),
    "Join_Requests": obj.get_join_requests(),
    "Members": obj.get_members(),
    "Roles": obj.get_roles(),
    "Settings": obj.get_settings(),
    "Description": obj.description,
    "Wall_Posts": obj.get_wall_posts(),
    "ID": obj.id,
    "Can_Join_Without_Request": obj.public_entry_allowed,
    "Owner": {
        "Name": obj.owner.name, #Get the user's name
        "Display Name": obj.owner.display_name, #Get the user's display name
        "ID": obj.owner.id, #Get the User's id
        "Robux": obj.owner.get_currency(), #Get how much robux they have
        "Follower_Count": obj.owner.get_follower_count(), #How many followers the account has
        "Friend_Count": obj.owner.get_friend_count(), #Gets how many friends the account has
        "Premium": obj.owner.has_premium(), #Get if the user has premium or not
        "Roles": obj.owner.get_group_roles(), #Gets all of the user's group roles
        "Status": obj.owner.get_status(), #Gets the user's current activity status
        "Badges": obj.owner.get_roblox_badges(), #Gets all of the user's badges
        "Followers": obj.owner.get_followers(), #Get all of the user's that follow the account
        "Friends": obj.owner.get_friends(), #Gets all of the user's friends
        "Primary_Group_Role": obj.owner.get_primary_group_role(), #Get the role of their primary group
    },
    "Member_Count": obj.member_count,
    "Shout": obj.shout,
}
print(group["Roles"])
print(group["Owner"]["Robux"])
