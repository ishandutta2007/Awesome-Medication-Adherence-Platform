import re

with open("README.md", "r", encoding="utf-8") as f:
    text = f.read()

# Replace sindresorhus link
text = text.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

print("Replaced sindresorhus link if present")
