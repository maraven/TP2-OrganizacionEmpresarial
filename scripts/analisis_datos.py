
import pandas as pd
import matplotlib.pyplot as plt
#se importan para trabajar los datos, tablas y graficos.
# -------------------------------------------------------
# SCRIPT: analisis_datos.py
# Descripcion: Analisis de ventas diarias 2024
# Autor: Mariano Avendano
# Issue Jira: AV-2
# -------------------------------------------------------

# 1. Cargar datos
# Ruta relativa para garantizar reproducibilidad en Colab
df = pd.read_csv('datos/dataset.csv', parse_dates=['sales_date'])

# 2. Agrupar por mes para obtener totales significativos
ventas_por_mes = df.groupby(df['sales_date'].dt.month)['sales_amount'].sum()

ventas_totales = df['sales_amount'].sum() #suma las ventas.
mes_mayor_venta = ventas_por_mes.idxmax() #mayor venta por mes
mes_menor_venta = ventas_por_mes.idxmin() #menor venta por mes
promedio_diario = df['sales_amount'].mean() #calcula el promedio de las ventas.

nombres_meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril',
                 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto',
                 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

print("=" * 45)
print("        RESUMEN DE VENTAS 2024")
print("=" * 45)
print(f"Ventas totales del año:   ${ventas_totales:,.2f}")
print(f"Promedio de venta diaria: ${promedio_diario:,.2f}")
print(f"Mes con mas ventas:       {nombres_meses[mes_mayor_venta]}")
print(f"Mes con menos ventas:     {nombres_meses[mes_menor_venta]}")
print()
print("Ventas por mes:")
for mes, total in ventas_por_mes.items():
    print(f"  {nombres_meses[mes]:<12} ${total:,.2f}")

# 3. Guardar resumen en /resultados
resumen = pd.DataFrame({
    'Mes': [nombres_meses[m] for m in ventas_por_mes.index],
    'Ventas_Totales': ventas_por_mes.values
})
resumen.to_csv('resultados/Resumen.csv', index=False)
print("Resumen guardado en /resultados")

# 4. Grafico de evolucion mensual
# Permite identificar estacionalidad a lo largo del año
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(ventas_por_mes.index, ventas_por_mes.values,
        marker='o', color='steelblue', linewidth=2, markersize=6)
ax.set_title('Evolucion de Ventas Mensuales - 2024', fontsize=14, fontweight='bold')
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas totales ($)')
ax.set_xticks(range(1, 13))
ax.set_xticklabels([nombres_meses[m] for m in range(1, 13)], rotation=45)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('resultados/Grafico_Resultados.png', dpi=150)
plt.show()
print("Grafico guardado en /resultados")
