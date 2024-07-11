### romanballesteros-pythonweb

- **Nombre e integrantes del proyecto:**

Follow-up por Roman Jose Ballesteros

- **Descripción:**

Bienvenido a la página web Follow-up

Esta página web está desarrollada utilizando lenguaje Python con el framework Django y proporciona funcionalidades para gestionar varios modelos de datos.

Esta página web permite a usuarios operarios registrados consultar información sobre: sitios, racks, proveedores, dispositivos y operadores, que han sido previamente creados por un usuario admin o staff.

Además los usuarios pueden crear casos relacionados a los dispositivos disponibles (estos están asociados a un sito, rack, proveedor, y operario en particular), también pueden crear tareas que están únicamente asociadas al propio usuario; básicamente para darle seguimiento a esos casos y tareas.

- **Tecnologías utilizadas:**

Python
Django
Bootstrap
DataTables
JQuery
Font Awesome
 
- **Funcionalidades:**

Registrarse con un usuario.

Ingresar con un usuario.

Usuarios admin y staff, pueden crear instancias de todos los modelos disponibles: sitios, racks, proveedores, dispositivos, operarios, casos y tareas.

Usuarios oper, pueden crear solo instancias de los modelos: casos y tareas.

Todos los usuarios pueden consultar información de todas las instancias de todos los modelos.

- **Modelos y Vistas Disponibles:**

1. Modelos:
   - Site, Rack, Vendor, Device, Operator, Case y Task.

2. Vistas:
   - Main: Home, Pages, About, Sing In, Sign Out
   - User: Edit profile, Logout
   - Site: Create, List, Table, Scroll, List / Grid, Nav, Edit / Delete
   - Rack: Create, List, Table, Nav, Edit / Delete
   - Vendor: Create, List, Table, Nav, Edit / Delete
   - Device: Create, List, Table, Nav, Edit / Delete
   - Operator: Create, List, Table, Nav, Edit / Delete
   - Case: Create, List, Table, Nav, Edit / Delete
   - Task: Create, List pending, List completed, Table, Edit/Delete

- **Tipos de Usuarios y Permisos de Acceso:**

Administrador (admin):

Acceso de administrador (frontend Django) para gestión de modelos, usuarios y grupos.
Puede acceder a todas las vistas y modelos disponibles.
Tiene permisos para crear, editar, eliminar y listar elementos en todos los modelos disponibles.

Personal (staff):

No tiene acceso de administrador (frontend Django) para gestión de modelos, usuarios y grupos.
Puede acceder a todas las vistas y modelos disponibles.
Tiene permisos para crear, editar, eliminar y listar elementos en todos los modelos disponibles.

Operador (oper):

Puede acceder a todas las vistas de los modelos caso y tarea.
Puede acceder solo a las vistas listar, tabla, detalle de todos los modelos disponibles.