import emoji
from emoji import emojize

# print(emoji.emojize("Python is :thumbs_up:"))
# print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
print(emoji.demojize('Python is 👍'))
