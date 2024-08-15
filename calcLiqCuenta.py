liq_inicial = int(input("\n\n[+] Ingrese el valor de la cuenta inicial: "))
por_opp = int(input("\n\n[+] Introduce el porcentaje que usas por operación: "))
op_sem = int(input("\n\n[+] Cuántas operaciones realizas semanalmente: "))
PnL = int(input("\n\n[+] Ingrese el % promedio de beneficio de cada operación\n\t[!Aviso!](si usas apalancamiento pon el porcentaje con el apalancamiento ya aplicado): "))
print("\n\n[!_!] Este programa simula la evolución de una supuesta cuenta de trading en 1 mes, 3 meses, 6 meses y 1 año")

exit = ""
while exit.lower() != "s":

    opcion = int(input("\n\nSi quieres calcular la evolución en 1 mes(1), 3 meses(2), 6 meses(3), 1 año(4): "))
    
    def un_mes():
        global liq_inicial  
        cont_t = 0
        total = 0  
        while cont_t < 4:  
            for _ in range(op_sem):
                liq_oper = liq_inicial * (por_opp / 100)
                resultado_opp = liq_oper * (PnL / 100)
                liq_inicial += resultado_opp
                total += resultado_opp
            cont_t += 1  
            print(f"Total acumulado después de {cont_t} semanas: {round(liq_inicial, 2)}$")

    def tres_meses():
        global liq_inicial  
        cont_t = 0
        total = 0  
        while cont_t < 12:  
            for _ in range(op_sem):
                liq_oper = liq_inicial * (por_opp / 100)
                resultado_opp = liq_oper * (PnL / 100)
                liq_inicial += resultado_opp
                total += resultado_opp
            cont_t += 1  
            print(f"Total acumulado después de {cont_t} semanas: {round(liq_inicial, 2)}$")

    def seis_meses():
        global liq_inicial  
        cont_t = 0
        total = 0  
        while cont_t < 24:  
            for _ in range(op_sem):
                liq_oper = liq_inicial * (por_opp / 100)
                resultado_opp = liq_oper * (PnL / 100)
                liq_inicial += resultado_opp
                total += resultado_opp
            cont_t += 1  
            print(f"Total acumulado después de {cont_t} semanas: {round(liq_inicial, 2)}$")

    def año():
        global liq_inicial  
        cont_t = 0
        total = 0  
        while cont_t < 52:  # Corregido para reflejar un año (52 semanas)
            for _ in range(op_sem):
                liq_oper = liq_inicial * (por_opp / 100)
                resultado_opp = liq_oper * (PnL / 100)
                liq_inicial += resultado_opp
                total += resultado_opp
            cont_t += 1  
            print(f"Total acumulado después de {cont_t} semanas: {round(liq_inicial, 2)}$")

    if opcion == 1:
        un_mes()
    elif opcion == 2:
        tres_meses()
    elif opcion == 3:
        seis_meses()
    elif opcion == 4:
        año()
    else:
        print("No es una opción válida")

    exit = input("\n\n[+]Deseas salir(S/N): ")
