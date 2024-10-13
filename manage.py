#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrud.settings')
    
    # Obtener el puerto desde la variable de entorno PORT, predeterminando al 8000 si no está definida
    port = os.environ.get('PORT', '8000')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Verificar si el primer argumento es "runserver" y no hay un puerto especificado
    if len(sys.argv) == 2 and sys.argv[1] == 'runserver':
        sys.argv.append(f'127.0.0.1:{port}')
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
