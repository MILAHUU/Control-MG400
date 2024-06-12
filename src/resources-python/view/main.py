import os, sys

# ---------copiar estas lineas de codigo en caso de marcar error en las importaciones----------
# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Obtener la ruta del directorio del proyecto (un nivel arriba del directorio actual)
project_dir = os.path.dirname(script_dir)
# Agregar la ruta del proyecto al PYTHONPATH
sys.path.append(project_dir)
# -----------------------------------------------------------------------------------------------

from view.view_principal import RobotUI

robot_ui = RobotUI()

robot_ui.pack()
robot_ui.mainloop()