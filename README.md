# 📌 Tabla de Contenido

- Descripción del Proyecto
- Alcance de Pruebas
- Stack Tecnológico
- Arquitectura del Framework
- Estructura del Proyecto
- Instalación
- Ejecución de Pruebas
- Casos de Prueba Automatizados
- Buenas Prácticas Implementadas
- Sección para Recruiters
- Autor

# 📖 Descripción del Proyecto

Este proyecto contiene pruebas automatizadas y manuales para la aplicación Urban Grocers, enfocadas en validar flujos críticos del usuario dentro de una plataforma de e-commerce.

El objetivo es asegurar la calidad del sistema mediante pruebas funcionales, validaciones de UI/API y cobertura de escenarios reales de usuario.

# 🎯 Alcance de Pruebas

- Pruebas funcionales de frontend
- Validación de flujo de compra
- Testing de APIs relacionadas
- Pruebas de regresión
- Validación de formularios
- Pruebas de integración

# 🛠️ Stack Tecnológico

| Tecnología     | Uso                  |
| -------------- | -------------------- |
| Python 3.14.3  | Lenguaje principal   |
| Request 2.32.5 | Solicitudes HTTP     |
| Pytest 9.0.2   | Framework de testing |
| Git            | Control de versiones |

# 🏗️ Arquitectura del Framework

El framework sigue una arquitectura modular basada en:

- Test Layer: Casos de prueba
- Service Layer: Lógica de consumo de API
- Utils/Helpers: Funciones reutilizables
- Data Layer: Datos de prueba

Esto permite escalabilidad, mantenimiento sencillo y reutilización de código.

# 📁 Estructura del Proyecto

api_stand_tests/  
├──api/  
├──config/  
├──data/  
├──helpers/  
└──test/

# ⚙️ Instalación

### Clonar repositorio

```bash
git clone https://github.com/usuario/qa-project-Urban-Grocers-app-es.git
```

### Crear entorno virtual (opcional pero recomendado)

```bash
1.python -m venv venv

2.venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecución de Pruebas

```bash
pytest .\test\create_kit_name_kit_test.py
```

# ✅ Casos de Prueba Automatizados

Vas a crear un kit dentro de un usuario o usuaria particular, no una tarjeta. Para ello, sigue estos pasos:

1. Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).

2. Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Authorization.

| №   | Descripción                                                                                                                                         | ER                                                                                                                              |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1   | El número permitido de caracteres (1): kit_body = { "name": "a"}                                                                                    | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud     |
| 2   | El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}                           | Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| 3   | El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }                                                           | Código de respuesta: 400                                                                                                        |
| 4   | El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } | Código de respuesta: 400                                                                                                        |
| 5   | Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }                                                                                  | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud     |
| 6   | Se permiten espacios: kit_body = { "name": " A Aaa " }                                                                                              | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud     |
| 7   | Se permiten números: kit_body = { "name": "123" }                                                                                                   | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud     |
| 8   | El parámetro no se pasa en la solicitud: kit_body = { }                                                                                             | Código de respuesta: 400                                                                                                        |
| 9   | Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }                                                                    | Código de respuesta: 400                                                                                                        |

# 🧠 Buenas Prácticas Implementadas

- Separación de responsabilidades
- Uso de datos dinámicos
- Tests independientes
- Naming claro y descriptivo
- Validaciones robustas de respuesta
- Reutilización de código

# 💼 Sección para Recruiters

Este proyecto demuestra:

- Conocimiento en testing de APIs
- Manejo de herramientas modernas de QA
- Estructuración de frameworks escalables
- Buenas prácticas en automatización

# 👨‍💻 Autor

Axel Arteaga

QA Engineer | Automation Tester | Software Quality

LinkedIn: www.linkedin.com/in/axel-arteaga
