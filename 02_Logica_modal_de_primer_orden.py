from modal import necessity, possibility, and_

# Definición de proposiciones
P = 'P'
Q = 'Q'

# Sentencias modales
necesidad_P = necessity(P)
posibilidad_Q = possibility(Q)
necesidad_P_y_posibilidad_Q = and_(necesidad_P, posibilidad_Q)

print(necesidad_P_y_posibilidad_Q)
