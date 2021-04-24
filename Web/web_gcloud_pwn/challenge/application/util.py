import os, subprocess
from urllib.parse import urlparse

generate = lambda x: os.urandom(x).hex()

def flash(message, level, **kwargs):
    return { 'message':message, 'level':level, **kwargs }

def gen_pdf_from(url):
    
    filename = f'{ generate(14) }.pdf'

    try:
        l = subprocess.run(
            [
                '/usr/bin/chromium-browser',
                '--headless',
                '--disable-web-security',
                '--disk-cache-dir=/dev/null',
                '--disk-cache-size=1',
                '--media-cache-size=1',
                '--no-startup-window',
                '--disable-gpu', 
                '--disable-software-rasterizer',
                '--disable-dev-shm-usage',
                '--hide-scrollbars',
                '--user-data-dir=/tmp/chrome_data',
                '--print-to-pdf-no-header',
                f'--print-to-pdf=/app/application/static/pdfs/{ filename }',
                url
            ], capture_output=True)
        print(l.stderr.decode("utf-8"))
        print(l.stdout.decode("utf-8"))

    except:
        return False
    
    return filename

def is_scheme_allowed(scheme):
    return scheme in ['http', 'https']

def gen_pdf(url):
    domain = urlparse(url).hostname
    scheme = urlparse(url).scheme

    if not domain or not scheme or not is_scheme_allowed(scheme):
        return flash(f'Malformed url {url}', 'danger')

    pdf = gen_pdf_from(url)

    if not pdf:
        return flash('Something went wrong!', 'error')

    return flash(f'Successfully cached {domain}', 'success', domain=domain, filename=pdf)
