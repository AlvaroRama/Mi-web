import reflex as rx

import datetime

from link_bio.styles.styles import ImageSize

from rxconfig import target_api_url

import httpx

from link_bio.components.info_service import info_service

class GithubState(rx.State):

    url: str = "https://github.com/reflex-dev"

    profile_image: str = "https://avatars.githubusercontent.com/u/104714959"

    @rx.event

    async def set_profile(self, username: str):
        
        if not username:

            return
        
        endpoint = f"{target_api_url}/github/{username}"

        try:

            # Llamamos al endpoint que definimos en FastAPI.

            async with httpx.AsyncClient(timeout=5) as client:

                r = await client.get(endpoint)
                
                print(r)

        except Exception:

            return

        if r.status_code == 200:

            data = r.json()

            self.url = data["url"]

            self.profile_image = data["avatar"]
            
            print(data)


def footer() -> rx.Component:
    return rx.vstack(
        info_service(),
        rx.text(
            "Web realizada con tecnología Reflex",
            trim="both"
        ),
        rx.link(
            rx.image(
                src="favicon.ico",
                style={
                    "margin": "0 auto",
                    "display": "block",  # Centrar imagen
                },
                width=rx.breakpoints(
                    initial=ImageSize.LOGO_MINI.value,  # móvil (pantallas pequeñas)
                    sm=ImageSize.LOGO.value, 
                ),
                height=rx.breakpoints(
                    initial=ImageSize.LOGO_MINI.value,
                    sm=ImageSize.LOGO.value,
                ),
                alt="Reflex Logo",
            ),
            href="https://reflex.dev/",
            is_external=True,
        ),
        
        rx.link(
            f"© 2024-{datetime.date.today().year} Álvaro Rama Benedicto",
            href="https://www.linkedin.com/in/alvaro-rama-benedicto-538603b4/?originalSubdomain=es",
            is_external=True,
        ),
    
        rx.hstack(
            rx.link(
                rx.avatar(src=GithubState.profile_image),
                href=GithubState.url,
        ),
            rx.input(
                placeholder="Your Github username",
                on_blur=GithubState.set_profile,
        ),

        ),
        
        align="center",
    )
