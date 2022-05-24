

def get_cs():
    st=input()
    return st


def cs_to_lot(cs):
    j=[]
    ll=cs.split(';')
    for i in ll:
       j.append(tuple(i.split('=')))
    return j


def lot_to_cs(lot):
    stt=''
    for a,b in lot:
      stt+=a+'='+b+';'
    return stt[:-1]


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
