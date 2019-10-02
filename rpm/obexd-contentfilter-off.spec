Name:          obexd-contentfilter-off
Summary:       Disable filter for known MIME types when transferring files per OBEX with bluez
Version:       0.1
Release:       1
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}-%{release}/%{name}-%{version}-%{release}.tar.gz
BuildArch:     noarch
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
%defattr(-,root,root,-)
%{_libexecdir}/obexd-contentfilter-helperapp

