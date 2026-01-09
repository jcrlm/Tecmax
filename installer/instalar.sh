#!/data/data/com.termux/files/usr/bin/bash

clear
echo "========================================"
echo "        INSTALADOR TECMAX"
echo " Sistema de Servicio Técnico"
echo "========================================"
echo

# -------- MOSTRAR MANUAL --------
echo "📘 MANUAL DE USUARIO"
echo "----------------------------------------"
if [ -f "../docs/manual_usuario.md" ]; then
  cat ../docs/manual_usuario.md
else
  echo "Manual no encontrado."
fi

echo
read -p "¿Desea continuar con la instalación? (s/n): " CONFIRMAR

if [ "$CONFIRMAR" != "s" ]; then
  echo "❌ Instalación cancelada por el usuario."
  exit 1
fi

# -------- ACTUALIZAR SISTEMA --------
echo
echo "🔄 Actualizando Termux..."
pkg update -y

# -------- PYTHON --------
if ! command -v python >/dev/null 2>&1; then
  echo "🐍 Instalando Python..."
  pkg install python -y
else
  echo "🐍 Python ya está instalado."
fi

# -------- PERMISOS --------
echo
echo "🔐 PERMISOS NECESARIOS"
echo "TECMAX necesita acceso a archivos para:"
echo "- Guardar reportes"
echo "- Enviar archivos por WhatsApp"
echo
echo "Se solicitará permiso de almacenamiento."
read -p "¿Autoriza estos permisos? (s/n): " PERMISOS

if [ "$PERMISOS" != "s" ]; then
  echo "❌ Permisos no concedidos. No se puede continuar."
  exit 1
fi

termux-setup-storage

# -------- ESTRUCTURA --------
cd ..
mkdir -p reportes
chmod +x main.py

echo
echo "✅ INSTALACIÓN COMPLETA"
echo "----------------------------------------"
echo "El sistema se ejecutará ahora."
echo
sleep 2

python main.py
