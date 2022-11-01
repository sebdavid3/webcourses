enero = int(input("Escribre tu presupuesto para enero "))
febrero =  int(input("Escribre tu presupuesto para febrero "))
marzo =  int(input("Escribre tu presupuesto para marzo "))

budget_total = enero + febrero + marzo
print(f"El presupuesto total de los 3 meses es {budget_total}")

avg_budget = budget_total/3
print(f"El presupuesto promedio de los 3 meses es {avg_budget}")
