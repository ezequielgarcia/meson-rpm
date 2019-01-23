%global libname mesonbuild

Name:           meson
Version:        0.49.1
Release:        1%{?dist}
Summary:        High productivity build system

License:        ASL 2.0
URL:            http://mesonbuild.com/
Source0:        https://github.com/mesonbuild/meson/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
Requires:       ninja-build

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%prep
%autosetup -p1
# Macro should not change when we are redefining bindir
sed -i -e "/^%%__meson /s| .*$| %{_bindir}/%{name}|" data/macros.%{name}

%build
%py3_build

%install
%py3_install
install -Dpm0644 data/macros.%{name} %{buildroot}%{_rpmmacrodir}/macros.%{name}

%files
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%{libname}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_mandir}/man1/%{name}.1*
%{_rpmmacrodir}/macros.%{name}
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy

%changelog
* Wed Jan 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.1-1
- Update to 0.49.1

* Sun Dec 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.0-1
- Update to 0.49.0

* Sat Dec 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.48.2-1
- Initial package
