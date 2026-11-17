# ACT 14 - Docker Image en GitHub

API FastAPI de ejemplo para probar dependencias, pruebas unitarias, GitHub Actions, publicación de imagen en GHCR y ejecución local con Docker.

## Estructura
- `requirements.txt`: dependencias de producción usadas por la imagen Docker.
- `requirements-dev.txt`: dependencias de desarrollo, pytest y cliente de pruebas.
- `tests/test_api.py`: pruebas unitarias para `/` y `/health`.
- `.github/workflows/docker-image.yml`: job de pruebas y job de publicación en GHCR.
- `Dockerfile`: imagen Python 3.12 que expone la API en el puerto 8000.

## Ejecutar localmente
Desde esta carpeta:

```console
python -m pip install -r requirements-dev.txt
python -m pytest -v
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

En otra terminal, consultar `http://localhost:8000/` o `http://localhost:8000/health`.

## Publicar en GitHub
Crea un repositorio público llamado `act14-docker-github`, añade el remoto, y sube la rama `main`. Cada push a `main` primero ejecuta las pruebas. Si el job de pruebas termina correctamente, el segundo job construye y publica `ghcr.io/USUARIO/act14-docker-github:latest`.

El workflow usa `GITHUB_TOKEN` y requiere `packages: write`. En pull requests se ejecutan las pruebas; no se inicia sesión ni se publica la imagen.

```console
git init
git config --local user.name "USUARIO"
git config --local user.email "CORREO_DE_GITHUB"
git add .
git commit -m "Add API tests and Docker image workflow"
git branch -M main
git remote add origin https://github.com/USUARIO/act14-docker-github.git
git push -u origin main
```

## Descargar y ejecutar la imagen
Reemplaza `USUARIO` con el propietario real del repositorio. El paquete de GHCR puede requerir `docker login ghcr.io` si no es público.

```console
docker pull ghcr.io/USUARIO/act14-docker-github:latest
docker run -d --name act14-api -p 8000:8000 ghcr.io/USUARIO/act14-docker-github:latest
curl http://localhost:8000/
curl http://localhost:8000/health
```

La respuesta raíz debe incluir el mensaje de la API y la versión `1.0.0`; `/health` devuelve `status: ok`.