
Feature: Acceso a receta médica y descripciones de exámenes 
#Como usuario de la aplicación quiero que la app cuente con mejores funciones para poder tener una aplicación completa y poder realizar todos los trámites necesarios desde un solo lugar 
Scenario: 1 Acceso dentro de la aplicación aprobado


Given que el paciente quiere hacer uso de la [receta medica]
And [descripciones de los exámenes]
When  la aplicación le brinde esta información 
And esta le llegue a su [correo electrónico]
Then el cliente podrá dirigirse de manera directa a recoger la medicina en la farmacia
And así podrá evitar largas filas para la recepción de estas recetas médicas 
And descripciones de exámenes de laboratorio  
 
Input:
receta medica
descripciones de los exámenes
Output:
correo 

------------------------------------------
Feature:Acceso a receta médica y descripciones de exámenes 
#Como usuario de la aplicación quiero que la app cuente con mejores funciones para poder tener una aplicación completa y poder realizar todos los trámites necesarios desde un solo lugar 
Scenario: 2 Error en el sistema 


Given que el paciente quiere hacer uso de la [receta medica]
And [descripciones de los exámenes]
When la aplicación le informe de un [error] en el sistema 
Then el paciente se tendrá que dirigir al consultorio del doctor
And así podrá recibir las recetas médicas para que pueda recibir su medicina 

Input:
receta medica
descripciones de los exámenes
Output:
error

-------------------------------------------
Feature:Acceso a receta médica y descripciones de exámenes 
#Como usuario de la aplicación quiero que la app cuente con mejores funciones para poder tener una aplicación completa y poder realizar todos los trámites necesarios desde un solo lugar 
Scenario: 3 Solo receta medica

Given que el paciente solo quiere tener acceso a la [receta médica]
And a la firma digital del médico 
When el paciente elija solamente esta opción 
Then el paciente recibirá en su [correo electrónico] su receta médica completa 
And la firma digital del medico 

Input:
receta medica
Output:
correo

----------------------------------------------------------------------------------------
Feature: Sistema de seguimiento del servicio
#Como gerente quiero implementar un sistema de seguimiento del servicio a domicilio para que el cliente conozca el tiempo aproximado de espera.
Scenario: 1 Uso del GPS

Given que el cliente quiere estar al tanto sobre el seguimiento del personal
And quiere que sea una función dentro de la aplicación
When el empleado se retire de las instalaciones de LavarCarPeru
And se le pedirá al cliente compartir su [ubicación actual]
Then el cliente podrá visualizar todo el trayecto que esta realizando 
And podrá conocer en cuanto tiempo esta llegando a su domicilio

Input:
ubicación actual cliente
Output:
ubicación actual empleado

Feature: Sistema de seguimiento del servicio
#Como gerente quiero implementar un sistema de seguimiento del servicio a domicilio para que el cliente conozca el tiempo aproximado de espera.
Scenario: 2 Fallo en GPS

Dado que el cliente quiere estar al tanto sobre el seguimiento del personal
And quiere que sea una función dentro de la aplicación
And se le pedirá al cliente compartir su [ubicación actual]
Cuando el cliente quiera estar al tanto del tiempo de espera
And esta función presente fallas dentro de nuestra aplicación
Entonces el cliente no podrá ver dentro de nuestra app el tiempo aproximado de espera
And no confiará en nuestros servicios 


Input:
ubicación actual cliente
Output:
error



Feature: Sistema de seguimiento del servicio
#Como gerente quiero implementar un sistema de seguimiento del servicio a domicilio para que el cliente conozca el tiempo aproximado de espera.
Scenario: 2 Información extra

Given que el cliente conozca el tiempo aproximado de llegada
And nos brinde su [ubicación actual]
And pueda visualizar información en detalle de nuestro servicio
When el cliente haga uso de esta función de gps
Then podrá visualizar [detalle del servicio] como precio e información del empleado
| Cliente        | Ubicación Actual | Función GPS Utilizada | Detalle | Información | Precio del Servicio | Tiempo Aproximado de Llegada |
| Thiago Mathey  | Av Jorge Chavez, Ciudad Lima  | Sí       | Servicio de limpieza | Nombre: Luis González, ID: 456   | $50 | 30 minutos     |
| Giovanni Mathey| Av Jorge Grau  , Ciudad Arequipa  | Sí   | Reparación de electrodomésticos   | Nombre: María López, ID: 789   | $70  | 45 minutos |
And así podrá conocer que servicio se le estará brindando 



Input:
ubicación actual cliente
Output:
detalle del servicio

===============================================================================================================================






Feature:Limpieza de datos 
#Como usuario  quiero realizar una limpieza de datos de forma manual para aprovechar el resto de las funciones la inteligencia artificial 
Scenario: 1 Limpieza funcional 
Given que el usuario  quiere realizar una limpieza de datos 
And quiere sea manual 
When el usuario  se encuentre dentro de nuestro chat bot
And  presione en el [botón de limpieza]
And el programa valide la limpieza
      | Botón de limpieza | Limpieza de datos |
      | Presionado        | Sí                |
And el programa limpiará toda la conversación 
And  así podrá agilizarse el proceso de consultas 


Input:
boton de limpieza
Output:
limpieza de datos

=================================================================
Feature:Limpieza de datos 
#Como usuario quiero realizar una limpieza de datos de forma manual para aprovechar el resto de las funciones la inteligencia artificial 
Scenario: 2 Limpieza lenta
Given  que el usuario quiere realizar una limpieza de datos 
And quiere que sea manual 
When el usuario se encuentre dentro de nuestro chat bot
And presione en el [botón de limpieza]
Then el programa mostrará un [mensaje de alerta]
      | Botón de limpieza | Mensaje de alerta                                                       |
      | Presionado        | "La cantidad de información es demasiada y demorará cierto tiempo."     |
And  mencionará que la cantidad de información es demasiada y demorara cierto tiempo

Input:
boton de limpieza
Output:
mensaje de alerta
--------------------------------------------------
Feature: Nuevas funciones 
Como usuario quiero hacer uso de nuevas funciones sobre el ámbito económico para que pueda manejar mis finanzas de una mejor manera.
Scenario: 1 Informacióne encontrada 

Given que el usuario quiere nuevas funciones sobre economía 
And estas cuenten con un grado de complejidad
When el cliente presione el [botón sobre economía]
And el chat bot marque que están funciones se encuentran [disponibles]
      | Botón sobre economía | Funcion disponible | 
      | Presionado           | Sí                 |
Then el chat bot le presentará nuevas funciones que revolucionaran este ámbito
And 0 así podrá hacer uso de toda la información disponible al respecto .


Input 
boton sobre economia 
Output
disponible

------------------------------------------------
Feature: Nuevas funciones 
Como usuario quiero hacer uso de nuevas funciones sobre el ámbito económico para que pueda manejar mis finanzas de una mejor manera.
Scenario: 2 Información desconocida 

Dado que el usuario quiere nuevas funciones sobre economía 
Y estas cuenten con un grado de complejidad
Cuando el cliente presione el [botón sobre economía]
Entonces el chat bot le mandará un [mensaje de alerta]
    | Botón sobre economía | Mensaje de alerta                                   |
    | Presionado           | "Lo sentimos, aún no contamos con esa información." |
Y le indicará que aún no cuenta con la información necesaria
Y que si desea puede compartirle información sobre otros temas relacionados


Input 
boton sobre economia 
Output
mensaje de alerta