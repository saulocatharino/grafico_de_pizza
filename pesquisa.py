import matplotlib.pyplot as plt

a = 6
b = 4 
c = 3
d = 12

total = a + b + c + d

def percent(total,valor):
    per = total * .01 # também pode ser per = total / 100
    tot = valor / per

    return tot



aa = percent(total,a)
bb = percent(total,b)
cc = percent(total,c)
dd = percent(total,d)


print(aa,bb,cc,dd)

fig = plt.figure(figsize=(10,10)) # determina a proporção e o tamanho da figura
ax = fig.gca()

index = [1,2,3,4]
sources = ['Melhor no Pc', 'Melhor no Celular', 'Não digita sem olhar', 'Bom no Pc e no Celular']
pie_chart = [aa,bb,cc,dd]

ax.pie(pie_chart, labels=sources, autopct='%.2f')

plt.show()
