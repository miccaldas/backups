"""
We'll call rsync through subprocess, and send
the commands from here.
"""
import shlex
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from systemd import journal

from app import app

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@app.task
def go():
    """
    We have several rsync commands, that will send
    through subprocess.
    """

    boot = "sudo rsync -azvP --delete /boot /home/mic/secondary-hard-drive/directories_bkup "
    b = subprocess.Popen(boot, user="mic", shell=True, stdout=subprocess.PIPE)
    stdout = b.communicate()[0]
    journal.sendv("MESSAGE=Boot Rsync Command", "CODE_FILE=backups.py", "CODE_LINE=38")
    journal.sendv("MESSAGE=stdout is {}".format(stdout), "CODE_FILE=backups.py", "CODE_LINE=39")
    print("STDOUT:{}".format(stdout))
    print(b.returncode)

    etc = "sudo rsync -azvP --delete  /etc /home/mic/secondary-hard-drive/directories_bkup"
    e = subprocess.run(boot, user="mic", shell=True, stdout=subprocess.PIPE)
    print(e.returncode)

    home = "sudo rsync -azvP --exclude /home/mic/secondary-hard-drive --delete /home /home/mic/secondary-hard-drive/directories_bkup"
    h = subprocess.run(boot, user="mic", shell=True, stdout=subprocess.PIPE)
    print(h.returncode)

    opt = "sudo rsync -azvP --delete  /opt /home/mic/secondary-hard-drive/directories_bkup"
    o = subprocess.run(boot, user="mic", shell=True, stdout=subprocess.PIPE)
    print(o.returncode)

    usr = "sudo rsync -azvP --delete /usr /home/mic/secondary-hard-drive/directories_bkup"
    u = subprocess.run(boot, user="mic", shell=True, stdout=subprocess.PIPE)
    print(u.returncode)

    var = "sudo rsync -azvP --delete /var /home/mic/secondary-hard-drive/directories_bkup"
    v = subprocess.run(boot, user="mic", shell=True, stdout=subprocess.PIPE)
    print(v.returncode)

    srv = "sudo rsync -azvP --delete /srv /home/mic/secondary-hard-drive/directories_bkup"
    s = subprocess.run(boot, user="mic", shell=True, stdout=subprocess.PIPE)
    print(s.returncode)


if __name__ == "__main__":
    go()
