Name:          obexd-contentfilter-off
Summary:       Disable filter for supported MIME types when receiving files per OBEX with bluez
Version:       1.1.6
# Stop evaluating the Release tag content (only set it) and cease including it in git tags since v1.1.0, 
# in order to satisfy OBS' git_tar.  Consequently switch to a three field semantic versioning scheme for
# releases and their git tags.
# Hence any changes to the spec file now always trigger an increase of the bug fix release number, i.e.
# the third field of the Version.
# But the Release tag is now (ab)used to merely indicate the estimated release quality by setting it
# to {alpha, beta, stable}.  Note that no other identifiers shall be used.
Release:       stable
Group:         System/Base
# Distribution: SailfishOS # , MeeGo and maybe also other descendants of MeeGo
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to the Source tag(s):
# It only accepts a GIF or XPM file (a path is stripped to its basename!) in the SOURCE directory
# (but not in the tarball)!  Successfully tested GIF89a and XPMv3, but an XPM icon results in
# bad visual quality and large file size.
# Hence only to be used, when the file is put there:
#Icon:          kdebluetooth.256x256.gif
BuildArch:     noarch
Provides:      obexd-contentfilter-helper
# Obsoleting a vendor supplied system package (i.e., from a mandatory repository) is best
# done in a separate, single purpose repository, because enabling this repository results
# in installing obexd-contentfilter-off automatically when upgrading the operating system.
# Thus enabling the repository which hosts obexd-contentfilter-off becomes equivalent to
# installing obexd-contentfilter-off (sooner or later)!
Obsoletes:     obexd-contentfilter-helper
Conflicts:     obexd-contentfilter-helper

%description
%{summary} by substituting ("obsoleting") MeeGo's and SailfishOS' obexd-contentfilter-helper package, replacing its obexd-contentfilter-helperapp script with a "dummy".

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_libexecdir}
cp usr/libexec/* %{buildroot}%{_libexecdir}/

%files
%defattr(0755,root,root,-)
%{_libexecdir}/obexd-contentfilter-helperapp

