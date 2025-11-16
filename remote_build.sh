
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

rm -rf public
reflex init

# ---------------------------------------------------------------
# NOTA SOBRE API_URL:
# ---------------------------------------------------------------
# Reflex permite sobrescribir el parámetro api_url del rxconfig.py
# durante la exportación usando:
#
#     API_URL="https://TU_BACKEND" reflex export
#
# Esto era necesario en versiones anteriores o cuando NO se define
# api_url en rxconfig.py.
#
# En tu caso, ya tienes api_url configurado correctamente en:
#     config = rx.Config(api_url="https://api-forgingdata.up.railway.app")
#
# Por tanto, NO es necesario establecer API_URL aquí.
# Solo deberías activar esta línea si algún día necesitas:
#   - Generar builds con backend distinto (staging / dev / prod)
#   - Sobrescribir el valor de rxconfig.py en tiempo de exportación
#
# Ejemplo de uso (solo si lo necesitas):
# API_URL="https://api-forgingdata.up.railway.app" reflex export --frontend-only
# ---------------------------------------------------------------

reflex export --frontend-only

unzip frontend.zip -d public
rm -f frontend.zip

deactivate
