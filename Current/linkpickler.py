import pickle
import os

if __name__ == "__main__":
    PATH  = os.path.dirname(__file__) + 'youtubelinks.bin'
    obj = [
        'ammonium*https://www.youtube.com/watch?v=GTZBs3iZgg0',
        'lead*https://www.youtube.com/watch?v=f7PfeaA8kow',
        'copper*https://www.youtube.com/watch?v=czm2pwjiftc',
        'arsenic*https://www.gzaas.com/LHlLIl5S',
        'ferric*https://www.youtube.com/watch?v=PPG9XIp0HhY',
        'aluminium*https://www.youtube.com/watch?v=0HPi7X2yhbw',
        'zinc*https://www.youtube.com/watch?v=v7_glUDP_sk',
        'cobalt*https://www.youtube.com/watch?v=MRELKbMFF_E',
        'nickel*https://www.youtube.com/watch?v=TVNRUMMCg4o',
        'manganese*https://www.youtube.com/watch?v=Abcyr8AqwAc',
        'barium*https://www.youtube.com/watch?v=gaamIjai20o',
        'strontium*https://www.youtube.com/watch?v=M8YqOhM2J54',
        'calcium*https://www.youtube.com/watch?v=uKy424Vf_44',
        'magnesium*https://www.youtube.com/watch?v=j8a7ItqTowc',
        'carbonate*https://www.youtube.com/watch?v=PXB8McUBNT4',
        'nitrate*https://www.youtube.com/watch?v=fXo39WiDNhg',
        'sulphite*https://www.youtube.com/watch?v=-pdKtHePATQ',
        'nitrite*https://www.youtube.com/watch?v=CWSMiXq-7Wc',
        'sulphide*https://www.youtube.com/watch?v=3bxac77mzuI',
        'iodide*https://www.youtube.com/watch?v=YVs24Q9yjgI',
        'bromide*https://www.youtube.com/watch?v=dMK4RoYh01o',
        'chloride*https://www.youtube.com/watch?v=O3d_NKyhIwg',
        'sulphate*https://www.youtube.com/watch?v=-YVH0DXbqmo',
        'phosphate*https://www.youtube.com/watch?v=FdVO1zX6doA',
        'oxalate*https://www.youtube.com/watch?v=0B_Mq5uY9Ng',
        'acetate*https://www.youtube.com/watch?v=Iqn4UdKY1MY'
    ]
    with open(PATH, 'wb') as fl:
        pickle.dump(obj, fl)

    with open(PATH, 'rb') as fl:
        a = pickle.load(fl)
    for i in a:
        print(i)
