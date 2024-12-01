# Proyecto Deep Blue - Diseño GIS para la Experiencia Frontend

## Descripción

**Deep Blue** tiene como objetivo mejorar la experiencia frontend en el desarrollo de aplicaciones GIS (Sistemas de Información Geográfica) utilizando herramientas y lenguajes geoespaciales. A través de esta plataforma interactiva, los usuarios pueden explorar regiones protegidas y visualizar los efectos del cambio climático de manera dinámica y accesible.

La aplicación está construida con Dash, una biblioteca de Python para la creación de aplicaciones web interactivas, y Dash Bootstrap Components, para facilitar el diseño con una interfaz limpia y moderna.

## Características

- **Interfaz limpia y atractiva**: La aplicación presenta una landing page con una imagen de fondo atractiva y una sección con un título, subtítulo y un botón de acción.
- **Redirección dinámica**: Al hacer clic en el botón, el usuario es redirigido a una nueva sección o página de la plataforma donde se pueden ver más detalles sobre las regiones protegidas y sus interacciones con el cambio climático.
- **Responsive**: El diseño está optimizado para ser visualizado en diferentes dispositivos gracias al uso de flexbox y Dash Bootstrap.

## Tecnologías Utilizadas

- **Dash**: Framework de Python para la creación de aplicaciones web interactivas.
- **Dash Bootstrap Components**: Para el diseño visual y la integración con Bootstrap.
- **HTML y CSS**: Para la estructura y el estilo de la aplicación.
  
## Instalación

Para ejecutar la aplicación localmente, primero necesitas instalar las dependencias. Asegúrate de tener **Python 3.x** instalado y luego ejecuta los siguientes comandos:

1. Crea un entorno virtual (opcional pero recomendado):
    ```
    python -m venv venv
    ```

2. Activa el entorno virtual:
    - En Windows:
      ```
      .\venv\Scripts\activate
      ```
    - En MacOS/Linux:
      ```
      source venv/bin/activate
      ```

3. Instala las dependencias necesarias:
    ```
    pip install dash dash-bootstrap-components
    ```

4. Ejecuta el archivo de la aplicación:
    ```
    python app.py
    ```

Esto abrirá la aplicación en tu navegador predeterminado.

## Uso

1. **Landing Page**: Cuando se inicie la aplicación, verás una página inicial con un diseño atractivo que incluye una imagen de fondo y una descripción del proyecto.
2. **Botón de acción**: Al hacer clic en el botón "Descubrir más", serás redirigido a la siguiente sección o página de la plataforma donde se podrá acceder a visualizaciones detalladas.

## Desarrollo Futuro

Este proyecto está en desarrollo y tiene como objetivo implementar más funcionalidades interactivas, como mapas dinámicos, análisis de datos geoespaciales y más herramientas de visualización para el cambio climático y la protección de regiones.

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu mejora o corrección.
3. Haz un pull request explicando tu contribución.