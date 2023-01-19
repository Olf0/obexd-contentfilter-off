Name:          obexd-contentfilter-off
Summary:       Disable filter for supported MIME types when receiving files per OBEX
Version:       1.1.10
# Stop evaluating the Release tag content (only set it) and cease including it in git tags since
# v1.1.0, in order to satisfy the SailfishOS OBS' tar_git.
# Consequently switch to a three field semantic versioning scheme for releases and their git tags.
# Hence any changes to the spec file now always trigger an increase of the bug fix release number,
# i.e., the third field of the Version.
# The Release tag is now (ab)used to merely indicate the estimated release quality by setting it
# to {alpha,beta,rc,stable}.  Note that no other identifiers shall be used.
Release:       stable
Group:         System/Base
# Distribution: SailfishOS  # , MeeGo and maybe also other descendants of MeeGo
Vendor:        meego
License:       LGPL-2.1-only
URL:           https://github.com/Olf0/%{name}
Source:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to the Source tag(s):
# It only accepts a GIF or XPM file (a path is stripped to its basename) in the SOURCES directory
# (but not inside a tarball there)!  Successfully tested GIF89a and XPMv3, but an XPM icon results
# in bad visual quality and large file size.
# Hence only to be used, when the file (or a symlink to it) is put there:
#Icon:          kdebluetooth.256x256.gif
BuildArch:     noarch
Provides:      obexd-contentfilter-helper
# Obsoleting a vendor supplied system package (i.e., from a mandatory repository) is best
# done in a separate, single purpose repository, because enabling this repository results
# in installing obexd-contentfilter-off automatically when upgrading the operating system.
# Thus enabling the repository which hosts obexd-contentfilter-off becomes equivalent to
# installing obexd-contentfilter-off (sooner or later)!
# This is alleviated by an enhancement of SailfishOS' GUI upgrade utility in SailfishOS 3.4.0:
# An OS upgrade at the GUI on SFOS 3.4.0+ will (unconditionally?) delete / disable / "isolate" (?)
# enabled repositories with RPMs which replace(d ?) "system RPMs" (i.e., those provided by Jolla).
Obsoletes:     obexd-contentfilter-helper
Conflicts:     obexd-contentfilter-helper

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%description
%{summary} with bluez by substituting ("obsoleting") MeeGo's / SailfishOS' obexd-contentfilter-helper package, replacing its obexd-contentfilter-helperapp script with a "dummy".

%if "%{?vendor}" == "chum"
PackageName: Disable file type filter for Bluetooth
Type: generic
Categories:
 - Utilities
 - System
DeveloperName: olf (Olf0)
Custom:
  Repo: %{url}
Icon: %{url}/raw/master/icon/kdebluetooth.256x256.png
Url:
  Homepage: %{url}
  Help: %{url}/issues
  Bugtracker: %{url}/issues
  Donation: https://openrepos.net/donate* Wed Jan 04 2* Wed Jan 04 2023 olf <Olf0@users.noreply.github.com> - 2.1.7-release6
- Create double-fork-in-shell.md023 olf <Olf0@users.noreply.github.com> - 2.1.7-release6
- Create double-fork-in-shell.md
%endif

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_libexecdir}
cp usr/libexec/* %{buildroot}%{_libexecdir}/

%files
%defattr(0755,root,root,-)
%{_libexecdir}/obexd-contentfilter-helperapp

%changelog
* Thu Jan 01 1970 olf <Olf0@users.noreply.github.com> - 0.0.0
- %{url}/releases
