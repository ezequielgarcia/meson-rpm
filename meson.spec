%global __python %{__python3}

Name:           meson
Version:        0.27.0
Release:        1%{?dist}
Summary:        High productivity build system

License:        ASL 2.0
URL:            http://mesonbuild.com/
Source0:        https://github.com/mesonbuild/meson/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel ninja-build
# Test deps
BuildRequires:  gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ java-devel mono-core mono-devel
BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  vala
BuildRequires:  wxGTK3-devel
BuildRequires:  flex bison
BuildRequires:  gettext
BuildRequires:  gnustep-base-devel
BuildRequires:  git
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) python3-gobject-base gtk-doc
BuildRequires:  pkgconfig(zlib)
Requires:       ninja-build
Requires:       python3

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%package gui
Summary:        GUI for high productivity build system

Requires:       %{name} = %{version}-%{release}
Requires:       python3-qt5

%description gui
GUI for high productivity build system.

%prep
%autosetup

%build
# Nothing to build

%install
./install_meson.py --prefix=%{_prefix} --destdir=%{buildroot}

%check
MESON_PRINT_TEST_OUTPUT=1 ./run_tests.py

%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}conf
%{_bindir}/%{name}introspect
%{_bindir}/wraptool
%dir %{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/*.ui
%exclude %{_datadir}/%{name}/mesongui.py
%exclude %{_datadir}/%{name}/__pycache__/mesongui.*
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}conf.1.*
%{_mandir}/man1/%{name}introspect.1.*
%{_mandir}/man1/wraptool.1.*
%{_rpmconfigdir}/macros.d/macros.%{name}

%files gui
%license COPYING
%{_bindir}/%{name}gui
%{_datadir}/%{name}/*.ui
%{_datadir}/%{name}/mesongui.py
%{_datadir}/%{name}/__pycache__/mesongui.*
%{_mandir}/man1/%{name}gui.1.*

%changelog
* Wed Nov 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.27.0-1
- 0.27.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 30 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.26.0-2
- Fix rpm macros for using optflags

* Sun Sep 13 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.26.0-1
- 0.26.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.25.0-4
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.25.0-2
- rebuild for Boost 1.58

* Sun Jul 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.25.0-1
- 0.25.0

* Sat Jul 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.24.0-3
- Update URLs
- drop unneded hacks in install section
- enable print test output for tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.24.0-1
- Update to 0.24.0

* Thu May 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.0-3.20150328git0ba1d54
- Update to latest git

* Thu May 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.0-3
- Add patch to accept .S files

* Wed Apr 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.0-2
- Add python3 to Requires (Thanks to Ilya Kyznetsov)

* Tue Mar 31 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.0-1
- 0.23.0

* Sat Mar 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-9.20150328git3b49b71
- Update to latest git

* Mon Mar 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-9.20150325git18550fe
- Update to latest git
- Include mesonintrospect

* Mon Mar 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-9.20150322git78d31ca
- Fix filelists for mesongui (python-bytecode-without-source)

* Sun Mar 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-8.20150322git78d31ca
- Enable C# tests

* Sun Mar 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-7.20150322git78d31ca
- update to latest git
- fix tests on arm

* Sat Mar 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-7.20150321gita084a8e
- update to latest git

* Mon Mar 16 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-7.20150316gitfa2c659
- update to latest git

* Tue Mar 10 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-7.20150310gitf9f51b1
- today's git snapshot with support for cool GNOME features
- re-enable wxGTK3 tests, package fixed in rawhide

* Thu Feb 26 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-6.git7581895
- split gui to subpkg
- update to latest snapshot
- enable tests

* Thu Feb 26 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-5.gitc6dbf98
- Fix packaging style
- Make package noarch

* Mon Feb 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-4.git.c6dbf98
- Use development version

* Sat Feb 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-3
- Add ninja-build to requires

* Thu Jan 22 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-2
- fix shebang in python files

* Wed Jan 21 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-1
- Initial package
