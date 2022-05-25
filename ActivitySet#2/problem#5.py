

def get_cs():
    st=input()
    return st


def cs_to_dict(cs):
    d={}
    for i in cs.split(';'):
      s=i.split('=')
      d[s[0]]=s[1]
    return d


def dict_to_cs(d):
    st=''
    for a,b in d.items():
      st+=a+'='+b+';'
    return st[:-1]


def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
