Name:          obexd-contentfilter-off
Summary:       Disable filter for supported MIME types when receiving files per OBEX with bluez
Version:       0.1
Release:       3
Group:         System/Base
# Distribution: SailfishOS # , MeeGo and maybe also other descendants of MeeGo
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}-%{release}/%{name}-%{version}-%{release}.tar.gz
BuildArch:     noarch
Provides:      obexd-contentfilter-helper
# Obsoleting a vendor supplied system package (i.e., from a mandatory repository) is best
# done in a separate, single purpose repository, because enabling this repository results
# in installing %{name} automatically when upgrading the operating system.
# Thus enabling the repository which hosts %{name} becomes equivalent to installing %{name} (sooner or later)!
Obsoletes:     obexd-contentfilter-helper
Conflicts:     obexd-contentfilter-helper

%description
%{summary}.

%prep
%setup -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_libexecdir}
cp usr/libexec/* %{buildroot}%{_libexecdir}/

%files
%defattr(0755,root,root,-)
%{_libexecdir}/obexd-contentfilter-helperapp

