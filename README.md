### romanballesteros-pythonweb

- **Nombre del Proyecto:**
Follow-up

- **Descripción:** 
Esta página web está desarrollada utilizando Python con el framework Django y proporciona funcionalidades para gestionar varios modelos de datos. A continuación se detallan los modelos disponibles y las vistas asociadas para cada tipo de usuario.

- **Requisitos:** falta completar
- **Instalación:** falta completar
 - **Uso:** falta completar
- **Funcionalidades:** falta completar
- **Contribuciones:** falta completar
- **Licencia:** falta completar

- **Modelos y Vistas Disponibles:**
Modelo: Sitios

    Listar Sitios
        Muestra en una tabla todos los sitios cargados.
    Crear Sitio
        Permite añadir un nuevo sitio utilizando un formulario.
    Editar/Eliminar Sitio
        Formulario para actualizar los campos de un sitio existente o eliminarlo.

Modelo: Proveedores

    Listar Proveedores
        Muestra en una tabla todos los proveedores cargados.
    Crear Proveedor
        Permite añadir un nuevo proveedor utilizando un formulario.
    Editar/Eliminar Proveedor
        Formulario para actualizar los campos de un proveedor existente o eliminarlo.

Modelo: Dispositivos

    Listar Dispositivos
        Muestra en una tabla todos los dispositivos cargados.
    Crear Dispositivo
        Permite añadir un nuevo dispositivo utilizando un formulario.
    Editar/Eliminar Dispositivo
        Formulario para actualizar los campos de un dispositivo existente o eliminarlo.

Modelo: Operadores

    Listar Operadores
        Muestra en una tabla todos los operadores cargados.
    Crear Operador
        Permite añadir un nuevo operador utilizando un formulario.
    Editar/Eliminar Operador
        Formulario para actualizar los campos de un operador existente o eliminarlo.

Modelo: Casos

    Listar Casos
        Muestra en una tabla todos los casos cargados.
    Crear Caso
        Permite añadir un nuevo caso utilizando un formulario.
    Editar/Eliminar Caso
        Formulario para actualizar los campos de un caso existente o eliminarlo.

Modelo: Tareas

    Listar Tareas
        Muestra en una tabla todas las tareas cargadas.
    Crear Tarea
        Permite añadir una nueva tarea utilizando un formulario.
    Editar/Eliminar Tarea
        Formulario para actualizar los campos de una tarea existente o eliminarla.
    Completar Tarea
        Muestra una lista de las tareas que han sido completadas.

- **Tipos de Usuarios y Permisos de Acceso:**
Administrador (Admin)

    Acceso de Admin para administración de los elementos de la página, gestión de usuarios y grupos.
    Puede acceder a todas las views y models disponibles.
    Tiene permisos para crear, editar, eliminar y listar elementos en todos los models.

Personal (Staff)

    Puede acceder a todas las views y models disponibles.
    Tiene permisos para crear, editar, eliminar y listar elementos en todos los models.

Operador (Oper)

    Puede acceder únicamente a los models Case y Task.
    Puede ver la view List de todos los models, pero solo puede interactuar (crear, editar, eliminar y listar) con models Case y Task.