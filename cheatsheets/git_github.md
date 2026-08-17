# Hoja de Referencia: Comandos de Git y GitHub

Esta guía rápida resume los comandos esenciales para el control de versiones y la colaboración en repositorios remotos.

---

## Configuración Inicial

Configure sus credenciales globales antes de interactuar con repositorios locales:

```bash
# Establecer el nombre del usuario
git config --global user.name "Su Nombre"

# Establecer el correo electrónico
git config --global user.email "usuario@mail.com"

# Verificar la configuración activa
git config --list
```

---

## Flujo de Trabajo Local

Gestione el historial de cambios de sus archivos localmente:

```bash
# Inicializar un repositorio Git local
git init

# Verificar el estado del árbol de trabajo
git status

# Agregar archivos al área de preparación (Staging Area)
git add nombre_archivo.txt

# Agregar todos los cambios del directorio actual
git add .

# Confirmar los cambios preparados en el historial
git commit -m "feat: agregar módulo de autenticación"

# Ver el historial de commits realizados
git log --oneline -n 10
```

---

## Gestión de Ramas (Branches)

Trabaje de forma segura en características aisladas:

```bash
# Listar las ramas locales
git branch

# Crear una nueva rama
git branch nombre-rama

# Cambiar a una rama específica
git checkout nombre-rama
git switch nombre-rama

# Crear una rama y cambiar a ella de inmediato
git checkout -b nueva-rama

# Fusionar los cambios de otra rama en la activa
git merge nombre-rama

# Eliminar una rama local integrada
git branch -d nombre-rama
```

---

## Interacción con Repositorios Remotos (GitHub)

Sincronice sus cambios locales con la nube:

```bash
# Vincular el repositorio local con uno remoto
git remote add origin https://github.com/usuario/repo.git

# Verificar los repositorios remotos configurados
git remote -v

# Enviar los cambios de la rama main al remoto
git push -u origin main

# Descargar las novedades del remoto y fusionarlas
git pull

# Clonar un repositorio existente a su equipo
git clone https://github.com/usuario/repo.git
```
