import sys
sys.path.append('{{calendar_email_digest_srcdir}}/src/')
from calendar_email_digest import WSGIApplication

application = WSGIApplication(
        config_files = ['/etc/calendar-email-digest.conf'])
