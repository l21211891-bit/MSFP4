[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l21211891-bit/MSFP4)
# Práctica 5.4 : Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información del estudiante
Rodriguez Garcia AFRICA MONTSERRAT [C21211891]; L21211891@tijuana.tecnm.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

La asignatura de Modelado de Sistemas Fisiológicos permite comprender y representar el comportamiento de los sistemas del cuerpo humano mediante modelos matemáticos y simulaciones computacionales. Integra conocimientos de Ingeniería de Control, Electrónica Analógica y Fisiología para analizar sistemas fisiológicos y diseñar controladores que permitan modificar su respuesta dinámica.

## Objetivos

Identificar los elementos y parámetros del modelo cardiovascular Windkessel de cuatro elementos.

Obtener las ecuaciones integro-diferenciales y la función de transferencia del sistema.

Analizar el error en estado estacionario y la estabilidad mediante los polos.

Simular las condiciones normotensa, hipotensa e hipertensa en MATLAB/Simulink.

Diseñar y sintonizar controladores PID para regular la respuesta cardiovascular.

Reproducir las simulaciones en Python y comparar los resultados con MATLAB.

Analizar las respuestas en lazo abierto y en lazo cerrado.

## Descripción detallada del sistema

El modelo Windkessel de cuatro elementos permite representar el comportamiento del sistema cardiovascular mediante una analogía entre el flujo sanguíneo y los circuitos eléctricos. Está formado por cuatro parámetros: impedancia característica (Z), resistencia periférica (R), inertancia arterial (L) y distensibilidad arterial (C).

El modelo considera la presión arterial de entrada Pa(t), el flujo sanguíneo y la presión asociada a la distensibilidad arterial. Estos elementos permiten estudiar cómo responde el sistema ante diferentes condiciones fisiológicas.

Durante la práctica se analizan los estados normotenso, hipotenso e hipertenso, comparando sus respuestas mediante simulaciones numéricas. Posteriormente, se incorporan controladores para reducir las diferencias respecto a la condición normotensa y evaluar el comportamiento del sistema con retroalimentación.

## Palabras clave: 
Sistema cardiovascular; Modelo Windkessel; Circuito RLC; Controlador PID; Función de transferencia; MATLAB; Simulink; Python.

## Lista de archivos incluidos en el repositorio

Cuaderno computacional de MATLAB [.mlx].

Modelo de Simulink [.slx].

Código de simulación en Python [.py].

Imágenes de los parámetros de los controladores.

Gráficas de las simulaciones [.pdf y .png].

Evidencia del análisis matemático y resultados obtenidos.

## Referencias

[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos. Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. https://biomath.xyz/course/

[2] M. C. Khoo, Physiological Control Systems: Analysis, Simulation, and Estimation, 2nd ed., IEEE Press, 2018.

[3] N. S. Nise, Control Systems Engineering, 8th ed., John Wiley & Sons, 2020.

[4] T. Kind et al., "Estimation of three- and four-element Windkessel parameters using subspace model identification", IEEE Transactions on Biomedical Engineering, vol. 57, no. 7, pp. 1531–1538, 2010. https://doi.org/10.1109/TBME.2010.2041351
