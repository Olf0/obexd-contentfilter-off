Name:          bluez-obexd-no-mime-filter
Summary:       Scripts for safe and automated upgrading of SailfishOS with logging
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
Requires:      bluez-

%description
%{summary}

%prep
%setup -n %{name}-%{version}-%{release}

%build

%preinst
if [ -x /usr/libexec/obexd-contentfilter-helperapp ]
then
  if [ "$(wc -c /usr/libexec/obexd-contentfilter-helperapp)" -ge "30" ]
  then mv /usr/libexec/obexd-contentfilter-helperapp /usr/libexec/obexd-contentfilter-helperapp.orig
  fi
else
  exit 1
fi

%install
mkdir -p %{buildroot}%{_libexecdir}
cp usr/libexec/* %{buildroot}%{_libexecdir}/

%files
%defattr(-,root,root,-)
%{_libexecdir}/obexd-no-mime-filter

%postun
