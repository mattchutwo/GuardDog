#Matthew Chu
import string, random
def passGen(size):
    chars=string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(size))

print(passGen(int(input('How long would  the password be?'))))
