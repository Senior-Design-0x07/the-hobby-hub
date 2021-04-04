from hobby_hub_pkg.Log import Log

log = Log('ex.txt')
log.write("hello world")
log.write("testing...")
log.clear()
log.write("re-write")
syslog = Log()
syslog.write("THIS IS A LOG TEST")
