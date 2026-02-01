
#!/usr/bin/env python
import os, sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','MdRiyadulIslamRatul_REG_ICT_WADP_L4_001145_JobPortal.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
if __name__=='__main__':
    main()
