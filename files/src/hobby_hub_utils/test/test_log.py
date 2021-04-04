from hobby_hub_pkg.Log import Log

log = Log.Log('ex.txt')
log.write("hello world")
log.write("testing...")
log.clear()
log.write("re-write")