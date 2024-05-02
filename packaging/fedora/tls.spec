Name:           tls
Version:        0.1.0
Release:        1%{?dist}
Summary:        Tempory Linux Shell/System
License:        GPLv3
URL:            https://github.com/Noriskky/tls
Source0:        https://github.com/Noriskky/tls/archive/v0.1.0.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Wrapper around Chroot to make it easy to use temporary Linux Shells.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/tls

%changelog
