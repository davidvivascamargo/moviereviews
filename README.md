# 🎬 MovieReviews

**MovieReviews** es una aplicación web desarrollada con **Django 5** que permite gestionar usuarios, publicar reseñas de películas y mostrar noticias relacionadas con el cine.  
El proyecto incluye autenticación de usuarios, un sistema de reseñas dinámico, manejo de archivos multimedia y un panel de administración completo.

---

## 🚀 Características principales

- 🔐 Sistema de autenticación de usuarios (registro, login y logout).
- 📝 Publicación de reseñas de películas con soporte multimedia.
- 📰 Sección de noticias relacionadas al cine.
- 📂 Gestión de contenido estático y archivos multimedia.
- 🎛️ Panel de administración con **Django Admin** y editor enriquecido con **CKEditor**.
- 💾 Base de datos soportada en **SQLite** (desarrollo) y **MySQL** (producción).

---

## 📂 Estructura del proyecto
moviereviews/
│── accounts/ # App de autenticación de usuarios
│── media/ # Archivos subidos por los usuarios
│── movie/ # App para reseñas y gestión de películas
│── moviereviews/ # Configuración principal del proyecto Django
│── news/ # App de noticias de cine
│── static/ # Archivos estáticos (CSS, JS, imágenes)
│── manage.py # Script principal de Django
│── db.sqlite3 # Base de datos por defecto (SQLite)
│── requirements.txt # Dependencias del proyecto
│── README.md # Documentación
---

## Demo en vivo

Puedes ver la aplicación funcionando aquí:  
https://davidvivascamargo.pythonanywhere.com/


---

## ⚙️ Requisitos

Este proyecto usa **Python 3.12+** y **Django 5.2.4**.  
Dependencias principales:

- Django==5.2.4
- django-ckeditor==6.7.3
- mysqlclient==2.2.7
- PyMySQL==1.1.1
- Pillow==11.3.0

Puedes ver todas las dependencias en `requirements.txt`.

---

## 🛠️ Instalación y configuración

### 1️⃣ Clonar el repositorio
```bash
https://github.com/davidvivascamargo/moviereviews.git
cd moviereviews

2️⃣ Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Configurar variables de entorno

En el archivo moviereviews/settings.py, configura la base de datos y otras variables.
Por defecto se usa SQLite, pero puedes habilitar MySQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moviereviews_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5️⃣ Aplicar migraciones
python manage.py migrate

6️⃣ Crear superusuario
python manage.py createsuperuser

7️⃣ Ejecutar servidor de desarrollo
python manage.py runserver

Ahora entra en 👉 http://localhost:8000

🖼️ Capturas de pantalla
Home de la aplicación:  
<img width="1895" height="931" alt="Captura de pantalla 2025-09-25 142122" src="https://github.com/user-attachments/assets/addab7de-8016-4b3e-872d-9986c7dcc563" />

Login / Registro:  

<img width="1913" height="749" alt="Captura de pantalla 2025-09-25 142619" src="https://github.com/user-attachments/assets/27be4955-ed52-4f8b-9860-050d84daa675" />

<img width="1918" height="889" alt="Captura de pantalla 2025-09-25 142700" src="https://github.com/user-attachments/assets/689de020-e90b-4194-a81c-6f1137aa2244" />

Sección de reseñas:  

<img width="1910" height="893" alt="Captura de pantalla 2025-09-25 143831" src="https://github.com/user-attachments/assets/a7ef1c90-b46e-4c5c-b265-70c970373e49" />

<img width="1919" height="932" alt="Captura de pantalla 2025-09-25 143919" src="https://github.com/user-attachments/assets/218d2600-48af-49ff-9d00-689dedee79d3" />

Sección de news:

<img width="1916" height="949" alt="Captura de pantalla 2025-09-25 145340" src="https://github.com/user-attachments/assets/48ad8e8f-1798-488b-a21d-7e8507bd48e7" />

Vista general del panel:  

<img width="1908" height="843" alt="Captura de pantalla 2025-09-25 144146" src="https://github.com/user-attachments/assets/bc15ba13-067f-4eee-9c3d-72d622956cbc" />

Gestión de películas:

<img width="1919" height="889" alt="Captura de pantalla 2025-09-25 144246" src="https://github.com/user-attachments/assets/8b50a0d9-3e40-4b07-bcc5-70857f647894" />

<img width="1882" height="925" alt="Captura de pantalla 2025-09-25 144317" src="https://github.com/user-attachments/assets/bffaabef-48aa-410e-98f3-2af015bd3b35" />

Gestión de reseñas:  

<img width="1887" height="883" alt="Captura de pantalla 2025-09-25 144419" src="https://github.com/user-attachments/assets/1db45d3d-091e-4c48-a79b-972295869046" />

<img width="1895" height="909" alt="Captura de pantalla 2025-09-25 144530" src="https://github.com/user-attachments/assets/3d1edb30-9cbe-41f1-b9c9-759942040e79" />

Gestión de news:

<img width="1918" height="839" alt="Captura de pantalla 2025-09-25 145156" src="https://github.com/user-attachments/assets/01f4eb06-2ce0-4248-b313-d5e6e3179356" />

<img width="1896" height="943" alt="Captura de pantalla 2025-09-25 145301" src="https://github.com/user-attachments/assets/0cb25dfc-3379-4f6b-a6d4-825eaa2cc5cd" />

👨‍💻 Autor

Desarrollado por Jesús David Vivas C.

📜 Licencia

Este proyecto está bajo la licencia MIT.
Eres libre de usarlo, modificarlo y distribuirlo.
