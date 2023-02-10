import os
def getsettings(path: str) -> list:
    """ Retrive the settings for user preferences """
    with open(path, 'r') as colourconfig:
        a = colourconfig.readlines()
        temp = []
        for i in a:
            if '~' not in i:
                temp.append(i.strip())
        settings = []
        for i in temp:
            if '=' in i:
                settings.append(i.split(sep='=')[-1].strip())
        return settings


if __name__ == "__main__":
    print(os.path.dirname(__file__))
    print(getsettings('colourconfig.txt'))
