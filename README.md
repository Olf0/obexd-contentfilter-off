# Bluetooth file transfer for all file types

### Disable filter for supported MIME types when receiving files via OBEX with bluez<br />

SailfishOS and MeeGo use *bluez*, *obexd* and the RPM *obexd-contentfilter-helper*.  This package provides a single file, *obexd-contentfilter-helperapp*, which is usually installed in */usr/libexec/*.  *obexd-contentfilter-helperapp* is a shell script (as of v0.0.2), which checks per *lca-tool* if the MIME type of a file is registered (i.e., has a handler), when called as */usr/libexec/obexd-contentfilter-helperapp --receive-file \<filepath\>* (as usual, it exits with 0 for success and 1 if any failure occurred).

Unfortunately this RPM is marked as proprietary, see `rpm -q --info obexd-contentfilter-helper | fgrep License`.  Hence it cannot be found as part of either [mer-core](https://git.merproject.org/mer-core?filter=obexd-contentfilter), the [mer-mw (middleware)](https://build.merproject.org/project/show/nemo:devel:mw) or anywhere at the [mer-obs](https://build.merproject.org/project/list_public), and is consequently filed in the [section "Non OSS packages" on the list of SailfishOS OSS components](https://wiki.merproject.org/wiki/SailfishOSS#Non_OSS_packages).<br />
But luckily what triggers the installation of the *obexd-contentfilter-helper* RPM can be found (as that is FLOSS) in the [spec file of the *droid-hal-configs*](https://github.com/mer-hybris/droid-hal-configs/blob/master/droid-configs.inc#L91) of mer-hybris, providing a bit of context.

As adapting or altering the *obexd-contentfilter-helper* RPM or its contents (specifically the *obexd-contentfilter-helperapp* script) is out of scope due to their licensing, the *obexd-contentfilter-off* RPM simply replaces its counterpart and provides a dummy *obexd-contentfilter-helperapp* script, which always returns success.

Hence *obexd-contentfilter-off* provides a simple way to disable the filter for only registered MIME types, when receiving files via Bluetooth with its OBEX profile.<br />

#### Notes
* For easy installation, RPMs are available [in the release section](https://github.com/Olf0/obexd-contentfilter-off/releases) and [at OpenRepos](https://openrepos.net/content/obexdcontentfilterolf/bluetooth-obex-filter).
* *obexd-contentfilter-off* should install and work fine on all SailfishOS and even MeeGo releases.
* To restore the original behaviour and state of the OS, simply remove ("uninstall") this package.  Then also remove or disable [its repository](https://openrepos.net/user/14387/programs), if you have enabled it, in order to prevent automatic reinstallation of *obexd-contentfilter-off* when upgrading the OS.<br />
  **Mind that**, while *pkcon*, *zypper* / *libzypp* and consequently all tools using them (Jolla's system updater, Warehouse, Storeman etc.) satisfy all package dependencies fine when removing *obexd-contentfilter-off* (by reinstalling *obexd-contentfilter-helper* automatically), the basic *rpm* utility does not!  If one really wants to use *rpm* for removing (**not recommended**, anyway), one must execute `rpm -e --nodeps obexd-contentfilter-off && rpm -i obexd-contentfilter-helper` in order to restore the original behaviour and state without breaking the OS installation by doing so.  Also note that you need a local download of *obexd-contentfilter-helper* for that to succeed (e.g., per `pkcon download obexd-contentfilter-helper`).<br />
  TL;DR: Do not use `rpm` for removing *obexd-contentfilter-off*&#8202;__!__
* A coarse changelog is provided per [release comments](https://github.com/Olf0/obexd-contentfilter-off/releases).

#### Background
* The purpose of the original *obexd-contentfilter-helper(app)* is to strictly adhere to the OBEX specification in MeeGo and subsequently in SailfishOS.  The idea is to never let users receive files per Bluetooth, which cannot be processed on the device.<br />
  But this behaviour is contrary to most other file transfer methods and falls short, as e.g., TUI (textual user interface, "shell") programs usually do not register MIME types of files they can process and apparently the MIME type registrations of Android apps installed in an Android runtime environment (e.g., Alien Dalvik aka "Android App Support", Anbox → Waydroid) are not being passed through to the underlying GNU/Linux distribution.<br />
  The main argument from the manufacturers perspective was, "BT SIG qualification for Obex push requires that unsupported content is rejected, regardless of whether we want to let everything through or not." (2014-09-25).  Actually the OBEX aka [IrDA Interoperability (IrOBEX)](https://www.bluetooth.com/specifications/protocol-specifications/) (v2.0, 26 Aug 2010) and [Generic Object Exchange Profile (GOEP)](https://www.bluetooth.com/specifications/profiles-overview/) (v2.1.1, 15 Dec 2015) specifications do not require this, but the [Object Push Profile (OPP)](https://www.bluetooth.com/specifications/profiles-overview/) (v1.2.1, 15 Dec 2015) specification may (the latter does not seem to be publicly available, only [the aspects essential for implementing the OPP](https://www.amd.e-technik.uni-rostock.de/ma/gol/lectures/wirlec/bluetooth_info/k11_opp.html) are).
* The deliberate filtering for supported MIME types has sparked heated dicussions at TJC (e.g., [[1]](https://together.jolla.com/question/1302/bluetooth-file-transfer-for-all-file-types/), [[2]](https://together.jolla.com/question/55104/sending-files-from-pc-to-jolla-by-bluetooth-is-extension-dependent/?answer=56832#post-id-56832)), because users expect arbitrary files to be easily transferred as on their PCs.<br />
  Obviously the current behaviour does not fit well for this user group.
* *obexd-contentfilter-off* evolved from [this](https://together.jolla.com/question/1302/bluetooth-file-transfer-for-all-file-types/?answer=192893#192893-original-answer-2018-11-10) (kudos to [@hmallat](https://together.jolla.com/users/2541/hmallat/) for the original suggestion).
