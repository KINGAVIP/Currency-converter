#from ipywidgets import interact, interactive, fixed, interact_manual
#mport ipywidgets as widgets


def converter(amount):
    dics = {}
    with open('curremcy.txt') as f:
        a=f.readlines()


    for item in a:
        b=item.split("\t")
        dics[b[0]]=b[1]

    [print(item) for item in dics.keys()]

    currency=input("Enter your choice:")

    print("The amount converted is",amount*float(dics[currency]))
if __name__ == '__main__':
    amount=int(input("Enter the amount you want to convert:"))
    converter(amount)
    