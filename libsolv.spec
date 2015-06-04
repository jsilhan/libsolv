%global gitrev 2db517f87a8c0364d28c0fa2590ba034e866a4b8

Name:		libsolv
Version:	0.6.11
Release:	1%{?dist}
License:	BSD
Url:		https://github.com/openSUSE/libsolv
Source:		https://github.com/openSUSE/libsolv/archive/%{gitrev}.tar.gz
Group:		Development/Libraries
Summary:	Package dependency solver
BuildRequires:	cmake libdb-devel expat-devel rpm-devel zlib-devel
BuildRequires:	swig perl perl-devel ruby ruby-devel python2-devel
BuildRequires:  xz-devel
%description
A free package dependency solver using a satisfiability algorithm. The
library is based on two major, but independent, blocks:

- Using a dictionary approach to store and retrieve package
  and dependency information.

- Using satisfiability, a well known and researched topic, for
  resolving package dependencies.

%package devel
Summary:	A new approach to package dependency solving
Group:		Development/Libraries
Requires:	libsolv-tools%{?_isa} = %{version}-%{release}
Requires:	libsolv%{?_isa} = %{version}-%{release}
Requires:	rpm-devel%{?_isa}
Requires:	cmake

%description devel
Development files for libsolv,

%package tools
Summary:    A new approach to package dependency solving
Group:      Development/Libraries
Requires:   gzip bzip2 coreutils
Requires:   libsolv%{?_isa} = %{version}-%{release}

%description tools
Package dependency solver tools.

%package test
Summary:	A new approach to package dependency solving
Group:		Development/Libraries
Requires:	gzip bzip2 coreutils
Requires:	libsolv%{?_isa} = %{version}-%{release}

%description test
Binary running libsolv test cases.

%prep
%setup -q -n libsolv-%{gitrev}

%check
make ARGS="-V" test

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DFEDORA=1 \
       -DENABLE_LZMA_COMPRESSION=1 \

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT/usr/bin/solv

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE* README BUGS
%_libdir/libsolv.so.*
%_libdir/libsolvext.so.*

%files tools
%_bindir/deltainfoxml2solv
%_bindir/dumpsolv
%_bindir/installcheck
%_bindir/mergesolv
%_bindir/repo2solv.sh
%_bindir/repomdxml2solv
%_bindir/rpmdb2solv
%_bindir/rpmmd2solv
%_bindir/rpms2solv
%_bindir/updateinfoxml2solv
%_bindir/testsolv

%files test
%_bindir/testsolv

%files devel
%doc examples/solv.c
%_libdir/libsolv.so
%_libdir/libsolvext.so
%_includedir/solv
%_datadir/cmake/Modules/FindLibSolv.cmake
%{_mandir}/man?/*

%changelog
* Wed Jun 3 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.11-1
- initial package for RHEL 7.2 without unnecessary bindings
