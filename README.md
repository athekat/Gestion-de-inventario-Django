# Sistema de Gestión de Productos

## Realización: Grupo 5
#### Integrantes:
- Cortéz Alan
- Scarazzato Omar


## Descripción del Sistema:

El sistema permitirá realizar la gestión de stock de un depósito de mercadería.

La primera pantalla del sistema será inicio de sesión. No se mostrará contenido sin haber realizado el correcto logueo.

Se dispondrá de tres niveles de usuario, cada nivel tendrá los permisos propios del nivel sumados a los permisos de los niveles inferiores.

### Tipos de usuarios (con sus correspondientes funcionalidades asociadas):
- Empleado (Nivel 1):
  - Ver productos.
  - Ingresar y egresar mercadería

- Supervisor (Nivel 2):
  -	Ver productos (con opción de edición).
  - Alta producto.
  - Editar productos.
  - Baja producto.
  - Alta fabricante.
  - Editar fabricante.
  - Baja fabricante.
  - Ver facturas.

- Administrador (Nivel 3):
  - Ver usuarios.
  - Alta usuario.
  - Editar usuario.
  - Baja usuario.

### Funcionalidades:
- Ver productos: se listarán en una tabla los productos que están dados de alta en el sistema con su correspondiente nombre, fabricante y stock.
  - Según el tipo de usuario, en la ultima columna, se mostrará un botón para editar el producto.
- Ingresar y egresar mercadería: modificará el stock de los productos. Se asociará una factura a cada modificacion de stock.
- Alta producto: perimitirá registrar nuevos productos en el sistema. El stock inicial para todo producto registrado será 0.
- Ediar producto.
- Baja producto.
- Alta fabricante.
- Editar fabricante.
- Baja fabricante.
- Ver facturas: se listarán las facturas y se permititrá acceder al detalle de la misma.
- Ver usuarios.
- Alta usuario.
- Editar usuario.
- Baja usuario.

## Diagramas

### Diagrama Entidad Relación (DER)
![DER](/DER.png)