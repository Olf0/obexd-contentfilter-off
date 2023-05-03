Name:          obexd-contentfilter-off
Summary:       Bluetooth file transfer for all file types
Version:       1.1.12
# Stop evaluating the Release tag content (only set it) and cease including it in git tags since
# v1.1.0, in order to satisfy the SailfishOS OBS' tar_git.
# Consequently switch to a three field semantic versioning scheme for releases and their git tags.
# Hence any changes to the spec file now always trigger an increase of the bug fix release number,
# i.e., the third field of the Version.
# The Release tag is now (ab)used to merely indicate the estimated release quality by setting it
# to {alpha,beta,rc,stable}.  Note that no other identifiers shall be used.
Release:       stable
# The Group tag should comprise one of the groups listed here:
# https://github.com/mer-tools/spectacle/blob/master/data/GROUPS
Group:         System/Base
# Distribution: SailfishOS  # , MeeGo and maybe also other descendants of MeeGo
Vendor:        meego
# Do use the same Group and Vendor as the original obexd-contentfilter-helper-0.0.2 it replaces!
License:       LGPL-2.1-only
URL:           https://github.com/Olf0/%{name}
# Download URLs for gzipped tarballs at GitHub must conform to: %{url}/archive/<tag-name>/<arbitrary-string>.tar.gz
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
Disable filter for supported MIME types when receiving files via OBEX with bluez
by substituting ("obsoleting") MeeGo's / SailfishOS' obexd-contentfilter-helper
package, replacing its obexd-contentfilter-helperapp script with a "dummy".

%if 0%{?_chum}
PackageName: Bluetooth OBEX Filter off
Type: generic
Categories:
 - Utilities
 - System
DeveloperName: olf (Olf0)
Custom:
  Repo: %{url}
Icon: %{url}/raw/master/icon/kdebluetooth.256x256.png
Url:
  Homepage: https://openrepos.net/content/obexdcontentfilterolf/bluetooth-obex-filter
  Help: %{url}/issues
  Bugtracker: %{url}/issues
  Donation: https://openrepos.net/donate
%endif

%define _binary_payload w6.gzdio
%define _source_payload w6.gzdio

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
* Thu Sep  9 1999 olf <Olf0@users.noreply.github.com> - 99.99.99
- See %{url}/releases
