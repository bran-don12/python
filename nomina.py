print('buen dia, digite los siguientes datos para realizar la nomina')

print("Documento:")

D=int(input())

print("Nombres:")

N=str(input())

print("Apellidos:")

A=str(input())

print("¿cual es su salario?")

sl=int(input())

print("¿cuantos dias trabajó?")

Dt=int(input())

print("NOMINA")

tr=117100/30
sb=tr*Dt
vld=sl/30
st=vld*Dt
dps=st*8/100
st_d=st+sb-dps

print("El señor/a",N,A,"con numero de documento ",D,",que recibe por contrato el monto de ",sl,"y que trabajó",Dt,"dias el mes de julio, sumado al subsidio transporte por dias trabajados, y restando las prestaciones sociales, se le consigna un total de: ",st_d)
