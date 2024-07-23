# Crear un DataFrame con datos de ejemplo
data = pd.DataFrame({
    'date': pd.date_range(start='2021-01-01', periods=100, freq='D'),
    'value': range(100)  # Serie de tiempo con tendencia lineal
})

# Suavizado de los datos utilizando medias móviles
data['smoothed'] = data['value'].rolling(window=5).mean()

# Configurar el tamaño de la figura
plt.figure(figsize=(10, 6))

# Graficar los datos originales
plt.plot(data['date'], data['value'], label='Datos originales')

# Graficar los datos suavizados
plt.plot(data['date'], data['smoothed'], label='Datos suavizados', color='red')

# Añadir título y etiquetas
plt.title('Datos originales y suavizados')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.legend()

# Mostrar el gráfico
plt.show()
