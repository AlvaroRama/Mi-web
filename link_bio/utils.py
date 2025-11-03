import reflex as rx

#Comun:

preview = "icons/hammer-solid.svg"

def lang () -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

_meta = [
        {"name": "og:type","content": "website"},
        { "name": "og:image", "content": preview}
    ]



#Index:

index_title = "Alvaro Rama Benedicto | Mi web en Reflex con recursos"

index_description = "Hola, mi nombre es Álvaro. Bienvenido a esta página donde espero encuentres recursos interesantes relacionados con la ciencia de datos"

index_meta = [
        {"name": "og:title","content": index_title},
        {"name": "og:description","content": index_description}
        ]

index_meta.extend(_meta)

# Publicaciones:

publicaciones_title = "Alvaro Rama Benedicto | Publicaciones específicas"

publicaciones_description = "Publicaciones específicas"

publicaciones_meta = [
        {"name": "og:title","content": publicaciones_title},
        {"name": "og:description","content": publicaciones_description}
        ]

publicaciones_meta.extend(_meta)



