import instaloader
 
loader = instaloader.Instaloader()
 
loader.login('harshita.pandey143', 'ironman')
 
profile = instaloader.Profile.from_username(loader.context,'harshita.pandey143')

followers = profile.get_followers()
 
for follower in followers:
    print(follower)

"""media = profile.mediacount
print(media)"""