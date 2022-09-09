from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

'''for session in  AudioUtilities.GetAllSessions():
    print(session.Process)'''

def main():
    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(0.5, None)
        if session.Process == "wmplayer.exe":
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(0.10, None)


if __name__ == "__main__":
    main()