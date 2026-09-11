[app]
title = System Update
package.name = systemupdate
package.domain = org.system
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = WAKE_LOCK,FOREGROUND_SERVICE
android.api = 31
android.minapi = 21
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
p4a.branch = master
p4a.fork = kivy
p4a.source_dir = .

[buildozer]
log_level = 2
