from pyrogram.types import Message
from typing import Iterable

def is_spam(message: Message,
            testees: Iterable[str] = (
                'photo',
                'video',
                'audio',
                'vioce',
                'video_note'
            )) -> bool:
    return any([message.__dict__.get(testee) is not None
                for testee
                in testees])