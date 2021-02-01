#!/usr/bin/env python
"""管理タスク用のDjangoのコマンドライン実行"""
import os
import sys


def main():
    # djangoの環境変数(config.settings.py)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 0:'C:\\work\\python\\DRF2\\drf-simplest-sample-master\\manage.py'
    # 1:'runserver'
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
