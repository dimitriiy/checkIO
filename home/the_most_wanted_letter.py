def checkio(text):
    env = {}
    for t in text:
        if t.isalpha():
            t = t.lower()
            if t not in env:
                env[t] = 1
            else:
                env[t] += 1
    max = 0
    world = text[0].lower()
    for l in env:
        if env[l] > max:
            world = l
            max = env[l]
        elif env[l] == max:
          if world > l:
            world = l
    return world
