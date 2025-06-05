import configparser
from Engine.Scripts.Global.Constants import Binaries

class Ini:
    def __init__(self):
        self.ConfigParser = None

    def LoadIni(self, Path: str):
        self.ConfigParser = configparser.ConfigParser()
        self.ConfigParser.read(Path)

    def GetGameSettings(self):
        GameSettings = self.ConfigParser["Game"]
        GameMap      = {
            "Logging": GameSettings.getboolean("Logging"),
            "Debug":   GameSettings.getboolean("Debug")
        }
        return GameMap

    def GetVideoSettings(self):
        VideoSettings = self.ConfigParser["Video"]
        VideoMap      = {
            "Fullscreen":    VideoSettings.getboolean("Fullscreen"),
            "Bordered":      VideoSettings.getboolean("Bordered"),
            "ExFullscreen":  VideoSettings.getboolean("ExFullscreen"),
            "VSync":         VideoSettings.getboolean("VSync"),
            "WinWidth":      VideoSettings.getint("WinWidth"),
            "WinHeight":     VideoSettings.getint("WinHeight"),
            "RefreshRate":   VideoSettings.getint("RefreshRate"),
            "ViewportWidth": VideoSettings.getint("ViewportWidth")
        }
        return VideoMap

    def GetAudioSettings(self):
        AudioSettings = self.ConfigParser["Video"]
        AudioMap      = {
            "MusicStreaming": AudioSettings.getboolean("MusicStreaming"),
            "MusicVolume":    AudioSettings.getint("MusicVolume"),
            "SFXVolume":      AudioSettings.getint("SFXVolume")
        }
        return AudioMap

    def GetInputSettings(self):
        IS = []
        for Player in range(1, 5):
            if self.ConfigParser.has_section(f"Input{Player}"):
                InputData = self.ConfigParser[f"Input{Player}"]
                InputMap  = {
                    "Type":         InputData.get("Type"),
                    "ButtonUp":     InputData.get("ButtonUp"),
                    "ButtonDown":   InputData.get("ButtonDown"),
                    "ButtonLeft":   InputData.get("ButtonLeft"),
                    "ButtonRight":  InputData.get("ButtonRight"),
                    "ButtonA":      InputData.get("ButtonA"),
                    "ButtonB":      InputData.get("ButtonB"),
                    "ButtonC":      InputData.get("ButtonC"),
                    "ButtonX":      InputData.get("ButtonX"),
                    "ButtonY":      InputData.get("ButtonY"),
                    "ButtonZ":      InputData.get("ButtonZ"),
                    "ButtonStart":  InputData.get("ButtonStart"),
                    "ButtonSelect": InputData.get("ButtonSelect")
                }
                IS.append(InputMap)
        return IS
    
    def GetGameConfig(self):
        GameConfig = self.ConfigParser["GameConfig"]
        GameConfigMap = {
            "Name":     GameConfig.get("Name"),
            "Version":  GameConfig.getint("Version"),
            "Icon":     GameConfig.get("Icon")
        }
        return GameConfigMap
    
    def GetSceneConfig(self):
        Categories = {}
        for s in self.ConfigParser.sections():
            section = str(s)
            if section.startswith("Category"):
                Categories[section[9:]] = []
            elif section.startswith("Scene"):
                Category = self.ConfigParser[section].get("Category").strip('"')
                Categories[Category].append(section[6:])
        return Categories
                

class Config:
    def __init__(self):
        self.Config = None
        self.Path   = None

    def LoadConfig(self, Path: str):
        self.Path = Path
        self.Config = Ini()
        self.Config.LoadIni(Path)

    def GetGameConfigData(self):
        return self.Config.GetGameConfig()

    def GetSceneConfigData(self):
        return self.Config.GetSceneConfig()

class Scene:
    def __init__(self):
        self.BackgroundColor = None