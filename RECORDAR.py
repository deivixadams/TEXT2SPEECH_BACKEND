#DOCKERS
'''
docker-compose down

docker-compose up --build

docker run -p 5000:5000 my-flask-app

curl -X POST http://localhost:5000/upload -F "file=@/path/to/your/file"
curl -X POST http://localhost:5000/upload -F "file=@1.pdf"

'''



#---Flask, React, Axios, Docker, SQLite, PostgreSQL, html, css, javascript


'''PENDENTES

#Grafico
#Progress bar o iconos que den feedback al usuario
# Ir desplegando un texto en la pantalla
Usar un Servidor WSGI para el Backend:
    Flask viene con un servidor de desarrollo que no es adecuado para producción.
    Usa un servidor WSGI como Gunicorn para ejecutar tu aplicación Flask en producción.


    
    
'''






#-------------------------------------------------------
#Arquitectura
'''
Crear una API REST usando Flask o FastAPI
    Endpoints para:
    Subir y procesar archivos PDF.
    Generar archivos de audio.
    Modificar propiedades de audio.
    Reproducir audio (posiblemente, devolver el archivo de audio para su descarga).

Crear una interfaz de usuario con React o Vue
Formularios para:
    Subir archivos PDF.
    Seleccionar opciones de velocidad y tono.
    Reproducir o descargar el archivo de audio generado.

    
Integración
    Axios o Fetch API: Para hacer peticiones HTTP desde el frontend al backend.
    Socket.IO (si se necesita comunicación en tiempo real).

    
Despliegue
Docker:
    Descripción: Docker permite empaquetar la aplicación en contenedores para un despliegue consistente en cualquier entorno.
    Ventajas:
    Portabilidad y consistencia.
    Facilita el despliegue y escalado.

Heroku o AWS:
    Descripción: Plataformas de computación en la nube para el despliegue y gestión de aplicaciones.
    Ventajas:
    Heroku es fácil de usar para despliegues rápidos.
    AWS ofrece servicios avanzados y escalabilidad.

Base de Datos (opcional, si necesitas almacenar datos)
SQLite:

    Descripción: SQLite es una base de datos ligera que no requiere configuración de servidor.
    Ventajas:
    Fácil de usar y configurar.
    Ideal para aplicaciones pequeñas o medianas.
PostgreSQL:
    Descripción: PostgreSQL es una base de datos relacional potente y de código abierto.
    Ventajas:
    Escalable y robusta.
    Soporte avanzado para consultas complejas y transacciones.
'''
