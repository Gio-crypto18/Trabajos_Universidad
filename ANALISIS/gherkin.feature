---13
#lenguaje: es 
Feature: Agendar horarios de capacitación.
# Como estudiante en prácticas, quiero tener acceso a capacitaciones que se ajusten a mi tiempo libre para poder completar las simulaciones y los trabajos aplicados con IA.
       Scenario: Selección de horarios.
                  Given  soy un “<estudiante>” en prácticas 
                  And quiero “<agendar>”  un horario de capacitación que se ajuste a mi tiempo libre,
                  When acceda al “<menú>” de capacitación de la plataforma,
                     | estudiante  |     menú       |      horarios     | 
                     |      Juan   |  Capacitación  |  mañana, tarde    |
                     |    María    | Capacitación   |    tarde, noche   |
                  Then podré “<seleccionar>” manualmente los horarios disponibles en un calendario
                   And podrá elegir “<horarios>” que mejor se adapten a mi agenda personal.

#lenguaje: es 
Feature: Agendar horarios de capacitación.
# Como estudiante en prácticas, quiero tener acceso a capacitaciones que se ajusten a mi tiempo libre para poder completar las simulaciones y los trabajos aplicados con IA.
       Scenario: Sugerencias automáticas de horarios.
                Given soy un”<estudiante>” en prácticas 
                And necesitas agendar un horario de capacitación que se ajuste a disponibilidad,
                When Ingrese mi disponibilidad o “<calendario>” en el menú de “<capacitación>”,
                Then la plataforma me sugerirá automáticamente los mejores horarios de “<capacitación>” basados “<disponibilidad>” e                                                                   
                | estudiante  | calendario | Capacitación | disponibilidad | sesiones | simulaciones      |
                |      Juan   | calendario | Capacitación  |    mañana     | sesión 1  | simulación A | 
                |      María  | calendario | Capacitación  |       tarde   |  sesión 2  | simulación B |
                   And en los horarios disponibles de las “<sesiones>”y“<simulaciones>”.

---14

#lenguaje: es 
Feature: Recibir notificaciones sobre actividades.
# Como estudiante en prácticas, quiero recibir notificaciones constantemente para que pueda estar al pendiente de las nuevas tareas.
       Scenario:  Notificación de nueva tarea.
                 Given soy un “<estudiante>” en prácticas 
              And necesitas estar informado sobre nuevas las nuevas “<notificaciones de  noticias>” y “<actividades>”.
                 When se me “<asigna>” nuevas tareas dentro de la plataforma,
               | estudiante | notificaciones de noticias  | actividades   | asigna  |
               | Juan       | noticias de cursos          | tarea nueva   | tarea 1 |
               | María      | actualizaciones de sistema  | tarea urgente | tarea 2 |
                 Then recibiré una notificación instantánea en mi correo electrónico 
          And  en la aplicación móvil para que pueda comenzar a trabajar en ella lo antes posible.

#lenguaje: es 
Feature: Recibir notificaciones sobre actividades.
# Como estudiante en prácticas, quiero recibir notificaciones constantemente para que pueda estar al pendiente de las nuevas tareas.
       Scenario:  Notificación de tarea modificada.
                 Given soy un “<estudiante>” en prácticas 
And es importante estar “<actualizado>” con cualquier cambio en las tareas asignadas,
                  When se “< modifique>” los detalles de una tarea existente,
                 | estudiante | actualizado | modifique | notificación |
                 | Juan       | sí          | cambios 1 | correo       | 
                 | María      | sí          | cambios 2 | app          |
Then recibiré una “<notificación>” inmediata detallando los cambios realizados para  que pueda ajustar mi trabajo según las nuevas instrucciones.

---15


#lenguaje: es 
Feature: Ajustar el nivel de dificultad.
# Como estudiante en prácticas, quiero tener la opción de poder ajustar el nivel de dificultad para que pueda adaptarme eficazmente a las situaciones planteadas.
       Scenario:  Selección de nivel de dificultad.
                 Dado que soy un [estudiante] en prácticas
                  Y quiero adaptar las simulaciones a mi nivel de habilidad actual,
                  Cuando inicie una [simulación] en la plataforma,
                   | estudiante | simulación   | seleccionar |
                   | Juan        | Simulación A | intermedio | 
                   | María       | Simulación B | avanzado   |
Entonces podré [seleccionar] el nivel de dificultad (básico, intermedio, avanzado) antes de comenzar, permitiéndole enfrentar situaciones que correspondan a mi nivel de experiencia.

#lenguaje: es 
Feature: Ajustar el nivel de dificultad.
# Como estudiante en prácticas, quiero tener la opción de poder ajustar el nivel de dificultad para que pueda adaptarme eficazmente a las situaciones planteadas.
       Scenario:  Ajuste de la dificultad durante la simulación
                 Dado que soy un “<estudiante>” en prácticas 
                 Y necesito que las “<simulaciones>” se adapten a mi “<rendimiento>”,
                 Cuando esté participando en una “<simulación>”  en tiempo real,
Entonces la plataforma ajustará dinámicamente el nivel de dificultad en función de              mis respuestas 
| estudiante en prácticas | habilidades | práctica continua | menú   | simulaciones |
| Juan                    | habilidades A | constante | Simulaciones | Simulación 1 |
| María                   | habilidades B | constante | Simulaciones | Simulación 2 |
Y  proporciona simulaciones de acuerdo al “<rendimiento académico>” en el que me encuentro.



---16

#lenguaje: es 
Feature:  Repetir simulaciones sin un límite establecido.
# Como estudiante en prácticas, quiero poder repetir las simulaciones sin un límite de intentos para que pueda mejorar constantemente cada día.
       Scenario: Acceso Ilimitado a Simulaciones. 
                  Given que soy un “<estudiante en prácticas>”
                   And quiero mejorar mis “<habilidades>” mediante la “<práctica continua>”,
                   When acceda al “<menú>” y su lista de “<simulaciones>”,
     | estudiante en prácticas | simulación | progreso | resultados | rendimiento |                                                                  |   | Juan                    | Simulación E| sí | guardados | alto      | técnica 1  |
     | María                   | Simulación F| sí | guardados | medio     | técnica 2  |
                   Then podré iniciar y repetir cualquier “<simulación>” sin
                    restricciones en la cantidad de intentos, permitiendo practicar 
                    And mejorar tanto como sea necesario.

#lenguaje: es 
Feature: Repetir simulaciones sin un límite establecido.
#Como estudiante en prácticas, quiero poder repetir las simulaciones sin un límite de intentos para que pueda mejorar constantemente cada día.
        Scenario: Registro Automático de Progreso. 
        Given estoy enfocado en medir mi mejora a lo largo del tiempo como “<estudiante en prácticas>”, 
        When repita una “<simulación>” en la plataforma,
      | estudiante en prácticas | simulación | progreso | resultados | rendimiento | áreas de mejora | 
      | Juan                    | Simulación E | sí | guardados | alto  | técnica 1 |
      | María                   | Simulación F| sí  | guardados | medio | técnica 2 | 
        Then mi “<progreso>” y “<resultados>” se almacenan automáticamente sin importar el número de intentos, permitiéndole revisar mi “<rendimiento>” 
        And podrá enfocarse en “<áreas de mejora>” específicas.



---17 

#lenguaje: es 
Feature:Acceder al catálogo de simulaciones.
#Como estudiante en prácticas, quiero  tener acceso a un catálogo de simulaciones para que pueda practicar en diferentes situaciones en mi vida laboral.
         Scenario: Búsqueda del catálogo. 
                    Dado que el usuario accede al “<catálogo de simulaciones>”,
                    Cuando quiera practicar sus “<habilidades blandas>”, 
        | catálogo de simulaciones | habilidades blandas | menú | situaciones en la vida laboral | 
        | Catálogo A   | Comunicación   | Simulaciones | Situación 1  | 
        | Catálogo B   | Liderazgo      | Simulaciones | Situación 2  | 
Entonces se desplegará un “<menú>” con todas las “<posibles situaciones en la vida laboral>”. 


#lenguaje: es 
Feature: Acceder al catálogo de simulaciones.
# Como estudiante en prácticas, quiero  tener acceso a un catálogo de simulaciones para que pueda practicar en diferentes situaciones en mi vida laboral.
         Scenario: Elección de una opción dentro del catálogo. 
                    Given que el usuario ya eligió una de las “<opciones disponibles>”,
                    When se sienta listo podrá iniciar la “<actividad>”, 
             | opciones disponibles | actividad   | simulación |
             | Opción 1                | Actividad A | Simulación G|
             | Opción 2                | Actividad B | Simulación H|
                    Then la “<simulación>” comenzará. 
                    And podrá mejorar su habilidades blandas.



