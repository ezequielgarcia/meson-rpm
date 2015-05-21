%global __python %{__python3}

Name:           meson
Version:        0.23.0
Release:        3%{?dist}
Summary:        High productivity build system

License:        ASL 2.0
URL:            https://jpakkane.github.io/meson/
Source0:        https://github.com/jpakkane/meson/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/jpakkane/meson/commit/0ba1d545afe021e09090f434d5242ae942e7d5b4
Patch0:         0001-Accept-.S-files-as-assembler-too.patch
BuildArch:      noarch

BuildRequires:  python3-devel ninja-build
# Test deps
BuildRequires:  gcc-gfortran gcc-objc gcc-objc++ java-devel mono-core mono-devel
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
#BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
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
# protobuf broken
rm -rf "test cases/frameworks/5 protocol buffers/"

%build
# Nothing to build

%install
./install_meson.py --prefix=%{_prefix} --destdir=%{buildroot}
sed -i '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{_datadir}/%{name}/dependencies.py
sed -i '1{\@^#!/usr/bin/python@d}' %{buildroot}%{_datadir}/%{name}/mparser.py
chmod +x %{buildroot}%{_bindir}/meson*

%check
./run_tests.py

%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}conf
%{_bindir}/%{name}introspect
%dir %{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/*.ui
%exclude %{_datadir}/%{name}/mesongui.py
%exclude %{_datadir}/%{name}/__pycache__/mesongui.*
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}conf.1.*
%{_mandir}/man1/%{name}introspect.1.*
%{_rpmconfigdir}/macros.d/macros.%{name}

%files gui
%license COPYING
%{_bindir}/%{name}gui
%{_datadir}/%{name}/*.ui
%{_datadir}/%{name}/mesongui.py
%{_datadir}/%{name}/__pycache__/mesongui.*
%{_mandir}/man1/%{name}gui.1.*

%changelog
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
