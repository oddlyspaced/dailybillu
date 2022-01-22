from youtubesearchpython import VideoDurationFilter

class Config :
    DEBUG = True
    QUERY_FILE = "queries"
    SEARCH_RESULT_DURATION = VideoDurationFilter.short
    SEARCH_QUERY_LIMIT = 1
    CLIENT_EMAIL = "randomcat@meowmeow.com" # Mail used to send out email
    RECEIVER_EMAIL = ["goodhuman@ilovecats.com"] # Mail(s) to which the email would be sent