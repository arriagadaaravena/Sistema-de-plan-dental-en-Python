import os
os.system('clear')

PLAN_DENTAL = 80000
RADIOGRAFIA_DENTAL = 12000
dscto_plan = 0
dscto_radiografia = 0

try:

    edad = int(input("Ingrese su edad\n"))
    quintil = int(input("Ingrese el quintil al que pertenece (1 a 5)\n"))

    if edad <=25 and quintil in (1, 2):
        dscto_plan = 0.18
    elif edad <=25 and quintil in (3, 4):
        dscto_plan = 0.12
    elif edad >=26 and edad <=45 and quintil in (1, 2):
        dscto_plan = 0.12
    elif edad >=26 and edad <=45 and quintil in (3, 4):
        dscto_plan = 0.08

    if quintil in (1, 2, 3):
        dscto_radiografia = 0.10

    if edad >=40 and edad <=45:
        dscto_radiografia += 0.05

    if edad > 45:
        print("No tiene descuentos en el plan dental")
    
    if quintil == 5:
        print("No existen descuentos para el quintil 5")

    PLAN_DENTAL = PLAN_DENTAL - (PLAN_DENTAL * dscto_plan)
    RADIOGRAFIA_DENTAL = RADIOGRAFIA_DENTAL - (RADIOGRAFIA_DENTAL * dscto_radiografia) 

    print(f"El valor del plan es:{PLAN_DENTAL}")
    print(f"El valor de la radiografía es:{RADIOGRAFIA_DENTAL}")

except:
    print("Error: los datos deben ser numéricos, intente nuevamente.")