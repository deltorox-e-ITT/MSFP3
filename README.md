[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=deltorox-e-ITT/ModeladoDeSistemasFisiologicosP4)

# Práctica 3: Modelado y control del sistema musculoesquelético

## Información del estudiante
Eduardo Del Toro Nuñez; LC23212399.tijuana.tecnm.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplindarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Identificar las variables mecánicas del modelo musculoesquelético simplificado y construir su circuito eléctrico equivalente aplicando la analogía fuerza-voltaje.
2. Formular las ecuaciones del sistema y determinar las funciones de transferencia $G(s) = X(s)/F(s)$ para un individuo sano (control) y un caso simulado de atrofia muscular (caso).
3. Analizar la estabilidad de ambos modelos mediante la localización de polos en el plano complejo y calcular el error en estado estacionario.
4. Simular la respuesta al impulso unitario en MATLAB, Simulink y Simscape Electrical en el intervalo $t \in [0, 10]\text{ s}$.
5. Diseñar y sintonizar las ganancias de un controlador PID mediante la herramienta Tune de Simulink para minimizar el error entre el caso y el control.
6. Realizar la verificación cruzada entre MATLAB/Simulink y Python (Visual Studio Code) en lazo abierto y lazo cerrado.
7. Elaborar un diagrama biológico en BioRender que relacione los componentes del músculo/tendón con el modelo mecánico y el circuito eléctrico equivalente.

## Descripción detallada del sistema

Este trabajo aborda la representación viscoelástica de un compartimento musculoesquelético mediante un modelo mecánico simplificado y su circuito eléctrico equivalente derivado de la analogía fuerza-voltaje:

* **Analogía Fuerza-Voltaje:** La fuerza transmitida $F(t)$ se mapea como voltaje $V(t)$, la velocidad $\dot{x}(t)$ como corriente $I(t)$, el desplazamiento $x(t)$ como carga eléctrica $q(t)$, el amortiguador viscoso $R$ como resistencia, y las compliancias pasiva y serie ($C_p$, $C_s$) como capacitancias.
* **Componentes biomecánicos:** 
  * $F_0(t) = \alpha F(t)$ ($0 < \alpha < 1$): Fuerza desarrollada por el elemento contráctil activo del músculo.
  * $R$: Amortiguación viscosa inherente al tejido muscular.
  * $C_p$: Compliancia pasiva en paralelo (asociada con la elasticidad del sarcolema y tejidos pasivos).
  * $C_s$: Compliancia en serie (asociada con tendones y componentes elásticos estructurales).

Se analizan dos condiciones fisiológicas caracterizadas por la variación del parámetro resistivo $R$:
1. **Sano / Control ($R = 100\ \Omega$):** Representa el comportamiento mecánico dinámico de referencia de un individuo sano.
2. **Atrofia Muscular / Caso ($R = 10\text{ k}\Omega$):** Modifica la componente viscosa del modelo para simular la alteración mecánica de la atrofia muscular.

Se diseña un sistema de control de retroalimentación con un controlador PID ($k_P$, $k_I$, $k_D$) para reducir la discrepancia de la respuesta transitoria y estacionaria $e(t) = x_{\text{control}}(t) - x_{\text{caso}}(t)$, logrando que la dinámica del músculo atrofiado siga de forma precisa la respuesta de referencia del individuo sano ante un estímulo de impulso.

**Palabras clave:** Modelo musculoesquelético; Analogía fuerza-voltaje; Atrofia muscular; Propiedades viscoelásticas; Controlador PID; Simulaciones *in silico*.

## Lista de archivos incluidos en el repositorio
1. Cuaderno computacional de MATLAB [.mlx].
2. Modelo de Simulink y Simscape Electrical [.slx].
3. Archivos de código fuente en Python [.py].
4. Captura de pantalla de las ganancias sintonizadas del controlador PID ($k_P, k_I, k_D$).
5. Figuras de las simulaciones en lazo abierto y lazo cerrado en MATLAB y Python [.pdf].
6. Capturas de pantalla de los esquemas y resultados de las simulaciones.
7. Diagrama biológico del sistema musculoesquelético realizado en BioRender.
8. Archivo de metadatos de citación [CITATION.cff].

## Referencias
\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems: Analysis, Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.

\[4] J. E. Hall, Guyton and Hall Textbook of Medical Physiology, 14th ed. Elsevier, 2021.
