import instaloader

ig=instaloader.Instaloader()
for i in ('harshita.pandey143', 'dhriti_awasthi', 'coco_mocco'):
    profile = i
    ig.download_profile(profile, profile_pic_only=True)
    print("Done for-\t",i)