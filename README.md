### romanballesteros-pythonweb

- **Nombre del proyecto e integrantes del proyecto:**

Follow-up por Roman Jose Ballesteros

- **Video presentación del proyecto:**
 
https://youtu.be/DGOS938CIJo

- **Descripción:**

Bienvenido a la página web y aplicación Follow-up (Seguimiento).

Esta página web y aplicación están creadas en lenguaje Python y utilizan el framework Django, el cual incluye una interfaz para administrar y gestionar usuarios, grupos y diferentes modelos que vayamos creando en la aplicación.

Básicamente, el proyecto consiste en una página web con una aplicación que permite darle seguimiento a Casos asociados a Dispositivos y a Tareas asociadas a Operadores (usuarios registrados).

Los usuarios registrados una vez que ingresan al sistema, pueden crear, consultar, modificar o eliminar elementos de diferentes tipos: Sitios, Racks, Proveedores, Dispositivos, Operadores, Casos y Tareas.

Existen 3 tipos de usuarios con capacidades y privilegios diferentes:
- admin o superuser: acceso a todo, incluida la gestión de usuarios y grupos
- staff: similar al admin, sin gestión de usuarios y grupos
- normal: similar al staff, pero con algunas limitaciones a páginas, contenidos y funciones

Los usuarios admin y staff pueden crear, consultar, modificar y eliminar elementos de todos los tipos: Sitios, Racks, Proveedores, Dispositivos, Operadores, Casos y Tareas, además pueden acceder a todas la páginas sin ninguna restricción.

Los usuarios normales pueden consultar información de todos los elementos disponibles y además pueden crear, modificar y eliminar los elementos de tipo Caso y Tarea.

Cada Operador se puede asociar únicamente a un usuario registrado.

Cada Caso está únicamente relacionado a un Dispositivo, que a su vez está asociado a un Sitio, Rack y Proveedor en particular, además el Caso se puede asociar a un único Operador.

Las Tareas están únicamente asociadas al propio usuario que las crea.

- **Tecnologías utilizadas:**

Software:
- Python
- Django
- Bootstrap
- DataTables
- JQuery
- Font Awesome

- **requirements.txt**

Software:
- asgiref==3.8.1
- certifi==2024.6.2
- charset-normalizer==3.3.2
- Django==5.0.6
- django-smart-selects==1.6.0
- et-xmlfile==1.1.0
- idna==3.7
- openpyxl==3.1.5
- pillow==10.3.0
- requests==2.32.3
- setuptools==70.2.0
- sqlparse==0.5.0
- tzdata==2024.1
- urllib3==2.2.2