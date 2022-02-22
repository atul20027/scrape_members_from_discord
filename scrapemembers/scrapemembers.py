from lib2to3.pgen2 import token
import discum

bot = discum.Client(token="OTQ0MzIzNDgxNDMxMDcyNzg4.YhSIpA.p1pstoJADe9BighpiSzbFd1C9vk")

def close_after_fetching(resp,guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched=len(bot.gateway.session.guild(guild_id).members)

        print(str(lenmembersfetched) + 'fetched members')
        bot.gateway.removeCommand({'function':close_after_fetching,'params':{'guild_id':guild_id}})
        bot.gateway.close()

def get_members(guild_id,channel_id):
    bot.gateway.fetchMembers(guild_id,channel_id,keep='all',wait=1)
    bot.gateway.command({'function':close_after_fetching,'params':{'guild_id':guild_id}})   
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members=get_members("860356969521217536","860731058559516722")
memberslist=[]

for memberid in members:
    memberslist.append(memberid)


f= open('user.txt','a')
for element in memberslist:
    f.write(element + '\n')
f.close()        