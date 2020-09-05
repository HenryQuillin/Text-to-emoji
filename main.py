input = input("Enter a message with ':(' or ':)' ")


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)":"😊",
        ":(":"😔"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


print(emoji_converter(input))
