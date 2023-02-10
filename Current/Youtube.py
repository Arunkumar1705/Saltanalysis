import os
import pickle


def Youtubelink(basicradical: str, acidradical: str) -> list:
    """ This helps generate links for the basic radical and the acid
    radical given as the argument to the function.
    It stores all the required links in a text file named youtubelinks.txt """

    basic_url = ''
    acidic_url = ''
    link_dict = {}
    b = basicradical.lower()
    a = acidradical.lower()

    PATH = os.path.dirname(__file__)
    filepath = os.path.join(PATH,'youtubelinks.bin')
    filename = filepath
    with open(filename, 'rb') as links:
        allinks = pickle.load(links)
        for link in allinks:

            radical, link_temp = link.split(sep='*')

            link_dict[radical] = link_temp.strip()

    basic_url = link_dict.get(b)
    acidic_url = link_dict.get(a)

    return [basic_url, acidic_url]
