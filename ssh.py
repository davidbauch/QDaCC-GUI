from fabric2 import Connection

out = Connection("noctua2").run("ssh noctua2 pc2status")
print(out.stdout.split("\n"))