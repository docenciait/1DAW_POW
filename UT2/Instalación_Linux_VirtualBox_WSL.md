# Instalación de Ubuntu 22.04 en Virtual Box

1. Requisitos previos
Asegúrate de tener suficiente espacio en tu disco duro (al menos 25 GB para la máquina virtual).
Tener instalado [VirtualBox](https://www.virtualbox.org/) y, opcionalmente, [VirtualBox Extension Pack](https://download.virtualbox.org/virtualbox/7.1.4/Oracle_VirtualBox_Extension_Pack-7.1.4.vbox-extpack) . Para funciones avanzadas y que instalarás después del Virtualbox.

2. Descargar Ubuntu 22.04

Ve a la página oficial de descarga de0 Ubuntu.
Descarga la versión de [Ubuntu 22.04](https://releases.ubuntu.com/jammy/ubuntu-22.04.5-desktop-amd64.iso) (archivo .iso).

3. Crear una máquina virtual en VirtualBox

Abre VirtualBox y selecciona Nueva.
Configura el nombre de la máquina virtual (puedes llamarla "Ubuntu 22.04") y elige la ubicación donde se guardarán los archivos de la VM.
Tipo: selecciona Linux.
Versión: selecciona Ubuntu (64-bit).
Haz clic en Siguiente.

4. Configuración de hardware

Memoria RAM: Asigna al menos 2 GB (2048 MB) de RAM, aunque 4 GB es lo recomendable para un rendimiento fluido. No excedas el 50% de la RAM de tu sistema.
Disco duro:
Selecciona Crear un disco duro virtual ahora y haz clic en Crear.
Tipo de disco duro: elige VDI (VirtualBox Disk Image) y haz clic en Siguiente.
Almacenamiento: selecciona Reservado dinámicamente.
Tamaño: configura al menos 25 GB. Luego, haz clic en Crear.

5. Configurar el archivo ISO de Ubuntu
Selecciona la máquina virtual recién creada y haz clic en Configuración.
En el menú lateral, ve a Almacenamiento.
En Controlador: IDE, selecciona el icono de CD (donde aparece Vacío).
En Atributos, haz clic en el icono de CD y selecciona Elegir un archivo de disco.
Selecciona el archivo .iso de Ubuntu 22.04 descargado anteriormente.
Haz clic en Aceptar.

6. Configurar red y pantalla

Red: En el menú lateral, ve a Red y asegúrate de que el Adaptador 1 esté habilitado en modo NAT para que la máquina virtual tenga acceso a Internet.
Pantalla: En Pantalla, aumenta la memoria de video al máximo (128 MB) para mejorar el rendimiento gráfico.

7. Iniciar la instalación de Ubuntu
Selecciona la máquina virtual y haz clic en Iniciar.
Al arrancar, VirtualBox cargará el archivo .iso de Ubuntu.
En la pantalla de bienvenida de Ubuntu, selecciona el idioma y haz clic en Instalar Ubuntu.

8. Configuración de instalación de Ubuntu
Distribución del teclado: Elige el idioma del teclado y haz clic en Continuar.
Actualizaciones y otro software: Selecciona Instalación normal y marca las opciones para descargar actualizaciones y software de terceros (si es necesario). Luego, haz clic en Continuar.
Tipo de instalación:
Selecciona Borrar disco e instalar Ubuntu (esto solo afectará a la máquina virtual, no a tu sistema operativo principal).

Haz clic en Instalar ahora y confirma en Continuar.
Zona horaria: Selecciona tu zona horaria y haz clic en Continuar.
Crear usuario: Introduce tu nombre, un nombre para el equipo, un nombre de usuario y una contraseña segura. Luego, haz clic en Continuar.

9. Completar la instalación
La instalación puede tardar unos minutos. Una vez completada, aparecerá una ventana indicando que debes reiniciar.
Haz clic en Reiniciar ahora.
Al reiniciar, es posible que VirtualBox pida presionar Enter para quitar el medio de instalación. Hazlo para continuar.

10. Ajustes finales
Instalar VirtualBox Guest Additions: Para mejorar el rendimiento y habilitar funciones como el cambio de resolución automática.

En el menú de VirtualBox, selecciona Dispositivos > Insertar imagen de CD de las Guest Additions.
Sigue las instrucciones en Ubuntu para instalar los complementos.
Reinicia la máquina virtual después de la instalación de Guest Additions.

### Aquí tienes un video demostrativo de cómo hacerlo
[Instalación Ubuntu 22.04 en Virtual Box Windows] (https://www.youtube.com/watch?v=YiHm8NtXNFc&t=308s)

---

# Forma alternativa WSL2

Existe otra forma para crear una Máquina Virtual de Linux en Windows. Es usando el servicio WSL2, que sería como tener ya el virtual box instalado. Es un poco más complejo, pero igualmente hay que seguir unas instrucciones.

### 1. Verificar Requisitos del Sistema 

Para instalar Ubuntu en WSL2, asegúrate de cumplir con los siguientes requisitos:

- Windows 11 (o Windows 10 versión 2004 y superior con el último parche).

- Windows Subsystem for Linux (WSL) habilitado.

### 2. Abrir PowerShell en Modo Administrador 
 
1. Presiona `Windows + X` y selecciona **Windows Terminal (Administrador)**  o **Windows PowerShell (Administrador)** .

### 3. Habilitar el Subsistema de Windows para Linux (WSL) 

Ejecuta el siguiente comando en PowerShell para habilitar WSL (Abrir Terminal como Administrador): 


```powershell
wsl --install
```

Este comando instalará WSL2, habilitará las características necesarias y descargará la distribución predeterminada de Ubuntu.

> **Nota** : Si ya tienes WSL1 instalado y deseas actualizar a WSL2, asegúrate de que tu máquina esté configurada para usar WSL2 como la versión predeterminada.
Para configurar WSL2 como la versión predeterminada, ejecuta:


```powershell
wsl --set-default-version 2
```

### 4. Instalar Ubuntu 22.04 Específicamente 

Si deseas instalar Ubuntu 22.04 en particular, puedes hacerlo desde la Microsoft Store o usando el comando de PowerShell:


```powershell
wsl --install -d Ubuntu-22.04
```

Este comando instalará específicamente Ubuntu 22.04 en WSL2.


Si no funcionara lo anterior, puedes ir a la Microsoft Store de Windows y buscar Ubuntu 22.04, se instala como si fuera una app.


### 5. Verificar la Instalación de Ubuntu 22.04 

Para confirmar que se instaló correctamente, ejecuta el siguiente comando en PowerShell:


```powershell
wsl -l -v
```
Esto debería mostrarte una lista de todas las distribuciones de WSL instaladas y sus versiones. Asegúrate de que `Ubuntu-22.04` esté en la lista y que esté configurado para WSL2.
### 6. Configurar y Ejecutar Ubuntu 22.04 
 
1. Abre la aplicación **Ubuntu 22.04**  desde el menú de inicio o ejecuta en PowerShell:

```powershell
wsl -d Ubuntu-22.04
```
 
2. La primera vez que abras Ubuntu, se te pedirá que configures un nombre de usuario y una contraseña para la cuenta de Linux.

### 7. Actualizar el Sistema Ubuntu 22.04 

Es recomendable actualizar el sistema una vez instalado. En la terminal de Ubuntu, ejecuta:


```bash
sudo apt update && sudo apt upgrade -y
```

### Video de Instalación 

Para una demostración visual del proceso, te recomiendo este video de YouTube, que cubre paso a paso la instalación de WSL2 y Ubuntu en Windows 11:

> UPDATE! Los videos sólo van a usar lo que viene en la web Microsoft : [Instalación de WSL2](https://learn.microsoft.com/es-es/windows/wsl/install-manual)
 
- [Instalar Ubuntu 22.04 en WSL2 - Video Tutorial](https://www.youtube.com/watch?v=Hmws650D2WI)

Este video está más actualizado. Podéis usar los subtítulos.