from enum import Enum

# Enum class that defines modes in which the bot can work
class Mode(Enum):
    NONE = 0
    STUDENT_HELPER = 1
    DALLE = 2
    WHISPER = 3
