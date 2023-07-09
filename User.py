import asyncio
from roblox import Client
client = Client()

async def main(name_or_id):
    if name_or_id.isnumeric():
        return await client.get_user(name_or_id)
    else:
        return await client.get_user_by_username(name_or_id)
    


obj = asyncio.get_event_loop().run_until_complete(main(1822437065)) #Replace the numbers with the person's id or the person's username (not display name) to find them
user = {
    "Name": obj.name, #Get the user's name
    "Display Name": obj.display_name, #Get the user's display name
    "ID": obj.id, #Get the User's id
    "Description": obj.description, #Get the account description
    "Created": obj.created, #Date account was created
    "Robux": obj.get_currency(), #Get how much robux they have
    "Follower_Count": obj.get_follower_count(), #How many followers the account has
    "Friend_Count": obj.get_friend_count(), #Gets how many friends the account has
    "Premium": obj.has_premium(), #Get if the user has premium or not
    "Banned": obj.is_banned, #Gets if the user is banned or not
    "Roles": obj.get_group_roles(), #Gets all of the user's group roles
    "Status": obj.get_status(), #Gets the user's current activity status
    "Badges": obj.get_roblox_badges(), #Gets all of the user's badges
    "Followers": obj.get_followers(), #Get all of the user's that follow the account
    "Friends": obj.get_friends(), #Gets all of the user's friends
    "Primary_Group_Role": obj.get_primary_group_role(), #Get the role of their primary group
    "Name_History": obj.username_history() #Gets the account's name history
}
print(user["Friends"])
