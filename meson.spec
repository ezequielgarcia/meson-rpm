%global libname mesonbuild

Name:           meson
Version:        0.51.1
Release:        1%{?dist}
Summary:        High productivity build system

License:        ASL 2.0
URL:            https://mesonbuild.com/
Source:         https://github.com/mesonbuild/meson/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python%{python3_version}dist(setuptools)
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
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir} data/macros.%{name}

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
* Wed Jul 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.51.1-1
- Update to 0.51.1

* Wed Apr 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.50.1-1
- Update to 0.50.1

* Mon Apr 08 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.50.0-2
- Fix -Db_ndebug=if-release with -Dbuildtype=plain

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.50.0-1
- Update to 0.50.0

* Mon Feb 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.2-1
- Update to 0.49.2

* Wed Jan 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.1-1
- Update to 0.49.1

* Sun Dec 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.0-1
- Update to 0.49.0

* Sat Dec 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.48.2-1
- Initial package
