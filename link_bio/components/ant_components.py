import reflex as rx

from link_bio.styles.colors import Color


# Boton flotante que asocio a la navbar:

# ================================================================
# 1️Definir una clase que envuelva el componente React
# ================================================================
# Cada componente React externo debe definirse como una subclase de rx.Component.
# La clase indica a Reflex qué librería y qué etiqueta de React debe importar.

class FloatButton(rx.Component):
    # ------------------------------------------------------------
    # Nombre del paquete de donde proviene el componente
    # (equivale a: import { FloatButton } from "antd")
    # ------------------------------------------------------------
    library = "antd"

    # ------------------------------------------------------------
    # Nombre exacto del componente dentro de la librería
    # (debe coincidir con el export de la librería React)
    # ------------------------------------------------------------
    tag = "FloatButton"

    # ------------------------------------------------------------
    # 🔸 Definición de props (propiedades del componente)
    # ------------------------------------------------------------
    # - Si el prop espera un valor primitivo (str, bool, num),
    #   se define como rx.Var[tipo].
    # - Si el prop espera un componente o ReactNode,
    #   se define como rx.Component.
    # ------------------------------------------------------------

    # Este prop espera un componente React (ej: un icono JSX)
    icon: rx.Component | None = None

    # Props simples (primitivos o estructuras JSON)
    href: rx.Var[str] | None = None
    target: rx.Var[str] | None = None
    badge: rx.Var[dict] | None = None


# ================================================================
# 2Crear una función "factory" para instanciar el componente
# ================================================================
# Reflex prohíbe instanciar directamente la clase (FloatButton(...)).
# En su lugar, se usa FloatButton.create(**props).
# Aquí definimos una función que prepara los props por defecto.

def float_button(**kwargs) -> rx.Component:
    """Devuelve un FloatButton listo para usar en Reflex."""
    # ------------------------------------------------------------
    # Valores por defecto: se pueden sobreescribir al llamar
    # float_button(href="...", badge={...}, etc.)
    # ------------------------------------------------------------
    defaults = dict(
        # 👇 Este icono es un componente Reflex,
        # no un string ni una expresión JS.
        # Es la forma correcta según la documentación oficial.
        icon=rx.image(src="/icons/arrow-up-solid.svg", alt="Subir"),

        # Props normales
        href="https://",
        target="_blank",
        badge={"dot": True, "color": Color.ORANGE.value},
    )

    # Mezclamos los defaults con los valores pasados por el usuario
    defaults.update(kwargs)

    # ------------------------------------------------------------
    # Llamamos al método oficial de creación de Reflex
    # ------------------------------------------------------------
    return FloatButton.create(**defaults)
    
    
    



#Importacion elementos React desde Ant Design:
#https://ant.design/components/float-button
##Importacion elementos React desde Ant Design:
#common API son las propiedades
