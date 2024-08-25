# Discord Package - Empaquetador de Bots de Discord

## Descripción

**Discord Package** es una herramienta de línea de comandos para crear y gestionar bots de Discord en Python. Además, incluye un monitor web simple para ver los logs del bot en tiempo real, permitiendo una mejor visualización y depuración.

## Características

- **Generación de proyectos de bots de Discord**: Crea rápidamente un nuevo proyecto de bot con la estructura de archivos y carpetas necesaria.
- **Monitorización de logs en tiempo real**: Un servidor web incorporado que muestra los logs del bot en tiempo real en una interfaz web.
- **Filtros avanzados**: Filtra los logs por nombre de servidor, ID del servidor, nombre de usuario y fecha para facilitar la depuración.

## Requisitos

- Python 3.6 o superior.
- Dependencias adicionales: `discord.py`, `watchdog`, `asyncio`, `datetime`, `requests`, `rich`.

## Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/MrWiki15/discord-package.git
cd discord-package
```

### 2. Instala el paquete

Usa pip para instalar el paquete localmente:

```bash
pip install .
```

### 3. Instala las dependencias requeridas

Asegúrate de instalar todas las dependencias necesarias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Uso

### Crear un Nuevo Proyecto de Bot

Para crear un nuevo proyecto de bot de Discord, utiliza el siguiente comando:

```bash
dcp create <nombre_del_proyecto>
```

Reemplaza `<nombre_del_proyecto>` con el nombre que desees para tu nuevo proyecto. Este comando creará una estructura de proyecto con todos los archivos y carpetas necesarios.

## Estructura del Proyecto

El comando `create` generará una estructura de proyecto similar a la siguiente:

```markdown
nombre_del_proyecto/
│
├── assets/
│ ├── imagen/
│ │ └── mi_imagen.png
│ └── **init**.py
├── buttons/
│ ├── **init**.py
│ └── buttons_help.py
├── commands/
│ ├── **init**.py
│ └── ping.py
├── config/
│ ├── **init**.py
│ └── bot_config.py
├── functions/
│ ├── **init**.py
│ └── print_logs.py
├── logs/
│ ├── **init**.py
│ └── logs.txt
├── monitor/
│ ├── **init**.py
│ ├── index.html
│ ├── style.css
│ ├── script.js
│ └── monitor.py
├── utils/
│ ├── **init**.py
│ └── error_message.py
├── bot.py
├── dev.py
├── requirements.txt
└── .gitignore
```

## Ejecutar el Bot y el Monitor Web

Para iniciar el bot de Discord y el servidor web de monitorización:

```bash
python dev.py
```
