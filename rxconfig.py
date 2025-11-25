# Importamos Reflex con alias 'rx' para poder acceder a sus clases y funciones
import reflex as rx

# Creamos el objeto de configuración de la aplicación
config = rx.Config(
    # Nombre de la aplicación. Reflex lo usará para generar la carpeta del frontend,
    # identificar el proyecto y en ciertos metadatos.
    app_name="link_bio",
    
    cors_allowed_origins=[
        "http://localhost:3000",
        r"https://.*\.vercel\.app", # Permite todos los dominios temporales
        "https://forgingdata.vercel.app"],
    
    
    # Añado api_url en remote_build
    #api_url="https://api-forgingdata.up.railway.app",
    
    
    # Lista de plugins que queremos activar en esta app
    plugins=[
        # Plugin que genera automáticamente un sitemap.xml
        # útil para que los buscadores indexen tu web (SEO).
        rx.plugins.SitemapPlugin(),

        # Plugin que añade soporte para Tailwind CSS v4 en el frontend.
        # Esto te permite usar utilidades de Tailwind en tus componentes.
        rx.plugins.TailwindV4Plugin(),
    ],
)
