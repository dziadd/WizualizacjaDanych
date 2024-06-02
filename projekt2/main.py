import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# plt.plot([1,2,3,4])
# plt.ylabel("jakieś liczby")
# plt.show()

# plt.plot([1,2,3,4], [1,4,9,16], 'ro-')
# plt.axis((0,6,0,20))
# plt.show
# plt.plot([1,2,3,4], [1,4,9,16], 'b')
# plt.plot([1,2,3,4], [1,4,9,16], 'o')
# plt.axis((0,6,0,20))
# plt.show
# plt.show()

# x=np.linspace(0,2,100)
# plt.plot(x,x, label="liniowa")
# plt.plot(x,x**2, label="kwadratowa")
# plt.plot(x,x**3, label="szcescienna")
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# plt.title("prosty wykres")
# plt.legend()
# plt.savefig("prosty_wykres.png")
# plt.show()
# im1 = Image.open("prosty_wykres.png")
# im1 = im1.convert("RGB")
# im1.save('nowy.jpg')

# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x,s,label="sin(x)")
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x)')
# plt.legend()
# plt.show()


# data = {'a':np.arange(50),
#      'c':np.random.randint(0,50,50),
#      'd':np.random.randn(50)}
#
# data['b'] = data['a'] + 10 * np.random.randint(50)
# data['d'] = np.abs(data['d'] * 100)
#
# print(f"a={data['a'][0]}, b={data['b'][0]}) , c={data['c'][0]}) , b={data['d'][0]}")
# plt.scatter('a','b', c='c', cmap='magma', s='d', data=data)
# plt.xlabel('wartosc a')
# plt.ylabel('wartosc b')
# plt.show()


# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi *x1)
# y2 = np.cos(2 * np.pi *x2)
# plt.subplot(2,1,1)
# plt.plot(x1,y1,'-')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(2,1,2)
# plt.plot(x2,y2,'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5, left=0.1, right=0.9)
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi *x1)
# y2 = np.cos(2 * np.pi *x2)
# fig, axs = plt.subplots(3,2)
# axs[0, 0].plot(x1,y1,'-')
# axs[0, 0].set_title('Wykres sin(x)')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[1, 1].plot(x2,y2,'r-')
# axs[1, 1].set_title('Wykres cos(x)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_title('Wykres cos(x)')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby('Kontynent')
# etykiety = np.array(list(grupa.groups.keys()))
# wartosci = list(grupa.agg('Populacja').sum())
# fig, ax = plt.subplots()
# ax.bar(x=etykiety, height=wartosci, color=['red', 'black', 'pink'])
# ax.set_xlabel('Kontynent')
# ax.set_ylabel('Populacja w mld')
# ax.ticklabel_format(axis='y', style='sci')
# fig.subplots_adjust(left=0.2)
#
# plt.show()


# df=pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa=df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':["sum"]})
# grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6,6),colors=['purple', 'grey'])
# plt.legend(loc="lower right")
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()

df=pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)

seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges, texts, autotexts = plt.pie(x=seria, labels=seria.index, autopct=lambda pct: '{:.1f}%'.format(pct),
                                   textprops=dict(color='black'),
                                   colors=['red', 'green'])
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()

