[app]
title = System Update
package.name = systemupdate
package.domain = org.system
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 1
android.permissions = WAKE_LOCK,FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
