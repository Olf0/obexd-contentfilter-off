Name:          obexd-contentfilter-off
Summary:       Disable filter for supported MIME types when receiving files per OBEX with bluez
Version:       1.1.0
# Stop evaluating the "Release:" field (per %{release}) and cease including it in git tags since v1.1.0, 
# in order to satisfy OBS and consequently switching to a three field semantic versioning scheme for
# releases and their git tags.
# Hence any changes to the spec file now always trigger an increase of the bug fix release number, i.e.
# the third field of %{version}.
# But %{release} is now (ab)used to merely *indicate* the estimated release quality by setting it
# to {alpha, beta, stable}.  Note that no other identifiers shall be used.
Release:       stable
Group:         System/Base
# Distribution: SailfishOS # , MeeGo and maybe also other descendants of MeeGo
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
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
%setup -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libexecdir}
cp usr/libexec/* %{buildroot}%{_libexecdir}/

%files
%defattr(0755,root,root,-)
%{_libexecdir}/obexd-contentfilter-helperapp

