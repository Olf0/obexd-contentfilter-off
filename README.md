# obexd-contentfilter-off
### Disable filter for supported MIME types when receiving files per OBEX with bluez.<br />

SailfishOS and MeeGo use *bluez*, *obexd* and the RPM *obexd-contentfilter-helper*.  This package provides a single file, *obexd-contentfilter-helperapp*, which is usually installed in */usr/libexec*.  *obexd-contentfilter-helperapp* is a shell script (as of v0.0.2), which checks per *lca-tool* if the MIME type of a file is registered (i.e., has a handler), when called as */usr/libexec/obexd-contentfilter-helperapp --receive-file \<filepath\>* (as usual, it exits with 0 for success and 1 if any failure occurred).

Unfortunately this RPM is marked as proprietary, see `rpm -q --info obexd-contentfilter-helper | fgrep License`.  Hence it cannot be found as part of either [mer-core](https://git.merproject.org/mer-core?filter=obexd-contentfilter), the [mer-mw (middleware)](https://build.merproject.org/project/show/nemo:devel:mw) or anywhere at the [mer-obs](https://build.merproject.org/project/list_public), and is consequently filed in the [section "Non OSS packages" on the list of SailfishOS OSS components](https://wiki.merproject.org/wiki/SailfishOSS#Non_OSS_packages).<br />
But luckily what triggers the installation of the *obexd-contentfilter-helper* RPM can be found (as that is FLOSS) in the [spec file of the *droid-hal-configs*](https://github.com/mer-hybris/droid-hal-configs/blob/master/droid-configs.inc#L91) of mer-hybris, providing a bit of context.

As adapting or altering the *obexd-contentfilter-helper* RPM or its contents (specifically the *obexd-contentfilter-helperapp* script) is out of scope due to their licensing, the *obexd-contentfilter-off* RPM simply replaces its counterpart and provides a dummy *obexd-contentfilter-helperapp* script, which always returns success.

Hence *obexd-contentfilter-off* provides a simple way to disable the filter for only registered MIME types, when receiving files per Bluetooth via the OBEX profile.<br />

#### Notes
* For easy installation, RPMs are available [in the release section](https://github.com/Olf0/obexd-contentfilter-off/releases) and [at OpenRepos](https://openrepos.net/content/obexdcontentfilterolf/bluetooth-obex-filter).
* *obexd-contentfilter-off* should install and work fine on all SailfishOS and even MeeGo releases.
* To restore the original behaviour and state, uninstall this package, also remove or disable [its repository](https://openrepos.net/user/14387/programs), if you have enabled it, finally reinstall the original package, e.g. by executing (must be root for that since SailfishOS 2.2.0): `pkcon install obexd-contentfilter-helper`
* A coarse changelog is provided per [release comments](https://github.com/Olf0/obexd-contentfilter-off/releases).

#### Background
* The purpose of the original *obexd-contentfilter-helper(app)* is to strictly adhere to the OBEX specification in MeeGo and subsequently in SailfishOS.  The idea is to never let pure GUI users receive files per Bluetooth, which cannot be processed on the device.  But this behaviour is contrary to most other file transfer methods and falls short, as e.g. TUI (textual user interface, "shell") programs usually do not register MIME types of files they can process and apparently the MIME type registrations of Android apps installed in an Android runtime environment (e.g. AlienDalvik, Anbox) are not being passed through to the underlying GNU/Linux distribution.<br />
The main argument from the manufacturers perspective was, "BT SIG qualification for Obex push requires that unsupported content is rejected, regardless of whether we want to let everything through or not." (2014-09-25).  Actually the OBEX aka [IrDA Interoperability](https://www.bluetooth.com/specifications/protocol-specifications/) specification (v2.0, 2010-08-26) does not require this, but the *Bluetooth Generic Object Exchange Profile Specification* or a *Bluetooth Application Profile* mentioned in section *1.2 Bluetooth OBEX-Related Specifications* may (these do not seem to be public).
* The deliberate filtering for supported MIME types has sparked heated dicussions at TJC (e.g. [[1]](https://together.jolla.com/question/1302/bluetooth-file-transfer-for-all-file-types/), [[2]](https://together.jolla.com/question/55104/sending-files-from-pc-to-jolla-by-bluetooth-is-extension-dependent/?answer=56832#post-id-56832)), because users expect arbitrary files to be easily transferred as on their PCs.<br />
Obviously the current behaviour does not fit well for this user group.
* *obexd-contentfilter-off* evolved from [this](https://together.jolla.com/question/1302/bluetooth-file-transfer-for-all-file-types/?answer=192893#192893-original-answer-2018-11-10) (kudos to @hmallat for the original suggestion).
