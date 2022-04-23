# challenge

1) Estructura de la base de datos realizada en SQLite3:

[Tabla]:
Atributo0 Atributo1 Atributo2 ...
#TipoAtributo0 TipoAtributo1 TipoAtributo2 ...
#Descripción


[Student]:
Code Name Email Address Phone DateOfBirth
numérico texto texto texto numérico fecha
#Tabla estudiante: Posee códgio único y corresponde al documento de identidad.

[StudentState]:
StudentCode State StateDate
numérico numérico fecha
#Tabla Estado de Estudiante: Para generar un historial del estado del estudiante (inscripto, abandono, graduado...)

[Course]:
Code Name
numérico texto
#Taba curso: Código y nombre de cada curso.

[Inscription]:
StudentCode CourseCode InscriptionDate
numérico numñerico fecha
#Tabla Inscripción: Correponde a la materia inscripta por el estudiante.

[DefinitiveGrade]:
InscriptionCode Grade GradeDate
numérico numérico fecha
#Tabla nota definitiva: corresponde a la nota definitiva de la materia cursada.

[InscriptionStatus]:
InscripctionCode Status StatusDate
numérico numérico fecha
#Tabla estado de inscripción: Corresponde al estado de la marteria inscripta (inscripta, abandonada, completada).

[Exam]:
CourseCode Order Ponderation 
numérico numérico fecha
#Tabla Exámen: Corresponde a cada examen de l materia y posee una poderación sobre la nota definitiva.

[ExamGrade]:
ExamCode Grade GradeDate
numérico numérico fecha
#Tabla calificación de exámen: corresponde a la calificación obtenida por el estudiante en un exámen específico.

[Carreer]:
Code Name
numñerico texto
#Tabla Carrera: corresponde a la carrera que está cursando el estudiante.

[CarreerCourses]:
CarreerCode CourseCode
numérico numérico
#Tabla cursos de carrera: corresponde a las materias que componen estudiar una carrera. Una materia puede ser común entre varias carreras.

[CarreerInscription]:
CarreerCode InscriptionDate
numñerico fecha
#Tabla inscripción en carrera: Correpsodne al historial de inscripción en una carrera del estudiante.

[CarreerInscriptionStatus]:
CarreerInscriptionCode Status StatusDate
numérico numérico fecha
#Tabla Estado de inscricpión de carrera: Corresponde al historial de la inscri`ción de un estudiante en una carrera (inscripto, en curso, abandono, completado).

2)Comandos de inrterfaz con el servidor:
A través de la línea de comandos se puede consultar por un estudiante en particular y se puede generar un nuevo estudiante de la siguiente forma:

2.1) Consulta de estudiante particular (ejemplo DNI 95562304; servidor en IP 192.168.0.251):
curl http://192.168.0.251/cha_api_get_student_by_id/95562304
Respuesta del servidor JSON si no existe:
{"status":200,"student_data":"not found"}

Respuesta del servidor JSON si existe:
{"status":200,"student_data":"(95562304, 'Nicolas Bernal', 'nicobernal187@gmail.com', 'Bernardo Houssay 1042', 1154711031, '1989-12-18')"}

2.2) Creación de estudiante nuevo:
orden de los datos y separados por '_' : Documento_Nombre_Apellido_email_dirección_teléfono_fechaDeNacimiento
Validaciones:
-Documento: debe ser numérico y de 8 dígitos.
-Nombre: cada caracter debe ser no numérico.
-Apellido: cada caracter debe ser no numérico.
-Email: debe contener símbolo '@'.
-Dirección: (sin validación, en este caso no se permiten espacios en la dirección).
-Teléfono: Debe ser numérico y de 10 dígitos.
-Fecha de nacimiento: (sin validación)
curl http://192.168.0.251/cha_api_create_student/95473189_maria_castillo_mariacastillotest@gmail_mariacastilloaddress_1122223333_1989-12-18

Respuesta del servidor si ya existe se creó el usuario:
{"status":200,"student_data":"new student saved"}

Respuesta del servidor si ya existe el usuario:
{"status":200,"student_data":"error student 95473188 allready exists"}

Respuesta del servidor si no valida algún cantidad de datos enviados:
{"status":200,"student_data":"error data lenght"}

Respuesta del servidor si no valida código de estudiante:
{"status":200,"student_data":"error student code"}

Respuesta del servidor si no valida nombre del estudiante:
{"status":200,"student_data":"error student name"}

Respuesta del servidor si no valida apellido del estudiante:
{"status":200,"student_data":"error student last name"}

Respuesta del servidor si no valida email del estudiante:
{"status":200,"student_data":"error student email"}

Respuesta del servidor si no valida teléfono del estudiante:
{"status":200,"student_data":"error student phone"}


