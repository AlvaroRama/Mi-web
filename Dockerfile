FROM python:3.13

WORKDIR /app

# Copy local context to `/app` inside container (see .dockerignore)
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip

RUN pip install --no.cache-dir -r requirements.txt

CMD sh -c "reflex run --env prod --backend-only & tail -f /dev/null"


## -------------------------------------------------------------------
## Imagen base
## -------------------------------------------------------------------
## Se usa Python 3.13, compatible con Reflex y con dependencias modernas.
#FROM python:3.13
#
## -------------------------------------------------------------------
## Variables y argumentos
## -------------------------------------------------------------------
## Railway inyecta automáticamente $PORT en tiempo de ejecución.
## Aun así, se define un valor por defecto (8080) para builds locales.
#ARG PORT=8080
## API_URL permite definir una URL externa para la API si fuera necesario.
#ARG API_URL
#
## Variables de entorno esenciales para Reflex y el entorno Docker.
#ENV PORT=$PORT \
#    REFLEX_API_URL=${API_URL:-http://localhost:$PORT} \
#    REFLEX_REDIS_URL=redis://localhost \
#    PYTHONUNBUFFERED=1
#
## -------------------------------------------------------------------
## Instalación de dependencias del sistema
## -------------------------------------------------------------------
## Se instalan:
## - Caddy → Servidor HTTP moderno que actuará como proxy inverso.
## - Redis → Servicio de colas que Reflex usa internamente.
#RUN apt-get update -y && \
#    apt-get install -y caddy redis-server && \
#    rm -rf /var/lib/apt/lists/*
#
## -------------------------------------------------------------------
## Configuración de la aplicación
## -------------------------------------------------------------------
#WORKDIR /app
#
## Copiamos el código del proyecto al contenedor.
#COPY . .
#
## Instalamos las dependencias de Python, incluyendo Reflex.
#RUN pip install --no-cache-dir -r requirements.txt
#
## Inicializamos Reflex (crea la estructura base, sin necesidad de compilar frontend).
#RUN reflex init
#
## -------------------------------------------------------------------
## FRONTEND (omitido porque se sirve desde Vercel)
## -------------------------------------------------------------------
## El Dockerfile oficial de Reflex compila el frontend y lo mueve a /srv
## para que Caddy lo sirva estáticamente. En tu caso no es necesario,
## porque el frontend ya está desplegado en Vercel.
## Sin embargo, Caddy necesita que la carpeta /srv exista como raíz de archivos.
#RUN mkdir -p /srv
#
## -------------------------------------------------------------------
## Señales, puertos y ejecución
## -------------------------------------------------------------------
## Reflex aún no maneja SIGTERM correctamente en contenedor,
## por lo que se usa SIGKILL al detenerlo.
#STOPSIGNAL SIGKILL
#
## Exponemos el puerto (Railway usa la variable $PORT automáticamente).
#EXPOSE $PORT
#
## -------------------------------------------------------------------
## Comando principal
## -------------------------------------------------------------------
## 1. Si existe la carpeta alembic (migraciones), se aplican.
## 2. Caddy se inicia y escucha en $PORT (sirviendo /srv y haciendo proxy al backend).
## 3. Redis se lanza en segundo plano.
## 4. Se ejecuta el backend de Reflex en modo producción.
#CMD [ -d alembic ] && reflex db migrate; \
#    caddy start && \
#    redis-server --daemonize yes && \
#    exec reflex run --env prod --backend-only

