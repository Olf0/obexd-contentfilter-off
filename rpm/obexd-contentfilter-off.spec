Name:          obexd-contentfilter-off
Summary:       Disable filter for supported MIME types when transferring files per OBEX with bluez
Version:       0.1
Release:       1
Group:         System/Base
# Distribution: SailfishOS # , maybe other descendants of MeeGo and MeeGo itself
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}-%{release}/%{name}-%{version}-%{release}.tar.gz
BuildArch:     noarch
Provides:      obexd-contentfilter-helper
# Obsoleting a vendor supplied systems package (i.e., from a mandatory repository) is best
# done in a separate, single purpose repository, because enabling this repository results
# in installing %{name} automatically when upgrading the operating system.
# Thus enabling the repository which hosts %{name} becomes equivalent to installing %{name} (sooner or later)!
# Obsoletes:    obexd-contentfilter-helper  # First try without
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
%defattr(-,root,root,-)
%{_libexecdir}/obexd-contentfilter-helperapp

