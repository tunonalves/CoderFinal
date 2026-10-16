# CoderFinal — proyecto Python/Django

Proyecto final del curso Python-Django de Coder House (2022), realizado por
**Federico Tuñon Alves**. Integra un sitio con servicios, blog, autenticación,
catálogo de productos y carrito de compras basado en sesiones.

Sitio del autor conservado del README original:
<https://tunonalves.wixsite.com/federico>.

## Funcionalidades y alcance

- Inicio y listado de servicios.
- Blog con categorías, imágenes y vistas de alta, consulta, edición y eliminación.
- Registro, inicio/cierre de sesión y vistas de administración de usuarios.
- Tienda y operaciones de agregar, quitar y vaciar el carrito.
- Formulario de contacto que utiliza el backend de correo de Django.
- Modelos de pedidos y líneas de pedido; la vista de pedidos solamente renderiza
  una plantilla. No se debe interpretar como un checkout o sistema de pagos completo.

Es un proyecto educativo, **no una aplicación lista para producción**.

## Tecnologías y requisitos

Python 3, Django, SQLite, plantillas de Django, Bootstrap, jQuery y Font Awesome.
La configuración registra `crispy_forms` con el paquete de plantillas `bootstrap4`;
los campos `ImageField` requieren Pillow.

No hay un manifiesto de dependencias ni versiones fijadas. La cabecera de
configuración menciona Django 2.2.7 como versión de generación, pero no acredita
la versión utilizada posteriormente. Se necesita seleccionar y validar una
combinación compatible de Python, Django, Pillow y django-crispy-forms antes de
ejecutar el proyecto. El soporte de `bootstrap4` de crispy-forms depende de la
versión elegida; instalar las últimas versiones sin revisar esa compatibilidad
no garantiza el arranque. No usar versiones antiguas sin soporte en un servicio público.

## Preparación local

```bash
git clone git@github.com:tunonalves/CoderFinal.git
cd CoderFinal
python3 -m venv .venv
source .venv/bin/activate
```

1. Instalar en ese entorno las dependencias compatibles indicadas arriba y
   registrar las versiones que se logren validar. No existe un `requirements.txt`
   que permita reconstruir automáticamente el entorno original.
2. Revisar [la configuración](ProyectoWeb/settings.py): contiene configuración
   de desarrollo y una clave incorporada al código. Sustituirla en una copia
   local, revisar hosts y correo, y no publicar claves ni reutilizar las incluidas.
   El proyecto no implementa por sí solo una carga de configuración desde `.env`.
3. Trabajar con una copia de la base SQLite y de los archivos multimedia;
   `db.sqlite3` está versionado. Las migraciones modificarán esa base.
4. Antes de usar contacto, configurar un backend local de consola
   (`django.core.mail.backends.console.EmailBackend`) y revisar los destinatarios
   definidos en la vista para evitar envíos reales.

Una vez preparado el entorno, desde la raíz del repositorio:

```bash
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

El superusuario es opcional para acceder al panel `/admin/`; no se proporcionan
credenciales de la base incluida. Estos comandos son una guía de uso local,
no una ejecución verificada durante esta revisión documental.

## Rutas principales

| Ruta | Uso |
| --- | --- |
| `/` | Inicio |
| `/servicios/` | Servicios |
| `/blog/` | Publicaciones |
| `/autenticacion/` | Registro |
| `/autenticacion/loguear` | Inicio de sesión |
| `/tienda/` | Catálogo y carrito |
| `/contacto/` | Formulario de correo; revisar configuración antes de enviarlo |
| `/pedidos/` | Plantilla de pedidos |
| `/admin/` | Administración Django |

## Estructura

| Directorio o archivo | Contenido |
| --- | --- |
| [manage.py](manage.py) | Entrada de los comandos Django |
| [ProyectoWeb/](ProyectoWeb/) | Configuración, enrutamiento principal y WSGI |
| [ProyectoWebApp/](ProyectoWebApp/) | Inicio, plantilla base y recursos estáticos |
| [servicios/](servicios/), [blog/](blog/) | Modelos, formularios y vistas de contenido |
| [autenticacion/](autenticacion/) | Registro, sesiones y usuarios |
| [tienda/](tienda/), [carro/](carro/), [pedidos/](pedidos/) | Productos, carrito en sesión y modelos de pedidos |
| [contacto/](contacto/) | Formulario y envío de correo |
| [media/](media/) | Imágenes incluidas |
| [Video/](Video/) | Grabación de la demostración original |
| [unit test/](unit%20test/) | Documentos originales sobre pruebas |

## Limitaciones conocidas y verificación

- La vista `UserList` referencia `auth/listUser.html`, pero la plantilla incluida
  se llama `auth/user_list.html`: esa pantalla requiere corrección de código.
- Las vistas de modificación de publicaciones y usuarios no aplican todas las
  mismas restricciones de acceso que sus listados. Revisar autorización antes
  de exponerlas fuera de un entorno local.
- Los documentos de pruebas no equivalen a una suite automatizada ejecutada.
- Esta revisión comprobó código, rutas y archivos mediante inspección estática;
  no instaló dependencias, ejecutó migraciones, arrancó el servidor ni envió correo.
  No se garantiza el funcionamiento de todos los flujos.