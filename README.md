# Adivina el Número 🎮

## Descripción 📌

Adivina el Número es un juego interactivo en Python en el que el jugador intenta adivinar un número aleatorio elegido por la máquina. Para hacerlo, debe seleccionar entre diferentes rangos hasta acertar o perder todas sus vidas.

## Reglas del Juego 📝

- La máquina selecciona un número aleatorio entre 1 y 100.
- El jugador debe adivinar el número seleccionando entre los rangos sugeridos.
- Si el jugador elige el rango correcto, avanza sin perder vidas.
- Si el jugador elige el rango incorrecto, pierde una vida.
- El jugador tiene un total de **3 vidas**.
- El rango se reducirá progresivamente hasta que el jugador adivine el número o pierda.
- Se guardan las últimas 5 partidas jugadas con los nombres de los jugadores y sus resultados.

## Menú Principal 🗋

1. **Jugar**: Inicia una nueva partida.
2. **Instrucciones**: Muestra cómo jugar el juego.
3. **Últimas Partidas**: Muestra un historial de las últimas 5 partidas.
4. **Salir**: Cierra el juego.

## Requisitos ⚙️

- **Python 3.8 o superior**.
- No se requieren librerías externas, solo la estándar de Python.

## Instalación y Ejecución ▶️

### Instalación de Python
Si no tienes Python instalado, descárgalo desde la página oficial:
- [Descargar Python](https://www.python.org/downloads/)

Una vez instalado, verifica la versión con el siguiente comando en la terminal o línea de comandos:
```bash
python --version
```
Si estás en macOS o Linux, puede que necesites usar `python3` en lugar de `python`.

### Ejecución del Juego
1. Descarga el archivo del juego (`adivina_el_numero.py`).
2. Abre una terminal o línea de comandos en la carpeta donde está el archivo.
3. Ejecuta el siguiente comando:
   ```bash
   python adivina_el_numero.py
   ```
   O en algunos sistemas:
   ```bash
   python3 adivina_el_numero.py
   ```

## Estructura del Repositorio 📚
 ```bash
Adivina-el-Numero/
│-- Diagramas de flujo        # Diagramas del juego
│-- .gitignore.txt            # Archivos a excluir del control de versiones
│-- adivina_el_numero.py      # Código principal del juego
│-- README.md                 # Documentación del proyecto
```

## Autor ✨

Desarrollado por Jair Ronquillo Espinoza

