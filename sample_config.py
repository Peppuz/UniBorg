import os

class Config(object):
    # Get this value from my.telegram.org! Please do not steal
    APP_ID = int(os.environ.get("APP_ID", "12345"))
    API_HASH = os.environ.get("API_HASH", "")
    # This is required for the plugins involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    # This is required for the hash to torrent file functionality to work.
    HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
    # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "UniBorg")
    # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_USERNAME = os.environ.get("IBM_WATSON_CRED_USERNAME", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # Send .get_id in any group to fill this value.
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID", "-100123456789"))
    # Send .get_id in any channel to fill this value. ReQuired for @Manuel15 inspiration to work!
    PRIVATE_CHANNEL_BOT_API_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_API_ID", "-100123456789"))
    #
    #
    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # TG API limit. A message can have maximum 4096 characters!
    TG_GLOBAL_ALBUM_LIMIT = 9
    # TG API limit. An album can have atmost 10 media!
